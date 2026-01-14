# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyTempStorageLeaseRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        size_in_bytes: int = None,
    ):
        # The file name, including the file extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The size of the file, in bytes.
        # 
        # This parameter is required.
        self.size_in_bytes = size_in_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        return self

