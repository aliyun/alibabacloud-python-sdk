# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridMonitorNamespaceListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        describe_hybrid_monitor_namespace: List[main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespace] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The response code.
        self.code = code
        # The details of the namespaces.
        self.describe_hybrid_monitor_namespace = describe_hybrid_monitor_namespace
        # The returned message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.describe_hybrid_monitor_namespace:
            for v1 in self.describe_hybrid_monitor_namespace:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DescribeHybridMonitorNamespace'] = []
        if self.describe_hybrid_monitor_namespace is not None:
            for k1 in self.describe_hybrid_monitor_namespace:
                result['DescribeHybridMonitorNamespace'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.describe_hybrid_monitor_namespace = []
        if m.get('DescribeHybridMonitorNamespace') is not None:
            for k1 in m.get('DescribeHybridMonitorNamespace'):
                temp_model = main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespace()
                self.describe_hybrid_monitor_namespace.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespace(DaraModel):
    def __init__(
        self,
        aliyun_product_metric_list: List[main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricList] = None,
        create_time: str = None,
        description: str = None,
        detail: main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceDetail = None,
        id: str = None,
        is_delete: int = None,
        modify_time: str = None,
        namespace: str = None,
        namespace_type: str = None,
        not_aliyun_task_number: int = None,
    ):
        # The configuration details of metric import tasks for Alibaba Cloud services.
        self.aliyun_product_metric_list = aliyun_product_metric_list
        # The timestamp that was generated when the namespace was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The description of the namespace.
        self.description = description
        # The details of the data retention period.
        self.detail = detail
        # The ID of the namespace.
        self.id = id
        # Indicates whether the namespace is deleted. Valid values:
        # 
        # *   0: The namespace is not deleted.
        # *   1: The namespace is deleted.
        self.is_delete = is_delete
        # The timestamp that was generated when the namespace was last modified.
        self.modify_time = modify_time
        # The name of the namespace.
        self.namespace = namespace
        # The storage scheme of metric data. Valid values:
        # 
        # *   m_prom_user: The metric data is stored in Simple Log Service.
        # *   m_prom_pool: The metric data is stored in the storage space provided by CloudMonitor.
        self.namespace_type = namespace_type
        # The number of metric import tasks for third-party services.
        self.not_aliyun_task_number = not_aliyun_task_number

    def validate(self):
        if self.aliyun_product_metric_list:
            for v1 in self.aliyun_product_metric_list:
                 if v1:
                    v1.validate()
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AliyunProductMetricList'] = []
        if self.aliyun_product_metric_list is not None:
            for k1 in self.aliyun_product_metric_list:
                result['AliyunProductMetricList'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_type is not None:
            result['NamespaceType'] = self.namespace_type

        if self.not_aliyun_task_number is not None:
            result['NotAliyunTaskNumber'] = self.not_aliyun_task_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aliyun_product_metric_list = []
        if m.get('AliyunProductMetricList') is not None:
            for k1 in m.get('AliyunProductMetricList'):
                temp_model = main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricList()
                self.aliyun_product_metric_list.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Detail') is not None:
            temp_model = main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceType') is not None:
            self.namespace_type = m.get('NamespaceType')

        if m.get('NotAliyunTaskNumber') is not None:
            self.not_aliyun_task_number = m.get('NotAliyunTaskNumber')

        return self

class DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceDetail(DaraModel):
    def __init__(
        self,
        namespace_region: str = None,
        prometheus_instance_id: str = None,
        slsproject: str = None,
        spec: str = None,
    ):
        # The region where the metric data is stored.
        # 
        # >  This parameter is returned if you select `m_prom_user` for `NamespaceType` when you create a namespace.
        self.namespace_region = namespace_region
        self.prometheus_instance_id = prometheus_instance_id
        # The project where the metric data is located.
        # 
        # >  This parameter is returned if you select `m_prom_user` for `NamespaceType` when you create a namespace.
        self.slsproject = slsproject
        # The data retention period. Valid values:
        # 
        # *   cms.s1.large (Retention Period 15 Days)
        # *   cms.s1.xlarge (Retention Period 32 Days)
        # *   cms.s1.2xlarge (Retention Period 63 Days)
        # *   cms.s1.3xlarge (Retention Period 93 Days)
        # *   cms.s1.6xlarge (Retention Period 185 Days)
        # *   cms.s1.12xlarge (Retention Period 367 Days)
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_region is not None:
            result['NamespaceRegion'] = self.namespace_region

        if self.prometheus_instance_id is not None:
            result['PrometheusInstanceId'] = self.prometheus_instance_id

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceRegion') is not None:
            self.namespace_region = m.get('NamespaceRegion')

        if m.get('PrometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('PrometheusInstanceId')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

class DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricList(DaraModel):
    def __init__(
        self,
        namespace_list: List[main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceList] = None,
        user_id: int = None,
        yamlconfig: str = None,
    ):
        # The namespaces.
        self.namespace_list = namespace_list
        # The account that is used to create the namespace.
        self.user_id = user_id
        # The configuration file of the Alibaba Cloud service that you want to monitor by using Hybrid Cloud Monitoring.
        # 
        # *   namespace: the namespace of the Alibaba Cloud service.
        # *   metric_list: the metrics of the Alibaba Cloud service.
        # *   dimension: the resources of the Alibaba Cloud service that you want to monitor by using Hybrid Cloud Monitoring. If you do not specify a dimension, all resources of the Alibaba Cloud service are monitored.
        self.yamlconfig = yamlconfig

    def validate(self):
        if self.namespace_list:
            for v1 in self.namespace_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NamespaceList'] = []
        if self.namespace_list is not None:
            for k1 in self.namespace_list:
                result['NamespaceList'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.yamlconfig is not None:
            result['YAMLConfig'] = self.yamlconfig

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespace_list = []
        if m.get('NamespaceList') is not None:
            for k1 in m.get('NamespaceList'):
                temp_model = main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceList()
                self.namespace_list.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('YAMLConfig') is not None:
            self.yamlconfig = m.get('YAMLConfig')

        return self

class DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceList(DaraModel):
    def __init__(
        self,
        metric_list: List[main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceListMetricList] = None,
        namespace: str = None,
    ):
        # The metrics for the Alibaba Cloud service.
        self.metric_list = metric_list
        # The namespace for the Alibaba Cloud service.
        self.namespace = namespace

    def validate(self):
        if self.metric_list:
            for v1 in self.metric_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricList'] = []
        if self.metric_list is not None:
            for k1 in self.metric_list:
                result['MetricList'].append(k1.to_map() if k1 else None)

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_list = []
        if m.get('MetricList') is not None:
            for k1 in m.get('MetricList'):
                temp_model = main_models.DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceListMetricList()
                self.metric_list.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

class DescribeHybridMonitorNamespaceListResponseBodyDescribeHybridMonitorNamespaceAliyunProductMetricListNamespaceListMetricList(DaraModel):
    def __init__(
        self,
        list: List[str] = None,
        period: int = None,
    ):
        # The metrics.
        self.list = list
        # The collection period of the metric.
        # 
        # Unit: seconds.
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list is not None:
            result['List'] = self.list

        if self.period is not None:
            result['Period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            self.list = m.get('List')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        return self

