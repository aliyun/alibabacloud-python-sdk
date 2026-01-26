# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAppListRequest(DaraModel):
    def __init__(
        self,
        pids: List[str] = None,
        region_id: str = None,
    ):
        # The list of PIDs for the applications monitored by Application Monitoring.
        self.pids = pids
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pids is not None:
            result['Pids'] = self.pids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

