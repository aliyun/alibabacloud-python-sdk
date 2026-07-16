# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The region ID of the resource.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/601478.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources to which you want to add tags. You can enter a maximum of 50 resource IDs.
        # 
        # Enter multiple resource IDs in the `["ResourceId. 1","ResourceId. 2",...]` format.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource to which you want to add tags. Valid values:
        # 
        # - key
        # 
        # - secret
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # A list of tags. You can enter up to 20 tags.
        # 
        # A tag consists of a key-value pair. Enter multiple tags in the `[{"Key":"key1","Value":"value1"},{"Key":"key2","Value":"value2"},..]` format.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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
        # The key of the tag. A tag consists of a key-value pair.
        # 
        # You can enter up to 20 tags. Enter multiple tags in the `[{"Key":"key1","Value":"value1"},{"Key":"key2","Value":"value2"},..]` format.
        # 
        # Each key can be up to 128 characters in length and can contain letters, digits, forward slashes (/), backslashes (\\), underscores (_), hyphens (-), periods (.), plus signs (+), equal signs (=), colons (:), and at signs (@).
        # 
        # > The key cannot start with aliyun or acs:.
        self.key = key
        # The value of the tag. A tag consists of a key-value pair.
        # 
        # You can enter up to 20 tags. Enter multiple tags in the `[{"Key":"key1","Value":"value1"},{"Key":"key2","Value":"value2"},..]` format.
        # 
        # Each value can be up to 128 characters in length and can contain letters, digits, forward slashes (/), backslashes (\\), underscores (_), hyphens (-), periods (.), plus signs (+), equal signs (=), colons (:), and at signs (@).
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

