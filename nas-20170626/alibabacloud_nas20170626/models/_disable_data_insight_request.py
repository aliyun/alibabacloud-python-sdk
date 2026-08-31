# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableDataInsightRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
    ):
        # The file system ID.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, for example, bmcpfs-0015\\*\\*\\*\\*.
        # > Only CPFS for Lingjun file systems are supported.
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

