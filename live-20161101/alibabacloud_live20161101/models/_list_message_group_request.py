# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMessageGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_num: int = None,
        page_size: int = None,
        sort_type: int = None,
        user_id: str = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The number of the page to return. Default value: 1. Valid values: 1 to 100000.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of message groups to return on each page. Default value: 20.
        # 
        # Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The sort order. Valid values:
        # 
        # *   0: ascending order by time
        # *   1: descending order by time
        self.sort_type = sort_type
        # The ID of the user. Each user has a unique ID in the application. You can specify multiple user IDs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

