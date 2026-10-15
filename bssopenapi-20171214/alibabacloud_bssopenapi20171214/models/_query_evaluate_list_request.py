# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryEvaluateListRequest(DaraModel):
    def __init__(
        self,
        bill_cycle: str = None,
        biz_type_list: List[str] = None,
        end_amount: int = None,
        end_biz_time: str = None,
        end_search_time: str = None,
        out_biz_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_type: int = None,
        start_amount: int = None,
        start_biz_time: str = None,
        start_search_time: str = None,
        type: int = None,
    ):
        # The billing cycle.
        self.bill_cycle = bill_cycle
        # The list of invoicing entities to which the invoiceable objects belong.
        self.biz_type_list = biz_type_list
        # The maximum amount for the query.
        self.end_amount = end_amount
        # The end of the time range to query based on the successful payment time. The format is yyyy-mm-dd hh:mm:ss.
        self.end_biz_time = end_biz_time
        # The end of the time range to query.
        self.end_search_time = end_search_time
        # The order ID, bill ID, or contract ID.
        self.out_biz_id = out_biz_id
        self.owner_id = owner_id
        # The page number.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The sorting type. Valid values:
        # 
        # - 1: sorts the results by ID in descending order.
        # 
        # - 2: sorts the results by type in descending order, and then by ID in descending order.
        # 
        # - 3: sorts the results by type in ascending order, and then by ID in descending order.
        self.sort_type = sort_type
        # The minimum amount for the query.
        self.start_amount = start_amount
        # The beginning of the time range to query based on the successful payment time. The format is yyyy-mm-dd hh:mm:ss.
        self.start_biz_time = start_biz_time
        # The start of the time range to query.
        self.start_search_time = start_search_time
        # The type. Valid values:
        # 
        # - 1: queries objects with a negative invoiceable amount.
        # 
        # - 2: queries objects with a positive invoiceable amount.
        # 
        # - 3: queries all objects with a non-zero invoiceable amount.
        # 
        # - 4: queries objects with an invoiced amount greater than 0.
        # 
        # > If you leave this parameter empty, all objects are queried.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle

        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list

        if self.end_amount is not None:
            result['EndAmount'] = self.end_amount

        if self.end_biz_time is not None:
            result['EndBizTime'] = self.end_biz_time

        if self.end_search_time is not None:
            result['EndSearchTime'] = self.end_search_time

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.start_amount is not None:
            result['StartAmount'] = self.start_amount

        if self.start_biz_time is not None:
            result['StartBizTime'] = self.start_biz_time

        if self.start_search_time is not None:
            result['StartSearchTime'] = self.start_search_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')

        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')

        if m.get('EndAmount') is not None:
            self.end_amount = m.get('EndAmount')

        if m.get('EndBizTime') is not None:
            self.end_biz_time = m.get('EndBizTime')

        if m.get('EndSearchTime') is not None:
            self.end_search_time = m.get('EndSearchTime')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('StartAmount') is not None:
            self.start_amount = m.get('StartAmount')

        if m.get('StartBizTime') is not None:
            self.start_biz_time = m.get('StartBizTime')

        if m.get('StartSearchTime') is not None:
            self.start_search_time = m.get('StartSearchTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

