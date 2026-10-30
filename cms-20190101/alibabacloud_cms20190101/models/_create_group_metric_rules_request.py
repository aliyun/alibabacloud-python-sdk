# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateGroupMetricRulesRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        group_metric_rules: List[main_models.CreateGroupMetricRulesRequestGroupMetricRules] = None,
        region_id: str = None,
    ):
        # The ID of the application group.
        # 
        # For information about how to obtain the application group ID, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The list of metric-based alert rules for the application group.
        self.group_metric_rules = group_metric_rules
        self.region_id = region_id

    def validate(self):
        if self.group_metric_rules:
            for v1 in self.group_metric_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['GroupMetricRules'] = []
        if self.group_metric_rules is not None:
            for k1 in self.group_metric_rules:
                result['GroupMetricRules'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.group_metric_rules = []
        if m.get('GroupMetricRules') is not None:
            for k1 in m.get('GroupMetricRules'):
                temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRules()
                self.group_metric_rules.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateGroupMetricRulesRequestGroupMetricRules(DaraModel):
    def __init__(
        self,
        escalations: main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalations = None,
        category: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        labels: List[main_models.CreateGroupMetricRulesRequestGroupMetricRulesLabels] = None,
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
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain the abbreviation, see the `metricCategory` tag in the `Labels` response parameter of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        # 
        # This parameter is required.
        self.category = category
        # The alert contact group.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain the alert contact group, see [DescribeContactGroupList](https://help.aliyun.com/document_detail/114922.html).
        self.contact_groups = contact_groups
        # The monitoring dimensions of the specified resource.
        # 
        # The value is a collection of `key:value` pairs, such as `{"userId":"120886317861****"}` and `{"instanceId":"i-2ze2d6j5uhg20x47****"}`.
        self.dimensions = dimensions
        # The effective period of the alert rule. Valid values of N: 1 to 200.
        self.effective_interval = effective_interval
        # The subject of the alert notification email.
        # 
        # Valid values of N: 1 to 200.
        self.email_subject = email_subject
        # The detection period of the alert rule.
        # 
        # Valid values of N: 1 to 200.
        # 
        # Unit: seconds. The default value is the minimum reporting frequency of the metric.
        # 
        # > Keep the detection period of the alert rule consistent with the data reporting period. If the detection period is shorter than the data reporting period, alerts may not be triggered due to insufficient data.
        self.interval = interval
        # The tag keys of the alert rule.
        self.labels = labels
        # The name of the metric.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain the metric name, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Cloud service monitoring](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain the namespace of an Alibaba Cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Cloud service monitoring](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The processing method when no monitoring data is found. Valid values:
        # - KEEP_LAST_STATE (default): No action is performed.
        # - INSUFFICIENT_DATA: An alert whose content is "Insufficient Data" is triggered.
        # - OK: The status is considered normal.
        # 
        # Valid values of N: 1 to 200.
        self.no_data_policy = no_data_policy
        # The time period during which the alert rule is ineffective. Valid values of N: 1 to 200.
        self.no_effective_interval = no_effective_interval
        # The advanced settings.
        # 
        # Format: {"key1":"value1","key2":"value2"}. For example, {"NotSendOK":true} specifies whether to send an alert recovery notification. The key is NotSendOK, and the value is true (do not send) or false (send, which is the default).
        self.options = options
        # The reporting period of monitoring data.
        # 
        # Valid values of N: 1 to 200. 
        # 
        # The value of `Period` must be 60 or a multiple of 60. Unit: seconds. Default value: 300.
        self.period = period
        # The ID of the alert rule.
        # 
        # Valid values of N: 1 to 200.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # Valid values of N: 1 to 200.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The mute period of the alert notification. Valid values of N: 1 to 200.
        # 
        # Unit: seconds. Default value: 86400. Minimum value: 3600.
        self.silence_time = silence_time
        # The callback URL to which an alert notification is sent. Valid values of N: 1 to 200.
        # 
        # Specify a publicly accessible URL. CloudMonitor sends a POST request to push alert information to this URL. Only the HTTP protocol is supported.
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
            temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRulesLabels()
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

class CreateGroupMetricRulesRequestGroupMetricRulesLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the alert rule. The tag is included in alert notifications.
        # 
        # Valid values of N: 1 to 200.
        self.key = key
        # The tag value of the alert rule. The tag is included in alert notifications.
        # 
        # Valid values of N: 1 to 200.
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

class CreateGroupMetricRulesRequestGroupMetricRulesEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsCritical = None,
        info: main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsInfo = None,
        warn: main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsWarn = None,
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
            temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.CreateGroupMetricRulesRequestGroupMetricRulesEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class CreateGroupMetricRulesRequestGroupMetricRulesEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for Warn-level alerts. Valid values:
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
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Warn-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For information about how to obtain the valid values, see [Cloud service monitoring](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.threshold = threshold
        # The number of times that the monitoring metric must reach the alert threshold before a Warn-level alert notification is sent.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Settings for at least one of the alert severity levels Critical, Warn (warning), or Info must be specified. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
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

class CreateGroupMetricRulesRequestGroupMetricRulesEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for Info-level alerts. Valid values:
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
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For information about how to obtain the valid values, see [Cloud service monitoring](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.statistics = statistics
        # The threshold for Info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.threshold = threshold
        # The number of times that the monitoring metric must reach the alert threshold before an Info-level alert notification is sent.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Settings for at least one of the alert severity levels Critical, Warn (warning), or Info must be specified. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
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

class CreateGroupMetricRulesRequestGroupMetricRulesEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: str = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for Critical-level alerts. Valid values:
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
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # The statistical method for Critical-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column corresponding to the `MetricName` of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For information about how to obtain the valid values, see [Cloud service monitoring](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.statistics = statistics
        # The threshold that triggers Critical-level alert notifications.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Set at least one of the alert severity levels Critical, Warn, or Info. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
        self.threshold = threshold
        # The number of times that the monitoring metric must reach the alert threshold before a Critical-level alert notification is sent.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > Settings for at least one of the alert severity levels Critical, Warn (warning), or Info must be specified. For each specified alert severity level, you must set all of the following parameters: Statistics, ComparisonOperator, Threshold, and Times.
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

