# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateDBClusterRequest(DaraModel):
    def __init__(
        self,
        ainode_number: int = None,
        ainode_spec: str = None,
        backup_set_id: str = None,
        clone_source_region_id: str = None,
        compute_resource: str = None,
        dbcluster_description: str = None,
        dbcluster_network_type: str = None,
        dbcluster_version: str = None,
        disk_encryption: bool = None,
        enable_default_resource_pool: bool = None,
        enable_ssl: bool = None,
        kms_id: str = None,
        pay_type: str = None,
        period: str = None,
        product_form: str = None,
        product_version: str = None,
        region_id: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        resource_group_id: str = None,
        restore_to_time: str = None,
        restore_type: str = None,
        secondary_vswitch_id: str = None,
        secondary_zone_id: str = None,
        source_db_cluster_id: str = None,
        storage_resource: str = None,
        tag: List[main_models.CreateDBClusterRequestTag] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.ainode_number = ainode_number
        self.ainode_spec = ainode_spec
        # The ID of the backup set used for restoration from a backup set.
        # 
        # > You can call the [DescribeBackups](https://help.aliyun.com/document_detail/612318.html) operation to query the backup list of the cluster.
        self.backup_set_id = backup_set_id
        # The region of the source cluster.
        # > This parameter is required for cross-region cloning.
        self.clone_source_region_id = clone_source_region_id
        # The compute reserved resources. Valid values: 0 ACU to 4096 ACU, in increments of 16. 1 ACU is approximately equivalent to 1 core and 4 GB of memory.
        # > Include the unit when specifying this parameter.
        self.compute_resource = compute_resource
        # The description of the cluster.
        # - The description cannot start with `http://` or `https://`.
        # - The description must be 2 to 256 characters in length.
        self.dbcluster_description = dbcluster_description
        # The network type of the cluster. Only **VPC** (Virtual Private Cloud) is supported.
        self.dbcluster_network_type = dbcluster_network_type
        # The version of the Data Lakehouse Edition cluster. Valid values: **5.0**.
        # 
        # This parameter is required.
        self.dbcluster_version = dbcluster_version
        # Specifies whether to enable cloud disk encryption.
        self.disk_encryption = disk_encryption
        # Specifies whether to allocate all compute reserved resources to the default resource group (user_default). Valid values:
        # - **true** (default): All compute reserved resources are allocated to the default resource group.
        # - **false**: Not all compute reserved resources are allocated to the default resource group.
        self.enable_default_resource_pool = enable_default_resource_pool
        # Specifies whether to enable SSL encryption. Valid values:
        # 
        # - **true**: SSL encryption is enabled.
        # - **false**: SSL encryption is disabled.
        self.enable_ssl = enable_ssl
        # The ID of the key used to encrypt cloud disk data.
        # > This parameter is used only when cloud disk encryption is enabled for the AnalyticDB for MySQL cluster.
        self.kms_id = kms_id
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # - **Prepaid**: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription type of the subscription cluster. Valid values:
        # - **Year**: subscription on a yearly basis.
        # - **Month**: subscription on a monthly basis.
        # 
        # > This parameter is required when PayType is set to Prepaid.
        self.period = period
        # The product form. Valid values:
        # - **IntegrationForm**: integrated form.
        # - **LegacyForm**: Data Lakehouse Edition.
        self.product_form = product_form
        # The product version. Valid values:
        # - **BasicVersion**: Basic Edition.
        # - **EnterpriseVersion**: Enterprise Edition.
        # > This parameter is required only when ProductForm is set to IntegrationForm.
        self.product_version = product_version
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the region ID of a specific Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of reserved nodes. 
        # - Enterprise Edition uses 3 nodes by default, in increments of 3.
        # - Basic Edition uses 1 node by default.
        # > This parameter is required only when ProductForm is set to IntegrationForm.
        self.reserved_node_count = reserved_node_count
        # The node specifications of reserved nodes, in ACUs.
        self.reserved_node_size = reserved_node_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The point in time to which you want to restore data from the backup set.
        self.restore_to_time = restore_to_time
        # The restoration method. Valid values:
        # * **backup**: restores data from a backup set. You must also specify the **BackupSetId** and **SourceDBClusterId** parameters.
        # * **timepoint**: restores data to a specific point in time. You must also specify the **RestoreToTime** and **SourceDBClusterId** parameters.
        self.restore_type = restore_type
        # The secondary vSwitch ID.
        # > The value of this parameter must be different from the value of the VSwitchId parameter.
        self.secondary_vswitch_id = secondary_vswitch_id
        # The secondary zone ID.
        # > The value of this parameter must be different from the value of the ZoneId parameter.
        self.secondary_zone_id = secondary_zone_id
        # The instance ID of the source AnalyticDB for MySQL Data Warehouse Edition cluster. If this parameter is specified, the Data Lakehouse Edition cluster is used to recover from the Data Warehouse Edition cluster.
        self.source_db_cluster_id = source_db_cluster_id
        # The storage reserved resources. Valid values: 0 ACU to 2064 ACU, in increments of 24. 1 ACU is approximately equivalent to 1 core and 4 GB of memory.
        # > Include the unit when specifying this parameter.
        self.storage_resource = storage_resource
        # The list of tags.
        self.tag = tag
        # The subscription duration of the subscription cluster. Valid values:
        # - When **Period** is set to Year, the value of UsedTime ranges from 1 to 3 (integer).
        # - When **Period** is set to Month, the value of UsedTime ranges from 1 to 9 (integer).
        # 
        # > This parameter is required when PayType is set to **Prepaid**.
        self.used_time = used_time
        # The virtual private cloud (VPC) ID.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the zone ID of a specific Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.zone_id = zone_id

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
        if self.ainode_number is not None:
            result['AINodeNumber'] = self.ainode_number

        if self.ainode_spec is not None:
            result['AINodeSpec'] = self.ainode_spec

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.clone_source_region_id is not None:
            result['CloneSourceRegionId'] = self.clone_source_region_id

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version

        if self.disk_encryption is not None:
            result['DiskEncryption'] = self.disk_encryption

        if self.enable_default_resource_pool is not None:
            result['EnableDefaultResourcePool'] = self.enable_default_resource_pool

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.kms_id is not None:
            result['KmsId'] = self.kms_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.product_form is not None:
            result['ProductForm'] = self.product_form

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_node_count is not None:
            result['ReservedNodeCount'] = self.reserved_node_count

        if self.reserved_node_size is not None:
            result['ReservedNodeSize'] = self.reserved_node_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.restore_to_time is not None:
            result['RestoreToTime'] = self.restore_to_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.secondary_vswitch_id is not None:
            result['SecondaryVSwitchId'] = self.secondary_vswitch_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.source_db_cluster_id is not None:
            result['SourceDbClusterId'] = self.source_db_cluster_id

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AINodeNumber') is not None:
            self.ainode_number = m.get('AINodeNumber')

        if m.get('AINodeSpec') is not None:
            self.ainode_spec = m.get('AINodeSpec')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('CloneSourceRegionId') is not None:
            self.clone_source_region_id = m.get('CloneSourceRegionId')

        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')

        if m.get('DiskEncryption') is not None:
            self.disk_encryption = m.get('DiskEncryption')

        if m.get('EnableDefaultResourcePool') is not None:
            self.enable_default_resource_pool = m.get('EnableDefaultResourcePool')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('KmsId') is not None:
            self.kms_id = m.get('KmsId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedNodeCount') is not None:
            self.reserved_node_count = m.get('ReservedNodeCount')

        if m.get('ReservedNodeSize') is not None:
            self.reserved_node_size = m.get('ReservedNodeSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RestoreToTime') is not None:
            self.restore_to_time = m.get('RestoreToTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SecondaryVSwitchId') is not None:
            self.secondary_vswitch_id = m.get('SecondaryVSwitchId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SourceDbClusterId') is not None:
            self.source_db_cluster_id = m.get('SourceDbClusterId')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDBClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can use tags to filter the cluster list. You can specify up to 20 tag pairs. The value of N for each tag pair must be unique and must be a consecutive integer that starts from 1. The value of `Tag.N.Key` corresponds to the value of `Tag.N.Value`.
        # 
        # > The tag key can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        self.key = key
        # The tag value. You can use tags to filter the cluster list. You can specify up to 20 tag pairs. The value of N for each tag pair must be unique and must be a consecutive integer that starts from 1. The value of `Tag.N.Key` corresponds to the value of `Tag.N.Value`.
        # 
        # > The tag value can be up to 64 characters in length and cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
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

