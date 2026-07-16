# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDirectoriesRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        no_pagination: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        sort_direction: str = None,
    ):
        # ID of the group to which the directory belongs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Disable paging. Default is false.
        self.no_pagination = no_pagination
        self.owner_id = owner_id
        # Page number. Default is 1.
        self.page_num = page_num
        # Page size. Default is 20.
        self.page_size = page_size
        # Query by parent directory ID.
        self.parent_id = parent_id
        # Sort by the specified field. Default is by ID.
        self.sort_by = sort_by
        # Sort order. Default is ascending. Values:
        # 
        # - asc (ascending)
        # 
        # - desc (descending)
        self.sort_direction = sort_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.no_pagination is not None:
            result['NoPagination'] = self.no_pagination

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NoPagination') is not None:
            self.no_pagination = m.get('NoPagination')

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

        return self

