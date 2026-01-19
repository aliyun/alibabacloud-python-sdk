# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventResultListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        http_status_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeEventResultListResponseBodyResultObject] = None,
        success: bool = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Status code.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # HTTP status code
        self.http_status_code = http_status_code
        # Error details
        self.message = message
        # Page size, default value is 10
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Whether the query was successful.
        self.success = success
        # Total number of items.
        self.total_item = total_item
        # Total number of pages
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeEventResultListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeEventResultListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        pass_num: int = None,
        pending_num: int = None,
        reject_num: int = None,
        total_num: int = None,
    ):
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Number of passed checks.
        self.pass_num = pass_num
        # Number of pending items.
        self.pending_num = pending_num
        # Number of rejected approvals.
        self.reject_num = reject_num
        # Total number of items.
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.pass_num is not None:
            result['passNum'] = self.pass_num

        if self.pending_num is not None:
            result['pendingNum'] = self.pending_num

        if self.reject_num is not None:
            result['rejectNum'] = self.reject_num

        if self.total_num is not None:
            result['totalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('passNum') is not None:
            self.pass_num = m.get('passNum')

        if m.get('pendingNum') is not None:
            self.pending_num = m.get('pendingNum')

        if m.get('rejectNum') is not None:
            self.reject_num = m.get('rejectNum')

        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')

        return self

