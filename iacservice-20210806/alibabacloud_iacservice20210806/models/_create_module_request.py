# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class CreateModuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_info: main_models.CreateModuleRequestGroupInfo = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        tags: List[main_models.CreateModuleRequestTags] = None,
        version_strategy: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
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
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.CreateModuleRequestGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateModuleRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')

        return self

class CreateModuleRequestTags(DaraModel):
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

class CreateModuleRequestGroupInfo(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.project_id is not None:
            result['projectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        return self

