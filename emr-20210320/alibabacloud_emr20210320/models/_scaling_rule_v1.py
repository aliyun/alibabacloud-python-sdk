# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ScalingRuleV1(DaraModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cool_down_time: int = None,
        rule_name: str = None,
        rule_param: main_models.ScalingRuleV1RuleParam = None,
        rule_type: str = None,
        scaling_config_biz_id: str = None,
    ):
        # 调整类型。
        self.adjustment_type = adjustment_type
        # 调整值,正数为扩容,负数为缩容。
        self.adjustment_value = adjustment_value
        # 冷却时间,单位秒。
        self.cool_down_time = cool_down_time
        # 规则名称。
        self.rule_name = rule_name
        # 规则参数。
        self.rule_param = rule_param
        # 规则类型。
        self.rule_type = rule_type
        # 弹性规则配置ID。
        self.scaling_config_biz_id = scaling_config_biz_id

    def validate(self):
        if self.rule_param:
            self.rule_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_param is not None:
            result['RuleParam'] = self.rule_param.to_map()

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scaling_config_biz_id is not None:
            result['ScalingConfigBizId'] = self.scaling_config_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleParam') is not None:
            temp_model = main_models.ScalingRuleV1RuleParam()
            self.rule_param = temp_model.from_map(m.get('RuleParam'))

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScalingConfigBizId') is not None:
            self.scaling_config_biz_id = m.get('ScalingConfigBizId')

        return self

class ScalingRuleV1RuleParam(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        metric_name: str = None,
        period: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        statistics: str = None,
        threshold: int = None,
    ):
        # [负载触发参数] 比较符。
        self.comparison_operator = comparison_operator
        # [负载触发参数] 统计次数。
        self.evaluation_count = evaluation_count
        # [时间调度参数] 周期类型周期过期时间。
        self.launch_expiration_time = launch_expiration_time
        # [时间调度参数] 周期类型周期开始时间。
        self.launch_time = launch_time
        # [负载触发参数] 度量名称。
        self.metric_name = metric_name
        # [负载触发参数] 统计时长,单位分钟。
        self.period = period
        # [时间调度参数] 周期类型周期结束时间。
        self.recurrence_end_time = recurrence_end_time
        # [时间调度参数] 周期类型。
        self.recurrence_type = recurrence_type
        # [时间调度参数] 周期类型周期值。
        self.recurrence_value = recurrence_value
        # [负载触发参数] 统计方式。
        self.statistics = statistics
        # [负载触发参数] 阈值。
        self.threshold = threshold

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

        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

