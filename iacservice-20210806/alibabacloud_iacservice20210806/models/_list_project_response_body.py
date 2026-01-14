# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListProjectResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        projects: List[main_models.ListProjectResponseBodyProjects] = None,
        request_id: str = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.projects = projects
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['projects'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.projects = []
        if m.get('projects') is not None:
            for k1 in m.get('projects'):
                temp_model = main_models.ListProjectResponseBodyProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProjectResponseBodyProjects(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        tags: List[main_models.ListProjectResponseBodyProjectsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.tags = tags
        self.task_cnt = task_cnt

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListProjectResponseBodyProjectsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')

        return self

class ListProjectResponseBodyProjectsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

