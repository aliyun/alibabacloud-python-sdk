# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ListAutoScalingConfigsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListAutoScalingConfigsResponseBodyData = None,
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
            temp_model = main_models.ListAutoScalingConfigsResponseBodyData()
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

class ListAutoScalingConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        scale_configs: List[main_models.ListAutoScalingConfigsResponseBodyDataScaleConfigs] = None,
    ):
        self.scale_configs = scale_configs

    def validate(self):
        if self.scale_configs:
            for v1 in self.scale_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScaleConfigs'] = []
        if self.scale_configs is not None:
            for k1 in self.scale_configs:
                result['ScaleConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scale_configs = []
        if m.get('ScaleConfigs') is not None:
            for k1 in m.get('ScaleConfigs'):
                temp_model = main_models.ListAutoScalingConfigsResponseBodyDataScaleConfigs()
                self.scale_configs.append(temp_model.from_map(k1))

        return self

class ListAutoScalingConfigsResponseBodyDataScaleConfigs(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        effective_time_end: str = None,
        effective_time_start: str = None,
        enabled: bool = None,
        engine: str = None,
        instance_id: str = None,
        nodes_max: int = None,
        nodes_min: int = None,
        scale_rule_list: List[main_models.ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList] = None,
        scale_type: str = None,
        spec_id: str = None,
        storage_capacity_max: int = None,
    ):
        self.config_id = config_id
        self.config_name = config_name
        self.effective_time_end = effective_time_end
        self.effective_time_start = effective_time_start
        self.enabled = enabled
        self.engine = engine
        self.instance_id = instance_id
        self.nodes_max = nodes_max
        self.nodes_min = nodes_min
        self.scale_rule_list = scale_rule_list
        self.scale_type = scale_type
        self.spec_id = spec_id
        self.storage_capacity_max = storage_capacity_max

    def validate(self):
        if self.scale_rule_list:
            for v1 in self.scale_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.effective_time_end is not None:
            result['EffectiveTimeEnd'] = self.effective_time_end

        if self.effective_time_start is not None:
            result['EffectiveTimeStart'] = self.effective_time_start

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nodes_max is not None:
            result['NodesMax'] = self.nodes_max

        if self.nodes_min is not None:
            result['NodesMin'] = self.nodes_min

        result['ScaleRuleList'] = []
        if self.scale_rule_list is not None:
            for k1 in self.scale_rule_list:
                result['ScaleRuleList'].append(k1.to_map() if k1 else None)

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.storage_capacity_max is not None:
            result['StorageCapacityMax'] = self.storage_capacity_max

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('EffectiveTimeEnd') is not None:
            self.effective_time_end = m.get('EffectiveTimeEnd')

        if m.get('EffectiveTimeStart') is not None:
            self.effective_time_start = m.get('EffectiveTimeStart')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodesMax') is not None:
            self.nodes_max = m.get('NodesMax')

        if m.get('NodesMin') is not None:
            self.nodes_min = m.get('NodesMin')

        self.scale_rule_list = []
        if m.get('ScaleRuleList') is not None:
            for k1 in m.get('ScaleRuleList'):
                temp_model = main_models.ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList()
                self.scale_rule_list.append(temp_model.from_map(k1))

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('StorageCapacityMax') is not None:
            self.storage_capacity_max = m.get('StorageCapacityMax')

        return self

class ListAutoScalingConfigsResponseBodyDataScaleConfigsScaleRuleList(DaraModel):
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

