# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOrganizationMembersRequest(DaraModel):
    def __init__(
        self,
        has_seat: bool = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # Specifies whether to filter by seat assignment.
        self.has_seat = has_seat
        # Fuzzy filter by member name. Matches accountName or email and is case-insensitive.
        self.name = name
        # The page number, starting from 1. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # Filters by member status, such as ACTIVE or FROZEN. Set to null to disable filtering.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_seat is not None:
            result['HasSeat'] = self.has_seat

        if self.name is not None:
            result['Name'] = self.name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasSeat') is not None:
            self.has_seat = m.get('HasSeat')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

