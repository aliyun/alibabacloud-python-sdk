# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConnectorRuntime(DaraModel):
    def __init__(
        self,
        mode: str = None,
        plugin_id: str = None,
        satellite_id: str = None,
    ):
        # Runtime mode
        # 
        # This parameter is required.
        self.mode = mode
        # Plugin ID
        self.plugin_id = plugin_id
        # Satellite ID
        self.satellite_id = satellite_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.satellite_id is not None:
            result['satelliteId'] = self.satellite_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('satelliteId') is not None:
            self.satellite_id = m.get('satelliteId')

        return self

