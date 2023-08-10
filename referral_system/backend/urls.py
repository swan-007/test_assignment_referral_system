from django.urls import path
from backend.views import RegisterAccount, ConfirmAccount, AccountDetails, AccountAlienInviteCode

urlpatterns = [
    path("user/register", RegisterAccount.as_view()),
    path("user/register/confirm", ConfirmAccount.as_view()),
    path("user/details", AccountDetails.as_view()),
    path("user/alienInvitecode", AccountAlienInviteCode.as_view()),
]
