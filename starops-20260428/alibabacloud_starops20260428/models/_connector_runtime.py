# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConnectorRuntime(DaraModel):
    def __init__(
        self,
        capability_id: str = None,
        extension_name: str = None,
        mode: str = None,
        plugin_id: str = None,
        satellite_id: str = None,
    ):
        # The native client capability referenced by the SATELLITE runtime. This parameter is mutually exclusive with extensionName.
        self.capability_id = capability_id
        # The environment agent extension name referenced by the SATELLITE runtime. This parameter is mutually exclusive with capabilityId.
        self.extension_name = extension_name
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
        if self.capability_id is not None:
            result['capabilityId'] = self.capability_id

        if self.extension_name is not None:
            result['extensionName'] = self.extension_name

        if self.mode is not None:
            result['mode'] = self.mode

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.satellite_id is not None:
            result['satelliteId'] = self.satellite_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilityId') is not None:
            self.capability_id = m.get('capabilityId')

        if m.get('extensionName') is not None:
            self.extension_name = m.get('extensionName')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('satelliteId') is not None:
            self.satellite_id = m.get('satelliteId')

        return self

