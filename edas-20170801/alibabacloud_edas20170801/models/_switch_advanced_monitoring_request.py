# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchAdvancedMonitoringRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable_advanced_monitoring: bool = None,
    ):
        # The ID of the application for which you want to query or configure the advanced application monitoring feature.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to enable the advanced application monitoring feature. Valid values:
        # 
        # *   true: enables the advanced application monitoring feature.
        # *   false: disables the advanced application monitoring feature.
        # 
        # If you call this operation to query the status of the advanced application monitoring feature, you do not need to specify this parameter.
        self.enable_advanced_monitoring = enable_advanced_monitoring

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.enable_advanced_monitoring is not None:
            result['EnableAdvancedMonitoring'] = self.enable_advanced_monitoring

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EnableAdvancedMonitoring') is not None:
            self.enable_advanced_monitoring = m.get('EnableAdvancedMonitoring')

        return self

