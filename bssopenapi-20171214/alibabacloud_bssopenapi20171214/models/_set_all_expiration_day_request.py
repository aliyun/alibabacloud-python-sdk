# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAllExpirationDayRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        unify_expire_day: str = None,
    ):
        self.owner_id = owner_id
        # The current unified expiration date settings only support unexpired ECS instances. Expired instances cannot be aligned to the unified expiration date. After the settings are complete, you can align the renewal time with the configured unified expiration time.
        # 
        # Valid values: 1 to 28, representing the 1st to the 28th day of each month.
        # 
        # This parameter is required.
        self.unify_expire_day = unify_expire_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.unify_expire_day is not None:
            result['UnifyExpireDay'] = self.unify_expire_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('UnifyExpireDay') is not None:
            self.unify_expire_day = m.get('UnifyExpireDay')

        return self

