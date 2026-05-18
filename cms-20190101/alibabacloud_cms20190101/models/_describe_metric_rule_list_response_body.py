# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricRuleListResponseBody(DaraModel):
    def __init__(
        self,
        alarms: main_models.DescribeMetricRuleListResponseBodyAlarms = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        self.alarms = alarms
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call is successful.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.alarms:
            self.alarms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarms is not None:
            result['Alarms'] = self.alarms.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarms()
            self.alarms = temp_model.from_map(m.get('Alarms'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMetricRuleListResponseBodyAlarms(DaraModel):
    def __init__(
        self,
        alarm: List[main_models.DescribeMetricRuleListResponseBodyAlarmsAlarm] = None,
    ):
        self.alarm = alarm

    def validate(self):
        if self.alarm:
            for v1 in self.alarm:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alarm'] = []
        if self.alarm is not None:
            for k1 in self.alarm:
                result['Alarm'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm = []
        if m.get('Alarm') is not None:
            for k1 in m.get('Alarm'):
                temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarm()
                self.alarm.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarm(DaraModel):
    def __init__(
        self,
        alert_state: str = None,
        composite_expression: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpression = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        enable_state: bool = None,
        escalations: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations = None,
        gmt_create: int = None,
        gmt_update: str = None,
        group_id: str = None,
        group_name: str = None,
        labels: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmLabels = None,
        mail_subject: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        period: str = None,
        product_category: str = None,
        prometheus: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheus = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        source_type: str = None,
        webhook: str = None,
    ):
        self.alert_state = alert_state
        self.composite_expression = composite_expression
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.effective_interval = effective_interval
        self.enable_state = enable_state
        self.escalations = escalations
        self.gmt_create = gmt_create
        self.gmt_update = gmt_update
        self.group_id = group_id
        self.group_name = group_name
        self.labels = labels
        self.mail_subject = mail_subject
        self.metric_name = metric_name
        self.namespace = namespace
        self.no_data_policy = no_data_policy
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.product_category = product_category
        self.prometheus = prometheus
        self.resources = resources
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.source_type = source_type
        self.webhook = webhook

    def validate(self):
        if self.composite_expression:
            self.composite_expression.validate()
        if self.escalations:
            self.escalations.validate()
        if self.labels:
            self.labels.validate()
        if self.prometheus:
            self.prometheus.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state

        if self.composite_expression is not None:
            result['CompositeExpression'] = self.composite_expression.to_map()

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.enable_state is not None:
            result['EnableState'] = self.enable_state

        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.labels is not None:
            result['Labels'] = self.labels.to_map()

        if self.mail_subject is not None:
            result['MailSubject'] = self.mail_subject

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_data_policy is not None:
            result['NoDataPolicy'] = self.no_data_policy

        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval

        if self.period is not None:
            result['Period'] = self.period

        if self.product_category is not None:
            result['ProductCategory'] = self.product_category

        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')

        if m.get('CompositeExpression') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpression()
            self.composite_expression = temp_model.from_map(m.get('CompositeExpression'))

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')

        if m.get('Escalations') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Labels') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmLabels()
            self.labels = temp_model.from_map(m.get('Labels'))

        if m.get('MailSubject') is not None:
            self.mail_subject = m.get('MailSubject')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoDataPolicy') is not None:
            self.no_data_policy = m.get('NoDataPolicy')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProductCategory') is not None:
            self.product_category = m.get('ProductCategory')

        if m.get('Prometheus') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheus()
            self.prometheus = temp_model.from_map(m.get('Prometheus'))

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheus(DaraModel):
    def __init__(
        self,
        annotations: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotations = None,
        level: str = None,
        prom_ql: str = None,
        times: int = None,
    ):
        self.annotations = annotations
        self.level = level
        self.prom_ql = prom_ql
        self.times = times

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations.to_map()

        if self.level is not None:
            result['Level'] = self.level

        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotations()
            self.annotations = temp_model.from_map(m.get('Annotations'))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotations(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotationsAnnotations] = None,
    ):
        self.annotations = annotations

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['Annotations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotationsAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmPrometheusAnnotationsAnnotations(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmLabels(DaraModel):
    def __init__(
        self,
        labels: List[main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmLabelsLabels] = None,
    ):
        self.labels = labels

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmLabelsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmLabelsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical = None,
        info: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo = None,
        warn: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()

        if self.info is not None:
            result['Info'] = self.info.to_map()

        if self.warn is not None:
            result['Warn'] = self.warn.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.pre_condition = pre_condition
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
            result['ComparisonOperator'] = self.comparison_operator

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.pre_condition = pre_condition
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
            result['ComparisonOperator'] = self.comparison_operator

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.pre_condition = pre_condition
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
            result['ComparisonOperator'] = self.comparison_operator

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpression(DaraModel):
    def __init__(
        self,
        expression_list: main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionList = None,
        expression_list_join: str = None,
        expression_raw: str = None,
        level: str = None,
        times: int = None,
    ):
        self.expression_list = expression_list
        self.expression_list_join = expression_list_join
        self.expression_raw = expression_raw
        self.level = level
        self.times = times

    def validate(self):
        if self.expression_list:
            self.expression_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_list is not None:
            result['ExpressionList'] = self.expression_list.to_map()

        if self.expression_list_join is not None:
            result['ExpressionListJoin'] = self.expression_list_join

        if self.expression_raw is not None:
            result['ExpressionRaw'] = self.expression_raw

        if self.level is not None:
            result['Level'] = self.level

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionList') is not None:
            temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionList()
            self.expression_list = temp_model.from_map(m.get('ExpressionList'))

        if m.get('ExpressionListJoin') is not None:
            self.expression_list_join = m.get('ExpressionListJoin')

        if m.get('ExpressionRaw') is not None:
            self.expression_raw = m.get('ExpressionRaw')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionList(DaraModel):
    def __init__(
        self,
        expression_list: List[main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionListExpressionList] = None,
    ):
        self.expression_list = expression_list

    def validate(self):
        if self.expression_list:
            for v1 in self.expression_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExpressionList'] = []
        if self.expression_list is not None:
            for k1 in self.expression_list:
                result['ExpressionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expression_list = []
        if m.get('ExpressionList') is not None:
            for k1 in m.get('ExpressionList'):
                temp_model = main_models.DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionListExpressionList()
                self.expression_list.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleListResponseBodyAlarmsAlarmCompositeExpressionExpressionListExpressionList(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: str = None,
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
            result['ComparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

