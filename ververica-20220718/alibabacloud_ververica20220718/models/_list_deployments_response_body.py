# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ListDeploymentsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.Deployment] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # - When success is true, returns a list of jobs that meet the query conditions;
        # 
        # - When success is false, returns an empty value.
        self.data = data
        # - When success is false, returns a business error code;
        # 
        # - When success is true, returns an empty value.
        self.error_code = error_code
        # - When success is false, returns a business error message;
        # 
        # - When success is true, returns an empty value.
        self.error_message = error_message
        # Static field with a fixed value of 200.
        self.http_code = http_code
        # Pagination parameter: page index, indicating the requested page number.
        self.page_index = page_index
        # Pagination parameter: the number of elements on the requested page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the business request succeeded.
        self.success = success
        # The total number of elements that meet the query conditions.
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
                temp_model = main_models.Deployment()
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

