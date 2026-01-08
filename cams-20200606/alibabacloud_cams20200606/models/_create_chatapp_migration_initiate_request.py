# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatappMigrationInitiateRequest(DaraModel):
    def __init__(
        self,
        country_code: str = None,
        cust_space_id: str = None,
        mobile_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The code of the country or region.
        # 
        # This parameter is required.
        self.country_code = country_code
        # The space ID of the user within the ISV account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The mobile number without the country code or region code.
        # 
        # This parameter is required.
        self.mobile_number = mobile_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

