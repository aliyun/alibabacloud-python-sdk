# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateBlackNoRequest(DaraModel):
    def __init__(
        self,
        black_no: str = None,
        operate_type: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tips: str = None,
    ):
        # The phone number to be added to or deleted from the blacklist.
        # 
        # This parameter is required.
        self.black_no = black_no
        # The type of the operation on the phone number. Valid values:
        # 
        # *   **AddBlack**: adds the phone number to the blacklist.
        # *   **DeleteBlack**: deletes the phone number from the blacklist.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description.
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_no is not None:
            result['BlackNo'] = self.black_no

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tips is not None:
            result['Tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        return self

