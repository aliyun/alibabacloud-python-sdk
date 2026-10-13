# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDirQuotasRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
    ):
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The page number.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of directories on each page. Default value: 10.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size
        # The absolute path of the directory in the file system.
        # 
        # If this parameter is left empty, all directories that have quotas configured in the file system are returned.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

