# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryGateVerifyRecordListRequest(DaraModel):
    def __init__(
        self,
        authentication_type: int = None,
        os_type: str = None,
        owner_id: int = None,
        phone_num: str = None,
        prod_code: str = None,
        query_date: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.authentication_type = authentication_type
        # This parameter is required.
        self.os_type = os_type
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_num = phone_num
        self.prod_code = prod_code
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.query_date is not None:
            result['QueryDate'] = self.query_date

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

