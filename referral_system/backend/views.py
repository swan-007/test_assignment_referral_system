from django.http import JsonResponse

from drf_spectacular.utils import extend_schema

from .models import User, PhonCode, AlienInviteCode
from rest_framework.views import APIView
from .serializers import UserSerializer, AlienInviteCodeSerializer
import random
from rest_framework.authtoken.models import Token
import time


def simulator_phone_code():
    time.sleep(2)
    code_list = random.sample(range(10), 4)
    code = "".join(map(str, code_list))
    return int(code)


class RegisterAccount(APIView):
    """
    Для регистрации пользователей
    """

    # Регистрация методом POST
    @extend_schema(summary="Регистрация по номеру телефона", tags=["Register"])
    def post(self, request, *args, **kwargs):
        # проверяем обязательные аргументы
        if {"phone_number"}.issubset(request.data):
            # проверяем есть ли пользователь в базе
            user = User.objects.filter(
                phone_number=request.data["phone_number"]
            ).first()
            simulator = simulator_phone_code()
            if user:
                PhonCode.objects.create(user=user, phon_code=simulator)
                return JsonResponse({"Status": True, "Phone_code": simulator})

        # проверяем данные пользователя
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            # сохраняем пользователя
            user = user_serializer.save()
            user.save()

            # добовляем код из смс в БД
            phone_code_create = PhonCode.objects.create(user=user, phon_code=simulator)
            return JsonResponse(
                {"Status": True, "Phone_code": simulator, "id": user.id}
            )
        else:
            return JsonResponse({"Status": False, "Errors": user_serializer.errors})
        return JsonResponse({"Status": False, "Errors": "Не указан номер телефона"})


class ConfirmAccount(APIView):
    """
    Класс для подтверждения телефона и входа
    """

    @extend_schema(
        summary="Подтверждение номера телефона и получение токена", tags=["Register"]
    )
    def post(self, request, *args, **kwargs):
        # проверяем обязательные аргументы
        if {"phone_code", "phone_number"}.issubset(request.data):
            # # проверяем код и номер телефона
            phone_code = PhonCode.objects.filter(
                user__phone_number=request.data["phone_number"],
                phon_code=request.data["phone_code"],
            ).first()
            #
            if phone_code:
                phone_code.user.is_active = True
                phone_code.user.save()
                phone_code.delete()
                # генерируем и отправляем токен
                token, _ = Token.objects.get_or_create(user=phone_code.user)
                return JsonResponse({"Status": True, "Token": token.key})

            else:
                return JsonResponse(
                    {
                        "Status": False,
                        "Errors": "Неправильно указан номер или код подтверждения",
                    }
                )
        else:
            return JsonResponse(
                {"Status": False, "Errors": "Не указаны все необходимые аргументы"}
            )


class AccountDetails(APIView):
    """
    Класс для работы с данными пользователя
    """

    # получить данные
    @extend_schema(summary="Получить данные пользователя", tags=["User"])
    def get(self, request, *args, **kwargs):
        # проверка аунтификации
        if not request.user.is_authenticated:
            return JsonResponse(
                {"Status": False, "Error": "Log in required"}, status=403
            )
        serializer = UserSerializer(request.user)
        subscribers_list = []
        for i in serializer.data["owner_code"]:
            x = AlienInviteCode.objects.filter(id=i).first()
            subscribers_list.append(str(x.code_user))
        user_info_dict = {
            "phone_number": serializer.data["phone_number"],
            "invite_code": serializer.data["invite_code"],
            "alien_invite_code": serializer.data.get("alien_invite_code"),
            "subscribers_your_invite_code": subscribers_list,
        }
        return JsonResponse(user_info_dict)


class AccountAlienInviteCode(APIView):
    """
    Класс для добавления чужого инвайт кода
    """

    @extend_schema(summary="Добавить чужой инвайт-код", tags=["User"])
    def post(self, request, *args, **kwargs):
        # проверка аунтификации
        if not request.user.is_authenticated:
            return JsonResponse(
                {"Status": False, "Error": "Log in required"}, status=403
            )

        # проверка вводил ли пользователь инвайт код
        serializer = UserSerializer(request.user)

        if serializer["alien_invite_code"]["code"].value:
            return JsonResponse(
                {"Status": False, "Error": "There can be only one code"}
            )

        # проверка данных
        if {"alien_invite_code"}.issubset(request.data):
            alien_invite_code_user = User.objects.filter(
                invite_code=request.data["alien_invite_code"]
            ).first()

            if alien_invite_code_user:
                # проверка не принадлежит ли код пользователю
                if request.user.phone_number == alien_invite_code_user.phone_number:
                    return JsonResponse(
                        {"Status": False, "Error": "You can't use your own code"}
                    )
                else:
                    # добовляем пользователя в request.data
                    request.data._mutable = True
                    request.data.update(
                        {
                            "code_user": str(request.user.id),
                            "owner_user": alien_invite_code_user.id,
                            "code": request.data["alien_invite_code"],
                        }
                    )
                    request.data._mutable = False

                    # проверка данных
                    alien_invite_code_serializer = AlienInviteCodeSerializer(
                        data=request.data
                    )
                    if alien_invite_code_serializer.is_valid():
                        # сохраняем чужой инвайт код
                        invite_code = alien_invite_code_serializer.save()
                        invite_code.save()
                        return JsonResponse({"Status": True})
                return JsonResponse({"Status": False, "Errors": "Incorrect data"})
            return JsonResponse(
                {
                    "Status": False,
                    "Errors": "Код не существует",
                }
            )
        return JsonResponse(
            {
                "Status": False,
                "Errors": "Не указаны все необходимые аргументы",
            }
        )
