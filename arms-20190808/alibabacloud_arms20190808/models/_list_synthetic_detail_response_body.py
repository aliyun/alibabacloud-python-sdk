# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListSyntheticDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListSyntheticDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The error message returned.
        self.message = message
        # Id of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListSyntheticDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSyntheticDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        page: int = None,
        page_size: int = None,
        task_create_time: int = None,
        total: int = None,
    ):
        # The list of results.
        self.items = items
        # The page number.
        self.page = page
        # The number of entries returned on each page.
        self.page_size = page_size
        # A reserved field.
        self.task_create_time = task_create_time
        # The total number of entries.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_create_time is not None:
            result['TaskCreateTime'] = self.task_create_time

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskCreateTime') is not None:
            self.task_create_time = m.get('TaskCreateTime')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

