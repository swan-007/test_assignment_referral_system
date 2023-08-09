from rest_framework import serializers

from .models import User, PhonCode, AlienInviteCode
import random
import string

def simulator_invite_code():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 6))
    return rand_string


class AlienInviteCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlienInviteCode
        fields = ('owner_user', 'code', 'code_user')
        read_only_fields = ('id', )


class UserSerializer(serializers.ModelSerializer):
    alien_invite_code = AlienInviteCodeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'invite_code', 'alien_invite_code', 'owner_code',
                  'phone_number')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Метод для создания + добавление инвайт кода"""
        invite_code = simulator_invite_code()
        validated_data['invite_code'] = str(invite_code)
        return super().create(validated_data)



class PhonCodeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PhonCode
        fields = ('phon_code', 'user')
        read_only_fields = ('id',)
