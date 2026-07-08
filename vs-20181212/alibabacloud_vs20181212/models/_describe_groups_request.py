# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupsRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        in_protocol: str = None,
        include_stats: bool = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
        sort_by: str = None,
        sort_direction: str = None,
        status: str = None,
    ):
        # The space ID.
        self.id = id
        # Ingest protocol used by the group. Valid values:
        # 
        # - gb28181
        # 
        # - rtmp
        self.in_protocol = in_protocol
        # Whether to return device statistics for the group. Default: false.
        self.include_stats = include_stats
        # Space name.
        self.name = name
        self.owner_id = owner_id
        # Page number. Default: 1.
        self.page_num = page_num
        # Number of entries per page.
        self.page_size = page_size
        # The service region where the group is located.
        self.region = region
        # Field to sort by. Valid values:
        # 
        # - Id (default)
        self.sort_by = sort_by
        # Sort order. Valid values:
        # 
        # - asc (ascending, default)
        # 
        # - desc (descending)
        self.sort_direction = sort_direction
        # Group status. Valid values:
        # 
        # - on (enabled)
        # 
        # - off (disabled)
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol

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

        if self.region is not None:
            result['Region'] = self.region

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')

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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

