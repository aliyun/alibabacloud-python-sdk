# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAsyncTasksRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        size: int = None,
        task_code: str = None,
        task_name: str = None,
        task_status: int = None,
        task_status_list: List[int] = None,
        task_type: str = None,
        task_type_list: List[str] = None,
    ):
        # The unique identifier of the workspace: [AgentKey](https://help.aliyun.com/document_detail/2587494.html)
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The end of the time range to query task creation times. Format: YYYY-MM-DD HH:mm:ss.
        self.create_time_end = create_time_end
        # The start of the time range to query task creation times. Format: YYYY-MM-DD HH:mm:ss.
        self.create_time_start = create_time_start
        # The current page number.
        self.current = current
        # The number of entries per page. Default value: 10.
        self.size = size
        # A term query for the task code.
        self.task_code = task_code
        # A term query for the task name.
        self.task_name = task_name
        # A term query for the task status. Valid values: 0 (Pending), 1 (Running), 2 (Succeeded), 3 (Paused), 4 (Failed and retriable), 5 (Failed and not retriable), and 6 (Canceled).
        self.task_status = task_status
        # A term query for a list of task statuses. Valid values: 0 (Pending), 1 (Running), 2 (Succeeded), 3 (Paused), 4 (Failed and retriable), 5 (Failed and not retriable), and 6 (Canceled).
        self.task_status_list = task_status_list
        # A term query for the task type.
        self.task_type = task_type
        # A term query for a list of task types.
        self.task_type_list = task_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.current is not None:
            result['Current'] = self.current

        if self.size is not None:
            result['Size'] = self.size

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_list is not None:
            result['TaskStatusList'] = self.task_status_list

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_list is not None:
            result['TaskTypeList'] = self.task_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusList') is not None:
            self.task_status_list = m.get('TaskStatusList')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeList') is not None:
            self.task_type_list = m.get('TaskTypeList')

        return self

