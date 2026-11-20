# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindSubs700Request(DaraModel):
    def __init__(
        self,
        industrial_id: str = None,
        order_id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: int = None,
        tel_x: str = None,
    ):
        # Optional. The Industrial Internet identification code, which has a one-to-one mapping with the OrderID. The code supports characters such as periods (.) and forward slashes (/) to separate code domains. The code must not contain non-printable characters, such as spaces or line feeds. This field is required when the service consumer generates the Industrial Internet identification code.
        self.industrial_id = industrial_id
        # The order ID. This parameter is required in practice. Encrypt the order ID for reporting to the regulatory platform.
        self.order_id = order_id
        self.owner_id = owner_id
        # The number pool key.
        # 
        # To obtain the **number pool key**, go to the [Number pool management](https://dyplsnext.console.aliyun.com/number-pool) page in the Phone Number Privacy Protection console.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number binding ID.
        # 
        # This parameter is required.
        self.subs_id = subs_id
        # The intermediate number X. If the service consumer does not specify number X, the application platform assigns a number from the number pool as number X.
        # 
        # This parameter is required.
        self.tel_x = tel_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industrial_id is not None:
            result['IndustrialId'] = self.industrial_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.subs_id is not None:
            result['SubsId'] = self.subs_id

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndustrialId') is not None:
            self.industrial_id = m.get('IndustrialId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

