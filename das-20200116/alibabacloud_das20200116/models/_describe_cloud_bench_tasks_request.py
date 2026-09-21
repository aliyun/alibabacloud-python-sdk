# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudBenchTasksRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
        status: str = None,
        task_type: str = None,
    ):
        # The end time of the query task. Specify the value as a UNIX timestamp. Unit: milliseconds.
        # >The end time of the query task must be later than the start time.
        self.end_time = end_time
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. Default value: 1.
        self.page_no = page_no
        # The maximum number of records per page. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. Default value: 10.
        self.page_size = page_size
        # The start time of the query task. Specify the value as a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The running status of the task. Valid values:
        # 
        # - **SUCCESS**: Successful.
        # - **IGNORED**: Ignored.
        # - **RUNNING**: Running.
        # - **EXCEPTION**: Exception.
        self.status = status
        # The type of the stress testing task. Valid values:
        # - **pressure test** (default): intelligent stress testing. Traffic captured from the target instance is replayed on the destination instance at the maximum speed supported by the destination instance specifications.
        # - **smart pressure test**: generated stress testing. By analyzing and learning from traffic captured from the target instance within a short period, traffic that is consistent with the business model and traffic distribution of the original traffic is generated for continuous stress testing. This reduces the time required to collect data from the target instance and lowers storage costs and performance overhead.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

