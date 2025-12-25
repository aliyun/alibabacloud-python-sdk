# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusInstancesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prometheus_instances: List[main_models.ListPrometheusInstancesResponseBodyPrometheusInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Maximum number of records to return.
        self.max_results = max_results
        # Token for the next query.
        self.next_token = next_token
        # List of Prometheus instances.
        self.prometheus_instances = prometheus_instances
        # ID of the request
        self.request_id = request_id
        # Total number of instances
        self.total_count = total_count

    def validate(self):
        if self.prometheus_instances:
            for v1 in self.prometheus_instances:
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

        result['prometheusInstances'] = []
        if self.prometheus_instances is not None:
            for k1 in self.prometheus_instances:
                result['prometheusInstances'].append(k1.to_map() if k1 else None)

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

        self.prometheus_instances = []
        if m.get('prometheusInstances') is not None:
            for k1 in m.get('prometheusInstances'):
                temp_model = main_models.ListPrometheusInstancesResponseBodyPrometheusInstances()
                self.prometheus_instances.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPrometheusInstancesResponseBodyPrometheusInstances(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        create_time: str = None,
        instance_type: str = None,
        payment_type: str = None,
        product: str = None,
        prometheus_instance_id: str = None,
        prometheus_instance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        status: str = None,
        support_auth_types: List[str] = None,
        tags: List[main_models.ListPrometheusInstancesResponseBodyPrometheusInstancesTags] = None,
        user_id: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # Access type:
        # readWrite, readOnly, httpReadOnly
        self.access_type = access_type
        # Instance creation time, using UTC+0 time, formatted as yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # Instance type.
        self.instance_type = instance_type
        # POSTPAY: Postpaid by metric.
        # POSTPAY_GB: Postpaid by write volume.
        # PREPAY: Prepaid.
        # FREE: Free.
        self.payment_type = payment_type
        # Product to which the prom instance belongs
        self.product = product
        # Instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # Instance name.
        self.prometheus_instance_name = prometheus_instance_name
        # Region ID
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Resource type.
        self.resource_type = resource_type
        # Backend data storage status
        self.status = status
        # Supported authentication types.
        self.support_auth_types = support_auth_types
        # Tags key.
        self.tags = tags
        # User ID.
        self.user_id = user_id
        # Version
        self.version = version
        # Workspace to which the Prometheus instance belongs
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
        if self.access_type is not None:
            result['accessType'] = self.access_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.product is not None:
            result['product'] = self.product

        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

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
        if m.get('accessType') is not None:
            self.access_type = m.get('accessType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

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
                temp_model = main_models.ListPrometheusInstancesResponseBodyPrometheusInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListPrometheusInstancesResponseBodyPrometheusInstancesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key
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

