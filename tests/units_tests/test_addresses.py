import pytest
from account.models import Address
from django.conf import settings


@pytest.mark.django_db
def test_first_address_is_default(user_1):
    address = Address.objects.create(
        user=user_1,
        address_line1="772 rte ..",
        city="Ons en Bray",
        postal_code="60650"
    )
    assert address.default is True


@pytest.mark.django_db
def test_max_addresses_limit(user_1, address_1_user1, address_2_user1):
    with pytest.raises(ValueError) as e:
        Address.objects.create(
        user=user_1,
        address_line1="772 rte ..",
        city="Ons en Bray",
        postal_code="60650"
    )
    assert str(e.value) == "Le nombre maximum d'adresses a été atteint."


@pytest.mark.django_db
def test_update_existing_address_when_max_reached(user_1, address_1_user1, address_2_user1):
    address_1_user1.address_line1 = "Updates address"
    address_1_user1.save()
    
    address_1_user1.refresh_from_db()
    
    assert address_1_user1.address_line1 == "Updates address"
