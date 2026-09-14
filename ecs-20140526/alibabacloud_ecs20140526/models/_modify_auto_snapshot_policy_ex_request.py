# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyAutoSnapshotPolicyExRequest(DaraModel):
    def __init__(
        self,
        copied_snapshots_retention_days: int = None,
        copy_encryption_configuration: main_models.ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfiguration = None,
        enable_cross_region_copy: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_copy_regions: str = None,
        target_tags: List[main_models.ModifyAutoSnapshotPolicyExRequestTargetTags] = None,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        time_points: str = None,
    ):
        # The retention period of cross-region replicated snapshots. Unit: days. Valid values:
        # 
        # - -1: The snapshot is retained permanently.
        # - 1 to 65535: The snapshot is retained for the specified number of days.
        # 
        # Default value: -1.
        self.copied_snapshots_retention_days = copied_snapshots_retention_days
        # The encryption configuration for cross-region snapshot replication.
        self.copy_encryption_configuration = copy_encryption_configuration
        # Specifies whether to allow automatic cross-region snapshot replication. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed.
        self.enable_cross_region_copy = enable_cross_region_copy
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination region for cross-region snapshot replication. You can specify only one destination region.
        self.target_copy_regions = target_copy_regions
        # The list of target resource tags. The automatic snapshot policy matches target resources based on tags.
        self.target_tags = target_tags
        # The ID of the automatic snapshot policy. You can call [DescribeAutoSnapshotPolicyEx](https://help.aliyun.com/document_detail/25530.html) to query available automatic snapshot policies.
        # 
        # This parameter is required.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The name of the automatic snapshot policy. If this parameter is left empty, the name is not modified.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # The region ID of the automatic snapshot policy. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The days of the week on which to create automatic snapshots. Valid values: 1 to 7, where 1 represents Monday.
        # 
        # To create multiple automatic snapshots within a week, specify multiple days:
        # 
        # - You can specify up to 7 days.
        # - Specify multiple days as a JSON array in the format of `"1", "2", … "7"`. Separate multiple days with commas (,).
        self.repeat_weekdays = repeat_weekdays
        # The retention period of automatic snapshots. Unit: days. Valid values:
        # 
        # - -1: The snapshot is retained permanently.
        # - 1 to 65536: The snapshot is retained for the specified number of days.
        # 
        # Default value: -1.
        self.retention_days = retention_days
        # The time of day at which to create automatic snapshots. The time is in UTC+8 and in the format of hours. Valid values: 0 to 23, representing 24 points in time from 00:00 to 23:00. For example, 1 represents 01:00.
        # 
        # To create multiple automatic snapshots within a day, specify multiple time points:
        # 
        # - You can specify up to 24 time points.
        # - Specify multiple time points as a JSON array in the format of `"0", "1", … "23"`. Separate multiple time points with commas (,).
        self.time_points = time_points

    def validate(self):
        if self.copy_encryption_configuration:
            self.copy_encryption_configuration.validate()
        if self.target_tags:
            for v1 in self.target_tags:
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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_copy_regions is not None:
            result['TargetCopyRegions'] = self.target_copy_regions

        result['TargetTags'] = []
        if self.target_tags is not None:
            for k1 in self.target_tags:
                result['TargetTags'].append(k1.to_map() if k1 else None)

        if self.auto_snapshot_policy_id is not None:
            result['autoSnapshotPolicyId'] = self.auto_snapshot_policy_id

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
            temp_model = main_models.ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfiguration()
            self.copy_encryption_configuration = temp_model.from_map(m.get('CopyEncryptionConfiguration'))

        if m.get('EnableCrossRegionCopy') is not None:
            self.enable_cross_region_copy = m.get('EnableCrossRegionCopy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetCopyRegions') is not None:
            self.target_copy_regions = m.get('TargetCopyRegions')

        self.target_tags = []
        if m.get('TargetTags') is not None:
            for k1 in m.get('TargetTags'):
                temp_model = main_models.ModifyAutoSnapshotPolicyExRequestTargetTags()
                self.target_tags.append(temp_model.from_map(k1))

        if m.get('autoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('autoSnapshotPolicyId')

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

class ModifyAutoSnapshotPolicyExRequestTargetTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Valid values of N: 1 to 5.
        # 
        # The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with aliyun or acs:, or contain http:// or https://.
        self.key = key
        # The tag value.
        # 
        # Valid values of N: 1 to 5.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        # 
        # > If you pass an empty value or an empty string, the tag value matches any value.
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

class ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfiguration(DaraModel):
    def __init__(
        self,
        arn: List[main_models.ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfigurationArn] = None,
        encrypted: bool = None,
        kmskey_id: str = None,
    ):
        # This parameter is not available for use.
        self.arn = arn
        # Specifies whether to enable encryption for cross-region snapshot replication. Valid values:
        # 
        # - true: Yes. 
        # - false: No. 
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The key ID of the KMS key used for cross-region encrypted snapshot replication.
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
                temp_model = main_models.ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfigurationArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        return self

class ModifyAutoSnapshotPolicyExRequestCopyEncryptionConfigurationArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # This parameter is not available for use.
        self.assume_role_for = assume_role_for
        # This parameter is not available for use.
        self.role_type = role_type
        # This parameter is not available for use.
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

