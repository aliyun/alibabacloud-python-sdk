# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ListAutopilotTuningHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAutopilotTuningHistoriesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The tuning history list result.
        self.data = data
        # When success is false, this value is not empty and indicates the business error code. When success is true, this value is empty.
        self.error_code = error_code
        # When success is false, this value is not empty and indicates the business error message. When success is true, this value is empty.
        self.error_message = error_message
        # The business status code, which is always 200. Use success to determine whether the business request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the business request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListAutopilotTuningHistoriesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListAutopilotTuningHistoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        tuning_histories: List[main_models.TuningHistory] = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count
        # The list of tuning history records.
        self.tuning_histories = tuning_histories

    def validate(self):
        if self.tuning_histories:
            for v1 in self.tuning_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        result['tuningHistories'] = []
        if self.tuning_histories is not None:
            for k1 in self.tuning_histories:
                result['tuningHistories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        self.tuning_histories = []
        if m.get('tuningHistories') is not None:
            for k1 in m.get('tuningHistories'):
                temp_model = main_models.TuningHistory()
                self.tuning_histories.append(temp_model.from_map(k1))

        return self

