# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSyntheticTaskListResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.GetSyntheticTaskListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The query results.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.GetSyntheticTaskListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSyntheticTaskListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        has_next_page: str = None,
        has_previous_page: bool = None,
        is_first_page: bool = None,
        is_last_page: bool = None,
        list: List[main_models.GetSyntheticTaskListResponseBodyPageInfoList] = None,
        navigate_first_page: str = None,
        navigate_last_page: str = None,
        navigate_page_nums: str = None,
        next_page: str = None,
        pages: str = None,
        prepage: str = None,
        size: int = None,
        total: int = None,
    ):
        # Indicates whether the current page is followed by a page.
        self.has_next_page = has_next_page
        # Indicates whether a previous page exists.
        self.has_previous_page = has_previous_page
        # Indicates whether the page is the first page.
        self.is_first_page = is_first_page
        # Indicates whether the page is the last page.
        self.is_last_page = is_last_page
        # The task information.
        self.list = list
        # The first page on the navigation bar.
        self.navigate_first_page = navigate_first_page
        # The last page on the navigation bar.
        self.navigate_last_page = navigate_last_page
        # All navigation page numbers.
        self.navigate_page_nums = navigate_page_nums
        # The next page.
        self.next_page = next_page
        # The total number of pages returned.
        self.pages = pages
        # The previous page.
        self.prepage = prepage
        # The number of entries per page.
        self.size = size
        # The total number of entries returned.
        self.total = total

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
        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page

        if self.has_previous_page is not None:
            result['HasPreviousPage'] = self.has_previous_page

        if self.is_first_page is not None:
            result['IsFirstPage'] = self.is_first_page

        if self.is_last_page is not None:
            result['IsLastPage'] = self.is_last_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.navigate_first_page is not None:
            result['NavigateFirstPage'] = self.navigate_first_page

        if self.navigate_last_page is not None:
            result['NavigateLastPage'] = self.navigate_last_page

        if self.navigate_page_nums is not None:
            result['NavigatePageNums'] = self.navigate_page_nums

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.prepage is not None:
            result['Prepage'] = self.prepage

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')

        if m.get('HasPreviousPage') is not None:
            self.has_previous_page = m.get('HasPreviousPage')

        if m.get('IsFirstPage') is not None:
            self.is_first_page = m.get('IsFirstPage')

        if m.get('IsLastPage') is not None:
            self.is_last_page = m.get('IsLastPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetSyntheticTaskListResponseBodyPageInfoList()
                self.list.append(temp_model.from_map(k1))

        if m.get('NavigateFirstPage') is not None:
            self.navigate_first_page = m.get('NavigateFirstPage')

        if m.get('NavigateLastPage') is not None:
            self.navigate_last_page = m.get('NavigateLastPage')

        if m.get('NavigatePageNums') is not None:
            self.navigate_page_nums = m.get('NavigatePageNums')

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('Prepage') is not None:
            self.prepage = m.get('Prepage')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetSyntheticTaskListResponseBodyPageInfoList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        monitor_number: int = None,
        task_id: str = None,
        task_name: str = None,
        task_status: str = None,
        task_type: int = None,
        task_type_name: str = None,
        url: str = None,
        usable: float = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The number of detection points.
        self.monitor_number = monitor_number
        # The ID of the synthetic monitoring task.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The status of the task. Valid values:
        # 
        # *   **0**: The task is stopped.
        # *   **1**: The task is started.
        # *   **9**: The task is ended.
        self.task_status = task_status
        # The type of the task. Valid values:
        # 
        # 1.  3: web page performance - IE
        # 2.  34: web page performance - Chrome
        # 3.  0: network quality
        # 4.  40: file download
        # 5.  7: API performance
        self.task_type = task_type
        # The name of the task type.
        self.task_type_name = task_type_name
        # The URL for synthetic monitoring.
        self.url = url
        # The availability. Only the data of the last day is counted. If no data is available for the last day, an empty value is returned.
        self.usable = usable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.monitor_number is not None:
            result['MonitorNumber'] = self.monitor_number

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_name is not None:
            result['TaskTypeName'] = self.task_type_name

        if self.url is not None:
            result['Url'] = self.url

        if self.usable is not None:
            result['Usable'] = self.usable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MonitorNumber') is not None:
            self.monitor_number = m.get('MonitorNumber')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeName') is not None:
            self.task_type_name = m.get('TaskTypeName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Usable') is not None:
            self.usable = m.get('Usable')

        return self

