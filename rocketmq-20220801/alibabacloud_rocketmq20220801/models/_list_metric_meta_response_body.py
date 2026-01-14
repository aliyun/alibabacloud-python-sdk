# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListMetricMetaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListMetricMetaResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code
        self.code = code
        # Return result
        self.data = data
        # Dynamic error code
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListMetricMetaResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListMetricMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListMetricMetaResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Paged data
        self.list = list
        # Current page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Total record count
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListMetricMetaResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMetricMetaResponseBodyDataList(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        metric_name: str = None,
    ):
        # Monitoring item tag
        self.category = category
        # Monitoring item description
        self.description = description
        # Monitoring item name
        self.metric_name = metric_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        return self

