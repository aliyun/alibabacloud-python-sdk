# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CheckInstanceSupportRequest(DaraModel):
    def __init__(
        self,
        instances: List[str] = None,
        region: str = None,
    ):
        self.instances = instances
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['instances'] = self.instances

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

