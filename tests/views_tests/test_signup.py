import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client

from pytest_django.asserts import assertTemplateUsed


User = get_user_model()


VALID_SIGNUP_DATA = {
    "email": "jc@gmail.com",
    "username": "jc",
    "password1": "Mot_de_Passe123",
    "password2": "Mot_de_Passe123"
}


@pytest.mark.django_db
def test_signup_view_post(client):
    response = client.post(reverse("account:signup"), data=VALID_SIGNUP_DATA)
    # print(response.context["form"].errors)
    user = User.objects.get(email=VALID_SIGNUP_DATA["email"])
    assert user.is_active is False
    assert response.status_code == 302


def test_signup_view_get(client: Client):
    response = client.get(reverse("account:signup"))
    assert response.status_code == 200
    assertTemplateUsed(response, "account/signup.html")
