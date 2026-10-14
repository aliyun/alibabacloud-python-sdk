# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListAifgJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAifgJobsResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # The data under the root node.
        self.data = data
        # The maximum number of records to retrieve in a single request.
        self.max_results = max_results
        # Indicates the position read by the current call. An empty value indicates that all data has been read.
        # 
        # This parameter is required.
        self.message = message
        # The pagination token.
        # 
        # > A non-empty value indicates that more data is available.
        self.next_token = next_token
        # The unique identifier of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAifgJobsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAifgJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        command: Any = None,
        id: int = None,
        params: Any = None,
        result: Any = None,
        service_name: str = None,
        status: str = None,
        sub_status: str = None,
        submit_time: str = None,
        task_id: str = None,
        trace_task_id: str = None,
    ):
        # The first command in the data list.
        self.command = command
        # The ID of the first element in the data list.
        self.id = id
        # The first parameter in the root data.
        self.params = params
        # The first result in the root data.
        self.result = result
        # The service name.
        self.service_name = service_name
        # The status of the data item.
        self.status = status
        # The sub-status of the data item.
        self.sub_status = sub_status
        # The time when the data was submitted.
        self.submit_time = submit_time
        # The task ID.
        self.task_id = task_id
        # The unique identifier of the trace task.
        self.trace_task_id = trace_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['command'] = self.command

        if self.id is not None:
            result['id'] = self.id

        if self.params is not None:
            result['params'] = self.params

        if self.result is not None:
            result['result'] = self.result

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        if self.sub_status is not None:
            result['subStatus'] = self.sub_status

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trace_task_id is not None:
            result['traceTaskId'] = self.trace_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subStatus') is not None:
            self.sub_status = m.get('subStatus')

        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceTaskId') is not None:
            self.trace_task_id = m.get('traceTaskId')

        return self

