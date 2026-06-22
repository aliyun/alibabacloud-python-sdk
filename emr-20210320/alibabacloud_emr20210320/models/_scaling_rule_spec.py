# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ScalingRuleSpec(DaraModel):
    def __init__(
        self,
        adjustment_value: int = None,
        by_load_scaling_rule_spec: main_models.ScalingRuleSpecByLoadScalingRuleSpec = None,
        by_time_scaling_rule_spec: main_models.ScalingRuleSpecByTimeScalingRuleSpec = None,
        cool_down_interval: int = None,
        scaling_activity_type: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
    ):
        # 调整值。需要为正数，代表需要扩容或者缩容的实例数量。
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # 按照负载伸缩描述。
        self.by_load_scaling_rule_spec = by_load_scaling_rule_spec
        # 按照时间伸缩描述。
        self.by_time_scaling_rule_spec = by_time_scaling_rule_spec
        # 冷却时间。单位为秒，取值范围在30~10800秒之间。
        # 
        # This parameter is required.
        self.cool_down_interval = cool_down_interval
        # 伸缩活动类型。
        # 
        # This parameter is required.
        self.scaling_activity_type = scaling_activity_type
        # 规则名称。
        # 
        # This parameter is required.
        self.scaling_rule_name = scaling_rule_name
        # 伸缩规则类型。
        # 
        # This parameter is required.
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        if self.by_load_scaling_rule_spec:
            self.by_load_scaling_rule_spec.validate()
        if self.by_time_scaling_rule_spec:
            self.by_time_scaling_rule_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.by_load_scaling_rule_spec is not None:
            result['ByLoadScalingRuleSpec'] = self.by_load_scaling_rule_spec.to_map()

        if self.by_time_scaling_rule_spec is not None:
            result['ByTimeScalingRuleSpec'] = self.by_time_scaling_rule_spec.to_map()

        if self.cool_down_interval is not None:
            result['CoolDownInterval'] = self.cool_down_interval

        if self.scaling_activity_type is not None:
            result['ScalingActivityType'] = self.scaling_activity_type

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('ByLoadScalingRuleSpec') is not None:
            temp_model = main_models.ScalingRuleSpecByLoadScalingRuleSpec()
            self.by_load_scaling_rule_spec = temp_model.from_map(m.get('ByLoadScalingRuleSpec'))

        if m.get('ByTimeScalingRuleSpec') is not None:
            temp_model = main_models.ScalingRuleSpecByTimeScalingRuleSpec()
            self.by_time_scaling_rule_spec = temp_model.from_map(m.get('ByTimeScalingRuleSpec'))

        if m.get('CoolDownInterval') is not None:
            self.cool_down_interval = m.get('CoolDownInterval')

        if m.get('ScalingActivityType') is not None:
            self.scaling_activity_type = m.get('ScalingActivityType')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        return self

class ScalingRuleSpecByTimeScalingRuleSpec(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        # 重复执行定时任务的结束时间戳。单位为毫秒。
        self.end_time = end_time
        # 启动时间戳。单位为毫秒。
        # 
        # This parameter is required.
        self.launch_time = launch_time
        # 指定时间规则的执行类型。
        self.recurrence_type = recurrence_type
        # 重复执行定时任务的数值。具体取值取决于 recurrenceType 设置。
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        return self

class ScalingRuleSpecByLoadScalingRuleSpec(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: int = None,
        metric_name: str = None,
        statistics: str = None,
        threshold: float = None,
        time_window: int = None,
    ):
        # 比较符。
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # 统计次数。
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # 指标名称。指标名称需要在 ListAutoScalingMetrics 接口返回的指标名称列表中。
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # 统计量名称。
        # 
        # This parameter is required.
        self.statistics = statistics
        # 阈值。
        # 
        # This parameter is required.
        self.threshold = threshold
        # 统计窗口。单位为秒。
        # 
        # This parameter is required.
        self.time_window = time_window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.time_window is not None:
            result['TimeWindow'] = self.time_window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TimeWindow') is not None:
            self.time_window = m.get('TimeWindow')

        return self

