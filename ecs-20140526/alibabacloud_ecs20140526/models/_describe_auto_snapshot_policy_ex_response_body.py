# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoSnapshotPolicyExResponseBody(DaraModel):
    def __init__(
        self,
        auto_snapshot_policies: main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPolicies = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the automatic snapshot policies.
        self.auto_snapshot_policies = auto_snapshot_policies
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of automatic snapshot policies
        self.total_count = total_count

    def validate(self):
        if self.auto_snapshot_policies:
            self.auto_snapshot_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policies is not None:
            result['AutoSnapshotPolicies'] = self.auto_snapshot_policies.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicies') is not None:
            temp_model = main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPolicies()
            self.auto_snapshot_policies = temp_model.from_map(m.get('AutoSnapshotPolicies'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPolicies(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy: List[main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy] = None,
    ):
        self.auto_snapshot_policy = auto_snapshot_policy

    def validate(self):
        if self.auto_snapshot_policy:
            for v1 in self.auto_snapshot_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoSnapshotPolicy'] = []
        if self.auto_snapshot_policy is not None:
            for k1 in self.auto_snapshot_policy:
                result['AutoSnapshotPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policy = []
        if m.get('AutoSnapshotPolicy') is not None:
            for k1 in m.get('AutoSnapshotPolicy'):
                temp_model = main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy()
                self.auto_snapshot_policy.append(temp_model.from_map(k1))

        return self

class DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        copied_snapshots_retention_days: int = None,
        copy_encryption_configuration: main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyCopyEncryptionConfiguration = None,
        creation_time: str = None,
        disk_nums: int = None,
        enable_cross_region_copy: bool = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        resource_group_id: str = None,
        retention_days: int = None,
        status: str = None,
        tags: main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTags = None,
        target_copy_regions: str = None,
        time_points: str = None,
        type: str = None,
        volume_nums: int = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The name of the automatic snapshot policy.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        # >  This parameter is in invitational preview and is not publicly available.
        self.copied_snapshots_retention_days = copied_snapshots_retention_days
        # Encryption configurations for cross-region snapshot replication.
        self.copy_encryption_configuration = copy_encryption_configuration
        # The time when the automatic snapshot policy was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The number of disks to which the automatic snapshot policy is applied.
        self.disk_nums = disk_nums
        # >  This parameter is in invitational preview and is not publicly available.
        self.enable_cross_region_copy = enable_cross_region_copy
        # The region ID of the automatic snapshot policy.
        self.region_id = region_id
        # The days of the week on which to create automatic snapshots. Valid values: 1 to 7, which correspond to the days of the week. For example, 1 indicates Monday. One or more days can be specified.
        self.repeat_weekdays = repeat_weekdays
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The retention period of the automatic snapshots. Unit: days. Valid values:
        # 
        # *   \\-1: Automatic snapshots are retained until they are deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified number of days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The status of the automatic snapshot policy. Valid values:
        # 
        # *   Normal: The automatic snapshot policy is normal.
        # *   Expire: The automatic snapshot policy cannot be used because your account has overdue payments.
        self.status = status
        # The tags of the automatic snapshot policy.
        self.tags = tags
        # >  This parameter is in invitational preview and is not publicly available.
        self.target_copy_regions = target_copy_regions
        # The points in time of the day at which to create automatic snapshots.
        # 
        # The time is displayed in UTC+8. Unit: hours. Valid values: 0 to 23, which correspond to the 24 points in time on the hour from 00:00:00 to 23:00:00. For example, 1 indicates 01:00:00. Multiple points in time can be specified.
        # 
        # The parameter value is a JSON array that contains up to 24 points in time separated by commas (,). Example: `["0", "1", ... "23"]`.
        self.time_points = time_points
        # The type of the automatic snapshot policy. Valid values:
        # 
        # *   Custom: user-defined snapshot policy.
        # *   System: system-defined snapshot policy.
        self.type = type
        # The number of extended volumes to which the automatic snapshot policy is applied.
        self.volume_nums = volume_nums

    def validate(self):
        if self.copy_encryption_configuration:
            self.copy_encryption_configuration.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name

        if self.copied_snapshots_retention_days is not None:
            result['CopiedSnapshotsRetentionDays'] = self.copied_snapshots_retention_days

        if self.copy_encryption_configuration is not None:
            result['CopyEncryptionConfiguration'] = self.copy_encryption_configuration.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk_nums is not None:
            result['DiskNums'] = self.disk_nums

        if self.enable_cross_region_copy is not None:
            result['EnableCrossRegionCopy'] = self.enable_cross_region_copy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.target_copy_regions is not None:
            result['TargetCopyRegions'] = self.target_copy_regions

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        if self.type is not None:
            result['Type'] = self.type

        if self.volume_nums is not None:
            result['VolumeNums'] = self.volume_nums

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')

        if m.get('CopiedSnapshotsRetentionDays') is not None:
            self.copied_snapshots_retention_days = m.get('CopiedSnapshotsRetentionDays')

        if m.get('CopyEncryptionConfiguration') is not None:
            temp_model = main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyCopyEncryptionConfiguration()
            self.copy_encryption_configuration = temp_model.from_map(m.get('CopyEncryptionConfiguration'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskNums') is not None:
            self.disk_nums = m.get('DiskNums')

        if m.get('EnableCrossRegionCopy') is not None:
            self.enable_cross_region_copy = m.get('EnableCrossRegionCopy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TargetCopyRegions') is not None:
            self.target_copy_regions = m.get('TargetCopyRegions')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VolumeNums') is not None:
            self.volume_nums = m.get('VolumeNums')

        return self

class DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the automatic snapshot policy.
        self.tag_key = tag_key
        # The tag value of the automatic snapshot policy.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeAutoSnapshotPolicyExResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicyCopyEncryptionConfiguration(DaraModel):
    def __init__(
        self,
        encrypted: bool = None,
        kmskey_id: str = None,
    ):
        # Whether to enable encryption for cross-region snapshot replication. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key used to encrypt snapshots in cross-region snapshot replication.
        self.kmskey_id = kmskey_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        return self

