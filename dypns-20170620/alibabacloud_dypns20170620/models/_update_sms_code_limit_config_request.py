# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmsCodeLimitConfigRequest(DaraModel):
    def __init__(
        self,
        limit_day: int = None,
        limit_hour: int = None,
        limit_id: int = None,
        limit_minute: int = None,
        limit_other: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.limit_day = limit_day
        self.limit_hour = limit_hour
        # This parameter is required.
        self.limit_id = limit_id
        self.limit_minute = limit_minute
        self.limit_other = limit_other
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
        if self.limit_day is not None:
            result['LimitDay'] = self.limit_day

        if self.limit_hour is not None:
            result['LimitHour'] = self.limit_hour

        if self.limit_id is not None:
            result['LimitId'] = self.limit_id

        if self.limit_minute is not None:
            result['LimitMinute'] = self.limit_minute

        if self.limit_other is not None:
            result['LimitOther'] = self.limit_other

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitDay') is not None:
            self.limit_day = m.get('LimitDay')

        if m.get('LimitHour') is not None:
            self.limit_hour = m.get('LimitHour')

        if m.get('LimitId') is not None:
            self.limit_id = m.get('LimitId')

        if m.get('LimitMinute') is not None:
            self.limit_minute = m.get('LimitMinute')

        if m.get('LimitOther') is not None:
            self.limit_other = m.get('LimitOther')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

