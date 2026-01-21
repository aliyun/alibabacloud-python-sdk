# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertingMetricRuleResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resources: main_models.DescribeAlertingMetricRuleResourcesResponseBodyResources = None,
        success: bool = None,
        total: int = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The resources that are associated with the alert rule.
        self.resources = resources
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResourcesResource(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        enable: str = None,
        escalation: main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalation = None,
        group_id: str = None,
        last_alert_time: str = None,
        last_modify_time: str = None,
        level: int = None,
        metric_name: str = None,
        metric_values: str = None,
        namespace: str = None,
        product_category: str = None,
        resource: str = None,
        retry_times: str = None,
        rule_id: str = None,
        rule_name: str = None,
        start_time: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The dimensions based on which the resources are queried.
        self.dimensions = dimensions
        # Indicates whether the alert rule is enabled. Valid values:
        # 
        # *   true: The alert rule is enabled.
        # *   false: The alert rule is disabled.
        self.enable = enable
        # The alert rule based on which the alert is triggered.
        self.escalation = escalation
        # The ID of the application group.
        # 
        # >  If the alert rule is associated with an application group, the ID of the application group is returned in this parameter.
        self.group_id = group_id
        # The time when the last alert was triggered for the resource based on the alert rule. The value is a timestamp.
        # 
        # Unit: milliseconds.
        self.last_alert_time = last_alert_time
        # The time when the alert rule was last modified. The value is a timestamp.
        # 
        # Unit: milliseconds.
        self.last_modify_time = last_modify_time
        # The severity level and notification methods of the alert. Valid values:
        # 
        # *   4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # The metric name.
        self.metric_name = metric_name
        # The metric value that triggered the alert based on the alert rule. The value is a JSON string.
        self.metric_values = metric_values
        # The namespace of the cloud service.
        self.namespace = namespace
        # The type of the cloud service.
        self.product_category = product_category
        # The resources that are monitored.
        self.resource = resource
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.retry_times = retry_times
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The time when the resource was associated with the alert rule. The value is a timestamp.
        # 
        # Unit: milliseconds.
        self.start_time = start_time
        # The method used to calculate the metric values that trigger alerts.
        self.statistics = statistics
        # The alert threshold.
        self.threshold = threshold

    def validate(self):
        if self.escalation:
            self.escalation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.escalation is not None:
            result['Escalation'] = self.escalation.to_map()

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.last_alert_time is not None:
            result['LastAlertTime'] = self.last_alert_time

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_values is not None:
            result['MetricValues'] = self.metric_values

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.product_category is not None:
            result['ProductCategory'] = self.product_category

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Escalation') is not None:
            temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalation()
            self.escalation = temp_model.from_map(m.get('Escalation'))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LastAlertTime') is not None:
            self.last_alert_time = m.get('LastAlertTime')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricValues') is not None:
            self.metric_values = m.get('MetricValues')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ProductCategory') is not None:
            self.product_category = m.get('ProductCategory')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalation(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResource(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        expression: str = None,
        expression_list: main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionList = None,
        expression_list_join: str = None,
        expression_raw: str = None,
        level: int = None,
        pre_condition: str = None,
        tag: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The description of the alert rule.
        # 
        # >  This parameter indicates the content of the alert rule. If the metric value meets the alert condition, an alert is triggered.
        self.expression = expression
        # The description of the multi-metric alert rule.
        self.expression_list = expression_list
        # The relationship between multiple metrics. Valid values:
        # 
        # *   &&: If all metrics meet the alert conditions, CloudMonitor sends alert notifications.
        # *   ||: If one of the metrics meets the alert conditions, CloudMonitor sends alert notifications.
        self.expression_list_join = expression_list_join
        # The trigger conditions that are created by using expressions. You can use expressions to create trigger conditions in the following scenarios:
        # 
        # *   Set an alert blacklist for specific resources. For example, if you specify `$instanceId != \\"i-io8kfvcpp7x5****\\" ``&&`` $Average > 50`, no alert is triggered when the `average metric value` of the `i-io8kfvcpp7x5****` instance exceeds 50.
        # *   Set a special alert threshold for a specified instance in the rule. For example, if you specify `$Average > ($instanceId == \\"i-io8kfvcpp7x5****\\"? 80: 50)`, an alert is triggered when the `average metric value` of the `i-io8kfvcpp7x5****` instance exceeds 80 or the `average metric value` of other instances exceeds 50.
        # *   Limit the number of instances whose metric values exceed the threshold. For example, if you specify `count($Average > 20) > 3`, an alert is triggered only when the `average metric value` of more than three instances exceeds 20.
        self.expression_raw = expression_raw
        # The severity level and notification methods of the alert. Valid values:
        # 
        # *   4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # The operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   `>=`
        # *   `=`
        # *   `<=`
        # *   `>`
        # *   `<`
        # *   `!=`
        self.pre_condition = pre_condition
        # This parameter is deprecated.
        self.tag = tag
        # The alert threshold.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.times = times

    def validate(self):
        if self.expression_list:
            self.expression_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.expression_list is not None:
            result['ExpressionList'] = self.expression_list.to_map()

        if self.expression_list_join is not None:
            result['ExpressionListJoin'] = self.expression_list_join

        if self.expression_raw is not None:
            result['ExpressionRaw'] = self.expression_raw

        if self.level is not None:
            result['Level'] = self.level

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('ExpressionList') is not None:
            temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionList()
            self.expression_list = temp_model.from_map(m.get('ExpressionList'))

        if m.get('ExpressionListJoin') is not None:
            self.expression_list_join = m.get('ExpressionListJoin')

        if m.get('ExpressionRaw') is not None:
            self.expression_raw = m.get('ExpressionRaw')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionList(DaraModel):
    def __init__(
        self,
        expression_list: List[main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionListExpressionList] = None,
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
                temp_model = main_models.DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionListExpressionList()
                self.expression_list.append(temp_model.from_map(k1))

        return self

class DescribeAlertingMetricRuleResourcesResponseBodyResourcesResourceEscalationResourceExpressionListExpressionList(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The metric name.
        self.metric_name = metric_name
        # The statistical period of the metric. Unit: seconds. The default value is the interval at which the monitoring data of the metric is collected.
        self.period = period
        # The statistical method of the alert level. Valid values:
        # 
        # *   Maximum
        # *   Minimum
        # *   Average
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

