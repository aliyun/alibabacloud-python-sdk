# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class GetAutopilotPolicyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAutopilotPolicyResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The Autopilot tuning policy response data.
        self.data = data
        # The business error code. This field is not empty when success is false. This field is empty when success is true.
        self.error_code = error_code
        # The business error message. This field is not empty when success is false. This field is empty when success is true.
        self.error_message = error_message
        # The business status code, which is always 200. Use the success field to determine whether the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetAutopilotPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetAutopilotPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        policy_config: main_models.AutopilotPolicy = None,
    ):
        # Indicates whether automatic tuning is enabled. A value of true indicates that automatic tuning is in the ACTIVE state. A value of false indicates that tuning is not enabled.
        self.enabled = enabled
        # The tuning policy configuration.
        self.policy_config = policy_config

    def validate(self):
        if self.policy_config:
            self.policy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('policyConfig') is not None:
            temp_model = main_models.AutopilotPolicy()
            self.policy_config = temp_model.from_map(m.get('policyConfig'))

        return self

