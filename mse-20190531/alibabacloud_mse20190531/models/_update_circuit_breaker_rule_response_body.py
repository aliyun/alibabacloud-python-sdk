# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateCircuitBreakerRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateCircuitBreakerRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The details of the rule.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The request was successful.
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The request failed.
        # 
        #     <!-- -->
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
            temp_model = main_models.UpdateCircuitBreakerRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateCircuitBreakerRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        half_open_base_amount_per_step: int = None,
        half_open_recovery_step_num: int = None,
        id: int = None,
        max_allowed_rt_ms: int = None,
        min_request_amount: int = None,
        namespace: str = None,
        resource: str = None,
        retry_timeout_ms: int = None,
        stat_interval_ms: int = None,
        strategy: int = None,
        threshold: float = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # Indicates whether the rule is enabled.
        self.enable = enable
        # The minimum number of requests that can be passed in each step after circuit breaking recovers.
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        # The number of circuit breaking recovery steps.
        self.half_open_recovery_step_num = half_open_recovery_step_num
        # The ID of the rule.
        self.id = id
        # The maximum RT. Unit: milliseconds. If the RT of a request is greater than the value of this parameter, a slow call is counted. If you set Strategy to 0, you must specify this parameter.
        self.max_allowed_rt_ms = max_allowed_rt_ms
        # The minimum number of requests to trigger circuit breaking. If the number of requests in the current time window is less than the value of this parameter, circuit breaking is not triggered even if the circuit breaking rule is met.
        self.min_request_amount = min_request_amount
        # The microservice namespace to which the application belongs.
        self.namespace = namespace
        # The name of the interface to which the rule is applicable. The interface name must be the same as the name on the interface details page in the console.
        self.resource = resource
        # The period in which circuit breaking is implemented. Unit: milliseconds. If circuit breaking is implemented on the requests for the route, the calls to all the requests for the route fail in the configured circuit breaking period.
        self.retry_timeout_ms = retry_timeout_ms
        # The length of the time window. Unit: milliseconds. The valid range is from 1 second to 120 minutes.
        self.stat_interval_ms = stat_interval_ms
        # The threshold type.
        # 
        # Valid values:
        # 
        # *   0
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     slow call proportion
        # 
        #     <!-- -->
        # 
        # *   1
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     abnormal proportion
        # 
        #     <!-- -->
        self.strategy = strategy
        # A percentage threshold for triggering circuit breaking. Valid values: 0-1. These values represent 0% to 100%.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.half_open_base_amount_per_step is not None:
            result['HalfOpenBaseAmountPerStep'] = self.half_open_base_amount_per_step

        if self.half_open_recovery_step_num is not None:
            result['HalfOpenRecoveryStepNum'] = self.half_open_recovery_step_num

        if self.id is not None:
            result['Id'] = self.id

        if self.max_allowed_rt_ms is not None:
            result['MaxAllowedRtMs'] = self.max_allowed_rt_ms

        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.retry_timeout_ms is not None:
            result['RetryTimeoutMs'] = self.retry_timeout_ms

        if self.stat_interval_ms is not None:
            result['StatIntervalMs'] = self.stat_interval_ms

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('HalfOpenBaseAmountPerStep') is not None:
            self.half_open_base_amount_per_step = m.get('HalfOpenBaseAmountPerStep')

        if m.get('HalfOpenRecoveryStepNum') is not None:
            self.half_open_recovery_step_num = m.get('HalfOpenRecoveryStepNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxAllowedRtMs') is not None:
            self.max_allowed_rt_ms = m.get('MaxAllowedRtMs')

        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('RetryTimeoutMs') is not None:
            self.retry_timeout_ms = m.get('RetryTimeoutMs')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

