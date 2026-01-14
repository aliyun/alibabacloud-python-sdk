# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListModulesResponseBody(DaraModel):
    def __init__(
        self,
        modules: List[main_models.ListModulesResponseBodyModules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.modules = modules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.modules:
            for v1 in self.modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['modules'] = []
        if self.modules is not None:
            for k1 in self.modules:
                result['modules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modules = []
        if m.get('modules') is not None:
            for k1 in m.get('modules'):
                temp_model = main_models.ListModulesResponseBodyModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListModulesResponseBodyModules(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        group_info: main_models.ListModulesResponseBodyModulesGroupInfo = None,
        latest_version: str = None,
        module_id: str = None,
        name: str = None,
        source: str = None,
        status: str = None,
        tags: List[main_models.ListModulesResponseBodyModulesTags] = None,
    ):
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.description = description
        self.group_info = group_info
        self.latest_version = latest_version
        self.module_id = module_id
        self.name = name
        self.source = source
        self.status = status
        self.tags = tags

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['description'] = self.description

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.ListModulesResponseBodyModulesGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListModulesResponseBodyModulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListModulesResponseBodyModulesTags(DaraModel):
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

class ListModulesResponseBodyModulesGroupInfo(DaraModel):
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

