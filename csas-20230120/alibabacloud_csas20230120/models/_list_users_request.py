# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department: str = None,
        fuzzy_username: str = None,
        page_size: int = None,
        precise_username: str = None,
        sase_user_ids: List[str] = None,
        status: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.department = department
        self.fuzzy_username = fuzzy_username
        # This parameter is required.
        self.page_size = page_size
        self.precise_username = precise_username
        self.sase_user_ids = sase_user_ids
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.fuzzy_username is not None:
            result['FuzzyUsername'] = self.fuzzy_username

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.precise_username is not None:
            result['PreciseUsername'] = self.precise_username

        if self.sase_user_ids is not None:
            result['SaseUserIds'] = self.sase_user_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('FuzzyUsername') is not None:
            self.fuzzy_username = m.get('FuzzyUsername')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PreciseUsername') is not None:
            self.precise_username = m.get('PreciseUsername')

        if m.get('SaseUserIds') is not None:
            self.sase_user_ids = m.get('SaseUserIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

