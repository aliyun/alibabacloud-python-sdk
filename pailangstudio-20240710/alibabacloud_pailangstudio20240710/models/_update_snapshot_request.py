# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSnapshotRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        snapshot_name: str = None,
        workspace_id: str = None,
    ):
        # The snapshot description.
        self.description = description
        # The snapshot name. The format requirements are as follows:
        # * It can contain only letters, digits, and underscores (_).
        # * It must start with a letter.
        # * It must be 1 to 256 characters in length.
        self.snapshot_name = snapshot_name
        # The workspace ID. For information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

