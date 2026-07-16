# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TurnOffZoneRequest(DaraModel):
    def __init__(
        self,
        hp_alb_zone_drained: bool = None,
        zone: str = None,
    ):
        self.hp_alb_zone_drained = hp_alb_zone_drained
        # The zone of the instance.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hp_alb_zone_drained is not None:
            result['hpAlbZoneDrained'] = self.hp_alb_zone_drained

        if self.zone is not None:
            result['zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hpAlbZoneDrained') is not None:
            self.hp_alb_zone_drained = m.get('hpAlbZoneDrained')

        if m.get('zone') is not None:
            self.zone = m.get('zone')

        return self

