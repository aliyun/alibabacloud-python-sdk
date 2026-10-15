# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryRelationListRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status_list: List[str] = None,
        user_id: int = None,
    ):
        # The page number. The default value is 1.
        self.page_num = page_num
        # The number of entries per page. The default value is 20.
        self.page_size = page_size
        # A list of relationship statuses. The value is an enumeration of RelationshipStatusEnum. If you do not specify this parameter, only relationships that are in effect are queried.
        self.status_list = status_list
        # The UID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

