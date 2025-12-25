# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetThreadResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        digital_employee_name: str = None,
        request_id: str = None,
        status: str = None,
        thread_id: str = None,
        title: str = None,
        update_time: str = None,
        variables: main_models.GetThreadResponseBodyVariables = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.digital_employee_name = digital_employee_name
        # Id of the request
        self.request_id = request_id
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('variables') is not None:
            temp_model = main_models.GetThreadResponseBodyVariables()
            self.variables = temp_model.from_map(m.get('variables'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetThreadResponseBodyVariables(DaraModel):
    def __init__(
        self,
        project: str = None,
        workspace: str = None,
    ):
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

