# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrawlerRunsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCrawlerRunsResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCrawlerRunsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCrawlerRunsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        crawler_runs: List[main_models.ListCrawlerRunsResponseBodyPagingInfoCrawlerRuns] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.crawler_runs = crawler_runs
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.crawler_runs:
            for v1 in self.crawler_runs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrawlerRuns'] = []
        if self.crawler_runs is not None:
            for k1 in self.crawler_runs:
                result['CrawlerRuns'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crawler_runs = []
        if m.get('CrawlerRuns') is not None:
            for k1 in m.get('CrawlerRuns'):
                temp_model = main_models.ListCrawlerRunsResponseBodyPagingInfoCrawlerRuns()
                self.crawler_runs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrawlerRunsResponseBodyPagingInfoCrawlerRuns(DaraModel):
    def __init__(
        self,
        duration: float = None,
        finished_time: int = None,
        started_time: int = None,
        status: str = None,
        task_instance_id: int = None,
        total_table_count: int = None,
    ):
        self.duration = duration
        self.finished_time = finished_time
        self.started_time = started_time
        self.status = status
        self.task_instance_id = task_instance_id
        self.total_table_count = total_table_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        if self.total_table_count is not None:
            result['TotalTableCount'] = self.total_table_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        if m.get('TotalTableCount') is not None:
            self.total_table_count = m.get('TotalTableCount')

        return self

