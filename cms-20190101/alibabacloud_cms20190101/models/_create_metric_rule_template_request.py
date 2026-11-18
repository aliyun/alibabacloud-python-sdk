# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateMetricRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        alert_templates: List[main_models.CreateMetricRuleTemplateRequestAlertTemplates] = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The alert templates.
        self.alert_templates = alert_templates
        # The description of the alert template.
        self.description = description
        # The name of the alert template.
        # 
        # This parameter is required.
        self.name = name
        self.region_id = region_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_templates = []
        if m.get('AlertTemplates') is not None:
            for k1 in m.get('AlertTemplates'):
                temp_model = main_models.CreateMetricRuleTemplateRequestAlertTemplates()
                self.alert_templates.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateMetricRuleTemplateRequestAlertTemplates(DaraModel):
    def __init__(
        self,
        escalations: main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalations = None,
        category: str = None,
        metric_name: str = None,
        namespace: str = None,
        period: int = None,
        rule_name: str = None,
        selector: str = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # The Alibaba Cloud service name or product specification abbreviation. Valid values of N: 1 to 200. Valid values:
        # - ecs: ECS instances and non-Alibaba Cloud hosts
        # - rds: ApsaraDB RDS database
        # - ads: AnalyticDB database
        # - slb: load balancing
        # - vpc: Elastic IP
        # - apigateway: API Gateway
        # - cdn: Content Delivery Network
        # - cs: Container Service for Swarm
        # - dcdn: Dynamic Route for CDN
        # - ddos: Anti-DDoS
        # - eip: Elastic IP Address
        # - elasticsearch: Elasticsearch
        # - emr: E-MapReduce
        # - ess: elastic scaling
        # - hbase: ApsaraDB for HBase database
        # - iot_edge: IoT Edge
        # - k8s_pod: Kubernetes pod
        # - kvstore_sharding: ApsaraDB for Redis Cluster Edition
        # - kvstore_splitrw: ApsaraDB for Redis Read/Write Splitting Edition
        # - kvstore_standard: ApsaraDB for Redis Standard Edition
        # - memcache: ApsaraDB for Memcache database
        # - mns: Message Service
        # - mongodb: MongoDB replica set
        # - mongodb_cluster: MongoDB cluster edition
        # - mongodb_sharding: MongoDB sharded cluster
        # - mq_topic: Message Service topic
        # - ocs: legacy ApsaraDB for Memcache database
        # - opensearch: OpenSearch
        # - oss: Object Storage Service
        # - polardb: PolarDB database
        # - petadata: HybridDB for MySQL
        # - scdn: secure acceleration
        # - sharebandwidthpackages: Internet Shared Bandwidth
        # - sls: Simple Log Service
        # - vpn: VPN Gateway
        # 
        # This parameter is required.
        self.category = category
        # The name of the metric. Valid values of N: 1 to 200.
        # 
        # > For more information, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Cloud service metrics](https://help.aliyun.com/document_detail/28619.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service. Valid values of N: 1 to 200.
        # 
        # > For more information, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Cloud service metrics](https://help.aliyun.com/document_detail/28619.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The aggregation period of the monitoring data. Unit: seconds.
        # 
        # Default value: the minimum aggregation period of the metric. You do not need to specify this parameter in most cases.
        # 
        # Valid values of N: 1 to 200.
        self.period = period
        # The name of the alert rule. Valid values of N: 1 to 200.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The options for extended fields. Valid values of N: 1 to 200.
        self.selector = selector
        # The webhook URL to which a POST request is sent when an alert is triggered.
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
            temp_model = main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalations()
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

class CreateMetricRuleTemplateRequestAlertTemplatesEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsCritical = None,
        info: main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsInfo = None,
        warn: main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsWarn = None,
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
            temp_model = main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.CreateMetricRuleTemplateRequestAlertTemplatesEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class CreateMetricRuleTemplateRequestAlertTemplatesEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the warn-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to 
        # - GreaterThanThreshold: greater than 
        # - LessThanOrEqualToThreshold: less than or equal to 
        # - LessThanThreshold: less than 
        # - NotEqualToThreshold: not equal to 
        # - GreaterThanYesterday: greater than the value at the same time yesterday 
        # - LessThanYesterday: less than the value at the same time yesterday 
        # - GreaterThanLastWeek: greater than the value at the same time last week 
        # - LessThanLastWeek: less than the value at the same time last week 
        # - GreaterThanLastPeriod: greater than the value in the last period 
        # - LessThanLastPeriod: less than the value in the last period 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for warning alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` of the specified cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for warn-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of consecutive times the monitoring metrics must reach the alert threshold to send a warning alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

class CreateMetricRuleTemplateRequestAlertTemplatesEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the info-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to 
        # - GreaterThanThreshold: greater than 
        # - LessThanOrEqualToThreshold: less than or equal to 
        # - LessThanThreshold: less than 
        # - NotEqualToThreshold: not equal to 
        # - GreaterThanYesterday: greater than the value at the same time yesterday 
        # - LessThanYesterday: less than the value at the same time yesterday 
        # - GreaterThanLastWeek: greater than the value at the same time last week 
        # - LessThanLastWeek: less than the value at the same time last week 
        # - GreaterThanLastPeriod: greater than the value in the last period 
        # - LessThanLastPeriod: less than the value in the last period 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` of the specified cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold for info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of consecutive times the monitoring metrics must reach the alert threshold to send an info-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

class CreateMetricRuleTemplateRequestAlertTemplatesEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # The comparison operator for the critical-level threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to 
        # - GreaterThanThreshold: greater than 
        # - LessThanOrEqualToThreshold: less than or equal to 
        # - LessThanThreshold: less than 
        # - NotEqualToThreshold: not equal to 
        # - GreaterThanYesterday: greater than the value at the same time yesterday 
        # - LessThanYesterday: less than the value at the same time yesterday 
        # - GreaterThanLastWeek: greater than the value at the same time last week 
        # - LessThanLastWeek: less than the value at the same time last week 
        # - GreaterThanLastPeriod: greater than the value in the last period 
        # - LessThanLastPeriod: less than the value in the last period 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for critical-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` of the specified cloud service. Examples: Maximum, Minimum, and Average. For more information about how to obtain the valid values, see [Cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.statistics = statistics
        # The threshold that triggers a critical-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
        self.threshold = threshold
        # The number of consecutive times the monitoring metrics must reach the alert threshold to send a critical-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, or Info. For the specified alert level, you must specify the Statistics, ComparisonOperator, Threshold, and Times parameters at the same time.
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

