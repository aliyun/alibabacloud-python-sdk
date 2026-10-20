# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCalendarsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
    ):
        # The name of the scheduling calendar. Partial match is supported.
        self.name = name
        # The account ID of the owner. Exact match is supported.
        self.owner = owner
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of items per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The workspace ID. Queries the calendars applicable to this workspace, including those applicable to all workspaces. If this parameter is not specified, the calendars of the current tenant are queried.
        self.project_id = project_id
        # The sorting rule. The format is "Field Direction", separated by a space.
        # 
        # - Field: ModifyTime, Name, or Id.
        # - Direction: Asc for ascending order, or Desc for descending order. If this parameter is not specified, Asc is used.
        # 
        # Default value: ModifyTime Desc.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

