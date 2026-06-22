# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManagedScalingConstraints(DaraModel):
    def __init__(
        self,
        max_capacity: int = None,
        max_on_demand_capacity: int = None,
        min_capacity: int = None,
    ):
        # The maximum number of nodes in a node group.
        self.max_capacity = max_capacity
        # The maximum number of pay-as-you-go task nodes.
        self.max_on_demand_capacity = max_on_demand_capacity
        # The minimum number of nodes in a node group.
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.max_on_demand_capacity is not None:
            result['MaxOnDemandCapacity'] = self.max_on_demand_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MaxOnDemandCapacity') is not None:
            self.max_on_demand_capacity = m.get('MaxOnDemandCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

