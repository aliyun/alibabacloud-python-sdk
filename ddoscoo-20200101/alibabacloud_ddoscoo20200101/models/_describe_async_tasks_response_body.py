# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeAsyncTasksResponseBody(DaraModel):
    def __init__(
        self,
        async_tasks: List[main_models.DescribeAsyncTasksResponseBodyAsyncTasks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details of the asynchronous export tasks.
        self.async_tasks = async_tasks
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of asynchronous export tasks that are returned.
        self.total_count = total_count

    def validate(self):
        if self.async_tasks:
            for v1 in self.async_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k1 in self.async_tasks:
                result['AsyncTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k1 in m.get('AsyncTasks'):
                temp_model = main_models.DescribeAsyncTasksResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAsyncTasksResponseBodyAsyncTasks(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        task_id: int = None,
        task_params: str = None,
        task_result: str = None,
        task_status: int = None,
        task_type: int = None,
    ):
        # The end time of the task. This value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The start time of the task. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The ID of the job.
        self.task_id = task_id
        # The task parameter. The value is a JSON string. The returned field in the value varies based on the value of **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following filed is returned:
        # 
        # *   **instanceId**: the ID of the instance. Data type: string.
        # 
        # If **TaskType** is set to **2**, the following field is returned:
        # 
        # *   **domain**: the domain name of the website. Data type: string.
        self.task_params = task_params
        # The execution result of the task. The value is a JSON string. The returned fields in the value vary based on the value of **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following fields are returned:
        # 
        # *   **instanceId**: the ID of the instance. Data type: string.
        # *   **url**: the URL to download the exported file from Object Storage Service (OSS). Data type: string.
        # 
        # If **TaskType** is set to **2**, the following fields are returned:
        # 
        # *   **domain**: the domain name of the website. Data type: string.
        # *   **url**: the URL to download the exported file from OSS. Data type: string.
        self.task_result = task_result
        # The status of the task. Valid values:
        # 
        # *   **0**: indicates that the task is being initialized.
        # *   **1**: indicates that the task is in progress.
        # *   **2**: indicates that the task is successful.
        # *   **3**: indicates that the task failed.
        self.task_status = task_status
        # The type of the task. Valid values:
        # 
        # *   **1**: the task to export the port forwarding rules of an instance
        # *   **2**: the task to export the forwarding rules of a website protected by an instance
        # *   **3**: the task to export the sessions and health check settings of an instance
        # *   **4**: the task to export the mitigation policies of an instance
        # *   **5**: the task to download the blacklist for destination IP addresses of an instance
        # *   **6**: the task to download the whitelist for destination IP addresses of an instance
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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_params is not None:
            result['TaskParams'] = self.task_params

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

