# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryMaterialTaskListRequest(DaraModel):
    def __init__(
        self,
        biz_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        status_list: List[str] = None,
        task_type_list: List[str] = None,
    ):
        # The business group ID.
        self.biz_group_id = biz_group_id
        # The number of entries per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The token for the next query. This parameter is empty if no more results exist.
        self.next_token = next_token
        # The field used for sorting.
        self.order_column = order_column
        # The sort type. Valid values: ASC and DESC.
        self.order_type = order_type
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The list of task statuses.
        self.status_list = status_list
        # The list of task types.
        self.task_type_list = task_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_group_id is not None:
            result['BizGroupId'] = self.biz_group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.task_type_list is not None:
            result['TaskTypeList'] = self.task_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroupId') is not None:
            self.biz_group_id = m.get('BizGroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TaskTypeList') is not None:
            self.task_type_list = m.get('TaskTypeList')

        return self

