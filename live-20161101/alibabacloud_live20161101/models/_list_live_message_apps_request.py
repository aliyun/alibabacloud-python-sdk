# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveMessageAppsRequest(DaraModel):
    def __init__(
        self,
        data_center: str = None,
        next_page_token: int = None,
        sort_type: int = None,
    ):
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The starting page number for the query. If you leave this parameter empty or set this parameter to -1, the query starts from the first page.
        self.next_page_token = next_page_token
        # The sort order based on the creation time. Valid values:
        # 
        # *   1: ascending order
        # *   2: descending order
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
        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

