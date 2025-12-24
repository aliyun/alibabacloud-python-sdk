# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLiveMessageGroupByPageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_center: str = None,
        group_status: int = None,
        page_number: int = None,
        page_size: int = None,
        sort_type: int = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The status of the groups to query. Default value: 0. Valid values:
        # 
        # *   0: all groups
        # *   1: existing groups
        # *   2: deleted groups
        self.group_status = group_status
        # The page number. Valid values: [1,10000].
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:[1,50].
        # 
        # Default value: 20.
        self.page_size = page_size
        # The sort order based on the time when the groups were created. Valid values:
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.group_status is not None:
            result['GroupStatus'] = self.group_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

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

        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

