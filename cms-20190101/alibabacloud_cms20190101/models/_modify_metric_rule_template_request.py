# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyMetricRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        alert_templates: List[main_models.ModifyMetricRuleTemplateRequestAlertTemplates] = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        rest_version: int = None,
        template_id: int = None,
    ):
        # The details of the alert template.
        self.alert_templates = alert_templates
        # The description of the alert template.
        self.description = description
        # The name of the alert template.
        # 
        # For information about how to obtain the name of an alert template, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
        self.name = name
        self.region_id = region_id
        # The version of the alert template. The version changes with the number of times that the alert template is modified.
        # 
        # For information about how to obtain the version of an alert template, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
        # 
        # This parameter is required.
        self.rest_version = rest_version
        # The ID of the alert template.
        # 
        # For information about how to obtain the ID of an alert template, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.alert_templates:
            for v1 in self.alert_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertTemplates'] = []
        if self.alert_templates is not None:
            for k1 in self.alert_templates:
                result['AlertTemplates'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rest_version is not None:
            result['RestVersion'] = self.rest_version

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_templates = []
        if m.get('AlertTemplates') is not None:
            for k1 in m.get('AlertTemplates'):
                temp_model = main_models.ModifyMetricRuleTemplateRequestAlertTemplates()
                self.alert_templates.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RestVersion') is not None:
            self.rest_version = m.get('RestVersion')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class ModifyMetricRuleTemplateRequestAlertTemplates(DaraModel):
    def __init__(
        self,
        escalations: main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalations = None,
        category: str = None,
        metric_name: str = None,
        namespace: str = None,
        period: int = None,
        rule_name: str = None,
        selector: str = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # The abbreviation of the cloud service name.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For more information about how to obtain the abbreviation of a cloud service name, see `metricCategory` in the response parameter `Labels` of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        self.category = category
        # The metric name.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain metrics, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For information about how to obtain the namespace of a cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The statistical period of the monitoring data.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > If the value is set to 300 seconds, the monitoring data is collected every 300 seconds. If the monitoring data is reported every 1 minute, the alert system calculates the average, maximum, and minimum values of the monitoring data of 5 minutes and checks whether the aggregated values exceed the threshold. To prevent unexpected alerts, we recommend that you set this parameter together with other parameters.
        self.period = period
        # The name of the alert rule.
        # 
        # Valid values of N: 1 to 200.
        self.rule_name = rule_name
        # The dimension of the alert. It is an extended field.
        # 
        # Valid values of N: 1 to 200.
        # 
        # For example, an alert template is applied to an application group, this parameter is set to `{"disk":"/"}`, and the MetricName parameter is set to `DiskUtilization`. In this case, the generated alert rule is applied to the root disk partition (`"/"`) of all instances in the application group to which the alert template is applied.
        # 
        # > For more information about the values of extended fields, see [DescribeMetricRuleTemplateAttribute](https://help.aliyun.com/document_detail/114979.html).
        self.selector = selector
        # The callback URL.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The callback URL must be accessible over the Internet. CloudMonitor pushes an alert notification to the specified callback URL by sending an HTTP POST request. Only the HTTP protocol is supported.
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.category is not None:
            result['Category'] = self.category

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.period is not None:
            result['Period'] = self.period

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.selector is not None:
            result['Selector'] = self.selector

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Escalations') is not None:
            temp_model = main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Selector') is not None:
            self.selector = m.get('Selector')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class ModifyMetricRuleTemplateRequestAlertTemplatesEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsCritical = None,
        info: main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsInfo = None,
        warn: main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsWarn = None,
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
            temp_model = main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.n = n
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.n = n
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class ModifyMetricRuleTemplateRequestAlertTemplatesEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.n = n
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

        if self.n is not None:
            result['N'] = self.n

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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

