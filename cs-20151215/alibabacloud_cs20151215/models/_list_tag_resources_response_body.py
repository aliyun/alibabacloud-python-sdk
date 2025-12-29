# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: main_models.ListTagResourcesResponseBodyTagResources = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The details of the queried labels and resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.tag_resources is not None:
            result['tag_resources'] = self.tag_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('tag_resources') is not None:
            temp_model = main_models.ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m.get('tag_resources'))

        return self

class ListTagResourcesResponseBodyTagResources(DaraModel):
    def __init__(
        self,
        tag_resource: List[main_models.ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        # The resource and label.
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for v1 in self.tag_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['tag_resource'] = []
        if self.tag_resource is not None:
            for k1 in self.tag_resource:
                result['tag_resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('tag_resource') is not None:
            for k1 in m.get('tag_resource'):
                temp_model = main_models.ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k1))

        return self

class ListTagResourcesResponseBodyTagResourcesTagResource(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource. For more information, see [Labels](https://help.aliyun.com/document_detail/110425.html).
        self.resource_type = resource_type
        # The key of the label.
        self.tag_key = tag_key
        # The value of the label.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.tag_key is not None:
            result['tag_key'] = self.tag_key

        if self.tag_value is not None:
            result['tag_value'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')

        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')

        return self

