import pytest
from django.contrib.auth import get_user_model
from account.models import Address


User = get_user_model()


@pytest.fixture
def user_1():
    return User.objects.create_user(username="gab", email="user1@example.com", first_name="User", 
                                    last_name="One", password="password123")


@pytest.fixture
def address_1_user_1(user_1):
    return Address.objects.create(
        user=user_1,
        address_line1="123 Main St",
        address_line2="Apt 4B",
        city="Paris",
        postal_code="75001",
    )


@pytest.fixture
def address_2_user_1(user_1):
    return Address.objects.create(
        user=user_1,
        address_line1="456 Elm St",
        address_line2="",
        city="Lyon",
        postal_code="69001",
    )