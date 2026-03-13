# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Location(DaraModel):
    def __init__(
        self,
        location_type: str = None,
        location_value: Dict[str, Any] = None,
    ):
        self.location_type = location_type
        self.location_value = location_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location_type is not None:
            result['LocationType'] = self.location_type

        if self.location_value is not None:
            result['LocationValue'] = self.location_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationType') is not None:
            self.location_type = m.get('LocationType')

        if m.get('LocationValue') is not None:
            self.location_value = m.get('LocationValue')

        return self

