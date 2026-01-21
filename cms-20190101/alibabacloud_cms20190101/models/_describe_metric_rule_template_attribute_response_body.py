# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricRuleTemplateAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resource: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResource = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details of the alert template.
        self.resource = resource
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.resource:
            self.resource.validate()

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

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resource') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResource(DaraModel):
    def __init__(
        self,
        alert_templates: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplates = None,
        description: str = None,
        name: str = None,
        rest_version: str = None,
        template_id: str = None,
    ):
        # The queried alert templates.
        self.alert_templates = alert_templates
        # The description of the alert template.
        self.description = description
        # The name of the alert template.
        self.name = name
        # The version of the alert template.
        self.rest_version = rest_version
        # The ID of the alert template.
        self.template_id = template_id

    def validate(self):
        if self.alert_templates:
            self.alert_templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_templates is not None:
            result['AlertTemplates'] = self.alert_templates.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.rest_version is not None:
            result['RestVersion'] = self.rest_version

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTemplates') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplates()
            self.alert_templates = temp_model.from_map(m.get('AlertTemplates'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RestVersion') is not None:
            self.rest_version = m.get('RestVersion')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplates(DaraModel):
    def __init__(
        self,
        alert_template: List[main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplate] = None,
    ):
        self.alert_template = alert_template

    def validate(self):
        if self.alert_template:
            for v1 in self.alert_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertTemplate'] = []
        if self.alert_template is not None:
            for k1 in self.alert_template:
                result['AlertTemplate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_template = []
        if m.get('AlertTemplate') is not None:
            for k1 in m.get('AlertTemplate'):
                temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplate()
                self.alert_template.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplate(DaraModel):
    def __init__(
        self,
        category: str = None,
        escalations: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalations = None,
        labels: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabels = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        rule_name: str = None,
        selector: str = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        # The abbreviation of the Alibaba Cloud service name.
        self.category = category
        # The threshold and the alert level.
        self.escalations = escalations
        # The tags of the alert template.
        self.labels = labels
        # The metric name.
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service.
        self.namespace = namespace
        # The method that is used to handle alerts when no monitoring data is found. Valid values:
        # 
        # *   KEEP_LAST_STATE (default): No operation is performed.
        # *   INSUFFICIENT_DATA: An alert whose content is "Insufficient data" is triggered.
        # *   OK: The status is considered normal.
        self.no_data_policy = no_data_policy
        # The name of the alert rule.
        self.rule_name = rule_name
        # The dimension of the alert. It is an extended field.
        self.selector = selector
        self.silence_time = silence_time
        # The callback URL to which a request is sent when an alert is triggered.
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.labels is not None:
            result['Labels'] = self.labels.to_map()

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_data_policy is not None:
            result['NoDataPolicy'] = self.no_data_policy

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Escalations') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('Labels') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabels()
            self.labels = temp_model.from_map(m.get('Labels'))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoDataPolicy') is not None:
            self.no_data_policy = m.get('NoDataPolicy')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabels(DaraModel):
    def __init__(
        self,
        labels: List[main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabelsLabels] = None,
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
                temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabelsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateLabelsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the alert template.
        self.key = key
        # The tag value of the alert template.
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

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsCritical = None,
        info: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsInfo = None,
        warn: main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsWarn = None,
    ):
        # The conditions for triggering Critical-level alerts.
        self.critical = critical
        # The conditions for triggering Info-level alerts.
        self.info = info
        # The conditions for triggering Warn-level alerts.
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
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator that is used to compare the metric value with the threshold for Warn-level alerts. Valid values:
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
        # The statistical method for Warn-level alerts.
        # 
        # The value of the `Statistics` parameter varies with the cloud service. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Warn-level alerts.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before a Warn-level alert is triggered.
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

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator that is used to compare the metric value with the threshold for Info-level alerts. Valid values:
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
        # The statistical method for Info-level alerts.
        # 
        # The value of the `Statistics` parameter varies with the cloud service. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Info-level alerts.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before an Info-level alert is triggered.
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

class DescribeMetricRuleTemplateAttributeResponseBodyResourceAlertTemplatesAlertTemplateEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator that is used to compare the metric value with the threshold for Critical-level alerts. Valid values:
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
        # The statistical method for Critical-level alerts.
        # 
        # The value of the `Statistics` parameter varies with the cloud service. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.statistics = statistics
        # The threshold for Critical-level alerts.
        self.threshold = threshold
        # The consecutive number of times for which the metric value meets the alert condition before a Critical-level alert is triggered.
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

