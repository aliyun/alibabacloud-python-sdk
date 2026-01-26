# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListDashboardsResponseBody(DaraModel):
    def __init__(
        self,
        dashboard_vos: List[main_models.ListDashboardsResponseBodyDashboardVos] = None,
        environment_id: str = None,
        grafana_service_opened: str = None,
        prometheus_service_opened: str = None,
        request_id: str = None,
    ):
        # The information about the Grafana dashboard.
        self.dashboard_vos = dashboard_vos
        # The ID of the environment instance.
        self.environment_id = environment_id
        # Indicates whether Managed Service for Grafana is activated.
        self.grafana_service_opened = grafana_service_opened
        # Whether or not to turn on Prometheus service.
        self.prometheus_service_opened = prometheus_service_opened
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dashboard_vos:
            for v1 in self.dashboard_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k1 in self.dashboard_vos:
                result['DashboardVos'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.grafana_service_opened is not None:
            result['GrafanaServiceOpened'] = self.grafana_service_opened

        if self.prometheus_service_opened is not None:
            result['PrometheusServiceOpened'] = self.prometheus_service_opened

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k1 in m.get('DashboardVos'):
                temp_model = main_models.ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k1))

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('GrafanaServiceOpened') is not None:
            self.grafana_service_opened = m.get('GrafanaServiceOpened')

        if m.get('PrometheusServiceOpened') is not None:
            self.prometheus_service_opened = m.get('PrometheusServiceOpened')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDashboardsResponseBodyDashboardVos(DaraModel):
    def __init__(
        self,
        dashboard_type: str = None,
        exporter: str = None,
        http_url: str = None,
        https_url: str = None,
        i_18n_child: main_models.ListDashboardsResponseBodyDashboardVosI18nChild = None,
        id: str = None,
        is_arms_exporter: bool = None,
        kind: str = None,
        language: str = None,
        name: str = None,
        need_update: bool = None,
        tags: List[str] = None,
        time: str = None,
        title: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
        version: str = None,
    ):
        # The type of the Grafana dashboard. This parameter has the same effect as the Exporter parameter whereas provides clearer implication.
        self.dashboard_type = dashboard_type
        # The type of the exporter access source. Valid values:
        # 
        # *   Prometheus
        # *   Node
        # *   GPU
        # *   Redis
        # *   MySQL
        # *   Kafka
        # *   NGINX V2
        # *   Nginx
        # *   ZooKeeper
        # *   MongoDB
        # *   RabbitMQ
        # *   PostgreSQL
        # *   Kubernetes
        # *   Client Library
        # *   Elasticsearch
        # *   RocketMQ
        self.exporter = exporter
        # The URL of the Grafana dashboard.
        self.http_url = http_url
        # The URL of the Grafana dashboard.
        self.https_url = https_url
        # The information about the Grafana dashboard.
        self.i_18n_child = i_18n_child
        # The ID of the Grafana dashboard. The value is unique only when you install the Grafana dashboard.
        self.id = id
        # Indicates whether the exporter is provided by Application Real-Time Monitoring Service (ARMS).
        # 
        # *   `true:` The exporter is provided by ARMS.
        # *   `false:`: The exporter is not provided by ARMS.
        self.is_arms_exporter = is_arms_exporter
        # The category of the Grafana dashboard. Valid values: BASIC, THIRD, LIMIT, and CUSTOM.
        self.kind = kind
        # The language of the Grafana dashboard.
        self.language = language
        # The name of the Grafana dashboard. This parameter is different from the **Title** parameter as this parameter cannot be changed.
        self.name = name
        # Indicates whether the Grafana dashboard has a new version that is available for upgrade.
        self.need_update = need_update
        # The tags of the Grafana dashboard.
        self.tags = tags
        # The time when the Grafana dashboard was created. The value is a timestamp. Unit: seconds.
        self.time = time
        # The title of the Grafana dashboard.
        self.title = title
        # The type of the Grafana dashboard. Valid values:
        # 
        # *   `dash-db`: a dashboard
        # *   `dash-folder`: a folder that can include a dashboard
        self.type = type
        # The unique identifier of the Grafana dashboard.
        self.uid = uid
        # The complete URL of the Grafana dashboard.
        self.url = url
        # The version of the Grafana dashboard. The combination of version and name uniquely identifies a dashboard.
        self.version = version

    def validate(self):
        if self.i_18n_child:
            self.i_18n_child.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type

        if self.exporter is not None:
            result['Exporter'] = self.exporter

        if self.http_url is not None:
            result['HttpUrl'] = self.http_url

        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url

        if self.i_18n_child is not None:
            result['I18nChild'] = self.i_18n_child.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.time is not None:
            result['Time'] = self.time

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.url is not None:
            result['Url'] = self.url

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')

        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')

        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')

        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')

        if m.get('I18nChild') is not None:
            temp_model = main_models.ListDashboardsResponseBodyDashboardVosI18nChild()
            self.i_18n_child = temp_model.from_map(m.get('I18nChild'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListDashboardsResponseBodyDashboardVosI18nChild(DaraModel):
    def __init__(
        self,
        dashboard_type: str = None,
        exporter: str = None,
        http_url: str = None,
        https_url: str = None,
        id: str = None,
        is_arms_exporter: bool = None,
        kind: str = None,
        language: str = None,
        name: str = None,
        need_update: bool = None,
        tags: List[str] = None,
        time: str = None,
        title: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
        version: str = None,
    ):
        # The type of the Grafana dashboard. This parameter has the same effect as the Exporter parameter whereas provides clearer implication.
        self.dashboard_type = dashboard_type
        # The type of the exporter access source. Valid values:
        # 
        # *   Prometheus
        # *   Node
        # *   GPU
        # *   Redis
        # *   MySQL
        # *   Kafka
        # *   NGINX V2
        # *   Nginx
        # *   ZooKeeper
        # *   MongoDB
        # *   RabbitMQ
        # *   PostgreSQL
        # *   Kubernetes
        # *   Client Library
        # *   Elasticsearch
        # *   RocketMQ
        self.exporter = exporter
        # The URL of the Grafana dashboard.
        self.http_url = http_url
        # The URL of the Grafana dashboard.
        self.https_url = https_url
        # The ID of the Grafana dashboard. The value is unique only when you install the Grafana dashboard.
        self.id = id
        # Indicates whether the exporter is provided by ARMS.
        # 
        # *   `true:` The exporter is provided by ARMS.
        # *   `false:`: The exporter is not provided by ARMS.
        self.is_arms_exporter = is_arms_exporter
        # The category of the Grafana dashboard. Valid values: BASIC, THIRD, LIMIT, and CUSTOM.
        self.kind = kind
        # The language of the Grafana dashboard.
        self.language = language
        # The name of the Grafana dashboard. This parameter is different from the **Title** parameter as this parameter cannot be changed.
        self.name = name
        # Indicates whether the Grafana dashboard has a new version that is available for upgrade.
        self.need_update = need_update
        # The tags of the Grafana dashboard.
        self.tags = tags
        # The time when the Grafana dashboard was created. The value is a timestamp.
        self.time = time
        # The title of the Grafana dashboard.
        self.title = title
        # The type of the Grafana dashboard. Valid values:
        # 
        # *   `dash-db`: a dashboard
        # *   `dash-folder`: a folder that can include a dashboard
        self.type = type
        # The unique identifier of the Grafana dashboard.
        self.uid = uid
        # The complete URL of the Grafana dashboard.
        self.url = url
        # The version of the Grafana dashboard. The combination of version and name uniquely identifies a dashboard.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type

        if self.exporter is not None:
            result['Exporter'] = self.exporter

        if self.http_url is not None:
            result['HttpUrl'] = self.http_url

        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url

        if self.id is not None:
            result['Id'] = self.id

        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.time is not None:
            result['Time'] = self.time

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.url is not None:
            result['Url'] = self.url

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')

        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')

        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')

        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

