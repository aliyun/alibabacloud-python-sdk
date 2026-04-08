# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class AiPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

