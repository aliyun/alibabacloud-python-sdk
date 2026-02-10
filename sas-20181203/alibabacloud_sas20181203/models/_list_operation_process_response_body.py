# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOperationProcessResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListOperationProcessResponseBodyPageInfo = None,
        processes: List[main_models.ListOperationProcessResponseBodyProcesses] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The information about the operation tasks.
        self.processes = processes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.processes:
            for v1 in self.processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Processes'] = []
        if self.processes is not None:
            for k1 in self.processes:
                result['Processes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListOperationProcessResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.ListOperationProcessResponseBodyProcesses()
                self.processes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOperationProcessResponseBodyProcesses(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        detail_task_ready_count: int = None,
        detail_task_total_count: int = None,
        end_time: int = None,
        finish_count: int = None,
        start_time: int = None,
        status_code: int = None,
        task_id: str = None,
        task_source: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        # The time when the task was created. Unit: milliseconds.
        self.create_time = create_time
        # Number of completed subtasks
        self.detail_task_ready_count = detail_task_ready_count
        # Total number of subtasks.
        self.detail_task_total_count = detail_task_total_count
        # The end time of the task. Unit: milliseconds.
        self.end_time = end_time
        # The number of tasks that are complete.
        self.finish_count = finish_count
        # The start time of the task. Unit: milliseconds.
        self.start_time = start_time
        # The task status code. Valid values:
        # 
        # *   0: not started.
        # *   1: running.
        # *   2: complete.
        # *   3: times out.
        self.status_code = status_code
        # The ID of the operation task.
        self.task_id = task_id
        # Task source. Values: 
        # - **YAO_CHI**: YaoChi.
        self.task_source = task_source
        # The task type. Valid values:
        # 
        # *   CHECK_ALL: full check.
        # *   CHECK_POLICY: policy-based check for which check items are configured.
        # *   CHECK_SCHEDULE: scheduled check.
        # *   CHECK_ITEM: specific check item-based check.
        # *   CHECK_INSTANCE: specific check item-based check on specific instances.
        self.task_type = task_type
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail_task_ready_count is not None:
            result['DetailTaskReadyCount'] = self.detail_task_ready_count

        if self.detail_task_total_count is not None:
            result['DetailTaskTotalCount'] = self.detail_task_total_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_source is not None:
            result['TaskSource'] = self.task_source

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetailTaskReadyCount') is not None:
            self.detail_task_ready_count = m.get('DetailTaskReadyCount')

        if m.get('DetailTaskTotalCount') is not None:
            self.detail_task_total_count = m.get('DetailTaskTotalCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskSource') is not None:
            self.task_source = m.get('TaskSource')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationProcessResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

