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
        enable_severity_suppression: bool = None,
        escalation_type: str = None,
        express_escalation: main_models.AlertRuleConditionExpressEscalation = None,
        no_data_alert_level: str = None,
        no_data_append_value: str = None,
        no_data_policy: str = None,
        oper: str = None,
        relation: str = None,
        simple_escalation: main_models.AlertRuleConditionSimpleEscalation = None,
        triggers: List[main_models.AlertRuleConditionTriggers] = None,
        type: str = None,
        value: float = None,
    ):
        # Applicable to the SLS_CONDITION type.
        # 
        # The number of times the condition must be met to trigger an alert. The default value is 1.
        self.alert_count = alert_count
        # Applicable to the SLS_CONDITION type.
        # 
        # A list of SLS alert conditions.
        self.case_list = case_list
        # Applicable to the APM_CONDITION type.
        # 
        # A list of Application Performance Management (APM) alert comparison conditions.
        self.compare_list = compare_list
        # Applicable to the CMS_BASIC_CONDITION type.
        # 
        # This parameter is valid only when escalationType is set to composite. It specifies the alert condition for composite metrics.
        self.composite_escalation = composite_escalation
        self.enable_severity_suppression = enable_severity_suppression
        # Applicable to the CMS_BASIC_CONDITION type.
        # 
        # Valid values:
        # 
        # - simple: A simple metric condition.
        # 
        # - composite: A composite metric condition.
        # 
        # - express: An expression-based condition.
        self.escalation_type = escalation_type
        # This parameter is applicable only to the CMS_BASIC_CONDITION condition type.
        # 
        # This parameter takes effect when escalationType is set to composite. It defines the conditions for a composite alert based on multiple metrics.
        self.express_escalation = express_escalation
        # Applicable to the APM_CONDITION type.
        # 
        # The alert level for when no data is available. If you do not specify this parameter, no alert is triggered when no data is available.
        self.no_data_alert_level = no_data_alert_level
        # Applicable to the APM_CONDITION type.
        # 
        # The value to use when no data is available.
        self.no_data_append_value = no_data_append_value
        # Applicable to the CMS_BASIC_CONDITION type.
        # 
        # The method for handling alerts when no monitoring data is available. Valid values:
        # 
        # - KEEP_LAST_STATE (default): No action is taken.
        # 
        # - INSUFFICIENT_DATA: The alert content indicates that no data is available.
        # 
        # - OK: The status is normal.
        self.no_data_policy = no_data_policy
        # The comparison operation. It determines whether to perform a year-over-year or period-over-period comparison.
        # 
        # - GT: Greater than.
        # 
        # - GTE: Greater than or equal to.
        # 
        # - LT: Less than.
        # 
        # - LTE: Less than or equal to.
        # 
        # - EQ: Equal to.
        # 
        # - NE: Not equal to.
        # 
        # - YOY_UP: Year-over-year increase.
        # 
        # - YOY_DOWN: Year-over-year decrease.
        self.oper = oper
        # Applicable to the APM_CONDITION type.
        # 
        # The logical relationship between multiple conditions. Valid values:
        # 
        # - and
        # 
        # - or
        self.relation = relation
        # Applicable to the CMS_BASIC_CONDITION type.
        # 
        # This parameter is valid only when escalationType is set to simple. It specifies the alert condition for a single metric.
        self.simple_escalation = simple_escalation
        self.triggers = triggers
        # The type of the rule condition. Valid values:
        # 
        # - SLS_CONDITION: An SLS alert condition.
        # 
        # - APM_CONDITION: An APM alert condition.
        # 
        # - CMS_BASIC_CONDITION: A basic Cloud Monitor alert condition.
        # 
        # This parameter is required.
        self.type = type
        # The threshold that triggers an alert.
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
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

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

        if self.enable_severity_suppression is not None:
            result['enableSeveritySuppression'] = self.enable_severity_suppression

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

        result['triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['triggers'].append(k1.to_map() if k1 else None)

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

        if m.get('enableSeveritySuppression') is not None:
            self.enable_severity_suppression = m.get('enableSeveritySuppression')

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

        self.triggers = []
        if m.get('triggers') is not None:
            for k1 in m.get('triggers'):
                temp_model = main_models.AlertRuleConditionTriggers()
                self.triggers.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AlertRuleConditionTriggers(DaraModel):
    def __init__(
        self,
        duration_secs: int = None,
        expression: main_models.AlertRuleConditionTriggersExpression = None,
        severity: str = None,
    ):
        self.duration_secs = duration_secs
        self.expression = expression
        self.severity = severity

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.expression is not None:
            result['expression'] = self.expression.to_map()

        if self.severity is not None:
            result['severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('expression') is not None:
            temp_model = main_models.AlertRuleConditionTriggersExpression()
            self.expression = temp_model.from_map(m.get('expression'))

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        return self

class AlertRuleConditionTriggersExpression(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.AlertRuleConditionTriggersExpressionConditions] = None,
        expression_type: str = None,
        logic_operator: str = None,
    ):
        self.conditions = conditions
        self.expression_type = expression_type
        self.logic_operator = logic_operator

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.expression_type is not None:
            result['expressionType'] = self.expression_type

        if self.logic_operator is not None:
            result['logicOperator'] = self.logic_operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.AlertRuleConditionTriggersExpressionConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('logicOperator') is not None:
            self.logic_operator = m.get('logicOperator')

        return self

class AlertRuleConditionTriggersExpressionConditions(DaraModel):
    def __init__(
        self,
        expression_type: str = None,
        operator: str = None,
        query_name: str = None,
        threshold: float = None,
    ):
        self.expression_type = expression_type
        self.operator = operator
        self.query_name = query_name
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_type is not None:
            result['expressionType'] = self.expression_type

        if self.operator is not None:
            result['operator'] = self.operator

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expressionType') is not None:
            self.expression_type = m.get('expressionType')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

class AlertRuleConditionSimpleEscalation(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.AlertRuleConditionSimpleEscalationEscalations] = None,
        metric_name: str = None,
        period: int = None,
    ):
        # A list of conditions. If an alert rule has multiple levels, each level has a corresponding condition object.
        self.escalations = escalations
        # Applicable to the CMS_BASIC_CONDITION type.
        # 
        # The metric associated with the alert condition.
        self.metric_name = metric_name
        # The time window for the metric, in seconds.
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
        # The comparison operator for the threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: Greater than or equal to.
        # 
        # - GreaterThanThreshold: Greater than.
        # 
        # - LessThanOrEqualToThreshold: Less than or equal to.
        # 
        # - LessThanThreshold: Less than.
        # 
        # - NotEqualToThreshold: Not equal to.
        # 
        # - EqualToThreshold: Equal to.
        # 
        # - GreaterThanYesterday: Higher than the value at the same time yesterday.
        # 
        # - LessThanYesterday: Lower than the value at the same time yesterday.
        # 
        # - GreaterThanLastWeek: Higher than the value at the same time last week.
        # 
        # - LessThanLastWeek: Lower than the value at the same time last week.
        # 
        # - GreaterThanLastPeriod: Higher than the value in the previous period.
        # 
        # - LessThanLastPeriod: Lower than the value in the previous period.
        self.comparison_operator = comparison_operator
        # The alert level that is triggered when the condition is met. Expression-based alerts support only one level.
        # 
        # - CRITICAL
        # 
        # - WARNING
        # 
        # - INFO
        self.level = level
        # The statistical method. The valid values for this parameter are determined by the Statistics column that corresponds to the MetricName of the specified cloud product. Examples: Maximum, Minimum, and Average.
        self.statistics = statistics
        # The alert threshold.
        self.threshold = threshold
        # The number of times the condition must be met to trigger an alert.
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
        # The alert level that is triggered when the condition is met. Expression-based alerts support only one level.
        # 
        # - CRITICAL
        # 
        # - WARNING
        # 
        # - INFO
        self.level = level
        # The alert condition expression.
        self.raw_expression = raw_expression
        # The number of times the condition must be met to trigger an alert.
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
        # A list of composite conditions for multiple metrics.
        self.escalations = escalations
        # The alert level that is triggered when the condition is met. Composite metric alerts support only one level.
        self.level = level
        # The relationship between multiple metric conditions. Valid values: and or or.
        self.relation = relation
        # The number of times the condition must be met to trigger an alert.
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
        # The comparison operator for the threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: Greater than or equal to.
        # 
        # - GreaterThanThreshold: Greater than.
        # 
        # - LessThanOrEqualToThreshold: Less than or equal to.
        # 
        # - LessThanThreshold: Less than.
        # 
        # - NotEqualToThreshold: Not equal to.
        # 
        # - EqualToThreshold: Equal to.
        # 
        # - GreaterThanYesterday: Higher than the value at the same time yesterday.
        # 
        # - LessThanYesterday: Lower than the value at the same time yesterday.
        # 
        # - GreaterThanLastWeek: Higher than the value at the same time last week.
        # 
        # - LessThanLastWeek: Lower than the value at the same time last week.
        # 
        # - GreaterThanLastPeriod: Higher than the value in the previous period.
        # 
        # - LessThanLastPeriod: Lower than the value in the previous period.
        self.comparison_operator = comparison_operator
        # The name of the metric.
        self.metric_name = metric_name
        # The time window for the metric.
        self.period = period
        # The statistical method. The valid values for this parameter are determined by the Statistics column that corresponds to the MetricName of the specified cloud product. Examples of statistical methods for metrics:
        # 
        # - $Maximum: The maximum value.
        # 
        # - $Minimum: The minimum value.
        # 
        # - $Average: The average value.
        # 
        # - $Availability: The availability rate. This is typically used for site monitoring.
        # 
        # Note: The dollar sign ($) is a standard prefix for metrics.
        self.statistics = statistics
        # The alert threshold.
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
        # The aggregate function for the time series.
        # 
        # - count
        # 
        # - sum
        # 
        # - avg
        # 
        # - min
        # 
        # - max
        # 
        # - p90
        # 
        # - p95
        # 
        # - p99
        self.aggregate = aggregate
        # The unit of the data.
        self.base_unit = base_unit
        # The unit for display.
        self.display_unit = display_unit
        # The comparison operation. It determines whether to perform a year-over-year or period-over-period comparison.
        # 
        # - GT: Greater than.
        # 
        # - GTE: Greater than or equal to.
        # 
        # - LT: Less than.
        # 
        # - LTE: Less than or equal to.
        # 
        # - EQ: Equal to.
        # 
        # - NE: Not equal to.
        # 
        # - YOY_UP: Year-over-year increase.
        # 
        # - YOY_DOWN: Year-over-year decrease.
        self.oper = oper
        # The threshold for comparison.
        self.value = value
        # A list of alert levels for different values.
        self.value_level_list = value_level_list
        # The time unit for year-over-year comparison. This parameter is valid only when oper is set to YOY_UP or YOY_DOWN. Valid values: minute, hour, day, week, and month.
        self.yoy_time_unit = yoy_time_unit
        # The time value for year-over-year comparison. Used with yoyTimeUnit.
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
        # The level corresponding to the threshold.
        self.level = level
        # The threshold for comparison.
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
        # The matching expression. Example: logLevel: error
        self.condition = condition
        # The expression for matching a quantity. Examples:
        # Combined range: **count** >= 3 && **count** <= 10
        # Single range: **count** >= 3
        self.count_condition = count_condition
        # The alert level when the condition is met.
        self.level = level
        # The match type. It can be data availability, a specific number of data entries, a data match, or a specific number of data entry matches.
        # 
        # Valid values:
        # 
        # - HasData: Data is available.
        # 
        # - HasDataCount: A specific number of data entries are available.
        # 
        # - HasDataMatch: Data matches the condition.
        # 
        # - HasDataMatchCount: A specific number of data entries match the condition.
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

