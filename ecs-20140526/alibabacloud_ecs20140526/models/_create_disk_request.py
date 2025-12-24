# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateDiskRequest(DaraModel):
    def __init__(
        self,
        advanced_features: str = None,
        arn: List[main_models.CreateDiskRequestArn] = None,
        bursting_enabled: bool = None,
        client_token: str = None,
        description: str = None,
        disk_category: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        instance_id: str = None,
        kmskey_id: str = None,
        multi_attach: str = None,
        owner_account: str = None,
        owner_id: int = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        size: int = None,
        snapshot_id: str = None,
        storage_cluster_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        tag: List[main_models.CreateDiskRequestTag] = None,
        zone_id: str = None,
    ):
        # This parameter is not publicly available.
        self.advanced_features = advanced_features
        # >  This parameter is not publicly available.
        self.arn = arn
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is available only if you set `DiskCategory` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # This parameter is left empty by default.
        self.description = description
        # The category of the data disk. Valid values for different disk categories:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: utra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: ESSD
        # *   cloud_auto: ESSD AutoPL disk
        # *   cloud_essd_entry: ESSD Entry disk
        # *   cloud_regional_disk_auto: Regional ESSD
        # *   elastic_ephemeral_disk_standard: standard elastic ephemeral disk
        # *   elastic_ephemeral_disk_premium: premium elastic ephemeral disk
        # 
        # Default value: cloud.
        # 
        # Enumerated values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: SSD
        # *   cloud_auto: ESSD AutoPL disk
        # *   cloud_regional_disk_auto: Regional ESSD
        # *   cloud_essd: ESSD
        # *   elastic_ephemeral_disk_standard: standard elastic ephemeral disk.
        # *   cloud_essd: ESSD
        # *   elastic_ephemeral_disk_premium: premium elastic ephemeral disk
        self.disk_category = disk_category
        # The name of the data disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-). The name must start with a letter.
        # 
        # This parameter is left empty by default.
        self.disk_name = disk_name
        # This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the subscription instance to which to attach the subscription disk.
        # 
        # *   If you specify an instance ID, the following parameters are ignored: ResourceGroupId, Tag.N.Key, Tag.N.Value, ClientToken, and KMSKeyId.
        # *   You cannot specify both ZoneId and InstanceId in a request.
        # 
        # This parameter is empty by default, which indicates that a pay-as-you-go disk is created in the region and zone specified by RegionId and ZoneId.
        self.instance_id = instance_id
        # The ID of the Key Management Service (KMS) key that is used for the disk.
        self.kmskey_id = kmskey_id
        # Specifies whether to enable the multi-attach feature for the disk. Valid values:
        # 
        # *   Disabled
        # *   Enabled Set the value to `Enabled` only for ESSDs.
        # 
        # Default value: Disabled.
        # 
        # >  Disks for which the multi-attach feature is enabled support only the pay-as-you-go billing method. When `MultiAttach` is set to Enabled, you cannot specify `InstanceId`. You can call the [AttachDisk](https://help.aliyun.com/document_detail/25515.html) operation to attach disks to instances after the disks are created. Disks for which the multi-attach feature is enabled can be attached only as data disks.
        self.multi_attach = multi_attach
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The performance level of the disk if the disk is an ESSD. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        # 
        # For information about ESSD performance levels, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # Specifies the read/write IOPS that is provisioned for the ESSD AutoPL disk. Valid value:
        # 
        # *   Capacity (GiB) <= 3: not configurable
        # *   Capacity (GiB) >= 4: [0, min{(1,000
        # 
        # IOPS/GiB × Capacity - Baseline IOPS), 50,000}]
        # 
        # Baseline performance: max{min{1,800 + 50 × Capacity, 50,000}, 3,000}
        # 
        # >  This parameter is available only if you set `DiskCategory` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The ID of the region in which to create the disk. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to add the disk.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The size of the data disk. Unit: GiB. This parameter is required. Valid values for different disk categories:
        # 
        # *   Valid values when DiskCategory is set to cloud: 5 to 2000.
        # 
        # *   Valid values when DiskCategory is set to cloud_efficiency: 20 to 32768.
        # 
        # *   Valid values when DiskCategory is set to cloud_ssd: 20 to 32768.
        # 
        # *   Valid values when DiskCategory is set to cloud_essd: vary based on the `PerformanceLevel` value.
        # 
        #     *   Valid values when PerformanceLevel is set to PL0: 1 to 65536.
        #     *   Valid values when PerformanceLevel is set to PL1: 20 to 65536.
        #     *   Valid values when PerformanceLevel is set to PL2: 461 to 65536.
        #     *   Valid values when PerformanceLevel is set to PL3: 1261 to 65536.
        # 
        # *   Valid values when DiskCategory is set to cloud_auto: 1 to 65536.
        # 
        # *   Valid values when DiskCategory is set to cloud_essd_entry: 10 to 32768.
        # 
        # *   Valid values when DiskCategory is set to cloud_regional_disk_auto: 10 to 65536.
        # 
        # *   Valid values when DiskCategory is set to elastic_ephemeral_disk_standard: 64 to 8192.
        # 
        # *   Valid values when DiskCategory is set to elastic_ephemeral_disk_premium: 64 to 8192.
        # 
        # If you specify `SnapshotId`, the following limits apply to `SnapshotId` and `Size`:
        # 
        # *   If the size of the snapshot specified by `SnapshotId` is larger than the value of `Size`, the size of the created disk is equal to the size of the snapshot.
        # *   If the size of the snapshot specified by `SnapshotId` is smaller than the value of `Size`, the size of the created disk is equal to the value of `Size`.
        self.size = size
        # The ID of the snapshot to use to create the disk. Snapshots that were created on or before July 15, 2013 cannot be used to create disks.
        # 
        # The following limits apply to `SnapshotId` and `Size`:
        # 
        # *   If the size of the snapshot specified by `SnapshotId` is larger than the value of `Size`, the size of the created disk is equal to the specified snapshot size.
        # *   If the size of the snapshot specified by `SnapshotId` is smaller than the value of `Size`, the size of the created disk is equal to the value of `Size`.
        # *   You cannot create elastic ephemeral disks from snapshots.
        self.snapshot_id = snapshot_id
        # The ID of the dedicated block storage cluster in which to create the disk. To create a disk in a specific dedicated block storage cluster, you must specify this parameter.
        # 
        # >  You can specify the storage set-related parameters (`StorageSetId` and `StorageSetPartitionNumber`) or the dedicated block storage cluster-related parameter (`StorageClusterId`), but not both. If you specify a storage set-related parameter and a dedicated block storage cluster-related parameter in a request, the request fails.
        self.storage_cluster_id = storage_cluster_id
        # The ID of the storage set.
        # 
        # > You cannot specify storage set-related parameters (`StorageSetId` and `StorageSetPartitionNumber`) and the dedicated block storage cluster-related parameter (`StorageClusterId`) at the same time. Otherwise, the operation cannot be called.
        self.storage_set_id = storage_set_id
        # The number of partitions in the storage set. The value must be greater than or equal to 2 but cannot exceed the quota obtained by calling the [DescribeAccountAttributes](https://help.aliyun.com/document_detail/73772.html)operation.
        # 
        # Default value: 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The tags to add to the disk.
        self.tag = tag
        # The ID of the zone in which to create the pay-as-you-go disk.
        # 
        # *   If you do not specify InstanceId, you must specify ZoneId.
        # *   You cannot specify both ZoneId and InstanceId in the same request.
        # 
        # >  You do not need to specify this parameter if you set DiskCategory to `cloud_regional_disk_auto` to create a Regional ESSD.
        self.zone_id = zone_id

    def validate(self):
        if self.arn:
            for v1 in self.arn:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_features is not None:
            result['AdvancedFeatures'] = self.advanced_features

        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedFeatures') is not None:
            self.advanced_features = m.get('AdvancedFeatures')

        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.CreateDiskRequestArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDiskRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateDiskRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the disk. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N to add to the disk. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class CreateDiskRequestArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # >  This parameter is not publicly available.
        self.assume_role_for = assume_role_for
        # >  This parameter is not publicly available.
        self.role_type = role_type
        # >  This parameter is not publicly available.
        self.rolearn = rolearn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')

        return self

