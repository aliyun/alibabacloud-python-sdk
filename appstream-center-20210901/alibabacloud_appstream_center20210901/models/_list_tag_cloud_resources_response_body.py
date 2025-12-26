# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListTagCloudResourcesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_tags: List[main_models.ListTagCloudResourcesResponseBodyResourceTags] = None,
        total_count: int = None,
    ):
        # Indicates whether the next query is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags added to the cloud resources.
        self.resource_tags = resource_tags
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.resource_tags:
            for v1 in self.resource_tags:
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

        result['ResourceTags'] = []
        if self.resource_tags is not None:
            for k1 in self.resource_tags:
                result['ResourceTags'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_tags = []
        if m.get('ResourceTags') is not None:
            for k1 in m.get('ResourceTags'):
                temp_model = main_models.ListTagCloudResourcesResponseBodyResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTagCloudResourcesResponseBodyResourceTags(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tags: List[main_models.ListTagCloudResourcesResponseBodyResourceTagsTags] = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        self.resource_type = resource_type
        # The tags.
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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTagCloudResourcesResponseBodyResourceTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListTagCloudResourcesResponseBodyResourceTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag type.
        # 
        # Valid values:
        # 
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

