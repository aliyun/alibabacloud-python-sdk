# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeClusterTasksResponseBodyPageInfo = None,
        request_id: str = None,
        tasks: List[main_models.DescribeClusterTasksResponseBodyTasks] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The information about the tasks.
        self.tasks = tasks

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_info') is not None:
            temp_model = main_models.DescribeClusterTasksResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.DescribeClusterTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class DescribeClusterTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        created: str = None,
        error: main_models.DescribeClusterTasksResponseBodyTasksError = None,
        state: str = None,
        task_id: str = None,
        task_type: str = None,
        updated: str = None,
    ):
        # The time when the task was created.
        self.created = created
        # The error returned for the task.
        self.error = error
        # The status of the task.
        self.state = state
        # The task ID.
        self.task_id = task_id
        # The type of task.
        self.task_type = task_type
        # The time when the task was updated.
        self.updated = updated

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.state is not None:
            result['state'] = self.state

        if self.task_id is not None:
            result['task_id'] = self.task_id

        if self.task_type is not None:
            result['task_type'] = self.task_type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('error') is not None:
            temp_model = main_models.DescribeClusterTasksResponseBodyTasksError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        if m.get('task_type') is not None:
            self.task_type = m.get('task_type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class DescribeClusterTasksResponseBodyTasksError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code returned.
        self.code = code
        # The error message returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class DescribeClusterTasksResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of the page returned.
        self.page_number = page_number
        # The number of entries per page.
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
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

