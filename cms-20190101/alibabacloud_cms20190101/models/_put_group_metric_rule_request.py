# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutGroupMetricRuleRequest(DaraModel):
    def __init__(
        self,
        escalations: main_models.PutGroupMetricRuleRequestEscalations = None,
        category: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        dry_run: bool = None,
        effective_interval: str = None,
        email_subject: str = None,
        extra_dimension_json: str = None,
        group_id: str = None,
        interval: str = None,
        labels: List[main_models.PutGroupMetricRuleRequestLabels] = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        options: str = None,
        period: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # For information about how to obtain the abbreviation of an Alibaba Cloud service name, see the `metricCategory` field in the `Labels` response parameter of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        self.category = category
        # The alert contact group.
        self.contact_groups = contact_groups
        # The first-level dimension of the alert rule in the application group.
        # 
        # Format: a collection of `key:value` pairs. Examples: `{"userId":"120886317861****"}` and `{"instanceId":"i-m5e1qg6uo38rztr4****"}`.
        self.dimensions = dimensions
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: sends a check request. The system does not bind a security group to the instance. The check items include whether required parameters are specified, the request format, and service limits. If the check fails, the system returns an error. If the check succeeds, the system returns the error code `DryRunOperation`.
        # - **false** (default value): sends a normal request. If the check succeeds, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The effective period of the alert rule.
        self.effective_interval = effective_interval
        # The subject of the alert email.
        self.email_subject = email_subject
        # The second-level or third-level dimension of the alert rule in the application group.
        # 
        # Format: a collection of `key:value` pairs. Examples: `port:80` and `/dev/xvda:d-m5e6yphgzn3aprwu****`.
        # 
        # If the first-level dimension of the alert rule is `{"instanceId":"i-m5e1qg6uo38rztr4****"}`, the second-level dimension is the cloud disk in the instance, such as `{"/dev/xvda":"d-m5e6yphgzn3aprwu****"}`.
        self.extra_dimension_json = extra_dimension_json
        # The ID of the application group.
        # 
        # For information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The detection period of the alert rule. Unit: seconds.
        # 
        # > Make sure the detection period of the alert rule is the same as the data reporting period. If the detection period is shorter than the data reporting period, alerts may not be triggered due to insufficient data.
        self.interval = interval
        # The tags of the alert rule.
        # 
        # Alert notifications include tags.
        self.labels = labels
        # The name of the metric.
        # 
        # For information about how to obtain the name of a metric, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service.
        # 
        # For information about how to obtain the namespace of an Alibaba Cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The action to take when no monitoring data is found. Valid values:
        # - KEEP_LAST_STATE (default value): Takes no action.
        # - INSUFFICIENT_DATA: Sends an alert notification indicating that no data is found.
        # - OK: Sends an alert notification indicating that the status is normal.
        self.no_data_policy = no_data_policy
        # The time range during which the alert rule is inactive.
        self.no_effective_interval = no_effective_interval
        # The advanced settings.
        # 
        # Format: `{"key1":"value1","key2":"value2"}`. Example: `{"NotSendOK":true}`, which specifies whether to send alert recovery notifications. The key is `NotSendOK`, and the value is `true` (do not send) or `false` (send by default).
        self.options = options
        # The reporting period of monitoring data.
        # 
        # The value of `Period` must be 60 or an integer multiple of 60. Unit: seconds. Default value: 300.
        self.period = period
        # The ID of the alert rule.
        # 
        # - To create an alert rule for the application group, enter an alert rule ID.
        # 
        # - To modify a specified alert rule in the application group, you must obtain the alert rule ID. For information about how to obtain the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # - To create an alert rule for the application group, enter an alert rule name.
        # 
        # - To modify a specified alert rule in the application group, you must obtain the alert rule name. For information about how to obtain the name of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The mute for epoch.
        # 
        # Unit: seconds. Default value: 86400.
        self.silence_time = silence_time
        # The webhook URL that is called when an alert is triggered.
        # 
        # Enter a publicly accessible URL. CloudMonitor pushes alert notifications to this URL by sending POST requests. Only HTTP is supported.
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

        if self.category is not None:
            result['Category'] = self.category

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject

        if self.extra_dimension_json is not None:
            result['ExtraDimensionJson'] = self.extra_dimension_json

        if self.group_id is not None:
            result['GroupId'] = self.group_id

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

        if self.options is not None:
            result['Options'] = self.options

        if self.period is not None:
            result['Period'] = self.period

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
        if m.get('Escalations') is not None:
            temp_model = main_models.PutGroupMetricRuleRequestEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('ExtraDimensionJson') is not None:
            self.extra_dimension_json = m.get('ExtraDimensionJson')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.PutGroupMetricRuleRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoDataPolicy') is not None:
            self.no_data_policy = m.get('NoDataPolicy')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class PutGroupMetricRuleRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the alert rule.
        self.key = key
        # The tag value of the alert rule.
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

class PutGroupMetricRuleRequestEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.PutGroupMetricRuleRequestEscalationsCritical = None,
        info: main_models.PutGroupMetricRuleRequestEscalationsInfo = None,
        warn: main_models.PutGroupMetricRuleRequestEscalationsWarn = None,
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
            temp_model = main_models.PutGroupMetricRuleRequestEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.PutGroupMetricRuleRequestEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.PutGroupMetricRuleRequestEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class PutGroupMetricRuleRequestEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The threshold comparison operator for Warn-level alerts. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold.
        # - GreaterThanThreshold: greater than the threshold.
        # - LessThanOrEqualToThreshold: less than or equal to the threshold.
        # - LessThanThreshold: less than the threshold.
        # - NotEqualToThreshold: not equal to the threshold.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the last period.
        # - LessThanLastPeriod: less than the value in the last period.
        self.comparison_operator = comparison_operator
        # The statistical method for Warn-level alerts. Separate multiple statistical methods with commas (,).
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        self.threshold = threshold
        # The number of retries for Warn-level alerts.
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

class PutGroupMetricRuleRequestEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The threshold comparison operator for Info-level alerts. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold.
        # - GreaterThanThreshold: greater than the threshold.
        # - LessThanOrEqualToThreshold: less than or equal to the threshold.
        # - LessThanThreshold: less than the threshold.
        # - NotEqualToThreshold: not equal to the threshold.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the last period.
        # - LessThanLastPeriod: less than the value in the last period.
        self.comparison_operator = comparison_operator
        # The statistical method for Info-level alerts. Separate multiple statistical methods with commas (,).
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Info-level alerts.
        self.threshold = threshold
        # The number of retries for Info-level alerts.
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

class PutGroupMetricRuleRequestEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The threshold comparison operator for Critical-level alerts. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold.
        # - GreaterThanThreshold: greater than the threshold.
        # - LessThanOrEqualToThreshold: less than or equal to the threshold.
        # - LessThanThreshold: less than the threshold.
        # - NotEqualToThreshold: not equal to the threshold.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the last period.
        # - LessThanLastPeriod: less than the value in the last period.
        self.comparison_operator = comparison_operator
        # The statistical method for Critical-level alerts. Separate multiple statistical methods with commas (,).
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service. Examples: Maximum, Minimum, and Average. For information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Critical-level alerts.
        self.threshold = threshold
        # The number of retries for Critical-level alerts.
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

