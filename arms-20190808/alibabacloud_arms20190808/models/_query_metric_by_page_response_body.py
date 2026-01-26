# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class QueryMetricByPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryMetricByPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned for the request. Valid values:
        # 
        # *   2XX: The request was successful.
        # *   3XX: A redirection message was returned.
        # *   4XX: The request was invalid.
        # *   5XX: A server error occurred.
        self.code = code
        # The information about the array object.
        self.data = data
        # The error message returned if the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   `true`: The call was successful.
        # *   `false`: The call failed.
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryMetricByPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMetricByPageResponseBodyData(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        items: List[Dict[str, Any]] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Whether the paging query ends.
        # 
        # true: end.
        # false: Need to continue pagination (continue to query after CurrentPage+1).
        self.completed = completed
        # The data entries returned.
        self.items = items
        # The page number of the returned page.
        self.page = page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed is not None:
            result['Completed'] = self.completed

        if self.items is not None:
            result['Items'] = self.items

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

