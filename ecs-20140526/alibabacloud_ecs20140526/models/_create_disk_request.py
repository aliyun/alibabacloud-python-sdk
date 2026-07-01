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
        # > This parameter is not publicly available.
        self.arn = arn
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # > This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # The category of the data disk. Valid values:
        # 
        # - cloud: basic disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: enterprise SSD.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # - cloud_regional_disk_auto: regional Enterprise SSD (ESSD).
        # - elastic_ephemeral_disk_standard: elastic ephemeral disk - Standard Edition.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - Premium Edition.
        # 
        # Default value: cloud.
        self.disk_category = disk_category
        # The name of the disk. The name must be 2 to 128 characters in length and can contain letters in the Unicode letter category (including English and Chinese characters) and ASCII digits (0-9). The name can contain colons (:), underscores (_), periods (.), or hyphens (-). The name must start with a character in the Unicode letter category.
        # 
        # Default value: empty.
        self.disk_name = disk_name
        # This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the disk. Valid values:
        # 
        # - true: Encrypted.
        # - false: Not encrypted.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the subscription instance to which the created subscription disk is automatically attached.
        # 
        # - After you specify the instance ID, the ResourceGroupId, Tag.N.Key, Tag.N.Value, ClientToken, and KMSKeyId parameters are ignored.
        # - You cannot specify both ZoneId and InstanceId.
        # 
        # Default value: empty. A pay-as-you-go disk is created, and the region of the disk is determined by RegionId and ZoneId.
        self.instance_id = instance_id
        # The ID of the Key Management Service (KMS) key used by the disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption. The KMSKeyId value is returned after the instance is created.
        # > - - If the disk is created from a non-shared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # > - - If the disk is created from a shared encrypted snapshot, the service key is used by default.
        # > - - If the disk is created in a region where account-level default encryption for block storage is enabled, the specified account-level key is used by default.
        # > - - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # Specifies whether to enable the multi-attach feature. Valid values:
        # 
        # - Disabled: Disabled.
        # - Enabled: Enabled. Only enterprise SSDs support setting this parameter to `Enabled`.
        # 
        # Default value: Disabled.
        # 
        # > Disks with the multi-attach feature enabled support only the pay-as-you-go billing method. Therefore, when `MultiAttach=Enabled`, you cannot specify the `InstanceId` parameter. After the disk is created, you can call [AttachDisk](https://help.aliyun.com/document_detail/25515.html) to attach it. Note that a disk with the multi-attach feature enabled can be attached only as a data disk.
        self.multi_attach = multi_attach
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The performance level of the enterprise SSD to create. Set this parameter to one of the following values:
        # 
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        # 
        # For information about how to select an ESSD performance level, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values:
        # 
        # - Capacity (GiB) <= 3: Provisioned performance is not supported.
        # 
        # - Capacity (GiB) >= 4: [0, min{(1,000 IOPS/GiB × Capacity - Baseline IOPS), 50,000}]
        # 
        # 
        # Baseline performance = max{min{1,800 + 50 × Capacity, 50,000}, 3,000}.
        # 
        # 
        # > This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The ID of the region. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the disk belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The size of the disk. Unit: GiB. You must specify a value for this parameter. Valid values:
        # 
        # -   cloud: 5 to 2,000.
        # -   cloud_efficiency: 20 to 32,768.
        # -   cloud_ssd: 20 to 32,768.
        # -   cloud_essd: The valid values depend on the `PerformanceLevel` value.
        #     - PL0: 1 to 65,536.
        #     - PL1: 20 to 65,536.
        #     - PL2: 461 to 65,536.
        #     - PL3: 1,261 to 65,536.
        # - cloud_auto: 1 to 65,536.
        # - cloud_essd_entry: 10 to 32,768.
        # - cloud_regional_disk_auto: 10 to 65,536.
        # - elastic_ephemeral_disk_standard: 64 to 8,192.
        # - elastic_ephemeral_disk_premium: 64 to 8,192.
        # 
        # If you specify `SnapshotId`, the `SnapshotId` and `Size` parameters have the following restrictions:
        # 
        # - If the snapshot specified by `SnapshotId` is larger than the specified `Size` value, the snapshot size of the created disk equals the size of the specified snapshot.
        # - If the snapshot specified by `SnapshotId` is smaller than the specified `Size` value, the snapshot size of the created disk equals the specified `Size` value.
        self.size = size
        # The ID of the snapshot to use to create the disk. Snapshots created on or before July 15, 2013 cannot be used to create disks. 
        # 
        # The `SnapshotId` and `Size` parameters have the following restrictions:
        # 
        # - If the snapshot specified by `SnapshotId` is larger than the specified `Size` value, the snapshot size of the created disk equals the size of the specified snapshot.
        # - If the snapshot specified by `SnapshotId` is smaller than the specified `Size` value, the snapshot size of the created disk equals the specified `Size` value.
        # - Elastic ephemeral disks cannot be created from snapshots.
        self.snapshot_id = snapshot_id
        # The ID of the dedicated block storage cluster. To create a disk in a specific dedicated block storage cluster, specify this parameter.
        # 
        # > You can set either the storage set parameters (`StorageSetId` and `StorageSetPartitionNumber`) or the dedicated block storage cluster parameter (`StorageClusterId`), but not both. If you set both, the API call fails.
        self.storage_cluster_id = storage_cluster_id
        # The ID of the storage set.
        # 
        # > You can set either the storage set parameters (`StorageSetId` and `StorageSetPartitionNumber`) or the dedicated block storage cluster parameter (`StorageClusterId`), but not both. If you set both, the API call fails.
        self.storage_set_id = storage_set_id
        # The number of partitions in the storage set. Valid values: 2 and greater. The maximum value cannot exceed the privilege quota limit returned by calling [DescribeAccountAttributes](https://help.aliyun.com/document_detail/73772.html).
        # 
        # Default value: 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The list of tags for the disk.
        self.tag = tag
        # The ID of the zone in which to create a pay-as-you-go disk.
        # 
        # - If you do not specify InstanceId, ZoneId is required.
        # - You cannot specify both ZoneId and InstanceId.
        # 
        # 
        # > You do not need to set ZoneId for disks of the `cloud_regional_disk_auto` type.
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
        # The tag key of the disk. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the disk. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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
        # > This parameter is not publicly available.
        self.assume_role_for = assume_role_for
        # > This parameter is not publicly available.
        self.role_type = role_type
        # > This parameter is not publicly available.
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

