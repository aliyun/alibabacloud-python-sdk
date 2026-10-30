# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutResourceMetricRulesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        rules: List[main_models.PutResourceMetricRulesRequestRules] = None,
    ):
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: The system only prechecks the request and does not bind a security group to the instance. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): The system sends a normal request. After the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The list of threshold alert rules.
        # 
        # Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.PutResourceMetricRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class PutResourceMetricRulesRequestRules(DaraModel):
    def __init__(
        self,
        escalations: main_models.PutResourceMetricRulesRequestRulesEscalations = None,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        labels: List[main_models.PutResourceMetricRulesRequestRulesLabels] = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_ok: bool = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # The alert contact group. Alert notifications are sent to the alert contacts in this alert contact group.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > An alert contact group is a group of alert contacts and can contain one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # The effective period of the alert rule.
        # 
        # Valid values of N: 1 to 50.
        self.effective_interval = effective_interval
        # The subject of the alert email.
        # 
        # Valid values of N: 1 to 50.
        self.email_subject = email_subject
        # The trigger period of the alert rule.
        # 
        # Unit: seconds.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > For more information about how to query the statistical period of a monitoring metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.interval = interval
        # The labels that are written to the metric and displayed in the alert notification when the metric meets the alert condition and an alert is triggered.
        self.labels = labels
        # The monitoring metric name.
        # 
        # Valid values of N: 1 to 50.
        # 
        # For more information about how to query the monitoring metric name, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The data namespace of the Alibaba Cloud service.
        # 
        # Valid values of N: 1 to 50.
        # 
        # For more information about how to query the data namespace of an Alibaba Cloud service, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The handling method for alerts when no monitoring data is available. Valid values:
        # 
        # - KEEP_LAST_STATE (default): No operations are performed.
        # - INSUFFICIENT_DATA: The alert content indicates that no data is available.
        # - OK: Normal.
        # 
        # Valid values of N: 1 to 50.
        self.no_data_policy = no_data_policy
        # The inactive time range of the alert rule.
        # 
        # Valid values of N: 1 to 50.
        self.no_effective_interval = no_effective_interval
        # The statistical period of the monitoring metric.
        # 
        # Unit: seconds. Default value: the original reporting period of the monitoring metric.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > For more information about how to query the statistical period of a monitoring metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        # The resource information. Examples: `[{"instanceId":"i-uf6j91r34rnwawoo****"}]` and `[{"userId":"100931896542****"}]`.
        # 
        # Valid values of N: 1 to 50.
        # 
        # For more information about the dimensions supported by resource information, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.resources = resources
        # The ID of the alert rule.
        # 
        # Valid values of N: 1 to 50.
        # 
        # You can enter a new alert rule ID or use an existing alert rule ID in CloudMonitor. For more information about how to query the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule ID, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # Valid values of N: 1 to 50.
        # 
        # You can enter a new alert rule name or use an existing alert rule name in CloudMonitor. For more information about how to query the name of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule name, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether to send a recovery notification.
        self.send_ok = send_ok
        # The mute epoch.
        # 
        # Unit: seconds. Default value: 86400.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > The mute epoch refers to the interval at which to send an alert notification again if the alert does not recover to Normal after it is triggered.
        self.silence_time = silence_time
        # The webhook URL to which a POST request is sent when an alert callback is triggered.
        # 
        # Valid values of N: 1 to 50.
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject

        if self.interval is not None:
            result['Interval'] = self.interval

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

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

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.send_ok is not None:
            result['SendOK'] = self.send_ok

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Escalations') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.PutResourceMetricRulesRequestRulesLabels()
                self.labels.append(temp_model.from_map(k1))

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

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SendOK') is not None:
            self.send_ok = m.get('SendOK')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class PutResourceMetricRulesRequestRulesLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        # 
        # > Tag values support template parameters. The template parameters are replaced with the actual tag values.
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

class PutResourceMetricRulesRequestRulesEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.PutResourceMetricRulesRequestRulesEscalationsCritical = None,
        info: main_models.PutResourceMetricRulesRequestRulesEscalationsInfo = None,
        warn: main_models.PutResourceMetricRulesRequestRulesEscalationsWarn = None,
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
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class PutResourceMetricRulesRequestRulesEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the Warn-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to.
        # - GreaterThanThreshold: greater than.
        # - LessThanOrEqualToThreshold: less than or equal to.
        # - LessThanThreshold: less than.
        # - NotEqualToThreshold: not equal to.
        # - EqualToThreshold: equal to.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the previous period.
        # - LessThanLastPeriod: less than the value in the previous period.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Warn-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the value of this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn (warning), and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Warn-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRulesRequestRulesEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the Info-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to.
        # - GreaterThanThreshold: greater than.
        # - LessThanOrEqualToThreshold: less than or equal to.
        # - LessThanThreshold: less than.
        # - NotEqualToThreshold: not equal to.
        # - EqualToThreshold: equal to.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the previous period.
        # - LessThanLastPeriod: less than the value in the previous period.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Info-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the value of this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn (warning), and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Info-level alerts.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Info-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRulesRequestRulesEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the Critical-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to.
        # - GreaterThanThreshold: greater than.
        # - LessThanOrEqualToThreshold: less than or equal to.
        # - LessThanThreshold: less than.
        # - NotEqualToThreshold: not equal to.
        # - EqualToThreshold: equal to.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the previous period.
        # - LessThanLastPeriod: less than the value in the previous period.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Critical-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the value of this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn (warning), and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Critical-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Critical-level alerts.
        # 
        # Valid values of N: 1 to 50.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must configure the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

