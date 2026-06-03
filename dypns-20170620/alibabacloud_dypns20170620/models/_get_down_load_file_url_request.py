# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDownLoadFileUrlRequest(DaraModel):
    def __init__(
        self,
        acct_id: int = None,
        id: int = None,
        order_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.acct_id = acct_id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.order_id = order_id
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
        if self.acct_id is not None:
            result['AcctId'] = self.acct_id

        if self.id is not None:
            result['Id'] = self.id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcctId') is not None:
            self.acct_id = m.get('AcctId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

