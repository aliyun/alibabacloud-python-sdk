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
        # Specifies whether to enable burst (performance bursting). Valid values:
        # 
        # - true: enables burst.
        # - false: disables burst.
        # 
        # > This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # Ensures the idempotency of the request. Generate a parameter value from your client to ensure uniqueness across different requests. **ClientToken** only supports ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The disk description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # The category of the data disk. Valid values:
        # 
        # - cloud: basic disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # - cloud_regional_disk_auto: ESSD zone-redundant disk.
        # - elastic_ephemeral_disk_standard: elastic ephemeral disk - standard.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - premium.
        # 
        # Default value: cloud.
        self.disk_category = disk_category
        # The disk name. The name must be 2 to 128 characters in length and can contain Unicode letters (including English and Chinese characters) and ASCII digits (0-9). It can contain colons (:), underscores (_), periods (.), or hyphens (-). It must start with a Unicode letter.
        # 
        # Default value: empty.
        self.disk_name = disk_name
        # This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the disk. Valid values:
        # 
        # - true: encrypts the disk.
        # - false: does not encrypt the disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # Creates a subscription disk and automatically attaches it to the specified subscription instance (InstanceId).
        # 
        # - After you set the instance ID, the ResourceGroupId, Tag.N.Key, Tag.N.Value, ClientToken, and KMSKeyId parameters that you set are ignored.
        # - You cannot specify both ZoneId and InstanceId.
        # 
        # Default value: empty, which means a pay-as-you-go disk is created. The location of the disk is determined by RegionId and ZoneId.
        self.instance_id = instance_id
        # The KMS key ID used by the disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is successfully created.
        # > - - Disk created from a non-shared encrypted snapshot: The encryption key used by the snapshot is used by default.
        # > - - Disk created from a shared encrypted snapshot: The service key is used by default.
        # > - - Disk created in a region where account-level default encryption for block storage is enabled: The specified account-level key is used by default.
        # > - - Other cases: The service key is used by default.
        self.kmskey_id = kmskey_id
        # Specifies whether to enable the multi-attach feature. Valid values:
        # 
        # - Disabled: disables the feature.
        # - Enabled: enables the feature. Currently, only ESSDs support setting this to `Enabled`.
        # 
        # Default value: Disabled.
        # 
        # > Disks with the multi-attach feature enabled only support the pay-as-you-go billing method. Therefore, when `MultiAttach=Enabled`, you cannot set the `InstanceId` parameter. You can call [AttachDisk](https://help.aliyun.com/document_detail/25515.html) to attach the disk after creation, but note that disks with multi-attach enabled can only be attached as data disks.
        self.multi_attach = multi_attach
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Sets the performance level of the disk when creating an ESSD. Valid values:
        # 
        # - PL0: maximum random read/write IOPS of 10,000 per disk.
        # - PL1: maximum random read/write IOPS of 50,000 per disk.
        # - PL2: maximum random read/write IOPS of 100,000 per disk.
        # - PL3: maximum random read/write IOPS of 1,000,000 per disk.
        # 
        # Default value: PL1.
        # 
        # For information about how to select an ESSD performance level, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk (per disk). Possible values:
        # 
        # - Capacity (GiB) <= 3: provisioned performance cannot be set.
        # 
        # - Capacity (GiB) >= 4: [0, min{(1,000
        # 
        #  IOPS/GiB * capacity - baseline IOPS), 50,000}]
        # 
        # 
        # Baseline performance = max{min{1,800 + 50 * capacity, 50,000}, 3,000}.
        # 
        # 
        # > This parameter is supported only when `DiskCategory` = `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group to which the disk belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The capacity size. Unit: GiB. You must specify a value for this parameter. Valid values:
        # 
        # -   cloud: 5 to 2,000.
        # -   cloud_efficiency: 20 to 32,768.
        # -   cloud_ssd: 20 to 32,768.
        # -   cloud_essd: The valid value range depends on the value of `PerformanceLevel`.
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
        # If you specify the `SnapshotId` parameter, the `SnapshotId` and `Size` parameters have the following restrictions:
        # 
        # - If the snapshot capacity corresponding to the `SnapshotId` parameter is greater than the specified `Size` parameter value, the actual size of the created disk equals the size of the specified snapshot.
        # - If the snapshot capacity corresponding to the `SnapshotId` parameter is less than the specified `Size` parameter value, the actual size of the created disk equals the specified `Size` parameter value.
        self.size = size
        # The snapshot ID used to create the disk. Snapshots created on or before July 15, 2013 cannot be used to create disks.
        # 
        # The `SnapshotId` and `Size` parameters have the following restrictions:
        # 
        # - If the snapshot capacity corresponding to the `SnapshotId` parameter is greater than the specified `Size` parameter value, the actual size of the created disk equals the size of the specified snapshot.
        # - If the snapshot capacity corresponding to the `SnapshotId` parameter is less than the specified `Size` parameter value, the actual size of the created disk equals the specified `Size` parameter value.
        # - Creating elastic ephemeral disks from snapshots is not supported.
        self.snapshot_id = snapshot_id
        # The dedicated block storage cluster ID. If you need to create a disk in a specified dedicated block storage cluster, specify this parameter.
        # 
        # > Storage set parameters (`StorageSetId`, `StorageSetPartitionNumber`) and dedicated block storage cluster parameter (`StorageClusterId`) are mutually exclusive. If both are set, the API call will fail.
        self.storage_cluster_id = storage_cluster_id
        # The storage set ID.
        # 
        # > Storage set parameters (`StorageSetId`, `StorageSetPartitionNumber`) and dedicated block storage cluster parameter (`StorageClusterId`) are mutually exclusive. If both are set, the API call will fail.
        self.storage_set_id = storage_set_id
        # The number of storage set partitions. Valid values: greater than or equal to 2, and cannot exceed the quota limit displayed after calling [DescribeAccountAttributes](https://help.aliyun.com/document_detail/73772.html).
        # 
        # Default value: 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The list of tag information for the disk.
        self.tag = tag
        # Creates a pay-as-you-go disk in the specified zone.
        # 
        # - If you do not set InstanceId, ZoneId is required.
        # - You cannot specify both ZoneId and InstanceId.
        # 
        # 
        # > Disks of the `cloud_regional_disk_auto` type do not require ZoneId to be set.
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
        # The tag key of the disk. Valid values of N: 1 to 20. Once a Tag.N.Key value is specified, it cannot be an empty string. It supports up to 128 characters and cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the disk. Valid values of N: 1 to 20. Once a Tag.N.Value value is specified, it can be an empty string. It supports up to 128 characters and cannot contain `http://` or `https://`.
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

