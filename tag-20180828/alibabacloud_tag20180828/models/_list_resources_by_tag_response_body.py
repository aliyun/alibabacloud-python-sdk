# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListResourcesByTagResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resources: List[main_models.ListResourcesByTagResponseBodyResources] = None,
    ):
        # Indicates whether the `next query` is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the `next query` is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the `token` used to start the next query.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
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

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListResourcesByTagResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class ListResourcesByTagResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        tags: List[main_models.ListResourcesByTagResponseBodyResourcesTags] = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The information of the tags.
        # 
        # This parameter is returned only if the `IncludeAllTags` parameter is set to `True`.
        self.tags = tags

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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListResourcesByTagResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListResourcesByTagResponseBodyResourcesTags(DaraModel):
    def __init__(
        self,
        category: str = None,
        key: str = None,
        value: str = None,
    ):
        # The type of the tag. Valid values:
        # 
        # *   custom
        # *   system
        self.category = category
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

