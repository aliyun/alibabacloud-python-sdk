# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetSecurityCheckResultBaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSecurityCheckResultBaseInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # >  200: The request was successful. Other codes (such as 500 or 400): An error occurred.
        self.code = code
        # The returned data list.
        self.data = data
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the current API call itself was successful. This does not indicate the success of subsequent business operations.
        # 
        # - **true**: Successful.
        # - **false**: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSecurityCheckResultBaseInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSecurityCheckResultBaseInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        config_completed: str = None,
        pending_security_alert_count: int = None,
        pending_vulnerability_count: int = None,
        progress: str = None,
    ):
        # The configuration item check result.
        self.config_completed = config_completed
        # The number of pending security alerts.
        self.pending_security_alert_count = pending_security_alert_count
        # The number of pending vulnerabilities.
        self.pending_vulnerability_count = pending_vulnerability_count
        # The percentage of the health check task progress.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_completed is not None:
            result['ConfigCompleted'] = self.config_completed

        if self.pending_security_alert_count is not None:
            result['PendingSecurityAlertCount'] = self.pending_security_alert_count

        if self.pending_vulnerability_count is not None:
            result['PendingVulnerabilityCount'] = self.pending_vulnerability_count

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCompleted') is not None:
            self.config_completed = m.get('ConfigCompleted')

        if m.get('PendingSecurityAlertCount') is not None:
            self.pending_security_alert_count = m.get('PendingSecurityAlertCount')

        if m.get('PendingVulnerabilityCount') is not None:
            self.pending_vulnerability_count = m.get('PendingVulnerabilityCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

