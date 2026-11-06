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
        destination_zone_id: str = None,
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
        # > This parameter is not available.
        self.arn = arn
        # Specifies whether to enable performance burst for the new disk. Valid values:
        # - true: enables performance burst.
        # - false: disables performance burst.
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://www.alibabacloud.com/help/en/ecs/user-guide/essd-autopl-disks).
        self.bursting_enabled = bursting_enabled
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The destination zone of the new disk.
        self.destination_zone_id = destination_zone_id
        # The category of the new disk. Valid values:
        # 
        # - cloud_essd: standard SSD (ESSD).
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # - cloud_regional_disk_auto: regional Standard SSD (ESSD).
        # 
        # > Disk category restrictions for disk cloning:
        # > - Non-zone-redundant disks can only be cloned to non-zone-redundant categories.
        # > - Zone-redundant disks can only be cloned to zone-redundant categories.
        # 
        # This parameter is required.
        self.disk_category = disk_category
        # The name of the disk. The name must be 2 to 128 characters in length and can contain letters and digits (0-9). It can also contain colons (:), underscores (_), periods (.), and hyphens (-). It must start with a letter.
        # 
        # Default value: empty.
        self.disk_name = disk_name
        # Specifies whether to only perform a dry run on the request. Valid values:
        # - true: performs a dry run only and does not perform the actual operation. The system checks whether your AccessKey pair is valid, whether the authorization of Resource Access Management (RAM) users is valid, and whether required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - false (default): sends a normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the actual operation is performed.
        self.dry_run = dry_run
        # Specifies whether the new disk is encrypted. Valid values:
        # - true: The new disk is encrypted.
        # - false: The new disk is not encrypted.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The KMS key ID used by the new disk.
        self.kms_key_id = kms_key_id
        # Specifies whether to enable the multi-attach feature for the new disk. Valid values:
        # 
        # - Disabled: disables the multi-attach feature.
        # - Enabled: enables the multi-attach feature. Currently, only ESSDs can be set to Enabled.
        # 
        # This parameter is required.
        self.multi_attach = multi_attach
        self.owner_id = owner_id
        # The performance level of the ESSD. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > If DiskCategory is set to cloud_essd, the PerformanceLevel parameter is required.
        # 
        # For more information about how to select the performance level of an ESSD, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values:
        # - If the capacity is less than or equal to 3 GiB, provisioned performance is not supported.
        # - If the capacity is greater than or equal to 4 GiB, the valid values are 0 to min{(1,000 IOPS/GiB × Capacity - Baseline IOPS), 50,000}.
        # 
        # Baseline performance = max{min{1,800 + 50 × Capacity, 50,000}, 3,000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://www.alibabacloud.com/help/en/ecs/user-guide/essd-autopl-disks).
        self.provisioned_iops = provisioned_iops
        # The region ID. You can call the [DescribeRegions](https://www.alibabacloud.com/help/en/ecs/api-regions-describeregions) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the disk belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        # The capacity of the new disk. Unit: GiB. You must specify this parameter. Valid values:
        # 
        # - cloud_essd: The valid values vary based on the performance level.
        #     - PL0: 1 to 65,536.
        #     - PL1: 20 to 65,536.
        #     - PL2: 461 to 65,536.
        #     - PL3: 1,261 to 65,536.
        # - cloud_auto: 1 to 65,536.
        # - cloud_essd_entry: 10 to 32,768.
        # - cloud_regional_disk_auto: 10 to 65,536.
        # 
        # This parameter is required.
        self.size = size
        # The ID of the source disk.
        # 
        # This parameter is required.
        self.source_disk_id = source_disk_id
        # The tags of the disk.
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

        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id

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

        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')

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
        # The key of tag N of the disk. Valid values of N: 1 to 20. If you specify Tag.N.Key, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The value of tag N of the disk. Valid values of N: 1 to 20. If you specify Tag.N.Value, it can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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
        # > This parameter is not available.
        self.assume_role_for = assume_role_for
        # > This parameter is not available.
        self.role_type = role_type
        # > This parameter is not available.
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

