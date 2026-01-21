# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitoringAgentConfigResponseBody(DaraModel):
    def __init__(
        self,
        auto_install: bool = None,
        code: str = None,
        enable_active_alert: str = None,
        enable_install_agent_new_ecs: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the CloudMonitor agent is automatically installed on existing Elastic Compute Service (ECS) instances. Valid values:
        # 
        # *   true
        # *   false
        self.auto_install = auto_install
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The cloud services for which proactive alerting is enabled.
        self.enable_active_alert = enable_active_alert
        # Indicates whether the CloudMonitor agent is automatically installed on newly purchased ECS instances. Valid values:
        # 
        # *   true
        # *   false
        self.enable_install_agent_new_ecs = enable_install_agent_new_ecs
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.code is not None:
            result['Code'] = self.code

        if self.enable_active_alert is not None:
            result['EnableActiveAlert'] = self.enable_active_alert

        if self.enable_install_agent_new_ecs is not None:
            result['EnableInstallAgentNewECS'] = self.enable_install_agent_new_ecs

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnableActiveAlert') is not None:
            self.enable_active_alert = m.get('EnableActiveAlert')

        if m.get('EnableInstallAgentNewECS') is not None:
            self.enable_install_agent_new_ecs = m.get('EnableInstallAgentNewECS')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

