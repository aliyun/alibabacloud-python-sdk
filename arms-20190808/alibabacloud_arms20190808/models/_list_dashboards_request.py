# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDashboardsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        dashboard_name: str = None,
        language: str = None,
        product: str = None,
        recreate_switch: bool = None,
        region_id: str = None,
        title: str = None,
    ):
        # The ID of the ACK cluster.
        self.cluster_id = cluster_id
        # Valid values: ACK, ASK, cloud-product-prometheus, and Node. You can query the dashboards of a virtual cluster by specifying the cluster type. For InfluxDB, set this parameter to `cloud-product-prometheus`.
        self.cluster_type = cluster_type
        # The unique names of the dashboards. You can query dashboards by specifying their names. The **dashboard title** can be changed whereas the **dashboard name** cannot. You can specify multiple names and separate them with commas (,), for example, `k8s-event,k8s-overview`. A dashboard may have multiple versions. If you want to specify a version, you can add version information after the name, for example, `k8s-event:v1,k8s-overview:latest`.
        self.dashboard_name = dashboard_name
        # The language of the returned Grafana dashboard. Valid values: en and zh. Default value: en.
        self.language = language
        # The cloud service code. This parameter is required if you set the ClusterType parameter to `cloud-product-prometheus`. The following cloud services are available: Serverless App Engine, Microservices Engine, Message Queue for Apache RocketMQ, Lindorm, Message Queue for Apache Kafka, ApsaraDB for ClickHouse, Data Lake Analytics, Message Queue for RabbitMQ, ApsaraDB for MongoDB, Time Series Database (TSDB) for InfluxDB, MSE Cloud-native Gateway, Grafana Service, SchedulerX, Global Transaction Service, Enterprise Distributed Application Service, Machine Learning Platform for AI - Elastic Algorithm Service (EAS), Application High Availability Service, and Performance Testing.
        self.product = product
        # Specifies whether to create or query a virtual cluster. This parameter provides backward compatibility.
        self.recreate_switch = recreate_switch
        # The region ID.
        self.region_id = region_id
        # The dashboard title. The dashboard title can be changed. We recommend that you specify the **DashboardName** parameter.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name

        if self.language is not None:
            result['Language'] = self.language

        if self.product is not None:
            result['Product'] = self.product

        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

