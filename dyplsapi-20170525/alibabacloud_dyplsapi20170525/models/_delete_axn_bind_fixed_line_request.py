# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAxnBindFixedLineRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        order_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sub_id: str = None,
        ts: str = None,
    ):
        # The number pool ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The unique identifier of the message request.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding ID.
        # 
        # This parameter is required.
        self.sub_id = sub_id
        # The business timestamp. Format: yyyyMMddHHmmssSSS. The time is in UTC+8, in 24-hour format, accurate to milliseconds.
        # 
        # This parameter is required.
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

