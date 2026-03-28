# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creation_type: str = None,
        description: str = None,
        snapshot_name: str = None,
        snapshot_resource_id: str = None,
        snapshot_resource_type: str = None,
        source_storage_path: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        # Workspace visibility. Valid values:
        # - PRIVATE: Visible only to you and administrators in this workspace.
        # - PUBLIC: Visible to everyone in this workspace.
        self.accessibility = accessibility
        # Snapshot creation type. Valid values:
        # * ManualCreated: manual creation
        # * DeploymentAutoCreated: automatic creation by service deployment
        # * EvaluationAutoCreated: automatic creation by evaluation job
        self.creation_type = creation_type
        # Description of the snapshot.
        self.description = description
        # Snapshot name. Requirements:
        # * Can contain only letters, digits, and underscores (_)
        # * Must start with a letter
        # * Length must be 1 to 256 characters
        self.snapshot_name = snapshot_name
        # Snapshot resource ID.
        self.snapshot_resource_id = snapshot_resource_id
        # Snapshot resource type. Valid values:
        # * Flow: pipeline
        self.snapshot_resource_type = snapshot_resource_type
        # Create a snapshot from source files under the specified OSS folder.
        self.source_storage_path = source_storage_path
        # OSS working directory for storing the snapshot.
        self.work_dir = work_dir
        # Workspace ID. For information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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

        if self.description is not None:
            result['Description'] = self.description

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_resource_id is not None:
            result['SnapshotResourceId'] = self.snapshot_resource_id

        if self.snapshot_resource_type is not None:
            result['SnapshotResourceType'] = self.snapshot_resource_type

        if self.source_storage_path is not None:
            result['SourceStoragePath'] = self.source_storage_path

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotResourceId') is not None:
            self.snapshot_resource_id = m.get('SnapshotResourceId')

        if m.get('SnapshotResourceType') is not None:
            self.snapshot_resource_type = m.get('SnapshotResourceType')

        if m.get('SourceStoragePath') is not None:
            self.source_storage_path = m.get('SourceStoragePath')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

