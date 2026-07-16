# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        backup_set_id: str = None,
        client_token: str = None,
        dbcluster_category: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbcluster_network_type: str = None,
        dbcluster_version: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        db_node_storage_type: str = None,
        encryption_key: str = None,
        encryption_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_dbcluster_id: str = None,
        tags: List[main_models.CreateDBInstanceRequestTags] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_bak: str = None,
        v_switch_bak_2: str = None,
        v_switch_id: str = None,
        zond_id_bak_2: str = None,
        zone_id: str = None,
        zone_id_bak: str = None,
    ):
        # Specifies whether to enable auto-renewal.
        # 
        # > This parameter applies only when `PayType` is set to `Prepaid`.
        self.auto_renew = auto_renew
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/360339.html) API to query backup set IDs.
        # 
        # > This parameter is required when restoring data to an ApsaraDB for ClickHouse cluster.
        self.backup_set_id = backup_set_id
        # A client token used to ensure request idempotence. The value must be a string of no more than 64 ASCII characters.
        self.client_token = client_token
        # The replica configuration. Valid values:
        # 
        # - **Basic**: single-replica
        # 
        # - **HighAvailability**: high availability (dual-replica)
        # 
        # This parameter is required.
        self.dbcluster_category = dbcluster_category
        # The instance type.<props="china">
        # 
        # - For single-replica clusters, valid values are:
        # 
        #   - **LS20**: Large-storage, 20 cores, 88 GB
        # 
        #   - **LS40**: Large-storage, 40 cores, 176 GB
        # 
        #   - **LS80**: Large-storage, 80 cores, 352 GB
        # 
        #   - **S8**: Standard, 8 cores, 32 GB
        # 
        #   - **S16**: Standard, 16 cores, 64 GB
        # 
        #   - **S32**: Standard, 32 cores, 128 GB
        # 
        #   - **S64**: Standard, 64 cores, 256 GB
        # 
        #   - **S80**: Standard, 80 cores, 384 GB
        # 
        #   - **S104**: Standard, 104 cores, 384 GB
        # 
        # - For high availability clusters, valid values are:
        # 
        #   - **LC20**: Large-storage, 20 cores, 88 GB
        # 
        #   - **LC40**: Large-storage, 40 cores, 176 GB
        # 
        #   - **LC80**: Large-storage, 80 cores, 352 GB
        # 
        #   - **C8**: Standard, 8 cores, 32 GB
        # 
        #   - **C16**: Standard, 16 cores, 64 GB
        # 
        #   - **C32**: Standard, 32 cores, 128 GB
        # 
        #   - **C64**: Standard, 64 cores, 256 GB
        # 
        #   - **C80**: Standard, 80 cores, 384 GB
        # 
        #   - **C104**: Standard, 104 cores, 384 GB
        # 
        # <props="intl">
        # 
        # - For single-replica clusters, valid values are:
        # 
        #   - **S8**: 8 cores, 32 GB
        # 
        #   - **S16**: 16 cores, 64 GB
        # 
        #   - **S32**: 32 cores, 128 GB
        # 
        #   - **S64**: 64 cores, 256 GB
        # 
        #   - **S104**: 104 cores, 384 GB
        # 
        # - For high availability clusters, valid values are:
        # 
        #   - **C8**: 8 cores, 32 GB
        # 
        #   - **C16**: 16 cores, 64 GB
        # 
        #   - **C32**: 32 cores, 128 GB
        # 
        #   - **C64**: 64 cores, 256 GB
        # 
        #   - **C104**: 104 cores, 384 GB
        # 
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The network type. Currently, only VPC is supported.
        # 
        # This parameter is required.
        self.dbcluster_network_type = dbcluster_network_type
        # The engine version. Valid values:
        # 
        # - **21.8.10.19**
        # 
        # - **22.8.5.29**
        # 
        # This parameter is required.
        self.dbcluster_version = dbcluster_version
        # The number of nodes.
        # 
        # - For single-replica clusters, the valid range is 1–48.
        # 
        # - For high availability clusters, the valid range is 1–24.
        # 
        # This parameter is required.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity per node, in GB. The valid range is 100–32,000.
        # 
        # > The value must be a multiple of 100.
        # 
        # This parameter is required.
        self.dbnode_storage = dbnode_storage
        # The storage type. Valid values:
        # 
        # <props="china">
        # 
        # - **CloudESSD_PL0**: ESSD PL0 cloud disk
        # 
        # 
        # 
        # 
        # - **CloudESSD**: ESSD PL1 cloud disk
        # 
        # - **CloudESSD_PL2**: ESSD PL2 cloud disk
        # 
        # - **CloudESSD_PL3**: ESSD PL3 cloud disk
        # 
        # - **CloudEfficiency**: Ultra Disk
        # 
        # This parameter is required.
        self.db_node_storage_type = db_node_storage_type
        # This parameter is required when `EncryptionType` is set to `CloudDisk`.
        # 
        # The ID of the cloud disk encryption key. You can create and manage keys in the Key Management Service console.
        # 
        # > If `EncryptionType` is not specified, you do not need to specify this parameter.
        self.encryption_key = encryption_key
        # The encryption type. Only cloud disk encryption is supported. Set this value to **CloudDisk**.
        # 
        # > If you do not specify this parameter, encryption is disabled.
        self.encryption_type = encryption_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription duration unit.
        # >Notice: This parameter is required only when `PayType` is set to `Prepaid`.
        # 
        # - **Year**: Measured in years.
        # 
        # - **Month**: Measured in months.
        self.period = period
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) API to query the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group that contains the cluster.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the source cluster. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) API to query cluster IDs.
        # 
        # > This parameter is required when restoring data to an ApsaraDB for ClickHouse cluster.
        self.source_dbcluster_id = source_dbcluster_id
        # The tags to add to the cluster.
        self.tags = tags
        # The subscription duration.
        # >Notice: This parameter is required only when `PayType` is set to `Prepaid`.
        # 
        # - If `Period` is `Year`, the valid range is 1–3.
        # 
        # - If `Period` is `Month`, the valid range is 1–9.
        self.used_time = used_time
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The ID of the secondary VSwitch.
        self.v_switch_bak = v_switch_bak
        # The ID of the second standby VSwitch.
        self.v_switch_bak_2 = v_switch_bak_2
        # The VSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the second standby availability zone.
        self.zond_id_bak_2 = zond_id_bak_2
        # The availability zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) API to query the latest availability zone list.
        self.zone_id = zone_id
        # The ID of the secondary availability zone.
        self.zone_id_bak = zone_id_bak

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.backup_set_id is not None:
            result['BackupSetID'] = self.backup_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category

        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version

        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.db_node_storage_type is not None:
            result['DbNodeStorageType'] = self.db_node_storage_type

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_dbcluster_id is not None:
            result['SourceDBClusterId'] = self.source_dbcluster_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_bak is not None:
            result['VSwitchBak'] = self.v_switch_bak

        if self.v_switch_bak_2 is not None:
            result['VSwitchBak2'] = self.v_switch_bak_2

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zond_id_bak_2 is not None:
            result['ZondIdBak2'] = self.zond_id_bak_2

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_bak is not None:
            result['ZoneIdBak'] = self.zone_id_bak

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BackupSetID') is not None:
            self.backup_set_id = m.get('BackupSetID')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')

        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')

        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DbNodeStorageType') is not None:
            self.db_node_storage_type = m.get('DbNodeStorageType')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceDBClusterId') is not None:
            self.source_dbcluster_id = m.get('SourceDBClusterId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateDBInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchBak') is not None:
            self.v_switch_bak = m.get('VSwitchBak')

        if m.get('VSwitchBak2') is not None:
            self.v_switch_bak_2 = m.get('VSwitchBak2')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZondIdBak2') is not None:
            self.zond_id_bak_2 = m.get('ZondIdBak2')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdBak') is not None:
            self.zone_id_bak = m.get('ZoneIdBak')

        return self

class CreateDBInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

