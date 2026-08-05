# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartOfflineTaskRequest(DaraModel):
    def __init__(
        self,
        parallelism: int = None,
        timestamp: int = None,
        region_id: str = None,
    ):
        # The degree of task parallelism.
        self.parallelism = parallelism
        # The start offset.
        self.timestamp = timestamp
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

