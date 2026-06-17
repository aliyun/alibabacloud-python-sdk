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
        composite_expression_shrink: str = None,
        contact_groups: str = None,
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
        # The alert conditions for multiple metrics.
        # 
        # > Single-metric and multi-metric alert conditions are mutually exclusive and cannot be set at the same time.
        self.composite_expression_shrink = composite_expression_shrink
        # The alert contact group. Alert notifications are sent to the alert contacts in this alert contact group.
        # 
        # > An alert contact group contains one or more alert contacts. For information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # The effective period of the alert rule.
        self.effective_interval = effective_interval
        # The subject of the alert email.
        self.email_subject = email_subject
        # The trigger period of the alert rule. Unit: seconds.
        # 
        # > For information about how to query the statistical period of a metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.interval = interval
        # The labels that are written to the metric and displayed in alert notifications when the metric meets the alert condition.
        # 
        # > This feature is the same as the Label feature in Prometheus alerting.
        self.labels = labels
        # The name of the metric. For information about how to query metric names, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > If you create a Prometheus alert rule for Hybrid Cloud Monitoring, this parameter specifies the name of the metric repository. For information about how to obtain the metric repository name, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service. For information about how to query the namespace of an Alibaba Cloud service, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > If you create a Prometheus alert rule for Hybrid Cloud Monitoring, set this parameter to `acs_prometheus`.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The processing method when no monitoring data is found. Valid values:
        # 
        # - KEEP_LAST_STATE (default): No action is taken.
        # - INSUFFICIENT_DATA: An alert whose content is "Insufficient data" is triggered.
        # - OK: The status is considered normal.
        self.no_data_policy = no_data_policy
        # The time range during which the alert rule is ineffective.
        self.no_effective_interval = no_effective_interval
        # The statistical period of the metric. Unit: seconds. The default value is the original reporting period of the metric.
        # 
        # > For information about how to query the statistical period of a metric, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        # The Prometheus alert configuration.
        # 
        # > Set this parameter only when you create a Prometheus alert rule for Hybrid Cloud Monitoring.
        self.prometheus_shrink = prometheus_shrink
        # The resource information, such as `[{"instanceId":"i-uf6j91r34rnwawoo****"}]` or `[{"userId":"100931896542****"}]`.
        # 
        # For information about the supported monitoring dimensions, see [Alibaba Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        self.resources = resources
        # The ID of the alert rule.
        # 
        # You can enter a new alert rule ID or use the ID of an existing alert rule in CloudMonitor. For information about how to query alert rule IDs, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule ID, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # You can enter a new alert rule name or use the name of an existing alert rule in CloudMonitor. For information about how to query alert rule names, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # > If you enter a new alert rule name, a threshold alert rule is created.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Specifies whether to send a recovery notification.
        self.send_ok = send_ok
        # The mute period. Unit: seconds. Default value: 86400.
        # 
        # > The mute period specifies the interval at which an alert notification is re-sent if the alert does not recover to Normal.
        self.silence_time = silence_time
        # The callback URL to which a POST request is sent when an alert is triggered.
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

        if self.composite_expression_shrink is not None:
            result['CompositeExpression'] = self.composite_expression_shrink

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

        if m.get('CompositeExpression') is not None:
            self.composite_expression_shrink = m.get('CompositeExpression')

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
        # > The label value supports template parameters. Template parameters are replaced with actual label values.
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
        # Warn级别阈值比较符。取值：
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
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        # Warn级别报警统计方法。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Warn级别报警阈值。
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Warn级别报警重试次数。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
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
        # Info级别阈值比较符。取值：
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
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        # Info级别报警统计方法。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Info级别报警阈值。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Info级别报警重试次数。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
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
        # Critical级别阈值比较符。取值：
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
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        # Critical级别报警统计方法。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Critical级别报警阈值。
        # 
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Critical级别报警重试次数。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
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

