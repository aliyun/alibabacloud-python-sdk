# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class AttachAssetGroupToInstanceRequest(DaraModel):
    def __init__(
        self,
        asset_group_list: List[main_models.AttachAssetGroupToInstanceRequestAssetGroupList] = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The information about the asset to be associated.
        # 
        # This parameter is required.
        self.asset_group_list = asset_group_list
        # The ID of the instance to query.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k1 in m.get('AssetGroupList'):
                temp_model = main_models.AttachAssetGroupToInstanceRequestAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AttachAssetGroupToInstanceRequestAssetGroupList(DaraModel):
    def __init__(
        self,
        member_uid: str = None,
        name: str = None,
        region: str = None,
        type: str = None,
    ):
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid
        # The ID of the asset that you want to add. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        # 
        # This parameter is required.
        self.name = name
        # The region ID of the asset.
        # 
        # This parameter is required.
        self.region = region
        # The type of the asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

