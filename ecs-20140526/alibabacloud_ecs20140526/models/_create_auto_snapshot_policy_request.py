# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        association_type: str = None,
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
        target_tags: List[main_models.CreateAutoSnapshotPolicyRequestTargetTags] = None,
        auto_snapshot_policy_name: str = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The association type between the automatic snapshot policy and target resources. Valid values:
        # ● AssociatedWithDisk: associated with disks.
        # ● AssociatedWithInstanceTag: associated with instance tags.
        # Default value: AssociatedWithDisk.
        self.association_type = association_type
        # The retention period of cross-region snapshot replicas. Unit: days. Valid values:
        # 
        # - -1: Snapshot replicas are permanently retained.
        # - 1 to 65535: Snapshot replicas are retained for the specified number of days.
        # 
        # Default value: -1.
        self.copied_snapshots_retention_days = copied_snapshots_retention_days
        # The backup encryption parameters for snapshot geo-redundancy.
        self.copy_encryption_configuration = copy_encryption_configuration
        # Specifies whether to allow automatic cross-region replication.
        # 
        # - true: allows automatic cross-region replication.
        # - false: does not allow automatic cross-region replication.
        self.enable_cross_region_copy = enable_cross_region_copy
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # > This parameter is not publicly available.
        self.storage_location_arn = storage_location_arn
        # The tags of the automatic snapshot policy.
        self.tag = tag
        # The destination region to which snapshots are replicated. You can set only one destination region.
        self.target_copy_regions = target_copy_regions
        # The list of target resource tags. The automatic snapshot policy matches target resources based on tags.
        # This parameter is required when AssociationType is set to AssociatedWithInstanceTag.
        self.target_tags = target_tags
        # The name of the automatic snapshot policy. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # Default value: null.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The region ID of the automatic snapshot policy. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The days of the week on which automatic snapshots are created. Unit: days. The cycle is weekly. Valid values: 1 to 7. For example, 1 indicates Monday. Format description:
        # 
        # - The parameter value must be a JSON array. For example, ["1"\\] indicates that automatic snapshots are created every Monday.
        # - To create multiple automatic snapshots within a week, specify multiple time points separated by commas (,). You can specify up to 7 time points. For example, ["1","3","5"\\] indicates that automatic snapshots are created every Monday, Wednesday, and Friday.
        # 
        # This parameter is required.
        self.repeat_weekdays = repeat_weekdays
        # The retention period of automatic snapshots. Unit: days. Valid values:
        # 
        # - -1: Automatic snapshots are permanently retained.
        # - 1 to 65535: Automatic snapshots are retained for the specified number of days.
        # 
        # Default value: -1.
        # 
        # This parameter is required.
        self.retention_days = retention_days
        # The points in time at which automatic snapshots are created. The time is displayed in UTC+8. Unit: hours. Valid values: 0 to 23, which represent 00:00 to 23:00 (a total of 24 time points). For example, 1 indicates 01:00. Format description:
        # 
        # - The parameter value must be a JSON array. For example, ["1"\\] indicates that automatic snapshots are created at 01:00.
        # - To create multiple automatic snapshots within a day, specify multiple time points separated by commas (,). You can specify up to 24 time points. For example, ["1","3","5"\\] indicates that automatic snapshots are created at 01:00, 03:00, and 05:00.
        # 
        # >If a disk contains a large amount of data and the time required to create a single automatic snapshot exceeds the interval between two time points, the next time point is skipped. For example, you set 09:00, 10:00, 11:00, and 12:00 as the automatic snapshot time points. Because the disk contains a large amount of data, the snapshot creation starts at 09:00 and is completed at 10:20, which takes 80 minutes. The system skips the 10:00 time point and creates the next automatic snapshot at 11:00.
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
        if self.target_tags:
            for v1 in self.target_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_type is not None:
            result['AssociationType'] = self.association_type

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

        result['TargetTags'] = []
        if self.target_tags is not None:
            for k1 in self.target_tags:
                result['TargetTags'].append(k1.to_map() if k1 else None)

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
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')

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

        self.target_tags = []
        if m.get('TargetTags') is not None:
            for k1 in m.get('TargetTags'):
                temp_model = main_models.CreateAutoSnapshotPolicyRequestTargetTags()
                self.target_tags.append(temp_model.from_map(k1))

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

class CreateAutoSnapshotPolicyRequestTargetTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # Valid values of N: 1 to 10.
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. The tag key cannot contain http:// or https://.
        self.key = key
        # The tag value.
        # Valid values of N: 1 to 10. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
        # Note: If you pass in an empty or empty string value, it indicates any value.
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

class CreateAutoSnapshotPolicyRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the automatic snapshot policy. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. The tag key cannot contain http:// or https://.
        self.key = key
        # The tag value of the automatic snapshot policy. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with acs:. The tag value cannot contain http:// or https://.
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
        # > This parameter is not publicly available.
        self.arn = arn
        # Specifies whether to enable encryption for cross-region snapshot backup. Valid values:
        # 
        # - true: enables encryption.
        # - false: does not enable encryption.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The key ID of the KMS key used for cross-region encrypted snapshot backup.
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

