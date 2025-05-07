import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from pytest_django.asserts import assertTemplateUsed


User = get_user_model()


VALID_SIGNUP_DATA = {
    "email": "j@j.com",
    "username": "gab",
    "password1": "Mot_de_Passe123",
    "password2": "Mot_de_Passe123",
}

@pytest.mark.django_db
def test_signup_view_post(client):
    response = client.post(reverse("account:signup"), data=VALID_SIGNUP_DATA)
    # print(response.context["form"].errors)
    user = User.objects.get(email=VALID_SIGNUP_DATA["email"])
    assert response.status_code == 302
    assert user.is_active is False
    assert user.username == VALID_SIGNUP_DATA["username"]


def test_signup_view_get(client):
    response = client.get(reverse("account:signup"))
    assertTemplateUsed(response, "account/signup.html")
    assert response.status_code == 200