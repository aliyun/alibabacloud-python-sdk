# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeEventCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeEventCountResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error details
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned object
        self.result_object = result_object
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeEventCountResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeEventCountResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        limit: bool = None,
        max_total_item: int = None,
        total_item: int = None,
    ):
        # Whether it exceeds the maximum number
        self.limit = limit
        # Maximum creation count
        self.max_total_item = max_total_item
        # Total count
        self.total_item = total_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.max_total_item is not None:
            result['maxTotalItem'] = self.max_total_item

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('maxTotalItem') is not None:
            self.max_total_item = m.get('maxTotalItem')

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        return self

