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
        # The data center. The value must be the same as the data center specified in [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html). Valid values: cn-shanghai (China (Shanghai)) and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The starting position of the query page. If this parameter is left empty or set to -1, the first page is returned by default.
        self.next_page_token = next_page_token
        # The sort type by creation time. Valid values:
        # - 1: ascending order.
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

