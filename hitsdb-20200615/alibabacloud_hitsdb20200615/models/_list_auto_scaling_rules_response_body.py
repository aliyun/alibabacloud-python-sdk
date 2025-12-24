# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ListAutoScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListAutoScalingRulesResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAutoScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAutoScalingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        scale_rules: List[main_models.ListAutoScalingRulesResponseBodyDataScaleRules] = None,
    ):
        self.scale_rules = scale_rules

    def validate(self):
        if self.scale_rules:
            for v1 in self.scale_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScaleRules'] = []
        if self.scale_rules is not None:
            for k1 in self.scale_rules:
                result['ScaleRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scale_rules = []
        if m.get('ScaleRules') is not None:
            for k1 in m.get('ScaleRules'):
                temp_model = main_models.ListAutoScalingRulesResponseBodyDataScaleRules()
                self.scale_rules.append(temp_model.from_map(k1))

        return self

class ListAutoScalingRulesResponseBodyDataScaleRules(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        enabled: bool = None,
        end_time: str = None,
        instance_id: str = None,
        observation_window: int = None,
        operation_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        scale_in_step: int = None,
        scale_out_step: int = None,
        silence_time: int = None,
        start_time: str = None,
        target_metric: str = None,
        target_nodes: int = None,
        threshold_lower: int = None,
        threshold_upper: int = None,
        trigger_cron_expr: str = None,
    ):
        self.config_id = config_id
        self.enabled = enabled
        self.end_time = end_time
        self.instance_id = instance_id
        self.observation_window = observation_window
        self.operation_type = operation_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scale_in_step = scale_in_step
        self.scale_out_step = scale_out_step
        self.silence_time = silence_time
        self.start_time = start_time
        self.target_metric = target_metric
        self.target_nodes = target_nodes
        self.threshold_lower = threshold_lower
        self.threshold_upper = threshold_upper
        self.trigger_cron_expr = trigger_cron_expr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.observation_window is not None:
            result['ObservationWindow'] = self.observation_window

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scale_in_step is not None:
            result['ScaleInStep'] = self.scale_in_step

        if self.scale_out_step is not None:
            result['ScaleOutStep'] = self.scale_out_step

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_metric is not None:
            result['TargetMetric'] = self.target_metric

        if self.target_nodes is not None:
            result['TargetNodes'] = self.target_nodes

        if self.threshold_lower is not None:
            result['ThresholdLower'] = self.threshold_lower

        if self.threshold_upper is not None:
            result['ThresholdUpper'] = self.threshold_upper

        if self.trigger_cron_expr is not None:
            result['TriggerCronExpr'] = self.trigger_cron_expr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ObservationWindow') is not None:
            self.observation_window = m.get('ObservationWindow')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScaleInStep') is not None:
            self.scale_in_step = m.get('ScaleInStep')

        if m.get('ScaleOutStep') is not None:
            self.scale_out_step = m.get('ScaleOutStep')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetMetric') is not None:
            self.target_metric = m.get('TargetMetric')

        if m.get('TargetNodes') is not None:
            self.target_nodes = m.get('TargetNodes')

        if m.get('ThresholdLower') is not None:
            self.threshold_lower = m.get('ThresholdLower')

        if m.get('ThresholdUpper') is not None:
            self.threshold_upper = m.get('ThresholdUpper')

        if m.get('TriggerCronExpr') is not None:
            self.trigger_cron_expr = m.get('TriggerCronExpr')

        return self

