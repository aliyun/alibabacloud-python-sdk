# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The list of resource IDs. You can specify up to 50 resource IDs in a single call.
        # > 
        # > - Supported resource types include users and access configurations:
        # > - - If the resource type is user, specify the user ID.
        # > - - If the resource type is access configuration, specify the access configuration ID.
        # 
        # <notice>If the directory ID parameter is not specified, you must add the prefix "${DirectoryId}_" to the resource ID.</notice>
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Users and access configurations are supported.
        # 
        # - If the resource type is user, set the value to user.
        # 
        # - If the resource type is access configuration, set the value to accessConfiguration.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tags. You can add up to 20 tags in a single call.
        # 
        # This parameter is required.
        self.tag = tag

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
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class TagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # > 
        # > - - The key cannot start with aliyun or acs: (case-insensitive). 
        # > - - The key cannot contain http:// or https:// (case-insensitive).
        # > - - The key cannot be an empty string.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # > 
        # > - - The value cannot contain http:// or https:// (case-insensitive).
        # > - - The value cannot be an empty string.
        # 
        # This parameter is required.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

