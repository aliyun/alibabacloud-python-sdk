# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class AddTagsRequest(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        region_id: str = None,
        tag: List[main_models.AddTagsRequestTag] = None,
    ):
        # The ID of the application group.
        # 
        # Valid values of N: 1 to 20.
        # 
        # For information about how to query the IDs of application groups, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/2513168.html).
        # 
        # This parameter is required.
        self.group_ids = group_ids
        self.region_id = region_id
        # The tags.
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
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AddTagsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class AddTagsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Valid values of N: 1 to 3. A tag key can be 1 to 64 characters in length.
        # 
        # You can create a tag key or specify an existing tag key. For more information about how to obtain a tag key, see [DescribeTagKeyList](https://help.aliyun.com/document_detail/2513189.html).
        # 
        # >  The tag key cannot start with `aliyun` or `acs:`. The tag key (`Tag.N.Key`) and tag value (`Tag.N.Value`) must be specified at the same time.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # Valid values of N: 1 to 3. A tag value can be 1 to 64 characters in length.
        # 
        # You can create a tag value or specify an existing tag value. For more information about how to obtain a tag value, see [DescribeTagValueList](https://help.aliyun.com/document_detail/2513188.html).
        # 
        # >  The tag value cannot start with `aliyun` or `acs:`. The tag key (`Tag.N.Key`) and tag value (`Tag.N.Value`) must be specified at the same time.
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

