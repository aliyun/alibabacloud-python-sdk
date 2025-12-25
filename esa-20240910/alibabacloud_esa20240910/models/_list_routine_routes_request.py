# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutineRoutesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        routine_name: str = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.page_size = page_size
        # The function name.
        # 
        # This parameter is required.
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        return self

