# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Snapshot(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creation_type: str = None,
        creator: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_resource_id: str = None,
        snapshot_resource_type: str = None,
        snapshot_storage_path: str = None,
        snapshot_url: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.creation_type = creation_type
        self.creator = creator
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.snapshot_resource_id = snapshot_resource_id
        self.snapshot_resource_type = snapshot_resource_type
        self.snapshot_storage_path = snapshot_storage_path
        self.snapshot_url = snapshot_url
        self.work_dir = work_dir
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_resource_id is not None:
            result['SnapshotResourceId'] = self.snapshot_resource_id

        if self.snapshot_resource_type is not None:
            result['SnapshotResourceType'] = self.snapshot_resource_type

        if self.snapshot_storage_path is not None:
            result['SnapshotStoragePath'] = self.snapshot_storage_path

        if self.snapshot_url is not None:
            result['SnapshotUrl'] = self.snapshot_url

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotResourceId') is not None:
            self.snapshot_resource_id = m.get('SnapshotResourceId')

        if m.get('SnapshotResourceType') is not None:
            self.snapshot_resource_type = m.get('SnapshotResourceType')

        if m.get('SnapshotStoragePath') is not None:
            self.snapshot_storage_path = m.get('SnapshotStoragePath')

        if m.get('SnapshotUrl') is not None:
            self.snapshot_url = m.get('SnapshotUrl')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

