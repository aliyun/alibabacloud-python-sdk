# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        file_system_ids: str = None,
    ):
        # The IDs of file systems.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to remove automatic snapshot policies from multiple file systems, separate the file system IDs with commas (,).
        # 
        # This parameter is required.
        self.file_system_ids = file_system_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')

        return self

