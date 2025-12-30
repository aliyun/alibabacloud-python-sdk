# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDnsGtmMonitorStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
        status: str = None,
    ):
        # The language of the values for specific response parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The ID of the health check task.
        # 
        # This parameter is required.
        self.monitor_config_id = monitor_config_id
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   OPEN: enables the health check feature.
        # *   CLOSE: disables the health check feature.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

