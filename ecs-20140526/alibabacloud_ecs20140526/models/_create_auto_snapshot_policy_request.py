# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        copied_snapshots_retention_days: int = None,
        copy_encryption_configuration: main_models.CreateAutoSnapshotPolicyRequestCopyEncryptionConfiguration = None,
        enable_cross_region_copy: bool = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_location_arn: str = None,
        tag: List[main_models.CreateAutoSnapshotPolicyRequestTag] = None,
        target_copy_regions: str = None,
        auto_snapshot_policy_name: str = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The retention period of the snapshot copy in the destination region. Unit: days. Valid values:
        # 
        # *   \\-1: The snapshot copy is retained until it is deleted.
        # *   1 to 65535: The snapshot copy is retained for the specified number of days. After the retention period of the snapshot copy expires, the snapshot copy is automatically deleted.
        # 
        # Default value: -1.
        self.copied_snapshots_retention_days = copied_snapshots_retention_days
        # The encryption parameters for cross-region snapshot replication.
        self.copy_encryption_configuration = copy_encryption_configuration
        # Specifies whether to enable cross-region replication for snapshots.
        # 
        # *   true
        # *   false
        self.enable_cross_region_copy = enable_cross_region_copy
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # > This parameter is not publicly available.
        self.storage_location_arn = storage_location_arn
        # The tags to add to the automatic snapshot policy.
        self.tag = tag
        # The destination region to which to copy the snapshot. You can specify only a single destination region.
        self.target_copy_regions = target_copy_regions
        # The name of the automatic snapshot policy. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # By default, this parameter is left empty.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The ID of the region in which to create the automatic snapshot policy. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The days of the week on which to create automatic snapshots. Valid values: 1 to 7, which correspond to Monday to Sunday. 1 indicates Monday. Format description:
        # 
        # *   Set this parameter to a JSON-formatted array. For example, a value of ["1"] specifies automatic snapshots to be created every Monday.
        # *   To schedule multiple automatic snapshots to be created in a week, you can specify multiple values. Separate the values with commas (,). You can specify a maximum of seven days. For example, a value of ["1","3","5"] specifies automatic snapshots to be created every Monday, Wednesday, and Friday.
        # 
        # This parameter is required.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of the automatic snapshot. Unit: days. Valid values:
        # 
        # *   \\-1: The automatic snapshot is retained until it is deleted.
        # *   1 to 65535: The automatic snapshot is retained for the specified number of days. After the retention period of the automatic snapshot expires, the automatic snapshot is automatically deleted.
        # 
        # Default value: -1.
        # 
        # This parameter is required.
        self.retention_days = retention_days
        # The points in time of the day at which to create automatic snapshots. The time must be in UTC+8. Unit: hours. Valid values: 0 to 23, which correspond to the 24 on-the-hour points in time from 00:00:00 to 23:00:00. For example, 1 indicates 01:00:00. Format description:
        # 
        # *   Set this parameter to a JSON-formatted array. For example, a value of ["1"] specifies automatic snapshots to be created at 01:00:00.
        # *   To schedule multiple automatic snapshots to be created in a day, you can specify multiple values. Separate the values with commas (,). You can specify up to 24 points in time. For example, a value of ["1","3","5"] specifies automatic snapshots to be created at 01:00:00, 03:00:00, and 05:00:00.
        # 
        # >  If an automatic snapshot is being created when the time scheduled for creating another automatic snapshot is due, the new snapshot task is skipped. This may occur when a disk contains a large volume of data. For example, you scheduled snapshots to be automatically created at 09:00, 10:00, 11:00, and 12:00. The system starts to create a snapshot for the disk at 09:00:00. The process takes 80 minutes to complete because the disk contains a large volume of data and ends at 10:20:00. The system skips the automatic snapshot task scheduled for 10:00:00 and creates the next automatic snapshot for the disk at 11:00:00.
        # 
        # This parameter is required.
        self.time_points = time_points

    def validate(self):
        if self.copy_encryption_configuration:
            self.copy_encryption_configuration.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copied_snapshots_retention_days is not None:
            result['CopiedSnapshotsRetentionDays'] = self.copied_snapshots_retention_days

        if self.copy_encryption_configuration is not None:
            result['CopyEncryptionConfiguration'] = self.copy_encryption_configuration.to_map()

        if self.enable_cross_region_copy is not None:
            result['EnableCrossRegionCopy'] = self.enable_cross_region_copy

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_location_arn is not None:
            result['StorageLocationArn'] = self.storage_location_arn

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_copy_regions is not None:
            result['TargetCopyRegions'] = self.target_copy_regions

        if self.auto_snapshot_policy_name is not None:
            result['autoSnapshotPolicyName'] = self.auto_snapshot_policy_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.repeat_weekdays is not None:
            result['repeatWeekdays'] = self.repeat_weekdays

        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days

        if self.time_points is not None:
            result['timePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopiedSnapshotsRetentionDays') is not None:
            self.copied_snapshots_retention_days = m.get('CopiedSnapshotsRetentionDays')

        if m.get('CopyEncryptionConfiguration') is not None:
            temp_model = main_models.CreateAutoSnapshotPolicyRequestCopyEncryptionConfiguration()
            self.copy_encryption_configuration = temp_model.from_map(m.get('CopyEncryptionConfiguration'))

        if m.get('EnableCrossRegionCopy') is not None:
            self.enable_cross_region_copy = m.get('EnableCrossRegionCopy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageLocationArn') is not None:
            self.storage_location_arn = m.get('StorageLocationArn')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAutoSnapshotPolicyRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetCopyRegions') is not None:
            self.target_copy_regions = m.get('TargetCopyRegions')

        if m.get('autoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('autoSnapshotPolicyName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('repeatWeekdays') is not None:
            self.repeat_weekdays = m.get('repeatWeekdays')

        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')

        if m.get('timePoints') is not None:
            self.time_points = m.get('timePoints')

        return self

class CreateAutoSnapshotPolicyRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the automatic snapshot policy. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The value of tag N to add to the automatic snapshot policy. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://. The tag value cannot start with acs:.
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

class CreateAutoSnapshotPolicyRequestCopyEncryptionConfiguration(DaraModel):
    def __init__(
        self,
        arn: List[main_models.CreateAutoSnapshotPolicyRequestCopyEncryptionConfigurationArn] = None,
        encrypted: bool = None,
        kmskey_id: str = None,
    ):
        # >  This parameter is not publicly available.
        self.arn = arn
        # Specifies whether to enable cross-region snapshot replication and encryption. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key used in cross-region snapshot replication and encryption.
        self.kmskey_id = kmskey_id

    def validate(self):
        if self.arn:
            for v1 in self.arn:
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

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.CreateAutoSnapshotPolicyRequestCopyEncryptionConfigurationArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        return self

class CreateAutoSnapshotPolicyRequestCopyEncryptionConfigurationArn(DaraModel):
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

