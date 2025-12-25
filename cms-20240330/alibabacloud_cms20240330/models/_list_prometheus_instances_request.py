# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusInstancesRequest(DaraModel):
    def __init__(
        self,
        filter_region_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        prometheus_instance_ids: str = None,
        prometheus_instance_name: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        tag: List[main_models.ListPrometheusInstancesRequestTag] = None,
        version: str = None,
    ):
        # Specified list of regionIds to filter (comma-separated).
        self.filter_region_ids = filter_region_ids
        # Maximum number of records to return.
        self.max_results = max_results
        # Query token.
        self.next_token = next_token
        # List of instance IDs (comma-separated)
        self.prometheus_instance_ids = prometheus_instance_ids
        # Instance name (partial match supported)
        self.prometheus_instance_name = prometheus_instance_name
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Resource type of the instance.
        self.resource_type = resource_type
        # List of tags.
        self.tag = tag
        # Instance version: V1 or V2
        self.version = version

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_region_ids is not None:
            result['filterRegionIds'] = self.filter_region_ids

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.prometheus_instance_ids is not None:
            result['prometheusInstanceIds'] = self.prometheus_instance_ids

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterRegionIds') is not None:
            self.filter_region_ids = m.get('filterRegionIds')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('prometheusInstanceIds') is not None:
            self.prometheus_instance_ids = m.get('prometheusInstanceIds')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.ListPrometheusInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListPrometheusInstancesRequestTag(DaraModel):
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

