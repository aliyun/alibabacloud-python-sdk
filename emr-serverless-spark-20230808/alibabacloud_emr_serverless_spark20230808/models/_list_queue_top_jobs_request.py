# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueueTopJobsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        top_n: int = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The maximum number of jobs to return. The maximum value is 10.
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.top_n is not None:
            result['topN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topN') is not None:
            self.top_n = m.get('topN')

        return self

