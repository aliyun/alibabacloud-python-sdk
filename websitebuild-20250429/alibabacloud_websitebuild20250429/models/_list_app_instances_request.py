# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppInstancesRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        end_time_begin: str = None,
        end_time_end: str = None,
        extend: str = None,
        max_results: int = None,
        next_token: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        query: str = None,
        status_list: List[str] = None,
    ):
        self.biz_id = biz_id
        self.end_time_begin = end_time_begin
        self.end_time_end = end_time_end
        self.extend = extend
        self.max_results = max_results
        self.next_token = next_token
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size
        self.query = query
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.end_time_begin is not None:
            result['EndTimeBegin'] = self.end_time_begin

        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end

        if self.extend is not None:
            result['Extend'] = self.extend

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

        if self.query is not None:
            result['Query'] = self.query

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('EndTimeBegin') is not None:
            self.end_time_begin = m.get('EndTimeBegin')

        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

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

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

