# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BuySecretNoRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        display_pool: bool = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        spec_id: int = None,
    ):
        # Specifies the home location of the phone number.
        # 
        # > 
        # 
        # *   The home location can be set only to a location in the Chinese mainland.
        # 
        # *   A phone number that starts with 95 does not have a home location. If you purchase a phone number that starts with 95, set this parameter to **Nationwide**.
        # 
        # This parameter is required.
        self.city = city
        # Specifies whether to add the phone number to the pool of numbers that will be displayed during calls.
        # 
        # >  This parameter takes effect only for customers who have enabled the number display feature.
        self.display_pool = display_pool
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The prefix of the phone number. If you specify the value of **SecretNo** when you purchase a phone number, a phone number starting with the specified prefix is selected.
        # 
        # >  You can specify up to 18 digits of the phone number prefix.
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

        if self.display_pool is not None:
            result['DisplayPool'] = self.display_pool

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

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

        if m.get('DisplayPool') is not None:
            self.display_pool = m.get('DisplayPool')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        return self

