# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceStatistic(DaraModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

