# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of instance IDs. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to query instance IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The list of tags.
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
        # The key of the tag.
        # 
        # > N specifies the sequence number of the tag key. For example:<ul>
        # <li>Tag.1.Key specifies the key of the first tag.</li>
        # <li>Tag.2.Key specifies the key of the second tag.</li></ul>.
        self.key = key
        # The value of the tag.
        # 
        # > N specifies the sequence number of the tag value. For example:<ul>
        # <li>Tag.1.Value specifies the value of the first tag.</li>
        # <li>Tag.2.Value specifies the value of the second tag.</li></ul>.
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

