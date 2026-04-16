# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataZoneSupportCompactionServiceValue(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
        resource_level: str = None,
        recommended: bool = None,
    ):
        self.zone_id = zone_id
        self.resource_level = resource_level
        self.recommended = recommended

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        if self.resource_level is not None:
            result['resourceLevel'] = self.resource_level

        if self.recommended is not None:
            result['recommended'] = self.recommended

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        if m.get('resourceLevel') is not None:
            self.resource_level = m.get('resourceLevel')

        if m.get('recommended') is not None:
            self.recommended = m.get('recommended')

        return self

