# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class TagCloudResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[main_models.TagCloudResourcesRequestTags] = None,
    ):
        # The list of resource IDs. A maximum of 50 resource IDs are supported. You do not need to specify this parameter when the resource type is tenant ID.
        self.resource_ids = resource_ids
        # The cloud resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tags. System tags and custom tags are supported.
        # 
        # - System tag enumeration values:
        #    - `System/Scheduler/GRAYSCALE`: canary release tag
        #    - `System/Scheduler/STOP_NEW_USER_CONNECTION`: tag that prevents new user connections from being established for the delivery group
        # 
        # - Custom tags: A maximum of 20 custom tags can be created.
        # 
        # > Each tag key on the same resource can have only one tag value. If you add a tag key that already exists, the corresponding tag value is updated to the new value.
        # 
        # This parameter is required.
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
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.TagCloudResourcesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class TagCloudResourcesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. This parameter is case-sensitive. The tag key must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. This parameter is case-sensitive. The tag value must be 1 to 128 characters in length.
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

