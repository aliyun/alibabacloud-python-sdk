# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        phase: str = None,
        slot_num: int = None,
        used_capacity: str = None,
    ):
        self.code = code
        self.message = message
        self.phase = phase
        self.slot_num = slot_num
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

