# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListExecutionRiskyTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risky_tasks: List[main_models.ListExecutionRiskyTasksResponseBodyRiskyTasks] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about high-risk tasks.
        self.risky_tasks = risky_tasks

    def validate(self):
        if self.risky_tasks:
            for v1 in self.risky_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskyTasks'] = []
        if self.risky_tasks is not None:
            for k1 in self.risky_tasks:
                result['RiskyTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risky_tasks = []
        if m.get('RiskyTasks') is not None:
            for k1 in m.get('RiskyTasks'):
                temp_model = main_models.ListExecutionRiskyTasksResponseBodyRiskyTasks()
                self.risky_tasks.append(temp_model.from_map(k1))

        return self

class ListExecutionRiskyTasksResponseBodyRiskyTasks(DaraModel):
    def __init__(
        self,
        api: str = None,
        service: str = None,
        task: List[str] = None,
        template: List[str] = None,
    ):
        # The name of the operation that the high-risk task calls.
        self.api = api
        # The cloud service in which the high-risk task runs.
        self.service = service
        # The details of the high-risk task.
        self.task = task
        # The details of templates to which the high-risk task belongs.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['API'] = self.api

        if self.service is not None:
            result['Service'] = self.service

        if self.task is not None:
            result['Task'] = self.task

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('API') is not None:
            self.api = m.get('API')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

