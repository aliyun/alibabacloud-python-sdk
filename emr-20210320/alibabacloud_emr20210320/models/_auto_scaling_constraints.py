# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class AutoScalingConstraints(DaraModel):
    def __init__(
        self,
        auto_scaling_metric_units: List[main_models.MetricUnitValue] = None,
        default_metric_triggered_rules: List[main_models.ScalingRule] = None,
        max_adjustment_value: int = None,
        max_by_load_rule_count: int = None,
        max_by_time_rule_count: int = None,
        support_metric_tags: List[main_models.AutoScalingConstraintsSupportMetricTags] = None,
        support_metrics: List[str] = None,
        support_rule_types: List[str] = None,
    ):
        # 按负载伸缩指标单位描述。
        self.auto_scaling_metric_units = auto_scaling_metric_units
        # 默认按负载弹性伸缩规则列表
        self.default_metric_triggered_rules = default_metric_triggered_rules
        # 单次伸缩活动最大扩缩容节点数量。
        self.max_adjustment_value = max_adjustment_value
        # 按负载规则数量最大值。
        self.max_by_load_rule_count = max_by_load_rule_count
        # 按时间规则数量最大值。
        self.max_by_time_rule_count = max_by_time_rule_count
        # 支持的按负载弹性伸缩指标Tag列表。
        self.support_metric_tags = support_metric_tags
        # 支持的按负载弹性伸缩指标列表。
        self.support_metrics = support_metrics
        # 支持的弹性伸缩规则类型。
        self.support_rule_types = support_rule_types

    def validate(self):
        if self.auto_scaling_metric_units:
            for v1 in self.auto_scaling_metric_units:
                 if v1:
                    v1.validate()
        if self.default_metric_triggered_rules:
            for v1 in self.default_metric_triggered_rules:
                 if v1:
                    v1.validate()
        if self.support_metric_tags:
            for v1 in self.support_metric_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoScalingMetricUnits'] = []
        if self.auto_scaling_metric_units is not None:
            for k1 in self.auto_scaling_metric_units:
                result['AutoScalingMetricUnits'].append(k1.to_map() if k1 else None)

        result['DefaultMetricTriggeredRules'] = []
        if self.default_metric_triggered_rules is not None:
            for k1 in self.default_metric_triggered_rules:
                result['DefaultMetricTriggeredRules'].append(k1.to_map() if k1 else None)

        if self.max_adjustment_value is not None:
            result['MaxAdjustmentValue'] = self.max_adjustment_value

        if self.max_by_load_rule_count is not None:
            result['MaxByLoadRuleCount'] = self.max_by_load_rule_count

        if self.max_by_time_rule_count is not None:
            result['MaxByTimeRuleCount'] = self.max_by_time_rule_count

        result['SupportMetricTags'] = []
        if self.support_metric_tags is not None:
            for k1 in self.support_metric_tags:
                result['SupportMetricTags'].append(k1.to_map() if k1 else None)

        if self.support_metrics is not None:
            result['SupportMetrics'] = self.support_metrics

        if self.support_rule_types is not None:
            result['SupportRuleTypes'] = self.support_rule_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_scaling_metric_units = []
        if m.get('AutoScalingMetricUnits') is not None:
            for k1 in m.get('AutoScalingMetricUnits'):
                temp_model = main_models.MetricUnitValue()
                self.auto_scaling_metric_units.append(temp_model.from_map(k1))

        self.default_metric_triggered_rules = []
        if m.get('DefaultMetricTriggeredRules') is not None:
            for k1 in m.get('DefaultMetricTriggeredRules'):
                temp_model = main_models.ScalingRule()
                self.default_metric_triggered_rules.append(temp_model.from_map(k1))

        if m.get('MaxAdjustmentValue') is not None:
            self.max_adjustment_value = m.get('MaxAdjustmentValue')

        if m.get('MaxByLoadRuleCount') is not None:
            self.max_by_load_rule_count = m.get('MaxByLoadRuleCount')

        if m.get('MaxByTimeRuleCount') is not None:
            self.max_by_time_rule_count = m.get('MaxByTimeRuleCount')

        self.support_metric_tags = []
        if m.get('SupportMetricTags') is not None:
            for k1 in m.get('SupportMetricTags'):
                temp_model = main_models.AutoScalingConstraintsSupportMetricTags()
                self.support_metric_tags.append(temp_model.from_map(k1))

        if m.get('SupportMetrics') is not None:
            self.support_metrics = m.get('SupportMetrics')

        if m.get('SupportRuleTypes') is not None:
            self.support_rule_types = m.get('SupportRuleTypes')

        return self

class AutoScalingConstraintsSupportMetricTags(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # 指标名称。
        self.metric_name = metric_name
        # 指标Tag。
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

