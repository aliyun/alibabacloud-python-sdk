# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleCondition(DaraModel):
    def __init__(
        self,
        alert_count: int = None,
        case_list: List[main_models.AlertRuleConditionCaseList] = None,
        compare_list: List[main_models.AlertRuleConditionCompareList] = None,
        composite_escalation: main_models.AlertRuleConditionCompositeEscalation = None,
        escalation_type: str = None,
        express_escalation: main_models.AlertRuleConditionExpressEscalation = None,
        no_data_alert_level: str = None,
        no_data_append_value: str = None,
        no_data_policy: str = None,
        oper: str = None,
        relation: str = None,
        simple_escalation: main_models.AlertRuleConditionSimpleEscalation = None,
        type: str = None,
        value: float = None,
    ):
        # 适用条件类型：SLS_CONDITION
        # 
        # 满足条件几次后告警，默认为1
        self.alert_count = alert_count
        # 适用条件类型： SLS_CONDITION。
        # 
        # SLS告警条件列表
        self.case_list = case_list
        # 适用条件类型：APM_CONDITION。
        # 
        # APM告警比较条件列表
        self.compare_list = compare_list
        # 适用条件类型：CMS_BASIC_CONDITION
        # 
        # escalationType=composite时有效，组合指标告警条件
        self.composite_escalation = composite_escalation
        # 适用条件类型：CMS_BASIC_CONDITION
        # 
        # 
        # 取值范围: 
        # 
        # - simple: 简单指标条件
        # - composite: 组合指标条件
        # - express: 表达式条件
        self.escalation_type = escalation_type
        # 适用条件类型：CMS_BASIC_CONDITION。
        # 
        # escalationType=composite时有效，多指标组合告警条件。
        self.express_escalation = express_escalation
        # 适用条件类型：APM_CONDITION。
        # 
        # 无数据时的告警级别，不指定则不对无数据报警
        self.no_data_alert_level = no_data_alert_level
        # 适用条件类型：APM_CONDITION。
        # 
        # 无数据时补偿的值。
        self.no_data_append_value = no_data_append_value
        # 适用条件类型：CMS_BASIC_CONDITION。
        # 
        # 
        # 无监控数据时报警的处理方式。取值：
        # 
        # - KEEP_LAST_STATE（默认值）：不做任何处理。
        # - INSUFFICIENT_DATA：报警内容为无数据。
        # - OK：正常。
        self.no_data_policy = no_data_policy
        # 比较操作，判断是否是同比、环比
        # 
        # - 大于 GT
        # - 大于等于 GTE
        # - 小于 LT
        # - 小于等于 LTE
        # - 等于 EQ
        # - 不等于 NE
        # - 同比增加 YOY_UP
        # - 同比减少 YOY_DOWN
        self.oper = oper
        # 适用条件类型：APM_CONDITION。
        # 
        # 多个条件之间的逻辑关系。 取值：
        # - and
        # - or
        self.relation = relation
        # 适用条件类型：CMS_BASIC_CONDITION。
        # 
        # 仅当escalationType=simple时有效，针对单一指标设置的告警条件
        self.simple_escalation = simple_escalation
        # 规则条件类型，取值范围：
        # - SLS_CONDITION(SLS告警条件)
        # - APM_CONDITION(APM告警条件)
        # - CMS_BASIC_CONDITION(基础云监控告警条件)
        # 
        # This parameter is required.
        self.type = type
        # 告警触发的阈值。
        self.value = value

    def validate(self):
        if self.case_list:
            for v1 in self.case_list:
                 if v1:
                    v1.validate()
        if self.compare_list:
            for v1 in self.compare_list:
                 if v1:
                    v1.validate()
        if self.composite_escalation:
            self.composite_escalation.validate()
        if self.express_escalation:
            self.express_escalation.validate()
        if self.simple_escalation:
            self.simple_escalation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_count is not None:
            result['alertCount'] = self.alert_count

        result['caseList'] = []
        if self.case_list is not None:
            for k1 in self.case_list:
                result['caseList'].append(k1.to_map() if k1 else None)

        result['compareList'] = []
        if self.compare_list is not None:
            for k1 in self.compare_list:
                result['compareList'].append(k1.to_map() if k1 else None)

        if self.composite_escalation is not None:
            result['compositeEscalation'] = self.composite_escalation.to_map()

        if self.escalation_type is not None:
            result['escalationType'] = self.escalation_type

        if self.express_escalation is not None:
            result['expressEscalation'] = self.express_escalation.to_map()

        if self.no_data_alert_level is not None:
            result['noDataAlertLevel'] = self.no_data_alert_level

        if self.no_data_append_value is not None:
            result['noDataAppendValue'] = self.no_data_append_value

        if self.no_data_policy is not None:
            result['noDataPolicy'] = self.no_data_policy

        if self.oper is not None:
            result['oper'] = self.oper

        if self.relation is not None:
            result['relation'] = self.relation

        if self.simple_escalation is not None:
            result['simpleEscalation'] = self.simple_escalation.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')

        self.case_list = []
        if m.get('caseList') is not None:
            for k1 in m.get('caseList'):
                temp_model = main_models.AlertRuleConditionCaseList()
                self.case_list.append(temp_model.from_map(k1))

        self.compare_list = []
        if m.get('compareList') is not None:
            for k1 in m.get('compareList'):
                temp_model = main_models.AlertRuleConditionCompareList()
                self.compare_list.append(temp_model.from_map(k1))

        if m.get('compositeEscalation') is not None:
            temp_model = main_models.AlertRuleConditionCompositeEscalation()
            self.composite_escalation = temp_model.from_map(m.get('compositeEscalation'))

        if m.get('escalationType') is not None:
            self.escalation_type = m.get('escalationType')

        if m.get('expressEscalation') is not None:
            temp_model = main_models.AlertRuleConditionExpressEscalation()
            self.express_escalation = temp_model.from_map(m.get('expressEscalation'))

        if m.get('noDataAlertLevel') is not None:
            self.no_data_alert_level = m.get('noDataAlertLevel')

        if m.get('noDataAppendValue') is not None:
            self.no_data_append_value = m.get('noDataAppendValue')

        if m.get('noDataPolicy') is not None:
            self.no_data_policy = m.get('noDataPolicy')

        if m.get('oper') is not None:
            self.oper = m.get('oper')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('simpleEscalation') is not None:
            temp_model = main_models.AlertRuleConditionSimpleEscalation()
            self.simple_escalation = temp_model.from_map(m.get('simpleEscalation'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleConditionSimpleEscalation(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.AlertRuleConditionSimpleEscalationEscalations] = None,
        metric_name: str = None,
        period: int = None,
    ):
        # 条件列表，同一个告警规则对应多个级别的，每一个级别会有一个条件对象。
        self.escalations = escalations
        # 适用条件类型：CMS_BASIC_CONDITION。
        # 
        # 告警条件关联的指标
        self.metric_name = metric_name
        # 指标的时间窗口，单位秒
        self.period = period

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['escalations'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.period is not None:
            result['period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.AlertRuleConditionSimpleEscalationEscalations()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('period') is not None:
            self.period = m.get('period')

        return self

class AlertRuleConditionSimpleEscalationEscalations(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        level: str = None,
        statistics: str = None,
        threshold: float = None,
        times: int = None,
    ):
        # 阈值比较符，取值范围：
        # 
        # - GreaterThanOrEqualToThreshold：大于等于。
        # - GreaterThanThreshold：大于。
        # - LessThanOrEqualToThreshold：小于等于。
        # - LessThanThreshold：小于。
        # - NotEqualToThreshold：不等于。
        # - EqualToThreshold：等于。
        # - GreaterThanYesterday：同比昨天时间上涨。
        # - LessThanYesterday：同比昨天时间下降。
        # - GreaterThanLastWeek：同比上周同一时间上涨。
        # - LessThanLastWeek：同比上周同一时间下降。
        # - GreaterThanLastPeriod：环比上周期上涨。
        # - LessThanLastPeriod：环比上周期下降。
        self.comparison_operator = comparison_operator
        # 满足条件时触发的告警级别(表达式告警仅支持一个级别)
        # 
        # - CRITICAL
        # - WARNING
        # - INFO
        self.level = level
        # 统计方法，该参数的取值由指定云产品的MetricName对应的Statistics列决定，例如：Maximum、Minimum 和 Average
        self.statistics = statistics
        # 告警阈值
        self.threshold = threshold
        # 触发告警需满足条件的次数
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.level is not None:
            result['level'] = self.level

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

class AlertRuleConditionExpressEscalation(DaraModel):
    def __init__(
        self,
        level: str = None,
        raw_expression: str = None,
        times: int = None,
    ):
        # 满足条件时触发的告警级别(表达式告警仅支持一个级别)
        # 
        # - CRITICAL
        # - WARNING
        # - INFO
        self.level = level
        # 告警条件表达式
        self.raw_expression = raw_expression
        # 触发告警需满足条件的次数
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['level'] = self.level

        if self.raw_expression is not None:
            result['rawExpression'] = self.raw_expression

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('rawExpression') is not None:
            self.raw_expression = m.get('rawExpression')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

class AlertRuleConditionCompositeEscalation(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.AlertRuleConditionCompositeEscalationEscalations] = None,
        level: str = None,
        relation: str = None,
        times: int = None,
    ):
        # 多指标的组合条件列表
        self.escalations = escalations
        # 满足条件时触发的告警级别(多指标组合告警仅支持一个级别)
        self.level = level
        # 多个指标条件之间的关系，取值为and或or
        self.relation = relation
        # 触发告警需满足条件的次数
        self.times = times

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['escalations'].append(k1.to_map() if k1 else None)

        if self.level is not None:
            result['level'] = self.level

        if self.relation is not None:
            result['relation'] = self.relation

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.AlertRuleConditionCompositeEscalationEscalations()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

class AlertRuleConditionCompositeEscalationEscalations(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # 阈值比较符，取值范围：
        # 
        # - GreaterThanOrEqualToThreshold：大于等于。
        # - GreaterThanThreshold：大于。
        # - LessThanOrEqualToThreshold：小于等于。
        # - LessThanThreshold：小于。
        # - NotEqualToThreshold：不等于。
        # - EqualToThreshold：等于。
        # - GreaterThanYesterday：同比昨天时间上涨。
        # - LessThanYesterday：同比昨天时间下降。
        # - GreaterThanLastWeek：同比上周同一时间上涨。
        # - LessThanLastWeek：同比上周同一时间下降。
        # - GreaterThanLastPeriod：环比上周期上涨。
        # - LessThanLastPeriod：环比上周期下降。
        self.comparison_operator = comparison_operator
        # 指标名称
        self.metric_name = metric_name
        # 指标的时间窗口
        self.period = period
        # 统计方法，该参数的取值由指定云产品的MetricName对应的Statistics列决定。  监控项的统计方法。取值示例：
        # 
        # - $Maximum：最大值。
        # - $Minimum：最小值。
        # - $Average：平均值。
        # - $Availability：可用率（通常用于站点监控）
        # 
        # 说明 $为监控项的统一前缀符号。
        self.statistics = statistics
        # 告警阈值
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.period is not None:
            result['period'] = self.period

        if self.statistics is not None:
            result['statistics'] = self.statistics

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

class AlertRuleConditionCompareList(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        base_unit: str = None,
        display_unit: str = None,
        oper: str = None,
        value: float = None,
        value_level_list: List[main_models.AlertRuleConditionCompareListValueLevelList] = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        # 时间序列后聚合函数
        # 
        # - count
        # - sum
        # - avg
        # - min
        # - max
        # - p90
        # - p95
        # - p99
        self.aggregate = aggregate
        # 数据单位
        self.base_unit = base_unit
        # 展示单位
        self.display_unit = display_unit
        # 比较操作，判断是否是同比、环比
        # 
        # - 大于 GT
        # - 大于等于 GTE
        # - 小于 LT
        # - 小于等于 LTE
        # - 等于 EQ
        # - 不等于 NE
        # - 同比增加 YOY_UP
        # - 同比减少 YOY_DOWN
        self.oper = oper
        # 对比的阈值
        self.value = value
        # 不同值的报警级别的列表。
        self.value_level_list = value_level_list
        # 同比时间单位（仅对oper=YOY_UP/YOY_DOWN生效）
        #  minute、hour、day、week、month
        self.yoy_time_unit = yoy_time_unit
        # 同比时间的值，与yoyTimeUnit配合使用
        self.yoy_time_value = yoy_time_value

    def validate(self):
        if self.value_level_list:
            for v1 in self.value_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.base_unit is not None:
            result['baseUnit'] = self.base_unit

        if self.display_unit is not None:
            result['displayUnit'] = self.display_unit

        if self.oper is not None:
            result['oper'] = self.oper

        if self.value is not None:
            result['value'] = self.value

        result['valueLevelList'] = []
        if self.value_level_list is not None:
            for k1 in self.value_level_list:
                result['valueLevelList'].append(k1.to_map() if k1 else None)

        if self.yoy_time_unit is not None:
            result['yoyTimeUnit'] = self.yoy_time_unit

        if self.yoy_time_value is not None:
            result['yoyTimeValue'] = self.yoy_time_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('baseUnit') is not None:
            self.base_unit = m.get('baseUnit')

        if m.get('displayUnit') is not None:
            self.display_unit = m.get('displayUnit')

        if m.get('oper') is not None:
            self.oper = m.get('oper')

        if m.get('value') is not None:
            self.value = m.get('value')

        self.value_level_list = []
        if m.get('valueLevelList') is not None:
            for k1 in m.get('valueLevelList'):
                temp_model = main_models.AlertRuleConditionCompareListValueLevelList()
                self.value_level_list.append(temp_model.from_map(k1))

        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')

        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')

        return self

class AlertRuleConditionCompareListValueLevelList(DaraModel):
    def __init__(
        self,
        level: str = None,
        value: float = None,
    ):
        # 阈值对应的级别
        self.level = level
        # 对比的阈值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['level'] = self.level

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleConditionCaseList(DaraModel):
    def __init__(
        self,
        condition: str = None,
        count_condition: str = None,
        level: str = None,
        type: str = None,
    ):
        # 匹配表达式，示例：  logLevel: error
        self.condition = condition
        # 数量匹配表达式，示例：
        # 区间组合： __count__ >= 3 && __count__ <= 10
        # 单区间： __count__ >= 3
        self.count_condition = count_condition
        # 满足条件后的告警级别
        self.level = level
        # 匹配类型： 有数据/有特定条数据/有数据匹配/有特定条数匹配。
        # 
        # 取值范围：
        # - HasData: 有数据
        # - HasDataCount:  有特定条数据
        # - HasDataMatch：有数据匹配
        # - HasDataMatchCount：有特定条数匹配
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.count_condition is not None:
            result['countCondition'] = self.count_condition

        if self.level is not None:
            result['level'] = self.level

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('countCondition') is not None:
            self.count_condition = m.get('countCondition')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

