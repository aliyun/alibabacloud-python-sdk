# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulCheckTaskStatusDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_statuses: List[main_models.DescribeVulCheckTaskStatusDetailResponseBodyTaskStatuses] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the status information about the vulnerability scan tasks on the server.
        self.task_statuses = task_statuses
        # The total number of vulnerability scan tasks on the server.
        self.total_count = total_count

    def validate(self):
        if self.task_statuses:
            for v1 in self.task_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskStatuses'] = []
        if self.task_statuses is not None:
            for k1 in self.task_statuses:
                result['TaskStatuses'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_statuses = []
        if m.get('TaskStatuses') is not None:
            for k1 in m.get('TaskStatuses'):
                temp_model = main_models.DescribeVulCheckTaskStatusDetailResponseBodyTaskStatuses()
                self.task_statuses.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVulCheckTaskStatusDetailResponseBodyTaskStatuses(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        task_status_list: List[main_models.DescribeVulCheckTaskStatusDetailResponseBodyTaskStatusesTaskStatusList] = None,
    ):
        # The ID of the main task.
        self.task_id = task_id
        # An array that consists of status information about the vulnerability scan subtask.
        self.task_status_list = task_status_list

    def validate(self):
        if self.task_status_list:
            for v1 in self.task_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['TaskStatusList'] = []
        if self.task_status_list is not None:
            for k1 in self.task_status_list:
                result['TaskStatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.task_status_list = []
        if m.get('TaskStatusList') is not None:
            for k1 in m.get('TaskStatusList'):
                temp_model = main_models.DescribeVulCheckTaskStatusDetailResponseBodyTaskStatusesTaskStatusList()
                self.task_status_list.append(temp_model.from_map(k1))

        return self

class DescribeVulCheckTaskStatusDetailResponseBodyTaskStatusesTaskStatusList(DaraModel):
    def __init__(
        self,
        code: str = None,
        status: str = None,
        type: str = None,
    ):
        # The error code returned.
        self.code = code
        # The status of the subtask. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: collecting
        # *   **2**: collected
        # *   **3**: matching
        # *   **4**: complete
        self.status = status
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **sca**: vulnerability that is detected based on software component analysis
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

