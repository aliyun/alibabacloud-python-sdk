# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The region ID. This parameter is required. Set this parameter to the ID of the region where the delivery group resides, such as `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs to which you want to bind tags. This parameter is required. Specify delivery group IDs. You can specify up to 50 IDs in a single request. Duplicate IDs are automatically deduplicated.
        # 
        # **All IDs must be existing delivery groups under the current Alibaba Cloud account.** If any ID does not exist or does not belong to the current account, the entire request fails and the error code `InvalidAppInstanceGroup.NotFound` is returned. No tags are bound to any resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. This parameter is required. **Currently, only delivery groups are supported.** The value is case-insensitive. We recommend that you use uppercase letters.
        # 
        # Valid values:
        # 
        # - APPINSTANCEGROUP: China Office (Chinese: Wuying) delivery group.
        # 
        # If you specify another value, the error code `InvalidResourceType.Invalid` is returned.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tags to bind. This parameter is required. You can specify up to 20 tags in a single request. Each tag must include both `Key` and `Value`.
        # 
        # - Tag keys in the same request must be unique. Otherwise, the error code `InvalidTag.Duplicated` is returned.
        # - If a tag key already exists on the resource, the tag value is updated to the value specified in the current request.
        # - A maximum of 20 custom tags can be bound to a single resource. If this limit is exceeded, the error code `ResourceTag.CustomTagCountExceed` is returned.
        # 
        # Tag keys that start with `System/` are China Office (Chinese: Wuying) system tags. Only the following values are supported, and the tag value can be only `true` or `false`:
        # 
        # - `System/Scheduler/GRAYSCALE`: the canary release tag for the delivery group.
        # - `System/Scheduler/STOP_NEW_USER_CONNECTION`: prevents newly bound users from establishing connections to the delivery group.
        # 
        # If you specify other tag keys that start with `System/`, the error code `InvalidTag.SystemTagKeyInvalid` or `InvalidTag.SystemKeyNotAllow` is returned.
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
        # The tag key. This parameter is required. The tag key must be 1 to 128 characters in length and is case-sensitive. The tag key cannot start with `aliyun` or `acs:` (case-insensitive) and cannot contain `http://` or `https://`. Letters, digits, spaces, and common punctuation marks are supported. If the tag key does not comply with the rules, the error code `InvalidTagPolicy.KeyInvalid` is returned.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. This parameter is required. The tag value must be 0 to 256 characters in length and is case-sensitive. An empty string is allowed. The tag value cannot contain `http://` or `https://`. If the tag value does not comply with the rules, the error code `InvalidTagPolicy.ValueInvalid` is returned.
        # 
        # If the tag key is a system tag, the tag value can be only `true` or `false`.
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

