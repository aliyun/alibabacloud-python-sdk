# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class QueryStatisticResponseBody(DaraModel):
    def __init__(
        self,
        instance_capacity_each_type: Dict[str, Any] = None,
        instance_num_each_type: Dict[str, Any] = None,
        request_id: str = None,
        slot_num_each_type: Dict[str, Any] = None,
    ):
        self.instance_capacity_each_type = instance_capacity_each_type
        self.instance_num_each_type = instance_num_each_type
        self.request_id = request_id
        self.slot_num_each_type = slot_num_each_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_capacity_each_type is not None:
            result['InstanceCapacityEachType'] = self.instance_capacity_each_type

        if self.instance_num_each_type is not None:
            result['InstanceNumEachType'] = self.instance_num_each_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slot_num_each_type is not None:
            result['SlotNumEachType'] = self.slot_num_each_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCapacityEachType') is not None:
            self.instance_capacity_each_type = m.get('InstanceCapacityEachType')

        if m.get('InstanceNumEachType') is not None:
            self.instance_num_each_type = m.get('InstanceNumEachType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlotNumEachType') is not None:
            self.slot_num_each_type = m.get('SlotNumEachType')

        return self

