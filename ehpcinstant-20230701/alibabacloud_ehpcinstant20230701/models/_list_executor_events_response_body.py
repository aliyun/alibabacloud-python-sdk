# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListExecutorEventsResponseBody(DaraModel):
    def __init__(
        self,
        executor_event_list: List[main_models.ListExecutorEventsResponseBodyExecutorEventList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of the running event.
        self.executor_event_list = executor_event_list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.executor_event_list:
            for v1 in self.executor_event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExecutorEventList'] = []
        if self.executor_event_list is not None:
            for k1 in self.executor_event_list:
                result['ExecutorEventList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executor_event_list = []
        if m.get('ExecutorEventList') is not None:
            for k1 in m.get('ExecutorEventList'):
                temp_model = main_models.ListExecutorEventsResponseBodyExecutorEventList()
                self.executor_event_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListExecutorEventsResponseBodyExecutorEventList(DaraModel):
    def __init__(
        self,
        content: str = None,
        executor_id: str = None,
        job_id: str = None,
        level: str = None,
        time: str = None,
    ):
        # The content of the running event.
        self.content = content
        # The ID of the executor. The format is JobId-TaskName-ArrayIndex.
        self.executor_id = executor_id
        # The job ID.
        self.job_id = job_id
        # The level of the running event. Valid values:
        # 
        # *   Normal
        # *   Warning
        # *   Error
        self.level = level
        # The event of the running event.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.level is not None:
            result['Level'] = self.level

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

