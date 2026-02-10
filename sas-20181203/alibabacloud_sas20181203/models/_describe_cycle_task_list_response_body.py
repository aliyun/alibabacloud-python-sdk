# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCycleTaskListResponseBody(DaraModel):
    def __init__(
        self,
        cycle_schedule_response_list: List[main_models.DescribeCycleTaskListResponseBodyCycleScheduleResponseList] = None,
        page_info: main_models.DescribeCycleTaskListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of periodic scan tasks.
        self.cycle_schedule_response_list = cycle_schedule_response_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cycle_schedule_response_list:
            for v1 in self.cycle_schedule_response_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CycleScheduleResponseList'] = []
        if self.cycle_schedule_response_list is not None:
            for k1 in self.cycle_schedule_response_list:
                result['CycleScheduleResponseList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cycle_schedule_response_list = []
        if m.get('CycleScheduleResponseList') is not None:
            for k1 in m.get('CycleScheduleResponseList'):
                temp_model = main_models.DescribeCycleTaskListResponseBodyCycleScheduleResponseList()
                self.cycle_schedule_response_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCycleTaskListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCycleTaskListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
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

class DescribeCycleTaskListResponseBodyCycleScheduleResponseList(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        enable: int = None,
        first_date_str: int = None,
        interval_period: int = None,
        last_task_id: str = None,
        next_start_time_str: int = None,
        param: str = None,
        period_unit: str = None,
        target_end_time: int = None,
        target_start_time: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Indicates whether the configuration for the task interval was enabled. Valid values:
        # 
        # *   **1**: enabled.
        # *   **0**: disabled.
        self.enable = enable
        # The time when the task first started.
        self.first_date_str = first_date_str
        # The interval between which two consecutive tasks are run.
        self.interval_period = interval_period
        # The ID of the last task.
        self.last_task_id = last_task_id
        # The time when the next task starts. The value is a UNIX timestamp. Unit: milliseconds.
        self.next_start_time_str = next_start_time_str
        # The extended information.
        self.param = param
        # The unit of the scan interval. Valid values:
        # 
        # *   **day**
        # *   **hour**
        self.period_unit = period_unit
        # The end time of the task. The time must be a time frame.
        self.target_end_time = target_end_time
        # The start time of the task. The start time must be a time frame.
        self.target_start_time = target_start_time
        # The name of the task.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.first_date_str is not None:
            result['FirstDateStr'] = self.first_date_str

        if self.interval_period is not None:
            result['IntervalPeriod'] = self.interval_period

        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id

        if self.next_start_time_str is not None:
            result['NextStartTimeStr'] = self.next_start_time_str

        if self.param is not None:
            result['Param'] = self.param

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.target_end_time is not None:
            result['TargetEndTime'] = self.target_end_time

        if self.target_start_time is not None:
            result['TargetStartTime'] = self.target_start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FirstDateStr') is not None:
            self.first_date_str = m.get('FirstDateStr')

        if m.get('IntervalPeriod') is not None:
            self.interval_period = m.get('IntervalPeriod')

        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')

        if m.get('NextStartTimeStr') is not None:
            self.next_start_time_str = m.get('NextStartTimeStr')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('TargetEndTime') is not None:
            self.target_end_time = m.get('TargetEndTime')

        if m.get('TargetStartTime') is not None:
            self.target_start_time = m.get('TargetStartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

