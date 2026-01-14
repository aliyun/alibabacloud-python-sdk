# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataServiceListRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # Data service name.
        self.name = name
        # Page number. Default value: **1**.
        self.page_no = page_no
        # Number of items per page in a paginated query:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

