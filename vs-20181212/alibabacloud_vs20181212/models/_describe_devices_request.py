# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDevicesRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        dsn: str = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        include_directory: bool = None,
        include_stats: bool = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        sort_direction: str = None,
        status: str = None,
        type: str = None,
        vendor: str = None,
    ):
        # The ID of the directory to which the device belongs.
        self.directory_id = directory_id
        # The serial number of the device. The value must be unique.
        self.dsn = dsn
        # You can query by device national standard ID.
        self.gb_id = gb_id
        # Query by device Space ID.
        self.group_id = group_id
        # The device ID.
        # 
        # > Specify multiple IDs. Separate them with commas (,).
        self.id = id
        # Specifies whether to return directory information. Default value: false.
        self.include_directory = include_directory
        # Specifies whether to return stream statistics. Default value: false.
        self.include_stats = include_stats
        # The device name.
        # 
        # > Specify multiple names. Separate them with commas (,).
        self.name = name
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The ID of the parent device.
        self.parent_id = parent_id
        # The field by which to sort the results. Valid value:
        # 
        # > id (default)
        self.sort_by = sort_by
        # The sort order. Valid values:
        # 
        # - asc (ascending) (default)
        # 
        # - desc (descending)
        self.sort_direction = sort_direction
        # Query devices by status.
        self.status = status
        # The device type. Valid values:
        # 
        # - ipc (camera)
        # 
        # - platform
        # 
        # - ied (intelligent edge device)
        self.type = type
        # Query by device manufacturer.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.dsn is not None:
            result['Dsn'] = self.dsn

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory

        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')

        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

