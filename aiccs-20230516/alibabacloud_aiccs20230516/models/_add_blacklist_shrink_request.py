# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddBlacklistShrinkRequest(DaraModel):
    def __init__(
        self,
        expired_day: str = None,
        numbers_shrink: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 有效天数
        # 
        # This parameter is required.
        self.expired_day = expired_day
        # 号码列表
        # 
        # This parameter is required.
        self.numbers_shrink = numbers_shrink
        self.owner_id = owner_id
        # 备注
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day

        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')

        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

