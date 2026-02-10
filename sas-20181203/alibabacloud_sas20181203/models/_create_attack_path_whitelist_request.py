# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateAttackPathWhitelistRequest(DaraModel):
    def __init__(
        self,
        attack_path_asset_list: List[main_models.CreateAttackPathWhitelistRequestAttackPathAssetList] = None,
        path_name: str = None,
        path_type: str = None,
        remark: str = None,
        whitelist_name: str = None,
        whitelist_type: str = None,
    ):
        # List of cloud product assets in the attack path.
        self.attack_path_asset_list = attack_path_asset_list
        # Path name.
        # 
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path name.
        self.path_name = path_name
        # Path type.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path type.
        # 
        # This parameter is required.
        self.path_type = path_type
        # Remark information.
        self.remark = remark
        # Whitelist name.
        # 
        # This parameter is required.
        self.whitelist_name = whitelist_name
        # Whitelist type. Values:
        # 
        # - **ALL_ASSET**: All assets
        # - **PART_ASSET**: Partial assets
        # 
        # This parameter is required.
        self.whitelist_type = whitelist_type

    def validate(self):
        if self.attack_path_asset_list:
            for v1 in self.attack_path_asset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackPathAssetList'] = []
        if self.attack_path_asset_list is not None:
            for k1 in self.attack_path_asset_list:
                result['AttackPathAssetList'].append(k1.to_map() if k1 else None)

        if self.path_name is not None:
            result['PathName'] = self.path_name

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.whitelist_name is not None:
            result['WhitelistName'] = self.whitelist_name

        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_path_asset_list = []
        if m.get('AttackPathAssetList') is not None:
            for k1 in m.get('AttackPathAssetList'):
                temp_model = main_models.CreateAttackPathWhitelistRequestAttackPathAssetList()
                self.attack_path_asset_list.append(temp_model.from_map(k1))

        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('WhitelistName') is not None:
            self.whitelist_name = m.get('WhitelistName')

        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')

        return self

class CreateAttackPathWhitelistRequestAttackPathAssetList(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        instance_id: str = None,
        node_type: str = None,
        region_id: str = None,
        vendor: int = None,
    ):
        # Subtype of the cloud product asset.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the subtype of the cloud product asset.
        self.asset_sub_type = asset_sub_type
        # Type of the cloud product asset.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the type of the cloud product asset.
        self.asset_type = asset_type
        # Cloud product asset instance ID.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the cloud product asset instance ID.
        self.instance_id = instance_id
        # Node type, with values:
        # - **start**: Start point.
        # - **end**: End point.
        self.node_type = node_type
        # Region ID of the cloud product asset instance.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the region ID of the cloud product asset instance.
        self.region_id = region_id
        # Vendor of the cloud product asset.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the vendor of the cloud product asset.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

