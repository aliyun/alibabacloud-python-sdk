# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class GetResourcesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource: main_models.GetResourcesResponseBodyResource = None,
        resources: List[main_models.GetResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the current request. This parameter is returned by the List operation.
        self.max_results = max_results
        # The position where the current call finished reading. An empty value indicates that all data has been read. This parameter is returned by the List operation.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The specified resource. This parameter is returned by the Get operation.
        self.resource = resource
        # A list of resources. This parameter is returned by the List operation.
        self.resources = resources
        # The total number of entries that match the query conditions. This parameter is returned by the List operation.
        self.total_count = total_count

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.resources:
            for v1 in self.resources:
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        result['resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resource') is not None:
            temp_model = main_models.GetResourcesResponseBodyResource()
            self.resource = temp_model.from_map(m.get('resource'))

        self.resources = []
        if m.get('resources') is not None:
            for k1 in m.get('resources'):
                temp_model = main_models.GetResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource_attributes: Dict[str, Any] = None,
        resource_id: str = None,
    ):
        # The resource properties in JSON format.
        self.resource_attributes = resource_attributes
        # The resource ID.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        return self

class GetResourcesResponseBodyResource(DaraModel):
    def __init__(
        self,
        resource_attributes: Dict[str, Any] = None,
        resource_id: str = None,
    ):
        # The resource properties in JSON format.
        self.resource_attributes = resource_attributes
        # The resource ID.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        return self

