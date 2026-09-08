# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressSync(DaraModel):
    def __init__(
        self,
        cost: float = None,
        state: str = None,
    ):
        # The parameter synchronization duration in seconds. This property has a value only when State is end.
        self.cost = cost
        # begin / end
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

