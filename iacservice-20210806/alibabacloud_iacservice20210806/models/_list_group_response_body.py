# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListGroupResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        groups: List[main_models.ListGroupResponseBodyGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.count = count
        self.groups = groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.ListGroupResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGroupResponseBodyGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        is_default: bool = None,
        module_cnt: int = None,
        name: str = None,
        project_id: str = None,
        scene_testing_task_cnt: int = None,
        tags: List[main_models.ListGroupResponseBodyGroupsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.is_default = is_default
        self.module_cnt = module_cnt
        self.name = name
        self.project_id = project_id
        self.scene_testing_task_cnt = scene_testing_task_cnt
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

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.module_cnt is not None:
            result['moduleCnt'] = self.module_cnt

        if self.name is not None:
            result['name'] = self.name

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.scene_testing_task_cnt is not None:
            result['sceneTestingTaskCnt'] = self.scene_testing_task_cnt

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

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('moduleCnt') is not None:
            self.module_cnt = m.get('moduleCnt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('sceneTestingTaskCnt') is not None:
            self.scene_testing_task_cnt = m.get('sceneTestingTaskCnt')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListGroupResponseBodyGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')

        return self

class ListGroupResponseBodyGroupsTags(DaraModel):
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

