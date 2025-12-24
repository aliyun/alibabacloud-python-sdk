# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotGroupsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshot_groups: main_models.DescribeSnapshotGroupsResponseBodySnapshotGroups = None,
    ):
        # The token used to start the next query.
        # 
        # > If the return value is empty, no more data exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the snapshot-consistent groups.
        self.snapshot_groups = snapshot_groups

    def validate(self):
        if self.snapshot_groups:
            self.snapshot_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_groups is not None:
            result['SnapshotGroups'] = self.snapshot_groups.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotGroups') is not None:
            temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroups()
            self.snapshot_groups = temp_model.from_map(m.get('SnapshotGroups'))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroups(DaraModel):
    def __init__(
        self,
        snapshot_group: List[main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroup] = None,
    ):
        self.snapshot_group = snapshot_group

    def validate(self):
        if self.snapshot_group:
            for v1 in self.snapshot_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotGroup'] = []
        if self.snapshot_group is not None:
            for k1 in self.snapshot_group:
                result['SnapshotGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_group = []
        if m.get('SnapshotGroup') is not None:
            for k1 in m.get('SnapshotGroup'):
                temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroup()
                self.snapshot_group.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroup(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        progress_status: str = None,
        resource_group_id: str = None,
        snapshot_group_id: str = None,
        snapshots: main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshots = None,
        status: str = None,
        tags: main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTags = None,
    ):
        # The creation time. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the snapshot-consistent group.
        self.description = description
        # The ID of the instance to which the snapshot-consistent group belongs. This parameter has a value only when all disk snapshots in the snapshot-consistent group belong to the same instance. If disk snapshots in the snapshot-consistent group belong to different instances, you can check the response parameters that start with `Snapshots.Snapshot.Tags.` to determine the ID of the instance to which each snapshot in the snapshot-consistent group belongs.
        self.instance_id = instance_id
        # The name of the snapshot-consistent group.
        self.name = name
        # >  This parameter is not publicly available.
        self.progress_status = progress_status
        # The ID of the resource group to which the snapshot-consistent group belongs.
        self.resource_group_id = resource_group_id
        # The ID of the snapshot-consistent group.
        self.snapshot_group_id = snapshot_group_id
        # The information about the snapshots in the snapshot-consistent group.
        self.snapshots = snapshots
        # The state of the snapshot-consistent group. Valid values:
        # 
        # *   progressing: The snapshot-consistent group was being created.
        # *   accomplished: The snapshot-consistent group was created.
        # *   failed: The snapshot-consistent group failed to be created.
        self.status = status
        # The tags of the snapshot-consistent group.
        self.tags = tags

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.progress_status is not None:
            result['ProgressStatus'] = self.progress_status

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snapshot_group_id is not None:
            result['SnapshotGroupId'] = self.snapshot_group_id

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProgressStatus') is not None:
            self.progress_status = m.get('ProgressStatus')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnapshotGroupId') is not None:
            self.snapshot_group_id = m.get('SnapshotGroupId')

        if m.get('Snapshots') is not None:
            temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTagsTag] = None,
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
                temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the snapshot-consistent group.
        self.key = key
        # The tag value of the snapshot-consistent group.
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

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for v1 in self.snapshot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k1 in self.snapshot:
                result['Snapshot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k1 in m.get('Snapshot'):
                temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshot(DaraModel):
    def __init__(
        self,
        available: bool = None,
        instant_access: bool = None,
        instant_access_retention_days: int = None,
        progress: str = None,
        snapshot_id: str = None,
        source_disk_id: str = None,
        source_disk_type: str = None,
        tags: main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTags = None,
    ):
        # Indicates whether the snapshot can be shared and be used to create or roll back a disk. Valid values:
        # 
        # *   true
        # *   false
        self.available = available
        # Indicates whether the instant access feature is enabled. Valid values:
        # 
        # *   true: The instant access feature is enabled. By default, the instant access feature is enabled for ESSDs.
        # *   false: The instant access feature is disabled. The snapshot is a standard snapshot for which the instant access feature is disabled.
        # 
        # >  This parameter is no longer used. By default, standard snapshots of ESSDs are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.instant_access = instant_access
        # The validity period of the instant access feature. When the validity period ends, the instant access snapshot is automatically released.
        # 
        # >  This parameter is no longer used. By default, standard snapshots of ESSDs are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.instant_access_retention_days = instant_access_retention_days
        # The progress of the snapshot creation task. Unit: percent (%).
        self.progress = progress
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The ID of the source disk. This parameter is retained even after the source disk of the snapshot is released.
        self.source_disk_id = source_disk_id
        # The type of the source disk. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
        self.source_disk_type = source_disk_type
        # The tags of the snapshot. The default values contain snapshot source information.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.instant_access_retention_days is not None:
            result['InstantAccessRetentionDays'] = self.instant_access_retention_days

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('InstantAccessRetentionDays') is not None:
            self.instant_access_retention_days = m.get('InstantAccessRetentionDays')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTagsTag] = None,
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
                temp_model = main_models.DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotGroupsResponseBodySnapshotGroupsSnapshotGroupSnapshotsSnapshotTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the snapshot. The default values of Key and Value contain snapshot source information.
        self.key = key
        # The tag value of the snapshot. The default values of Key and Value contain snapshot source information.
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

