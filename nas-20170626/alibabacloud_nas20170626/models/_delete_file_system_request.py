# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFileSystemRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The ID of the file system that you want to delete.
        # - General-purpose NAS: 31a8e4\\*\\*\\*\\*.
        # - Extreme NAS: The ID must start with `extreme-`, such as extreme-0015\\*\\*\\*\\*.
        # - Cloud Parallel File Storage (CPFS): The ID must start with `cpfs-`, such as cpfs-00cb6fa094ca\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

