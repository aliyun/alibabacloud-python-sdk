# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveMetricRuleListResponseBody(DaraModel):
    def __init__(
        self,
        alert_list: main_models.DescribeActiveMetricRuleListResponseBodyAlertList = None,
        code: str = None,
        datapoints: main_models.DescribeActiveMetricRuleListResponseBodyDatapoints = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.alert_list = alert_list
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        self.datapoints = datapoints
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.alert_list:
            self.alert_list.validate()
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_list is not None:
            result['AlertList'] = self.alert_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertList') is not None:
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertList()
            self.alert_list = temp_model.from_map(m.get('AlertList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Datapoints') is not None:
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m.get('Datapoints'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeActiveMetricRuleListResponseBodyDatapoints(DaraModel):
    def __init__(
        self,
        alarm: List[main_models.DescribeActiveMetricRuleListResponseBodyDatapointsAlarm] = None,
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
                temp_model = main_models.DescribeActiveMetricRuleListResponseBodyDatapointsAlarm()
                self.alarm.append(temp_model.from_map(k1))

        return self

class DescribeActiveMetricRuleListResponseBodyDatapointsAlarm(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        enable: str = None,
        end_time: str = None,
        evaluation_count: str = None,
        metric_name: str = None,
        namespace: str = None,
        period: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
        start_time: str = None,
        state: str = None,
        statistics: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.enable = enable
        self.end_time = end_time
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.namespace = namespace
        self.period = period
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.start_time = start_time
        self.state = state
        self.statistics = statistics
        self.threshold = threshold
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.period is not None:
            result['Period'] = self.period

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class DescribeActiveMetricRuleListResponseBodyAlertList(DaraModel):
    def __init__(
        self,
        alert: List[main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlert] = None,
    ):
        self.alert = alert

    def validate(self):
        if self.alert:
            for v1 in self.alert:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alert'] = []
        if self.alert is not None:
            for k1 in self.alert:
                result['Alert'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert = []
        if m.get('Alert') is not None:
            for k1 in m.get('Alert'):
                temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlert()
                self.alert.append(temp_model.from_map(k1))

        return self

class DescribeActiveMetricRuleListResponseBodyAlertListAlert(DaraModel):
    def __init__(
        self,
        alert_state: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        enable_state: bool = None,
        escalations: main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalations = None,
        mail_subject: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
        webhook: str = None,
    ):
        self.alert_state = alert_state
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.effective_interval = effective_interval
        self.enable_state = enable_state
        self.escalations = escalations
        self.mail_subject = mail_subject
        self.metric_name = metric_name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state

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

        if self.mail_subject is not None:
            result['MailSubject'] = self.mail_subject

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval

        if self.period is not None:
            result['Period'] = self.period

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')

        if m.get('Escalations') is not None:
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('MailSubject') is not None:
            self.mail_subject = m.get('MailSubject')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsCritical = None,
        info: main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsInfo = None,
        warn: main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsWarn = None,
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
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeActiveMetricRuleListResponseBodyAlertListAlertEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
    ):
        self.comparison_operator = comparison_operator
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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

