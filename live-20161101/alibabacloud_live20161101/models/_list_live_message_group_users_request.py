# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveMessageGroupUsersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_center: str = None,
        group_id: str = None,
        next_page_token: int = None,
        page_size: int = None,
        sort_type: int = None,
    ):
        # The ID of the live interactive application to query.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. This value must be the same as the data center specified in [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html). Valid values: cn-shanghai (Shanghai) and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The group ID of the group to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The start position of the query page. If this parameter is left empty, the first page is returned by default.
        self.next_page_token = next_page_token
        # The number of users to display per page. Valid values: **10 to 50**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The sort order. Users are sorted by the time they joined the group. Valid values:
        # 
        # - 1: ascending order.
        # 
        # - 2: descending order.
        # 
        # This parameter is required.
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

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

