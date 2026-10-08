# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SynchronizeResourceRequest(DaraModel):
    def __init__(
        self,
        resource_ids: str = None,
        type: str = None,
    ):
        # The ID of the resource. This parameter is required only when you set the Type parameter to `ecs`. If you specify multiple IDs, separate them with commas (,). You can synchronize up to 50 resources at a time.
        self.resource_ids = resource_ids
        # The type of the resource to be synchronized. Valid values: `ecs, slb, vpc, and all`. These values are case-sensitive.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

