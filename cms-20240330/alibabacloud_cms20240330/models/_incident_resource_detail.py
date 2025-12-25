# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class IncidentResourceDetail(DaraModel):
    def __init__(
        self,
        extra_id: str = None,
        resource_id: Dict[str, Any] = None,
        type: str = None,
    ):
        self.extra_id = extra_id
        self.resource_id = resource_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_id is not None:
            result['extraId'] = self.extra_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extraId') is not None:
            self.extra_id = m.get('extraId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

