# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusVirtualInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListPrometheusVirtualInstancesResponseBodyInstances] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # A list of instances.
        self.instances = instances
        # The maximum number of entries returned on each page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If all results are returned, this parameter is left empty.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.ListPrometheusVirtualInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPrometheusVirtualInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        http_api_url: str = None,
        instance_id: str = None,
        namespace: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The HTTP API URL.
        self.http_api_url = http_api_url
        # Returned for the `PROMETHEUS_DS` data source type.
        # 
        # The Prometheus instance ID.
        self.instance_id = instance_id
        # Returned for the `CMS_BASIC_QUERY` query type.
        # 
        # The namespace of the metric.
        self.namespace = namespace
        # The region ID.
        self.region_id = region_id
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.http_api_url is not None:
            result['httpApiUrl'] = self.http_api_url

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('httpApiUrl') is not None:
            self.http_api_url = m.get('httpApiUrl')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

