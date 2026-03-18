# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetGroupResponseBody(DaraModel):
    def __init__(
        self,
        asset_group_list: List[main_models.DescribeAssetGroupResponseBodyAssetGroupList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The information about the asset.
        self.asset_group_list = asset_group_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.asset_group_list:
            for v1 in self.asset_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k1 in self.asset_group_list:
                result['AssetGroupList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k1 in m.get('AssetGroupList'):
                temp_model = main_models.DescribeAssetGroupResponseBodyAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAssetGroupResponseBodyAssetGroupList(DaraModel):
    def __init__(
        self,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The ID of the asset.
        self.name = name
        # The region to which the asset belongs.
        self.region = region
        # The type of the asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

