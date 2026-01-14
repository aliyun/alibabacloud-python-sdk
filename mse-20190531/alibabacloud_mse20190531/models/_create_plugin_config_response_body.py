# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePluginConfigResponseBody(DaraModel):
    def __init__(
        self,
        plugin_config_id: int = None,
        request_id: str = None,
    ):
        # The plug-in configuration ID.
        self.plugin_config_id = plugin_config_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_config_id is not None:
            result['PluginConfigID'] = self.plugin_config_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginConfigID') is not None:
            self.plugin_config_id = m.get('PluginConfigID')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

