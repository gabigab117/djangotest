import pytest
from account.models import Address
from django.conf import settings


@pytest.mark.django_db
def test_first_address_is_default(user_1):
    """Test that the first address created for a user is set as default"""
    address = Address.objects.create(
        user=user_1,
        address_line1="789 Oak St",
        city="Paris",
        postal_code="75002",
    )
    assert address.default is True


@pytest.mark.django_db
def test_max_addresses_limit(user_1, address_1_user_1, address_2_user_1):
    """Test that user cannot exceed max addresses limit"""
    
    # Try to create third address
    with pytest.raises(ValueError) as exc:
        Address.objects.create(
            user=user_1,
            address_line1="Address 3",
            city="Paris",
            postal_code="75003",
        )
    assert str(exc.value) == "Le nombre maximum d'adresses a été atteint."


@pytest.mark.django_db
def test_update_existing_address_when_max_reached(user_1, address_1_user_1, address_2_user_1):
    """Test that existing address can be updated when max limit is reached"""
    
    # Update existing address should work
    address_2_user_1.address_line1 = "Updated Address"
    address_2_user_1.save()
    
    address_2_user_1.refresh_from_db()
    assert address_2_user_1.address_line1 == "Updated Address"