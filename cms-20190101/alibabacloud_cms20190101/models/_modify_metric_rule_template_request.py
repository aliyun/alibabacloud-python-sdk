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
        # The list of alert templates.
        self.alert_templates = alert_templates
        # The description of the alert template.
        self.description = description
        # The name of the alert template.
        self.name = name
        self.region_id = region_id
        # The version of the alert template to be modified.
        # >This parameter is automatically updated based on the number of modifications.
        # 
        # This parameter is required.
        self.rest_version = rest_version
        # The ID of the alert template.
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
        # The abbreviation of the Alibaba Cloud service name. Valid values of N: 1 to 200. Valid values:
        # - ecs: Alibaba Cloud and non-Alibaba Cloud hosts.
        # - rds: ApsaraDB RDS database.
        # - ads: AnalyticDB database.
        # - slb: load balancing.
        # - vpc: Elastic IP Address (EIP).
        # - apigateway: API Gateway.
        # - cdn: Content Delivery Network (CDN).
        # - cs: Container Service for Swarm.
        # - dcdn: Dynamic Route for CDN (DCDN).
        # - ddos: Anti-DDoS.
        # - eip: Elastic IP Address (EIP).
        # - elasticsearch: Elasticsearch.
        # - emr: E-MapReduce (EMR).
        # - ess: elastic scaling.
        # - hbase: ApsaraDB for HBase database.
        # - iot_edge: IoT Edge.
        # - kvstore_sharding: ApsaraDB for Redis Cluster Edition.
        # - kvstore_splitrw: ApsaraDB for Redis Read/Write Splitting Edition.
        # - kvstore_standard: ApsaraDB for Redis Standard Edition.
        # - memcache: ApsaraDB for Memcache database.
        # - mns: Message Service (MNS).
        # - mongodb: MongoDB replica set instance.
        # - mongodb_cluster: MongoDB cluster edition.
        # - mongodb_sharding: MongoDB sharded cluster.
        # - mq_topic: Message Service Topic.
        # - ocs: legacy cloud database Memcache.
        # - opensearch: OpenSearch.
        # - oss: Object Storage Service (OSS).
        # - polardb: PolarDB database.
        # - petadata: HybridDB for MySQL.
        # - scdn: secure acceleration.
        # - sharebandwidthpackages: Internet Shared Bandwidth.
        # - sls: Simple Log Service (SLS).
        # - vpn: VPN Gateway.
        self.category = category
        # The name of the metric. Valid values of N: 1 to 200.
        # 
        # >For more information about the valid values of the metric name, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service, which is used to distinguish different services. Valid values of N: 1 to 200.
        # 
        # Format: acs_<service name>.
        # 
        # >To obtain the namespace of each Alibaba Cloud service, call the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        self.namespace = namespace
        # The statistical period of the monitoring data. Valid values of N: 1 to 200.
        # 
        # >If you set this parameter to 300, the system collects and aggregates monitoring data every 300 seconds. If monitoring data is reported every minute, the system aggregates the data of 5 minutes, such as the average, maximum, and minimum values. Do not specify this parameter separately because the statistical period may cause unexpected alerts.
        self.period = period
        # The name of the alert rule. Valid values of N: 1 to 200.
        self.rule_name = rule_name
        # The options for the extended dimension fields. Valid values of N: 1 to 200.
        # 
        # For example, if the alert template is applied to an application group, this parameter is set to `{"disk":"/"}`, and the MetricName parameter is set to `DiskUtilization`, the root partition (`"/"`) of the disks for all instances in the application group is associated with the corresponding alert rule.
        # 
        # >For more information about the valid values of the extended dimension fields, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
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
        # The comparison operator for the warning-level alert threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold. 
        # - GreaterThanThreshold: greater than the threshold. 
        # - LessThanOrEqualToThreshold: less than or equal to the threshold. 
        # - LessThanThreshold: less than the threshold. 
        # - NotEqualToThreshold: not equal to the threshold. 
        # - GreaterThanYesterday: greater than the metric value at the same time yesterday. 
        # - LessThanYesterday: less than the metric value at the same time yesterday. 
        # - GreaterThanLastWeek: greater than the metric value at the same time last week. 
        # - LessThanLastWeek: less than the metric value at the same time last week. 
        # - GreaterThanLastPeriod: greater than the metric value in the previous period. 
        # - LessThanLastPeriod: less than the metric value in the previous period. 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for warning-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.statistics = statistics
        # The threshold for warning-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.threshold = threshold
        # The number of times that the monitoring metrics must reach the alert threshold to send a warning-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
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
        # The comparison operator for the info-level alert threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold. 
        # - GreaterThanThreshold: greater than the threshold. 
        # - LessThanOrEqualToThreshold: less than or equal to the threshold. 
        # - LessThanThreshold: less than the threshold. 
        # - NotEqualToThreshold: not equal to the threshold. 
        # - GreaterThanYesterday: greater than the metric value at the same time yesterday. 
        # - LessThanYesterday: less than the metric value at the same time yesterday. 
        # - GreaterThanLastWeek: greater than the metric value at the same time last week. 
        # - LessThanLastWeek: less than the metric value at the same time last week. 
        # - GreaterThanLastPeriod: greater than the metric value in the previous period. 
        # - LessThanLastPeriod: less than the metric value in the previous period. 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.statistics = statistics
        # The threshold for info-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.threshold = threshold
        # The number of times that the monitoring metrics must reach the alert threshold to send an info-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
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
        # The comparison operator for the critical-level alert threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to the threshold. 
        # - GreaterThanThreshold: greater than the threshold. 
        # - LessThanOrEqualToThreshold: less than or equal to the threshold. 
        # - LessThanThreshold: less than the threshold. 
        # - NotEqualToThreshold: not equal to the threshold. 
        # - GreaterThanYesterday: greater than the metric value at the same time yesterday. 
        # - LessThanYesterday: less than the metric value at the same time yesterday. 
        # - GreaterThanLastWeek: greater than the metric value at the same time last week. 
        # - LessThanLastWeek: less than the metric value at the same time last week. 
        # - GreaterThanLastPeriod: greater than the metric value in the previous period. 
        # - LessThanLastPeriod: less than the metric value in the previous period. 
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.comparison_operator = comparison_operator
        self.n = n
        # The statistical method for critical-level alerts.
        # 
        # Valid values of N: 1 to 200.
        # 
        # The valid values of this parameter are determined by the `Statistics` column that corresponds to the `MetricName` parameter of the specified Alibaba Cloud service, such as Maximum, Minimum, and Average. For more information about how to obtain the valid values of this parameter, see [cloud service monitoring metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.statistics = statistics
        # The threshold that triggers a critical-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
        self.threshold = threshold
        # The number of times that the monitoring metrics must reach the alert threshold to send a critical-level alert notification.
        # 
        # Valid values of N: 1 to 200.
        # 
        # > You must specify at least one of the following alert levels: Critical, Warn, and Info. The Statistics, ComparisonOperator, Threshold, and Times parameters must be specified at the same time for the specified alert level.
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

