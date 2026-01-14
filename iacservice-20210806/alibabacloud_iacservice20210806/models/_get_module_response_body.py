# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetModuleResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.GetModuleResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = main_models.GetModuleResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetModuleResponseBodyModule(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_info: main_models.GetModuleResponseBodyModuleGroupInfo = None,
        latest_version: str = None,
        module_id: str = None,
        name: str = None,
        output_path: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        status: str = None,
        tags: List[main_models.GetModuleResponseBodyModuleTags] = None,
        version_strategy: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_info = group_info
        self.latest_version = latest_version
        self.module_id = module_id
        self.name = name
        self.output_path = output_path
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.status = status
        self.tags = tags
        self.version_strategy = version_strategy

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

        if self.output_path is not None:
            result['outputPath'] = self.output_path

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.GetModuleResponseBodyModuleGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputPath') is not None:
            self.output_path = m.get('outputPath')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetModuleResponseBodyModuleTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')

        return self

class GetModuleResponseBodyModuleTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class GetModuleResponseBodyModuleGroupInfo(DaraModel):
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

