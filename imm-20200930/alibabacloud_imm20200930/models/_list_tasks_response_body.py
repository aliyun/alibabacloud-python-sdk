# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListTasksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        project_name: str = None,
        request_id: str = None,
        tasks: List[main_models.TaskInfo] = None,
    ):
        # The length of the returned result list.
        self.max_results = max_results
        # The pagination token. The pagination token is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter. This parameter has a value only when not all results are returned.
        # 
        # You can specify the value of the NextToken parameter in the next request to list remaining results.
        self.next_token = next_token
        # The name of the project.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.TaskInfo()
                self.tasks.append(temp_model.from_map(k1))

        return self

