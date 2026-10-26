# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppPluginFilesRequest(DaraModel):
    def __init__(
        self,
        plugin_id: str = None,
        plugin_version: str = None,
    ):
        # The ID of the gateway plugin.
        self.plugin_id = plugin_id
        # The version number. If you do not specify this parameter, the currently active version is used.
        self.plugin_version = plugin_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        return self

