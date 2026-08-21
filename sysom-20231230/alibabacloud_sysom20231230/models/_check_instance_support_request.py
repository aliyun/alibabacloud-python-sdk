# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CheckInstanceSupportRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        instances: List[str] = None,
        region: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The list of instance IDs to check.
        self.instances = instances
        # The region to which the instances belong. All instance IDs specified in instances must belong to the same region.
        self.region = region
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

        if self.instances is not None:
            result['instances'] = self.instances

        if self.region is not None:
            result['region'] = self.region

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

