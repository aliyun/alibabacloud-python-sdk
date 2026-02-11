# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTraceAppByNameRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        trace_app_name: str = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.trace_app_name = trace_app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')

        return self

