# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutoRenewInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew_cycle: str = None,
        auto_renew_duration: int = None,
        order_biz_id: int = None,
        owner_id: int = None,
        type: str = None,
    ):
        self.auto_renew_cycle = auto_renew_cycle
        self.auto_renew_duration = auto_renew_duration
        # This parameter is required.
        self.order_biz_id = order_biz_id
        self.owner_id = owner_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_cycle is not None:
            result['AutoRenewCycle'] = self.auto_renew_cycle

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewCycle') is not None:
            self.auto_renew_cycle = m.get('AutoRenewCycle')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

