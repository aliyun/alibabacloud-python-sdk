# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CloneDisksRequest(DaraModel):
    def __init__(
        self,
        arn: List[main_models.CloneDisksRequestArn] = None,
        bursting_enabled: bool = None,
        client_token: str = None,
        disk_category: str = None,
        disk_name: str = None,
        dry_run: str = None,
        encrypted: bool = None,
        kms_key_id: str = None,
        multi_attach: str = None,
        owner_id: int = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        size: int = None,
        source_disk_id: str = None,
        tag: List[main_models.CloneDisksRequestTag] = None,
    ):
        # > This parameter is not yet available.
        self.arn = arn
        # Specifies whether to enable performance bursting for the new disk. Valid values:
        # 
        # - `true`: Enables performance bursting.
        # 
        # - `false`: Disables performance bursting.
        # 
        # > This parameter is valid only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/zh/ecs/user-guide/essd-autopl-disks).
        self.bursting_enabled = bursting_enabled
        # A client-generated token that, when provided, ensures the idempotence of the request. The token must be unique for each request. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The type of the new disk. Valid values:
        # 
        # - `cloud_essd`: ESSD cloud disk.
        # 
        # - `cloud_auto`: ESSD AutoPL cloud disk.
        # 
        # - `cloud_essd_entry`: ESSD Entry cloud disk.
        # 
        # - `cloud_regional_disk_auto`: regional disk.
        # 
        # > Disk type limits for cloning
        # >
        # > - A non-regional disk can be cloned only as a non-regional disk.
        # >
        # > - A regional disk can be cloned only as a regional disk.
        # 
        # This parameter is required.
        self.disk_category = disk_category
        # The name of the new disk. The name must be 2 to 128 characters in length. It must start with a letter and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Default value: none.
        self.disk_name = disk_name
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - `true`: Performs a dry run to check the request without cloning the disk. The system checks whether your AccessKey is valid, whether the RAM user is authorized, and whether the required parameters are specified. If the request fails the check, the system returns the corresponding error message. If the request passes the check, the `DryRunOperation` error code is returned.
        # 
        # - `false` (default): Sends a normal request. If the request passes the check, the system returns a 2xx HTTP status code and clones the disk.
        self.dry_run = dry_run
        # Specifies whether to encrypt the new disk. Valid values:
        # 
        # - `true`: The disk is encrypted.
        # 
        # - `false`: The disk is not encrypted.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the KMS key to use for the new disk.
        self.kms_key_id = kms_key_id
        # Specifies whether to enable the multi-attach feature for the new disk. Valid values:
        # 
        # - `Disabled`: Disables the multi-attach feature.
        # 
        # - `Enabled`: Enables the multi-attach feature. You can set this parameter to `Enabled` only for ESSD cloud disks.
        # 
        # This parameter is required.
        self.multi_attach = multi_attach
        self.owner_id = owner_id
        # The performance level of the new ESSD cloud disk. Valid values:
        # 
        # - `PL0`: A single disk can deliver up to 10,000 random read/write IOPS.
        # 
        # - `PL1`: A single disk can deliver up to 50,000 random read/write IOPS.
        # 
        # - `PL2`: A single disk can deliver up to 100,000 random read/write IOPS.
        # 
        # - `PL3`: A single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > This parameter is required when `DiskCategory` is set to `cloud_essd`.
        # 
        # For more information about how to select an ESSD performance level, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL cloud disk. Valid values:
        # 
        # - You cannot set this parameter for disks that are 3 GiB or smaller in size.
        # 
        # - For disks that are 4 GiB or larger in size, the value must be in the range of `[0, min(1000 * Size - baseline performance, 50000)]`.
        # 
        # baseline performance = `max(min(1800 + 50 * Size, 50000), 3000)`.
        # 
        # > This parameter is valid only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/zh/ecs/user-guide/essd-autopl-disks).
        self.provisioned_iops = provisioned_iops
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/zh/ecs/api-regions-describeregions) operation to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group for the new disk.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        # The size of the new disk, in GiB. The value must be greater than or equal to the size of the source disk. The value range varies based on the `DiskCategory` value:
        # 
        # - `cloud_essd`: The value range depends on the `PerformanceLevel` value.
        # 
        #   - `PL0`: 1 to 65,536
        # 
        #   - `PL1`: 20 to 65,536
        # 
        #   - `PL2`: 461 to 65,536
        # 
        #   - `PL3`: 1,261 to 65,536
        # 
        # - `cloud_auto`: 1 to 65,536
        # 
        # - `cloud_essd_entry`: 10 to 32,768
        # 
        # - `cloud_regional_disk_auto`: 10 to 65,536
        # 
        # This parameter is required.
        self.size = size
        # The ID of the source disk.
        # 
        # This parameter is required.
        self.source_disk_id = source_disk_id
        # The tags to add to the new disk.
        self.tag = tag

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
        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach

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

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.size is not None:
            result['Size'] = self.size

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.CloneDisksRequestArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')

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

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CloneDisksRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CloneDisksRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the new disk. Valid values of N: 1 to 20. The tag key must be 1 to 128 characters in length and cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the new disk. Valid values of N: 1 to 20. The tag value can be an empty string or up to 128 characters in length, and it cannot contain `http://` or `https://`.
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

class CloneDisksRequestArn(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # > This parameter is not yet available.
        self.assume_role_for = assume_role_for
        # > This parameter is not yet available.
        self.role_type = role_type
        # > This parameter is not yet available.
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

