# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceTestTasksResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_test_tasks: List[main_models.ListServiceTestTasksResponseBodyServiceTestTasks] = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The number of items to return per page when paginating results. The maximum is 100, and the default is 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service test tasks.
        self.service_test_tasks = service_test_tasks

    def validate(self):
        if self.service_test_tasks:
            for v1 in self.service_test_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceTestTasks'] = []
        if self.service_test_tasks is not None:
            for k1 in self.service_test_tasks:
                result['ServiceTestTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_test_tasks = []
        if m.get('ServiceTestTasks') is not None:
            for k1 in m.get('ServiceTestTasks'):
                temp_model = main_models.ListServiceTestTasksResponseBodyServiceTestTasks()
                self.service_test_tasks.append(temp_model.from_map(k1))

        return self

class ListServiceTestTasksResponseBodyServiceTestTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        task_region_id: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # the status of service task.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The task region id.
        self.task_region_id = task_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_region_id is not None:
            result['TaskRegionId'] = self.task_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskRegionId') is not None:
            self.task_region_id = m.get('TaskRegionId')

        return self

