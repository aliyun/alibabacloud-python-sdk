# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutResourceMetricRuleRequest(DaraModel):
    def __init__(
        self,
        escalations: main_models.PutResourceMetricRuleRequestEscalations = None,
        composite_expression: main_models.PutResourceMetricRuleRequestCompositeExpression = None,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        labels: List[main_models.PutResourceMetricRuleRequestLabels] = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        period: str = None,
        prometheus: main_models.PutResourceMetricRuleRequestPrometheus = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # The trigger conditions for multiple metrics.
        # 
        # >  The trigger conditions for a single metric and multiple metrics are mutually exclusive. You cannot specify trigger conditions for a single metric and multiple metrics at the same time.
        self.composite_expression = composite_expression
        # The alert contact groups. Alert notifications are sent to the alert contacts in the alert contact group.
        # 
        # >  An alert contact group can contain one or more alert contacts. For information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # The period of time during which the alert rule is effective.
        self.effective_interval = effective_interval
        # The subject of the alert notification email.
        self.email_subject = email_subject
        # The interval at which alerts are triggered based on the alert rule. Unit: seconds.
        # 
        # >  For more information about how to query the statistical periods of metrics, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.interval = interval
        # If the metric meets the specified condition in the alert rule and CloudMonitor sends an alert notification, the tag is also written to the metric and displayed in the alert notification.
        # 
        # >  This parameter is equivalent to the Label parameter of Prometheus alerts.
        self.labels = labels
        # The metric name. For more information about how to query metric names, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  If you create a Prometheus alert rule for Hybrid Cloud Monitoring, you must set this parameter to the name of the namespace. For more information about how to query the names of namespaces, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the cloud service. For more information about how to query the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  If you create a Prometheus alert rule for Hybrid Cloud Monitoring, you must set this parameter to `acs_prometheus`.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The method that is used to handle alerts when no monitoring data is found. Valid value:
        # 
        # *   KEEP_LAST_STATE (default): No operation is performed.
        # *   INSUFFICIENT_DATA: An alert whose content is "Insufficient data" is triggered.
        # *   OK: The status is considered normal.
        self.no_data_policy = no_data_policy
        # The period of time during which the alert rule is ineffective.
        self.no_effective_interval = no_effective_interval
        # The statistical period of the metric. Unit: seconds. The default value is the interval at which the monitoring data of the metric is collected.
        # 
        # >  For more information about how to query the statistical periods of metrics, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        # Prometheus alerts.
        # 
        # >  This parameter is required only if you create a Prometheus alert rule for Hybrid Cloud Monitoring.
        self.prometheus = prometheus
        # The resource information. Examples: `[{"instanceId":"i-uf6j91r34rnwawoo****"}]` and `[{"userId":"100931896542****"}]`.
        # 
        # For more information about the supported dimensions that are used to query resources, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.resources = resources
        # The ID of the alert rule.
        # 
        # You can specify a new ID or the ID of an existing alert rule. For more information about how to query the IDs of alert rules, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # >  If you specify a new ID, a threshold-triggered alert rule is created.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # You can specify a new name or the name of an existing alert rule. For more information about how to query the names of alert rules, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        # 
        # >  If you specify a new name, a threshold-triggered alert rule is created.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        # 
        # >  If an alert is not cleared after the mute period ends, CloudMonitor resends an alert notification.
        self.silence_time = silence_time
        # The callback URL to which a POST request is sent when an alert is triggered based on the alert rule.
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()
        if self.composite_expression:
            self.composite_expression.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.prometheus:
            self.prometheus.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.composite_expression is not None:
            result['CompositeExpression'] = self.composite_expression.to_map()

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

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Escalations') is not None:
            temp_model = main_models.PutResourceMetricRuleRequestEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('CompositeExpression') is not None:
            temp_model = main_models.PutResourceMetricRuleRequestCompositeExpression()
            self.composite_expression = temp_model.from_map(m.get('CompositeExpression'))

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
                temp_model = main_models.PutResourceMetricRuleRequestLabels()
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
            temp_model = main_models.PutResourceMetricRuleRequestPrometheus()
            self.prometheus = temp_model.from_map(m.get('Prometheus'))

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

class PutResourceMetricRuleRequestPrometheus(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.PutResourceMetricRuleRequestPrometheusAnnotations] = None,
        level: str = None,
        prom_ql: str = None,
        times: int = None,
    ):
        # The annotations of the Prometheus alert rule. When a Prometheus alert is triggered, the system renders the annotated keys and values to help you understand the metrics and alert rule.
        # 
        # >  This parameter is equivalent to the annotations parameter of open source Prometheus.
        self.annotations = annotations
        # The alert level. Valid values:
        # 
        # *   Critical
        # *   Warn
        # *   Info
        self.level = level
        # PromQL statements are supported.
        # 
        # >  The data obtained by using the PromQL query statement is the monitoring data. You must include the alert threshold in this statement.
        self.prom_ql = prom_ql
        # The number of consecutive triggers. If the number of times that the metric values meet the trigger conditions reaches the value of this parameter, CloudMonitor sends alert notifications.
        self.times = times

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

        if self.level is not None:
            result['Level'] = self.level

        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.PutResourceMetricRuleRequestPrometheusAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRuleRequestPrometheusAnnotations(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the annotation.
        self.key = key
        # The value of the annotation.
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

class PutResourceMetricRuleRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        # 
        # >  You can use a template parameter to specify a tag value. CloudMonitor replaces the value of the template parameter with an actual tag value.
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

class PutResourceMetricRuleRequestCompositeExpression(DaraModel):
    def __init__(
        self,
        expression_list: List[main_models.PutResourceMetricRuleRequestCompositeExpressionExpressionList] = None,
        expression_list_join: str = None,
        expression_raw: str = None,
        level: str = None,
        times: int = None,
    ):
        # The trigger conditions that are created in standard mode.
        self.expression_list = expression_list
        # The relationship between the trigger conditions for multiple metrics. Valid value:
        # 
        # *   `&&`: An alert is triggered only if all metrics meet the trigger conditions. An alert is triggered only if the results of all expressions specified in the ExpressionList parameter are `true`.
        # *   `||`: An alert is triggered if one of the metrics meets the trigger conditions.
        self.expression_list_join = expression_list_join
        # The trigger conditions that are created by using expressions. You can use expressions to create trigger conditions in the following scenarios:
        # 
        # *   Set an alert blacklist for specific resources. For example, if you specify `$instanceId != \\"i-io8kfvcpp7x5****\\" ``&&`` $Average > 50`, no alert is triggered when the `average metric value` of the `i-io8kfvcpp7x5****` instance exceeds 50.
        # *   Set a special alert threshold for a specified instance in the rule. For example, if you specify `$Average > ($instanceId == \\"i-io8kfvcpp7x5****\\"? 80: 50)`, an alert is triggered when the `average metric value` of the `i-io8kfvcpp7x5****` instance exceeds 80 or the `average metric value` of other instances exceeds 50.
        # *   Limit the number of instances whose metric values exceed the threshold. For example, if you specify `count($Average > 20) > 3`, an alert is triggered only when the `average metric value` of more than three instances exceeds 20.
        self.expression_raw = expression_raw
        # The alert level. Valid values:
        # 
        # *   Critical
        # *   Warn
        # *   Info
        self.level = level
        # The number of consecutive triggers. If the number of times that the metric values meet the trigger conditions reaches the value of this parameter, CloudMonitor sends alert notifications.
        self.times = times

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
        self.expression_list = []
        if m.get('ExpressionList') is not None:
            for k1 in m.get('ExpressionList'):
                temp_model = main_models.PutResourceMetricRuleRequestCompositeExpressionExpressionList()
                self.expression_list.append(temp_model.from_map(k1))

        if m.get('ExpressionListJoin') is not None:
            self.expression_list_join = m.get('ExpressionListJoin')

        if m.get('ExpressionRaw') is not None:
            self.expression_raw = m.get('ExpressionRaw')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRuleRequestCompositeExpressionExpressionList(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The operator that is used to compare the metric value with the threshold. Valid value:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   EqualToThreshold: equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The metric that is used to monitor the cloud service.
        self.metric_name = metric_name
        # The aggregation period of the metric.
        # 
        # Unit: seconds.
        self.period = period
        # The statistical method of the metric. Valid value:
        # 
        # *   $Maximum: the maximum value
        # *   $Minimum: the minimum value
        # *   $Average: the average value
        # *   $Availability: the availability rate (usually used for site monitoring)
        # 
        # >  `$` is the prefix of the metric. For information about the Alibaba Cloud services that are supported by CloudMonitor, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
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

class PutResourceMetricRuleRequestEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.PutResourceMetricRuleRequestEscalationsCritical = None,
        info: main_models.PutResourceMetricRuleRequestEscalationsInfo = None,
        warn: main_models.PutResourceMetricRuleRequestEscalationsWarn = None,
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
            temp_model = main_models.PutResourceMetricRuleRequestEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.PutResourceMetricRuleRequestEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.PutResourceMetricRuleRequestEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class PutResourceMetricRuleRequestEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid value:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   EqualToThreshold: equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.comparison_operator = comparison_operator
        # The statistical methods for Warn-level alerts.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
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

class PutResourceMetricRuleRequestEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The operator that is used to compare the metric value with the threshold for Info-level alerts. Valid value:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   EqualToThreshold: equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.comparison_operator = comparison_operator
        # The statistical methods for Info-level alerts.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.statistics = statistics
        # The threshold for Info-level alerts.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
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

class PutResourceMetricRuleRequestEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid value:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   EqualToThreshold: equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.comparison_operator = comparison_operator
        # The statistical methods for Critical-level alerts.
        # 
        # The value of this parameter is determined by the `Statistics` column corresponding to the `MetricName` parameter of the specified cloud service. The value of this parameter can be Maximum, Minimum, or Average. For more information about how to obtain the value of this parameter, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.statistics = statistics
        # The threshold for Critical-level alerts.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered.
        # 
        # >  You must select at least one of the Critical, Warn, and Info alert levels and specify the Statistics, ComparisonOperator, Threshold, and Times parameters for each alert level.
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

