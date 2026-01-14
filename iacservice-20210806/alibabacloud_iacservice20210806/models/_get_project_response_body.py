# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        project: main_models.GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['project'] = self.project.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            temp_model = main_models.GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m.get('project'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetProjectResponseBodyProject(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.task_cnt = task_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')

        return self

