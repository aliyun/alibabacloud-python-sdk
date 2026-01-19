# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeOperationLogPageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeOperationLogPageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeOperationLogPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeOperationLogPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        gmt_create: int = None,
        new_content: str = None,
        old_content: str = None,
        operation_summary: str = None,
        operation_type: str = None,
        user_name: str = None,
    ):
        # Client IP.
        self.client_ip = client_ip
        # Creation time.
        self.gmt_create = gmt_create
        # Content after operation
        self.new_content = new_content
        # Content before operation
        self.old_content = old_content
        # Operation summary
        self.operation_summary = operation_summary
        # Operation type.
        self.operation_type = operation_type
        # Operator
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.new_content is not None:
            result['newContent'] = self.new_content

        if self.old_content is not None:
            result['oldContent'] = self.old_content

        if self.operation_summary is not None:
            result['operationSummary'] = self.operation_summary

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('newContent') is not None:
            self.new_content = m.get('newContent')

        if m.get('oldContent') is not None:
            self.old_content = m.get('oldContent')

        if m.get('operationSummary') is not None:
            self.operation_summary = m.get('operationSummary')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

