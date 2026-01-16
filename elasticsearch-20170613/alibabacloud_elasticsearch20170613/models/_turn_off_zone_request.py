# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TurnOffZoneRequest(DaraModel):
    def __init__(
        self,
        zone: str = None,
    ):
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone is not None:
            result['zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zone') is not None:
            self.zone = m.get('zone')

        return self

