# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ModifyLindormV2InstanceRequest(DaraModel):
    def __init__(
        self,
        cloud_storage_size: int = None,
        cloud_storage_type: str = None,
        engine_type: str = None,
        instance_id: str = None,
        node_group_list: List[main_models.ModifyLindormV2InstanceRequestNodeGroupList] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        upgrade_type: str = None,
    ):
        self.cloud_storage_size = cloud_storage_size
        self.cloud_storage_type = cloud_storage_type
        self.engine_type = engine_type
        # This parameter is required.
        self.instance_id = instance_id
        self.node_group_list = node_group_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # This parameter is required.
        self.upgrade_type = upgrade_type

    def validate(self):
        if self.node_group_list:
            for v1 in self.node_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_storage_size is not None:
            result['CloudStorageSize'] = self.cloud_storage_size

        if self.cloud_storage_type is not None:
            result['CloudStorageType'] = self.cloud_storage_type

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['NodeGroupList'] = []
        if self.node_group_list is not None:
            for k1 in self.node_group_list:
                result['NodeGroupList'].append(k1.to_map() if k1 else None)

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudStorageSize') is not None:
            self.cloud_storage_size = m.get('CloudStorageSize')

        if m.get('CloudStorageType') is not None:
            self.cloud_storage_type = m.get('CloudStorageType')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.node_group_list = []
        if m.get('NodeGroupList') is not None:
            for k1 in m.get('NodeGroupList'):
                temp_model = main_models.ModifyLindormV2InstanceRequestNodeGroupList()
                self.node_group_list.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        return self

class ModifyLindormV2InstanceRequestNodeGroupList(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        node_count: str = None,
        node_disk_size: int = None,
        node_disk_type: str = None,
        node_spec: str = None,
        resource_group_name: str = None,
    ):
        self.group_id = group_id
        self.node_count = node_count
        self.node_disk_size = node_disk_size
        self.node_disk_type = node_disk_type
        self.node_spec = node_spec
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size

        if self.node_disk_type is not None:
            result['NodeDiskType'] = self.node_disk_type

        if self.node_spec is not None:
            result['NodeSpec'] = self.node_spec

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')

        if m.get('NodeDiskType') is not None:
            self.node_disk_type = m.get('NodeDiskType')

        if m.get('NodeSpec') is not None:
            self.node_spec = m.get('NodeSpec')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

