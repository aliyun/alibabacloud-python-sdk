# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListServiceApplyRequest(DaraModel):
    def __init__(
        self,
        apply_type: List[str] = None,
        end_date: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: int = None,
        start_date: int = None,
        status: str = None,
    ):
        self.apply_type = apply_type
        self.end_date = end_date
        self.page_num = page_num
        self.page_size = page_size
        self.product_code = product_code
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_type is not None:
            result['applyType'] = self.apply_type

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyType') is not None:
            self.apply_type = m.get('applyType')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

