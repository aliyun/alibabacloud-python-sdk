# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstanceInspectionRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        instance: str = None,
        items: List[str] = None,
        metric_source: str = None,
        region: str = None,
        source: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The instance ID.
        self.instance = instance
        # The anomaly items.
        self.items = items
        # The metric source.
        self.metric_source = metric_source
        # The region to which the instance belongs.
        self.region = region
        # The source.
        self.source = source
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

        if self.instance is not None:
            result['instance'] = self.instance

        if self.items is not None:
            result['items'] = self.items

        if self.metric_source is not None:
            result['metricSource'] = self.metric_source

        if self.region is not None:
            result['region'] = self.region

        if self.source is not None:
            result['source'] = self.source

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('metricSource') is not None:
            self.metric_source = m.get('metricSource')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

