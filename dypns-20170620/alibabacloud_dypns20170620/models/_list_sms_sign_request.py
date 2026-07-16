# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSmsSignRequest(DaraModel):
    def __init__(
        self,
        customer_id: int = None,
        owner_id: int = None,
        prod_code: str = None,
        query_sms_sign: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.query_sms_sign = query_sms_sign
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.query_sms_sign is not None:
            result['QuerySmsSign'] = self.query_sms_sign

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('QuerySmsSign') is not None:
            self.query_sms_sign = m.get('QuerySmsSign')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

