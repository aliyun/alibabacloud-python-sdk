# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeListPocResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: str = None,
        http_status_code: str = None,
        message: str = None,
        page_size: str = None,
        request_id: str = None,
        result_object: bool = None,
        total_item: str = None,
        total_page: str = None,
    ):
        # Status code.
        self.code = code
        # Current page.
        self.current_page = current_page
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result_object = result_object
        # Total number of items returned.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

