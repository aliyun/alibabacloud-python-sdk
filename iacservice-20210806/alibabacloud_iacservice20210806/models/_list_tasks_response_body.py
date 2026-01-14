# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListTasksResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[main_models.ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

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
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        auto_apply: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        group_info: main_models.ListTasksResponseBodyTasksGroupInfo = None,
        latest_module_version: str = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        status: str = None,
        tags: List[main_models.ListTasksResponseBodyTasksTags] = None,
        task_id: str = None,
    ):
        self.auto_apply = auto_apply
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.current_job_status = current_job_status
        self.deletion_protection = deletion_protection
        self.group_info = group_info
        self.latest_module_version = latest_module_version
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.status = status
        self.tags = tags
        self.task_id = task_id

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id

        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status

        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.latest_module_version is not None:
            result['latestModuleVersion'] = self.latest_module_version

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')

        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')

        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')

        if m.get('groupInfo') is not None:
            temp_model = main_models.ListTasksResponseBodyTasksGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('latestModuleVersion') is not None:
            self.latest_module_version = m.get('latestModuleVersion')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListTasksResponseBodyTasksTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class ListTasksResponseBodyTasksTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
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

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListTasksResponseBodyTasksGroupInfo(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.project_name is not None:
            result['projectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        return self

