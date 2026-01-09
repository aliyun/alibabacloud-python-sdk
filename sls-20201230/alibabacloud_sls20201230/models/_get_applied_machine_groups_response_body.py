# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAppliedMachineGroupsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        machinegroups: List[str] = None,
    ):
        # The number of returned machine groups.
        self.count = count
        # The names of the returned machine groups.
        self.machinegroups = machinegroups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.machinegroups is not None:
            result['machinegroups'] = self.machinegroups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('machinegroups') is not None:
            self.machinegroups = m.get('machinegroups')

        return self

