# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MapFromHavanaBindIdShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        havana_bind_id: str = None,
        havana_bind_stations_shrink: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.havana_bind_id = havana_bind_id
        # This parameter is required.
        self.havana_bind_stations_shrink = havana_bind_stations_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.havana_bind_id is not None:
            result['HavanaBindId'] = self.havana_bind_id

        if self.havana_bind_stations_shrink is not None:
            result['HavanaBindStations'] = self.havana_bind_stations_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('HavanaBindId') is not None:
            self.havana_bind_id = m.get('HavanaBindId')

        if m.get('HavanaBindStations') is not None:
            self.havana_bind_stations_shrink = m.get('HavanaBindStations')

        return self

