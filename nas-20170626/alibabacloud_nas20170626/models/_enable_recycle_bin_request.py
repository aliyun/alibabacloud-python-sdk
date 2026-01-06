# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableRecycleBinRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        reserved_days: int = None,
    ):
        # The ID of the file system for which you want to enable the recycle bin feature.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # Valid values: 1 to 180.
        # 
        # Default value: 3.
        self.reserved_days = reserved_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')

        return self

