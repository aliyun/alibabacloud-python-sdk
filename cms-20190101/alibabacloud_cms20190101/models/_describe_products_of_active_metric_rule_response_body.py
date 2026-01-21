# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeProductsOfActiveMetricRuleResponseBody(DaraModel):
    def __init__(
        self,
        all_product_init_metric_rule_list: main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleList = None,
        code: int = None,
        datapoints: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the services for which one-click alert is enabled.
        self.all_product_init_metric_rule_list = all_product_init_metric_rule_list
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The information about the services for which the initiative alert feature is enabled. Services are separated with commas (,). Valid values:
        # 
        # *   ECS: Elastic Compute Service (ECS)
        # *   rds: ApsaraDB RDS
        # *   slb: Server Load Balancer (SLB)
        # *   redis_standard: Redis Open-Source Edition (standard architecture)
        # *   redis_sharding: Redis Open-Source Edition (cluster architecture)
        # *   redis_splitrw: Redis Open-Source Edition (read/write splitting architecture)
        # *   mongodb: ApsaraDB for MongoDB of the replica set architecture
        # *   mongodb_sharding: ApsaraDB for MongoDB of the sharded cluster architecture
        # *   hbase: ApsaraDB for HBase
        # *   elasticsearch: Elasticsearch
        # *   opensearch: OpenSearch
        self.datapoints = datapoints
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.all_product_init_metric_rule_list:
            self.all_product_init_metric_rule_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_product_init_metric_rule_list is not None:
            result['AllProductInitMetricRuleList'] = self.all_product_init_metric_rule_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllProductInitMetricRuleList') is not None:
            temp_model = main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleList()
            self.all_product_init_metric_rule_list = temp_model.from_map(m.get('AllProductInitMetricRuleList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleList(DaraModel):
    def __init__(
        self,
        all_product_init_metric_rule: List[main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRule] = None,
    ):
        self.all_product_init_metric_rule = all_product_init_metric_rule

    def validate(self):
        if self.all_product_init_metric_rule:
            for v1 in self.all_product_init_metric_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllProductInitMetricRule'] = []
        if self.all_product_init_metric_rule is not None:
            for k1 in self.all_product_init_metric_rule:
                result['AllProductInitMetricRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_product_init_metric_rule = []
        if m.get('AllProductInitMetricRule') is not None:
            for k1 in m.get('AllProductInitMetricRule'):
                temp_model = main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRule()
                self.all_product_init_metric_rule.append(temp_model.from_map(k1))

        return self

class DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRule(DaraModel):
    def __init__(
        self,
        alert_init_config_list: main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigList = None,
        product: str = None,
    ):
        # The initial alert rules that are generated after one-click alert is enabled for a service.
        self.alert_init_config_list = alert_init_config_list
        # The abbreviation of the service name.
        self.product = product

    def validate(self):
        if self.alert_init_config_list:
            self.alert_init_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_init_config_list is not None:
            result['AlertInitConfigList'] = self.alert_init_config_list.to_map()

        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertInitConfigList') is not None:
            temp_model = main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigList()
            self.alert_init_config_list = temp_model.from_map(m.get('AlertInitConfigList'))

        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

class DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigList(DaraModel):
    def __init__(
        self,
        alert_init_config: List[main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigListAlertInitConfig] = None,
    ):
        self.alert_init_config = alert_init_config

    def validate(self):
        if self.alert_init_config:
            for v1 in self.alert_init_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertInitConfig'] = []
        if self.alert_init_config is not None:
            for k1 in self.alert_init_config:
                result['AlertInitConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_init_config = []
        if m.get('AlertInitConfig') is not None:
            for k1 in m.get('AlertInitConfig'):
                temp_model = main_models.DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigListAlertInitConfig()
                self.alert_init_config.append(temp_model.from_map(k1))

        return self

class DescribeProductsOfActiveMetricRuleResponseBodyAllProductInitMetricRuleListAllProductInitMetricRuleAlertInitConfigListAlertInitConfig(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        evaluation_count: str = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        period: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # The operator that is used to compare the metric value with the threshold for Warn-level alerts.
        # 
        # Valid values:
        # 
        # *   LessThanThreshold: less than the threshold
        # 
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # 
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # 
        # *   NotEqualToThreshold: does not equal to the threshold
        # 
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # 
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # 
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # 
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # 
        # *   GreaterThanThreshold: greater than the threshold
        # 
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.evaluation_count = evaluation_count
        # The alert level.
        # 
        # Valid values:
        # 
        # *   INFO
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   WARN
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CRITICAL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.level = level
        # The metric name. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the service. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The aggregation period of monitoring data. Unit: minutes. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        # The method used to calculate metric values that trigger alerts. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
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

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

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

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

