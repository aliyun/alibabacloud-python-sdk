# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The file system type.
        # 
        # Valid values:
        # - all: all types.
        # - standard (default): General-purpose NAS.
        # - extreme: Extreme NAS.
        # - cpfs: CPFS.
        self.file_system_type = file_system_type
        # The page number of the list.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of regions on each page during a paged query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

