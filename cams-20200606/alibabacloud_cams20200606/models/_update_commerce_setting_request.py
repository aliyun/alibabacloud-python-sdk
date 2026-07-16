# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCommerceSettingRequest(DaraModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable the shopping cart. Valid values:
        # 
        # - true: Enable the shopping cart.
        # 
        # - false: Disable the shopping cart.
        # 
        # This parameter is required.
        self.cart_enable = cart_enable
        # Specifies whether to enable the product catalog. Valid values:
        # 
        # - true: Enable the product catalog.
        # 
        # - false: Disable the product catalog.
        # 
        # This parameter is required.
        self.catalog_visible = catalog_visible
        # The Space ID of the Independent Software Vendor (ISV) sub-customer.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable

        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')

        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

