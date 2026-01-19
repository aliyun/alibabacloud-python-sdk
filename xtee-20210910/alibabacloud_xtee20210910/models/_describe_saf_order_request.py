# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSafOrderRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: int = None,
        end_date: str = None,
        exact_product_code: str = None,
        page_size: int = None,
        reg_id: str = None,
        start_date: str = None,
    ):
        # Set the language type for request and response, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Current page number.
        self.current_page = current_page
        # End date.
        self.end_date = end_date
        # Product code.
        self.exact_product_code = exact_product_code
        # Page size, default value is 10.
        self.page_size = page_size
        # Region code.
        self.reg_id = reg_id
        # Start time.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.exact_product_code is not None:
            result['exactProductCode'] = self.exact_product_code

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.start_date is not None:
            result['startDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('exactProductCode') is not None:
            self.exact_product_code = m.get('exactProductCode')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        return self

