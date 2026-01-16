# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ResidentResourceAllocationStatus(DaraModel):
    def __init__(
        self,
        last_allocated_time: str = None,
        last_allocation: List[main_models.ResidentResourceAllocation] = None,
    ):
        self.last_allocated_time = last_allocated_time
        self.last_allocation = last_allocation

    def validate(self):
        if self.last_allocation:
            for v1 in self.last_allocation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_allocated_time is not None:
            result['lastAllocatedTime'] = self.last_allocated_time

        result['lastAllocation'] = []
        if self.last_allocation is not None:
            for k1 in self.last_allocation:
                result['lastAllocation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastAllocatedTime') is not None:
            self.last_allocated_time = m.get('lastAllocatedTime')

        self.last_allocation = []
        if m.get('lastAllocation') is not None:
            for k1 in m.get('lastAllocation'):
                temp_model = main_models.ResidentResourceAllocation()
                self.last_allocation.append(temp_model.from_map(k1))

        return self

