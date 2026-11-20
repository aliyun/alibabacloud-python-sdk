# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySecretNoRemainRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        spec_id: int = None,
    ):
        # The home location of the phone number.
        # 
        # *   If **SpecId** is set to 1 or 2, you can specify the **City** parameter to query the quantity of available phone numbers.
        # 
        # 1.  You can enter a single city name to perform a query.
        # 2.  You can enter National to query the quantity of remaining phone numbers available in the Chinese mainland for online purchase.
        # 3.  You can enter National List to query the cities with available phone numbers and the quantities of remaining phone numbers in the Chinese mainland. Cities without available phone numbers will not be returned.
        # 
        # *   If **SpecId** is set to 3, home locations are not distinguished for phone numbers that start with 95 and only the quantity of all the remaining phone numbers that start with 95 and are available for online purchase can be queried. If SpecId is set to 3, **City** must be set to **Nationwide**.
        # 
        # >  Home locations can be set to only locations in the Chinese mainland.
        # 
        # This parameter is required.
        self.city = city
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The prefix of the phone number. When you call the QuerySecretNoRemain operation with **SecretNo** specified, the quantity of remaining phone numbers with the specified prefix that are available for online purchase is queried.
        # 
        # Up to 18 digits of a phone number prefix can be specified.
        self.secret_no = secret_no
        # The type of the phone number. Valid values:
        # 
        # *   **1**: a phone number assigned by a virtual network operator, that is, a phone number that belongs to the 170 or 171 number segment.
        # *   **2**: a phone number provided by a carrier.
        # *   **3**: a phone number that starts with 95.
        # 
        # This parameter is required.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        return self

