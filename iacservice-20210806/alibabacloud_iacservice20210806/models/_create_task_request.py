# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class CreateTaskRequest(DaraModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        client_token: str = None,
        description: str = None,
        group_info: main_models.CreateTaskRequestGroupInfo = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        tags: List[main_models.CreateTaskRequestTags] = None,
        task_backend: main_models.CreateTaskRequestTaskBackend = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.protection_strategy = protection_strategy
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.tags = tags
        self.task_backend = task_backend
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.task_backend:
            self.task_backend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply

        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.name is not None:
            result['name'] = self.name

        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_backend is not None:
            result['taskBackend'] = self.task_backend.to_map()

        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version

        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')

        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.CreateTaskRequestGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateTaskRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskBackend') is not None:
            temp_model = main_models.CreateTaskRequestTaskBackend()
            self.task_backend = temp_model.from_map(m.get('taskBackend'))

        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')

        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        return self

class CreateTaskRequestTaskBackend(DaraModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        object_path: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.object_path = object_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint

        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.object_path is not None:
            result['objectPath'] = self.object_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')

        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('objectPath') is not None:
            self.object_path = m.get('objectPath')

        return self

class CreateTaskRequestTags(DaraModel):
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

class CreateTaskRequestGroupInfo(DaraModel):
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

