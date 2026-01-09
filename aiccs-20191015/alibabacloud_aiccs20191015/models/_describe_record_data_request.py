# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordDataRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_type: str = None,
        acid: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sec_level: int = None,
    ):
        self.account_id = account_id
        self.account_type = account_type
        self.acid = acid
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sec_level = sec_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.acid is not None:
            result['Acid'] = self.acid

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sec_level is not None:
            result['SecLevel'] = self.sec_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecLevel') is not None:
            self.sec_level = m.get('SecLevel')

        return self

