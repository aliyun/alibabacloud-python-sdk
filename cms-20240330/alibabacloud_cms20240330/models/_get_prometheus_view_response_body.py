# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetPrometheusViewResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_view: main_models.GetPrometheusViewResponseBodyPrometheusView = None,
        request_id: str = None,
    ):
        # View instance.
        self.prometheus_view = prometheus_view
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.prometheus_view:
            self.prometheus_view.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_view is not None:
            result['prometheusView'] = self.prometheus_view.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusView') is not None:
            temp_model = main_models.GetPrometheusViewResponseBodyPrometheusView()
            self.prometheus_view = temp_model.from_map(m.get('prometheusView'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPrometheusViewResponseBodyPrometheusView(DaraModel):
    def __init__(
        self,
        auth_free_read_policy: str = None,
        auth_token: str = None,
        create_time: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_token: bool = None,
        folder_url: str = None,
        grafana_instance_id: str = None,
        grafana_instance_name: str = None,
        http_api_inter_url: str = None,
        http_api_intra_url: str = None,
        instance_type: str = None,
        payment_type: str = None,
        product: str = None,
        prometheus_instances: List[main_models.GetPrometheusViewResponseBodyPrometheusViewPrometheusInstances] = None,
        prometheus_view_id: str = None,
        prometheus_view_name: str = None,
        region_id: str = None,
        remote_read_inter_url: str = None,
        remote_read_intra_url: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        status: str = None,
        support_auth_types: List[str] = None,
        tags: List[main_models.GetPrometheusViewResponseBodyPrometheusViewTags] = None,
        user_id: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # Password-free read policy (supports IP segments and VpcId).
        self.auth_free_read_policy = auth_free_read_policy
        # authToken string.
        self.auth_token = auth_token
        # Instance creation time, using UTC+0 time, format is yyyy-MM-ddTHH:mmZ.
        self.create_time = create_time
        # Whether to enable password-free read.
        self.enable_auth_free_read = enable_auth_free_read
        # Whether to enable authToken.
        self.enable_auth_token = enable_auth_token
        # Observability dashboard URL.
        self.folder_url = folder_url
        # Bound managed Grafana instance ID.
        self.grafana_instance_id = grafana_instance_id
        # Bound managed Grafana instance name.
        self.grafana_instance_name = grafana_instance_name
        # Public HTTP address.
        self.http_api_inter_url = http_api_inter_url
        # Private HTTP address.
        self.http_api_intra_url = http_api_intra_url
        # Instance type, fixed value prom-view.
        self.instance_type = instance_type
        # Payment type. Currently, the fixed value is FREE (free).
        self.payment_type = payment_type
        # Product that the prom instance belongs to.
        self.product = product
        # Prometheus instance list.
        self.prometheus_instances = prometheus_instances
        # Prometheus view ID.
        self.prometheus_view_id = prometheus_view_id
        # Prometheus view name.
        self.prometheus_view_name = prometheus_view_name
        # Region ID
        self.region_id = region_id
        # Remote read public URL.
        self.remote_read_inter_url = remote_read_inter_url
        # Remote read intranet URL.
        self.remote_read_intra_url = remote_read_intra_url
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Fixed value: PrometheusView
        self.resource_type = resource_type
        # Backend data storage status
        self.status = status
        # Supported authentication types.
        self.support_auth_types = support_auth_types
        # Instance tag keys.
        self.tags = tags
        # User ID.
        self.user_id = user_id
        # Version.
        self.version = version
        # Workspace to which the environment belongs
        self.workspace = workspace

    def validate(self):
        if self.prometheus_instances:
            for v1 in self.prometheus_instances:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token

        if self.folder_url is not None:
            result['folderUrl'] = self.folder_url

        if self.grafana_instance_id is not None:
            result['grafanaInstanceId'] = self.grafana_instance_id

        if self.grafana_instance_name is not None:
            result['grafanaInstanceName'] = self.grafana_instance_name

        if self.http_api_inter_url is not None:
            result['httpApiInterUrl'] = self.http_api_inter_url

        if self.http_api_intra_url is not None:
            result['httpApiIntraUrl'] = self.http_api_intra_url

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.product is not None:
            result['product'] = self.product

        result['prometheusInstances'] = []
        if self.prometheus_instances is not None:
            for k1 in self.prometheus_instances:
                result['prometheusInstances'].append(k1.to_map() if k1 else None)

        if self.prometheus_view_id is not None:
            result['prometheusViewId'] = self.prometheus_view_id

        if self.prometheus_view_name is not None:
            result['prometheusViewName'] = self.prometheus_view_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.remote_read_inter_url is not None:
            result['remoteReadInterUrl'] = self.remote_read_inter_url

        if self.remote_read_intra_url is not None:
            result['remoteReadIntraUrl'] = self.remote_read_intra_url

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        if self.support_auth_types is not None:
            result['supportAuthTypes'] = self.support_auth_types

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')

        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')

        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')

        if m.get('folderUrl') is not None:
            self.folder_url = m.get('folderUrl')

        if m.get('grafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('grafanaInstanceId')

        if m.get('grafanaInstanceName') is not None:
            self.grafana_instance_name = m.get('grafanaInstanceName')

        if m.get('httpApiInterUrl') is not None:
            self.http_api_inter_url = m.get('httpApiInterUrl')

        if m.get('httpApiIntraUrl') is not None:
            self.http_api_intra_url = m.get('httpApiIntraUrl')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('product') is not None:
            self.product = m.get('product')

        self.prometheus_instances = []
        if m.get('prometheusInstances') is not None:
            for k1 in m.get('prometheusInstances'):
                temp_model = main_models.GetPrometheusViewResponseBodyPrometheusViewPrometheusInstances()
                self.prometheus_instances.append(temp_model.from_map(k1))

        if m.get('prometheusViewId') is not None:
            self.prometheus_view_id = m.get('prometheusViewId')

        if m.get('prometheusViewName') is not None:
            self.prometheus_view_name = m.get('prometheusViewName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('remoteReadInterUrl') is not None:
            self.remote_read_inter_url = m.get('remoteReadInterUrl')

        if m.get('remoteReadIntraUrl') is not None:
            self.remote_read_intra_url = m.get('remoteReadIntraUrl')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supportAuthTypes') is not None:
            self.support_auth_types = m.get('supportAuthTypes')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetPrometheusViewResponseBodyPrometheusViewTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetPrometheusViewResponseBodyPrometheusViewTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # PagerDuty integration key.
        self.key = key
        # Tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetPrometheusViewResponseBodyPrometheusViewPrometheusInstances(DaraModel):
    def __init__(
        self,
        prometheus_instance_id: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # Instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # Region ID
        self.region_id = region_id
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

