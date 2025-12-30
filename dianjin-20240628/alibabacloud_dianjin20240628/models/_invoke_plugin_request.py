# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class InvokePluginRequest(DaraModel):
    def __init__(
        self,
        params: Dict[str, Any] = None,
        plugin_id: str = None,
    ):
        self.params = params
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['params'] = self.params

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        return self

