# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DettachAssetGroupToInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        asset_group_list_shrink: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset that you want to dissociate.
        # 
        # This parameter is required.
        self.asset_group_list_shrink = asset_group_list_shrink
        # The ID of the instance.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_group_list_shrink is not None:
            result['AssetGroupList'] = self.asset_group_list_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetGroupList') is not None:
            self.asset_group_list_shrink = m.get('AssetGroupList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

