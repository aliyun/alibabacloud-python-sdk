# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

