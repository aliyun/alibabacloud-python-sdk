# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSampleDataByBatchUUidPageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        batch_uuid: str = None,
        current_page: int = None,
        data_value: str = None,
        page_size: int = None,
        reg_id: str = None,
        update_begin_time: int = None,
        update_end_time: int = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Sample batch UUID
        self.batch_uuid = batch_uuid
        # Current page number.
        self.current_page = current_page
        # Content of the list entered in the text box
        self.data_value = data_value
        # Page size, default value is 10
        self.page_size = page_size
        # Region code
        self.reg_id = reg_id
        # Start time
        self.update_begin_time = update_begin_time
        # End time
        self.update_end_time = update_end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.batch_uuid is not None:
            result['batchUuid'] = self.batch_uuid

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.data_value is not None:
            result['dataValue'] = self.data_value

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.update_begin_time is not None:
            result['updateBeginTime'] = self.update_begin_time

        if self.update_end_time is not None:
            result['updateEndTime'] = self.update_end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('batchUuid') is not None:
            self.batch_uuid = m.get('batchUuid')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('dataValue') is not None:
            self.data_value = m.get('dataValue')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('updateBeginTime') is not None:
            self.update_begin_time = m.get('updateBeginTime')

        if m.get('updateEndTime') is not None:
            self.update_end_time = m.get('updateEndTime')

        return self

