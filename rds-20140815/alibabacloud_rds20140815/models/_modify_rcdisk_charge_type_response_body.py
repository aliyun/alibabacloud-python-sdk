# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyRCDiskChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        expired_time: List[str] = None,
        instance_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

