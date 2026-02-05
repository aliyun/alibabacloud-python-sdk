# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListYunQiTaskByUidRequest(DaraModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        free_order_apply_codes: List[str] = None,
        free_order_apply_ids: List[int] = None,
        order_ids: List[int] = None,
        page_num: int = None,
        page_size: int = None,
        status_list: List[str] = None,
    ):
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.free_order_apply_codes = free_order_apply_codes
        self.free_order_apply_ids = free_order_apply_ids
        self.order_ids = order_ids
        self.page_num = page_num
        self.page_size = page_size
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start

        if self.free_order_apply_codes is not None:
            result['freeOrderApplyCodes'] = self.free_order_apply_codes

        if self.free_order_apply_ids is not None:
            result['freeOrderApplyIds'] = self.free_order_apply_ids

        if self.order_ids is not None:
            result['orderIds'] = self.order_ids

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status_list is not None:
            result['statusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')

        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')

        if m.get('freeOrderApplyCodes') is not None:
            self.free_order_apply_codes = m.get('freeOrderApplyCodes')

        if m.get('freeOrderApplyIds') is not None:
            self.free_order_apply_ids = m.get('freeOrderApplyIds')

        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')

        return self

