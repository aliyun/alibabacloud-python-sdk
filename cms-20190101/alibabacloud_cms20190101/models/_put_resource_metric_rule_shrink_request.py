# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutResourceMetricRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        escalations: main_models.PutResourceMetricRuleShrinkRequestEscalations = None,
        client_token: str = None,
        composite_expression_shrink: str = None,
        contact_groups: str = None,
        dry_run: bool = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        labels: List[main_models.PutResourceMetricRuleShrinkRequestLabels] = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        period: str = None,
        prometheus_shrink: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_ok: bool = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        self.client_token = client_token
        # The alert conditions for multiple metrics.
        # 
        # > Single-metric and multi-metric alert conditions are mutually exclusive and cannot be configured at the same time.
        self.composite_expression_shrink = composite_expression_shrink
        # The alert contact group. Alert notifications are sent to the alert contacts in this alert contact group.
        # 
        # > An alert contact group contains one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # Specifies whether to only precheck this request. Valid values:
        # - **true**: The system only checks the request and does not bind the security group to the instance. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the check, the corresponding error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # - **false** (default value): The system sends a normal request. If the request passes the check, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The effective period of the alert rule.
        self.effective_interval = effective_interval
        # The subject of the alert email.
        self.email_subject = email_subject
        # The trigger period of the alert rule. Unit: seconds.
        # 
        # > For more information about how to query the statistical period of a metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.interval = interval
        # The labels that are added to the metric and displayed in the alert notification when the metric meets the alert condition and an alert is triggered.
        # 
        # > This feature is the same as the Label feature in Prometheus alerts.
        self.labels = labels
        # The metric name. For more information about how to query the metric name, see [CloudMonitor metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > If you create a Prometheus alert rule for Hybrid Cloud Monitoring, this parameter specifies the metric repository name. For more information about how to obtain the metric repository name, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The data namespace of the Alibaba Cloud service. For more information about how to query the data namespace of an Alibaba Cloud service, see [CloudMonitor metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > If you create a Prometheus alert rule for Hybrid Cloud Monitoring, you must set this parameter to `acs_prometheus`.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The action to take when no monitoring data is available. Valid values:
        # 
        # - KEEP_LAST_STATE (default value): No action is taken.
        # - INSUFFICIENT_DATA: The alert notification indicates that no data is available.
        # - OK: The status is normal.
        self.no_data_policy = no_data_policy
        # The ineffective time range of the alert rule.
        self.no_effective_interval = no_effective_interval
        # The statistical period of the metric. Unit: seconds. The default value is the original reporting period of the metric.
        # 
        # > For more information about how to query the statistical period of a metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        # The Prometheus alert configurations.
        # 
        # > You need to configure this parameter only when you create a Prometheus alert rule for Hybrid Cloud Monitoring.
        self.prometheus_shrink = prometheus_shrink
        # The resource information. Examples: `[{"instanceId":"i-uf6j91r34rnwawoo****"}]` and `[{"userId":"100931896542****"}]`.
        # 
        # For more information about the dimensions supported by the resource information, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.resources = resources
        # The alert rule ID.
        # 
        # You can enter a new alert rule ID or use an existing alert rule ID in CloudMonitor. For more information about how to query the alert rule ID, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule ID, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The alert rule name.
        # 
        # You can enter a new alert rule name or use an existing alert rule name in CloudMonitor. For more information about how to query the alert rule name, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule name, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether to send recovery notifications.
        self.send_ok = send_ok
        # The mute epoch. Unit: seconds. Default value: 86400.
        # 
        # > The mute epoch refers to the interval at which the system will send an alert notification again if the alert does not recover to Normal after it is triggered.
        self.silence_time = silence_time
        # The webhook URL to which a POST request is sent when an alert is triggered.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.composite_expression_shrink is not None:
            result['CompositeExpression'] = self.composite_expression_shrink

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if self.prometheus_shrink is not None:
            result['Prometheus'] = self.prometheus_shrink

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
            temp_model = main_models.PutResourceMetricRuleShrinkRequestEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompositeExpression') is not None:
            self.composite_expression_shrink = m.get('CompositeExpression')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.PutResourceMetricRuleShrinkRequestLabels()
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

        if m.get('Prometheus') is not None:
            self.prometheus_shrink = m.get('Prometheus')

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

class PutResourceMetricRuleShrinkRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key.
        self.key = key
        # The label value.
        # 
        # > The label value supports template parameters. The template parameters are replaced with the actual label values.
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

class PutResourceMetricRuleShrinkRequestEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.PutResourceMetricRuleShrinkRequestEscalationsCritical = None,
        info: main_models.PutResourceMetricRuleShrinkRequestEscalationsInfo = None,
        warn: main_models.PutResourceMetricRuleShrinkRequestEscalationsWarn = None,
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
            temp_model = main_models.PutResourceMetricRuleShrinkRequestEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.PutResourceMetricRuleShrinkRequestEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.PutResourceMetricRuleShrinkRequestEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class PutResourceMetricRuleShrinkRequestEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
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
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        # The statistical method for Warn-level alerts.
        # 
        # The valid values are determined by the Statistics column corresponding to the MetricName of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values for this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn, and Info. For the alert level you set, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Warn-level alerts.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

class PutResourceMetricRuleShrinkRequestEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
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
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        # The statistical method for Info-level alerts.
        # 
        # The valid values are determined by the Statistics column corresponding to the MetricName of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values for this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn, and Info. For the alert level you set, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Info-level alerts.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Info-level alerts.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

class PutResourceMetricRuleShrinkRequestEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
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
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        # The statistical method for Critical-level alerts.
        # 
        # The valid values are determined by the Statistics column corresponding to the MetricName of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values for this parameter, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must configure the Settings for at least one of the following alert levels: Critical, Warn, and Info. For the alert level you set, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for Critical-level alerts.
        # 
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of retries for Critical-level alerts.
        # 
        # > You must configure at least one of the following alert levels: Critical, Warn, and Info. For the configured alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

