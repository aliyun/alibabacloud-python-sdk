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
        # type=SLS_CONDITION时指定，满足条件几次后告警，默认为1
        self.alert_count = alert_count
        # type=SLS_CONDITION时指定
        self.case_list = case_list
        self.compare_list = compare_list
        self.composite_escalation = composite_escalation
        self.escalation_type = escalation_type
        self.express_escalation = express_escalation
        # 无数据时按什么级别告警，不指定则不对无数据报警
        self.no_data_alert_level = no_data_alert_level
        self.no_data_append_value = no_data_append_value
        self.no_data_policy = no_data_policy
        self.oper = oper
        self.relation = relation
        self.simple_escalation = simple_escalation
        # 规则条件类型，可选值：SLS_CONDITION
        # 
        # This parameter is required.
        self.type = type
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
        self.escalations = escalations
        self.metric_name = metric_name
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
        self.comparison_operator = comparison_operator
        self.level = level
        self.statistics = statistics
        self.threshold = threshold
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
        self.level = level
        self.raw_expression = raw_expression
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
        self.escalations = escalations
        self.level = level
        self.relation = relation
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
        self.comparison_operator = comparison_operator
        self.metric_name = metric_name
        self.period = period
        self.statistics = statistics
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
        self.aggregate = aggregate
        self.base_unit = base_unit
        self.display_unit = display_unit
        self.oper = oper
        self.value = value
        self.value_level_list = value_level_list
        self.yoy_time_unit = yoy_time_unit
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
        self.level = level
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
        self.condition = condition
        self.count_condition = count_condition
        self.level = level
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

