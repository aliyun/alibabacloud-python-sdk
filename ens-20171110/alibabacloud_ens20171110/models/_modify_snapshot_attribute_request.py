# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySnapshotAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
    ):
        # The description of the snapshot. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # The display name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain digits, half-width colons (:), underscores (_), and hyphens (-). To prevent name conflicts with automatic snapshots, the name cannot start with **auto**.
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        return self

