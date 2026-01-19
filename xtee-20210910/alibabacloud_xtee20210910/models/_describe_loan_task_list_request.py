# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoanTaskListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        batch_no: str = None,
        current_page: str = None,
        monitor_status: str = None,
        page_size: str = None,
        reg_id: str = None,
    ):
        # Set the language type for request and response messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Import batch number.
        self.batch_no = batch_no
        # Current page number. Default is: 1.
        self.current_page = current_page
        # Task status.
        self.monitor_status = monitor_status
        # Page size, default value is 10.
        self.page_size = page_size
        # Region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.batch_no is not None:
            result['batchNo'] = self.batch_no

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.monitor_status is not None:
            result['monitorStatus'] = self.monitor_status

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('batchNo') is not None:
            self.batch_no = m.get('batchNo')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('monitorStatus') is not None:
            self.monitor_status = m.get('monitorStatus')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

