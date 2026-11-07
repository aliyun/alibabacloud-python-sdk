# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWebFlowRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        burst: int = None,
        control_behavior: int = None,
        enable: bool = None,
        max_queueing_time_ms: int = None,
        metric_type: int = None,
        namespace: str = None,
        param_item: str = None,
        region_id: str = None,
        resource_mode: int = None,
        rule_id: int = None,
        stat_interval_ms: int = None,
        threshold: float = None,
    ):
        # The language in which you want the results to be displayed. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # The application ID.
        self.app_id = app_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The number of additional requests allowed for burst requests. The effect is equivalent to the maximum number of tokens for the token bucket algorithm.
        self.burst = burst
        # The flow control method. Valid values:
        # 
        # - 0: fast failure
        # 
        # - 2: wait in queue
        self.control_behavior = control_behavior
        # The rule status. Valid values:
        # 
        # - true (enabled)
        # 
        # - false (disabled)
        self.enable = enable
        # The timeout period. Unit: milliseconds. This parameter is required if the ControlBehavior parameter is set to 2.
        self.max_queueing_time_ms = max_queueing_time_ms
        # The threshold type. Valid values:
        # 
        # - 1: number of requests
        self.metric_type = metric_type
        # The namespace.
        self.namespace = namespace
        # The parameter description item, which is a JSON string containing the following key-value pairs:
        # 
        # - parseStrategy: the parameter property (0: client IP address. 1: remote host. 2: header. 3: URL parameter)
        # 
        # - fieldName: the header name or URL parameter name. You must specify this key only if parseStrategy is set to 2 or 3
        # 
        # - matchStrategy: the method to match the property value. You must specify this key only if parseStrategy is set to 2 or 3 and the property value is matched. Valid values: 0 (exact match), 2 (regular expression match), and 3 (substring match)
        # 
        # - pattern: the match string. You must specify this key only if parseStrategy is set to 2 or 3 and the property value is matched
        self.param_item = param_item
        # The region.
        self.region_id = region_id
        # The resource mode. Valid values:
        # 
        # - 0: resource name mode
        self.resource_mode = resource_mode
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The length of the time window. Unit: milliseconds.
        self.stat_interval_ms = stat_interval_ms
        # The threshold.
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

        if self.burst is not None:
            result['Burst'] = self.burst

        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.param_item is not None:
            result['ParamItem'] = self.param_item

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.stat_interval_ms is not None:
            result['StatIntervalMs'] = self.stat_interval_ms

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

        if m.get('Burst') is not None:
            self.burst = m.get('Burst')

        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ParamItem') is not None:
            self.param_item = m.get('ParamItem')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

