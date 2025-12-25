# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusViewsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prometheus_views: List[main_models.ListPrometheusViewsResponseBodyPrometheusViews] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Maximum number of records to return.
        self.max_results = max_results
        # Token for the next query.
        self.next_token = next_token
        # List of Prometheus view instances.
        self.prometheus_views = prometheus_views
        # ID of the request
        self.request_id = request_id
        # Total number of instances
        self.total_count = total_count

    def validate(self):
        if self.prometheus_views:
            for v1 in self.prometheus_views:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['prometheusViews'] = []
        if self.prometheus_views is not None:
            for k1 in self.prometheus_views:
                result['prometheusViews'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.prometheus_views = []
        if m.get('prometheusViews') is not None:
            for k1 in m.get('prometheusViews'):
                temp_model = main_models.ListPrometheusViewsResponseBodyPrometheusViews()
                self.prometheus_views.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPrometheusViewsResponseBodyPrometheusViews(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        instance_type: str = None,
        payment_type: str = None,
        product: str = None,
        prometheus_instance_count: int = None,
        prometheus_view_id: str = None,
        prometheus_view_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListPrometheusViewsResponseBodyPrometheusViewsTags] = None,
        user_id: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # Instance creation time, using UTC+0 time, formatted as yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # Instance type:
        # prom-view: new version aggregated view
        # global-view: old version aggregated view
        self.instance_type = instance_type
        # Payment type. Currently, the fixed value is FREE (free).
        self.payment_type = payment_type
        # Product that the prom instance belongs to (arms or cms).
        self.product = product
        # Number of Prometheus instances in the view.
        self.prometheus_instance_count = prometheus_instance_count
        # Prometheus view ID.
        self.prometheus_view_id = prometheus_view_id
        # Prometheus view name.
        self.prometheus_view_name = prometheus_view_name
        # Region ID.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Fixed value: PrometheusView.
        self.resource_type = resource_type
        # Backend data storage status.
        self.status = status
        # Tag values.
        self.tags = tags
        # User ID.
        self.user_id = user_id
        # Version.
        self.version = version
        # Workspace that the prom instance belongs to.
        self.workspace = workspace

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.product is not None:
            result['product'] = self.product

        if self.prometheus_instance_count is not None:
            result['prometheusInstanceCount'] = self.prometheus_instance_count

        if self.prometheus_view_id is not None:
            result['prometheusViewId'] = self.prometheus_view_id

        if self.prometheus_view_name is not None:
            result['prometheusViewName'] = self.prometheus_view_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('prometheusInstanceCount') is not None:
            self.prometheus_instance_count = m.get('prometheusInstanceCount')

        if m.get('prometheusViewId') is not None:
            self.prometheus_view_id = m.get('prometheusViewId')

        if m.get('prometheusViewName') is not None:
            self.prometheus_view_name = m.get('prometheusViewName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListPrometheusViewsResponseBodyPrometheusViewsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListPrometheusViewsResponseBodyPrometheusViewsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key
        self.key = key
        # Match value.
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

