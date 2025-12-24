# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMessageAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        page_num: int = None,
        page_size: int = None,
        sort_type: int = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The name of the interactive messaging application.
        self.app_name = app_name
        # The number of the page to return. Default value: 1. Valid values: 1 to 100000.
        self.page_num = page_num
        # The number of applications to return on each page. Default value: 20. Valid values: 1 to 50.
        self.page_size = page_size
        # The sort order. Valid values:
        # 
        # *   0: ascending order by time
        # *   1: descending order by time
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

