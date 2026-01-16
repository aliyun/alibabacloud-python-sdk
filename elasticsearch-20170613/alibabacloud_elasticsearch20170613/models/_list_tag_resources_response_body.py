# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListTagResourcesResponseBodyHeaders = None,
        page_size: int = None,
        request_id: str = None,
        tag_resources: main_models.ListTagResourcesResponseBodyTagResources = None,
    ):
        # The labels of the resource.
        self.headers = headers
        # The number of resources to query.
        self.page_size = page_size
        # A list of resources that have tags.
        self.request_id = request_id
        # The type of the resource. Fixed to `ALIYUN::ELASTICSEARCH::INSTANCE`.
        self.tag_resources = tag_resources

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListTagResourcesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagResources') is not None:
            temp_model = main_models.ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m.get('TagResources'))

        return self

class ListTagResourcesResponseBodyTagResources(DaraModel):
    def __init__(
        self,
        tag_resource: List[main_models.ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        # Indicates the ID of a resource.
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
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k1 in self.tag_resource:
                result['TagResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k1 in m.get('TagResource'):
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
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        # The tag key.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListTagResourcesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The value of the tag.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

