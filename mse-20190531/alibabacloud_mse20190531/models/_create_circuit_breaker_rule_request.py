# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCircuitBreakerRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        enable: bool = None,
        half_open_base_amount_per_step: int = None,
        half_open_recovery_step_num: int = None,
        max_allowed_rt_ms: int = None,
        min_request_amount: int = None,
        namespace: str = None,
        region_id: str = None,
        resource: str = None,
        resource_type: int = None,
        retry_timeout_ms: int = None,
        stat_interval_ms: int = None,
        strategy: int = None,
        threshold: float = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the application.
        self.app_id = app_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Specifies whether to enable the rule.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.enable = enable
        # The minimum number of requests that can be passed in each step after circuit breaking recovers. Default value: 1.
        self.half_open_base_amount_per_step = half_open_base_amount_per_step
        # The number of circuit breaking recovery steps. Default value: 1.
        self.half_open_recovery_step_num = half_open_recovery_step_num
        # The maximum response time (RT). Unit: milliseconds. If the RT of a request is greater than the value of this parameter, a slow call is counted. If you set Strategy to 0, you must specify this parameter.
        self.max_allowed_rt_ms = max_allowed_rt_ms
        # The minimum number of requests to trigger circuit breaking. If the number of requests in the current time window is less than the value of this parameter, circuit breaking is not triggered even if the circuit breaking rule is met. Default value: 10.
        self.min_request_amount = min_request_amount
        # The microservice namespace to which the application belongs.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region in which the instance resides.
        self.region_id = region_id
        # The name of the interface to which the rule applies. The interface name must be the same as the name on the interface details page in the console.
        # 
        # This parameter is required.
        self.resource = resource
        # The resource type.
        # 
        # Valid values:
        # 
        # *   0: custom interface
        # *   1: web
        # *   2: RPC
        # *   3: route
        # *   4: SQL
        self.resource_type = resource_type
        # The period in which circuit breaking is implemented. Unit: milliseconds. If circuit breaking is implemented on the requests for the route, the calls to all the requests for the route fail in the configured circuit breaking period. The value must be an integral multiple of 1,000. Default value: 10000. This value indicates 10 seconds.
        self.retry_timeout_ms = retry_timeout_ms
        # The length of the time window. Unit: milliseconds. The valid range is from 1 second to 120 minutes. The default value is 20000. This value indicates 20 seconds.
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
        # 
        # This parameter is required.
        self.strategy = strategy
        # A percentage threshold for triggering circuit breaking. Valid values: 0-1. These values represent 0% to 100%.
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

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

        if self.max_allowed_rt_ms is not None:
            result['MaxAllowedRtMs'] = self.max_allowed_rt_ms

        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

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

        if m.get('MaxAllowedRtMs') is not None:
            self.max_allowed_rt_ms = m.get('MaxAllowedRtMs')

        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RetryTimeoutMs') is not None:
            self.retry_timeout_ms = m.get('RetryTimeoutMs')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

