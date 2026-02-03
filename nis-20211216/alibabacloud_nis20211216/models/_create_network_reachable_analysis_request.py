# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkReachableAnalysisRequest(DaraModel):
    def __init__(
        self,
        network_path_id: str = None,
        region_id: str = None,
        tag: List[main_models.CreateNetworkReachableAnalysisRequestTag] = None,
    ):
        # The ID of the network path. You can call the [CreateNetworkPath](https://help.aliyun.com/document_detail/2366522.html) operation to obtain the ID of the network path.
        # 
        # This parameter is required.
        self.network_path_id = network_path_id
        # The ID of the region for which you want to create a task for analyzing network reachability.
        self.region_id = region_id
        # The tags to add to the resource.
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
        if self.network_path_id is not None:
            result['NetworkPathId'] = self.network_path_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathId') is not None:
            self.network_path_id = m.get('NetworkPathId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkReachableAnalysisRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateNetworkReachableAnalysisRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag to add to the resource. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key
        # The value of the tag to add to the resource. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`. The tag value can be an empty string.
        # 
        # You can add up to 20 tag values in each call.
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

