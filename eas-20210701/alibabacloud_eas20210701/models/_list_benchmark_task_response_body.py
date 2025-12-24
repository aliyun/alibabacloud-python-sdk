# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListBenchmarkTaskResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[main_models.ListBenchmarkTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stress testing tasks.
        self.tasks = tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListBenchmarkTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBenchmarkTaskResponseBodyTasks(DaraModel):
    def __init__(
        self,
        available_agent: int = None,
        create_time: str = None,
        message: str = None,
        region: str = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        # The number of instances that are available for stress testing.
        self.available_agent = available_agent
        # The time when the stress testing task was created.
        self.create_time = create_time
        # The returned message.
        self.message = message
        # The region ID of the stress testing task.
        self.region = region
        # The name of the service on which you want to perform a stress testing.
        self.service_name = service_name
        # The state of the stress testing task.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Error
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The ID of the stress testing task.
        self.task_id = task_id
        # The name of the stress testing task.
        self.task_name = task_name
        # The time when the stress testing task was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.region is not None:
            result['Region'] = self.region

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

