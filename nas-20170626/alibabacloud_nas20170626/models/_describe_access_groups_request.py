# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccessGroupsRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        use_utcdate_time: bool = None,
    ):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        self.access_group_name = access_group_name
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose Apsara File Storage NAS (NAS) file system
        # *   extreme: Extreme NAS file system.
        # *   cpfs: CPFS file system.
        self.file_system_type = file_system_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of permission groups returned per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # Specifies whether to display the creation time of the permission group in UTC.
        # 
        # Valid values:
        # 
        # *   true (default): The time is displayed in UTC.
        # *   false: The time is not displayed in UTC.
        self.use_utcdate_time = use_utcdate_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')

        return self

