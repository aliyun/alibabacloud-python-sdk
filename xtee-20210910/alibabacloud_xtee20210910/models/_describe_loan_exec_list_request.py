# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoanExecListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        batch_no: str = None,
        current_page: str = None,
        monitor_obj: str = None,
        monitor_status: str = None,
        page_size: str = None,
        reg_id: str = None,
    ):
        # The language type for sending requests and receiving responses. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The import batch number.
        self.batch_no = batch_no
        # The current page number.
        self.current_page = current_page
        # The monitoring metric data.
        self.monitor_obj = monitor_obj
        # The status.
        self.monitor_status = monitor_status
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID.
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

        if self.monitor_obj is not None:
            result['monitorObj'] = self.monitor_obj

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

        if m.get('monitorObj') is not None:
            self.monitor_obj = m.get('monitorObj')

        if m.get('monitorStatus') is not None:
            self.monitor_status = m.get('monitorStatus')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

