# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[main_models.ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # An array that encompasses both the resource details and its tags, comprising elements like the resource ID, the resource type, the tag key, and the tag value.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for v1 in self.tag_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagResources'] = []
        if self.tag_resources is not None:
            for k1 in self.tag_resources:
                result['TagResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k1 in m.get('TagResources'):
                temp_model = main_models.ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k1))

        return self

class ListTagResourcesResponseBodyTagResources(DaraModel):
    def __init__(
        self,
        propagate: bool = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # Indicates whether the tags of the scaling group can be propagated to instances. Valid values:
        # 
        # *   true: The tags of the scaling group can be propagated to only instances that are newly created.
        # *   false: The tags of the scaling group cannot be propagated to instances.
        self.propagate = propagate
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.propagate is not None:
            result['Propagate'] = self.propagate

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
        if m.get('Propagate') is not None:
            self.propagate = m.get('Propagate')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

