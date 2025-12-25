# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListThreadsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        thread_id: str = None,
        threads: List[main_models.ListThreadsResponseBodyThreads] = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.thread_id = thread_id
        self.threads = threads
        self.total = total

    def validate(self):
        if self.threads:
            for v1 in self.threads:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        result['threads'] = []
        if self.threads is not None:
            for k1 in self.threads:
                result['threads'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        self.threads = []
        if m.get('threads') is not None:
            for k1 in m.get('threads'):
                temp_model = main_models.ListThreadsResponseBodyThreads()
                self.threads.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListThreadsResponseBodyThreads(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        digital_employee_name: str = None,
        status: str = None,
        thread_id: str = None,
        title: str = None,
        update_time: str = None,
        variables: main_models.ListThreadsResponseBodyThreadsVariables = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.digital_employee_name = digital_employee_name
        self.status = status
        self.thread_id = thread_id
        self.title = title
        self.update_time = update_time
        self.variables = variables
        self.version = version

    def validate(self):
        if self.variables:
            self.variables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.status is not None:
            result['status'] = self.status

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.title is not None:
            result['title'] = self.title

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.variables is not None:
            result['variables'] = self.variables.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('variables') is not None:
            temp_model = main_models.ListThreadsResponseBodyThreadsVariables()
            self.variables = temp_model.from_map(m.get('variables'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListThreadsResponseBodyThreadsVariables(DaraModel):
    def __init__(
        self,
        project: str = None,
        workspace: str = None,
    ):
        # SLS project。
        self.project = project
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['project'] = self.project

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

