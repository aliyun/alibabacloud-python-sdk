# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchAdvancedMonitoringResponseBody(DaraModel):
    def __init__(
        self,
        advanced_monitoring_enabled: bool = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Indicates whether the advanced application monitoring feature is enabled. Valid values:
        # 
        # *   true: The advanced application monitoring feature is enabled.
        # *   false: The advanced application monitoring feature is disabled.
        self.advanced_monitoring_enabled = advanced_monitoring_enabled
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_monitoring_enabled is not None:
            result['AdvancedMonitoringEnabled'] = self.advanced_monitoring_enabled

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedMonitoringEnabled') is not None:
            self.advanced_monitoring_enabled = m.get('AdvancedMonitoringEnabled')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

