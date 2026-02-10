# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateAttackPathSensitiveAssetConfigRequest(DaraModel):
    def __init__(
        self,
        attack_path_asset_list: List[main_models.CreateAttackPathSensitiveAssetConfigRequestAttackPathAssetList] = None,
        config_type: str = None,
    ):
        # List of cloud product assets.
        # 
        # This parameter is required.
        self.attack_path_asset_list = attack_path_asset_list
        # Configuration type. Possible values:
        # - asset_instance: Asset.
        # 
        # This parameter is required.
        self.config_type = config_type

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

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_path_asset_list = []
        if m.get('AttackPathAssetList') is not None:
            for k1 in m.get('AttackPathAssetList'):
                temp_model = main_models.CreateAttackPathSensitiveAssetConfigRequestAttackPathAssetList()
                self.attack_path_asset_list.append(temp_model.from_map(k1))

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        return self

class CreateAttackPathSensitiveAssetConfigRequestAttackPathAssetList(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        instance_id: str = None,
        region_id: str = None,
        vendor: int = None,
    ):
        # Subtype of the cloud product asset.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the subtype of the cloud product asset.
        # 
        # This parameter is required.
        self.asset_sub_type = asset_sub_type
        # Type of the cloud product asset.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the type of the cloud product asset.
        # 
        # This parameter is required.
        self.asset_type = asset_type
        # Cloud product asset instance ID.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the cloud product asset instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Region ID of the cloud product asset instance.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the region ID of the cloud product asset instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Cloud product asset vendor.
        # 
        # > You can call [ListCloudAssetInstances](~~ListCloudAssetInstances~~) to query the cloud product asset vendor.
        # 
        # This parameter is required.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

