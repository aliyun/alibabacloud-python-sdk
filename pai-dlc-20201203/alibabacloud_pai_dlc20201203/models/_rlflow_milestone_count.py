# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowMilestoneCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        milestone: str = None,
    ):
        # The number of in-transit trajectories that remain at this milestone.
        self.count = count
        # The milestone. Valid values are the same as those of Stuck[].Milestone.
        self.milestone = milestone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.milestone is not None:
            result['Milestone'] = self.milestone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Milestone') is not None:
            self.milestone = m.get('Milestone')

        return self

