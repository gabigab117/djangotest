import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


User = get_user_model()


VALID_DATA = {
    "email": "g@g.com",
    "username": "Gab",
    "password1": "Mot_de_Passe_123456",
    "password2": "Mot_de_Passe_123456"
}


@pytest.mark.django_db
def test_signup(client: Client):
    response = client.post(reverse("account:signup"), data=VALID_DATA)
    user = User.objects.get(email=VALID_DATA["email"])
    assert response.status_code == 302
    assert user.is_active is False
