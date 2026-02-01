# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHealthPercentageRequest(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        end: float = None,
        instance: str = None,
        start: float = None,
    ):
        self.cluster = cluster
        # This parameter is required.
        self.end = end
        self.instance = instance
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.end is not None:
            result['end'] = self.end

        if self.instance is not None:
            result['instance'] = self.instance

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

