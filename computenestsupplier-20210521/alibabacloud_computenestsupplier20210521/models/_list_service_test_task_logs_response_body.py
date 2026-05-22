# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceTestTaskLogsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        task_logs: List[main_models.ListServiceTestTaskLogsResponseBodyTaskLogs] = None,
    ):
        # The number of items to return per page when paginating results. The maximum is 100, and the default is 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service test task logs.
        self.task_logs = task_logs

    def validate(self):
        if self.task_logs:
            for v1 in self.task_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskLogs'] = []
        if self.task_logs is not None:
            for k1 in self.task_logs:
                result['TaskLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_logs = []
        if m.get('TaskLogs') is not None:
            for k1 in m.get('TaskLogs'):
                temp_model = main_models.ListServiceTestTaskLogsResponseBodyTaskLogs()
                self.task_logs.append(temp_model.from_map(k1))

        return self

class ListServiceTestTaskLogsResponseBodyTaskLogs(DaraModel):
    def __init__(
        self,
        content: str = None,
        timestamp: str = None,
    ):
        # The log content.
        self.content = content
        # The UTC timestamp when the response is returned.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

