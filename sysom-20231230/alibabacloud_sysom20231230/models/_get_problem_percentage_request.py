# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProblemPercentageRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        cluster: str = None,
        end: float = None,
        instance: str = None,
        start: float = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The cluster ID.
        self.cluster = cluster
        # The end time.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        self.instance = instance
        # The start time.
        # 
        # This parameter is required.
        self.start = start
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.end is not None:
            result['end'] = self.end

        if self.instance is not None:
            result['instance'] = self.instance

        if self.start is not None:
            result['start'] = self.start

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

