import pytest
from django.contrib.auth import get_user_model
from account.models import Address


User = get_user_model()


@pytest.fixture
def user_1():
    return User.objects.create_user(username="Gab", email="e@.e.com", 
                                    password="password1234")


@pytest.fixture
def address_1_user1(user_1):
    return Address.objects.create(
        user=user_1,
        address_line1="773 rte ..",
        city="Ons en Bra",
        postal_code="60650"
    )


@pytest.fixture
def address_2_user1(user_1):
    return Address.objects.create(
        user=user_1,
        address_line1="774 rte ..",
        city="Ons en Bra",
        postal_code="60650"
    )
