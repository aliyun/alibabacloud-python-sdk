# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ComponentCapacityConstraint(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        max_capacity: int = None,
        min_capacity: int = None,
    ):
        self.component_type = component_type
        self.max_capacity = max_capacity
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.max_capacity is not None:
            result['maxCapacity'] = self.max_capacity

        if self.min_capacity is not None:
            result['minCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('maxCapacity') is not None:
            self.max_capacity = m.get('maxCapacity')

        if m.get('minCapacity') is not None:
            self.min_capacity = m.get('minCapacity')

        return self

