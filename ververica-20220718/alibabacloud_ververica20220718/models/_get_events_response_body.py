# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class GetEventsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.Event] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # A list of runtime events matching the filter criteria. Returned only when the request is successful (`success` is `true`).
        self.data = data
        # The business error code. Returned only when the request fails (that is, `success` is `false`).
        self.error_code = error_code
        # The business error message. Returned only when the request fails (that is, `success` is `false`).
        self.error_message = error_message
        # The business status code. This field always returns `200`. To confirm the request\\"s success, check the `success` parameter.
        self.http_code = http_code
        # The page number of the returned page.
        self.page_index = page_index
        # The number of entries on this page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the business request was successful.
        self.success = success
        # The total number of entries that match the query.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.Event()
                self.data.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

