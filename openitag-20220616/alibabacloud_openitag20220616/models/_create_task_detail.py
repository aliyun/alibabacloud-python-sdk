# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class CreateTaskDetail(DaraModel):
    def __init__(
        self,
        admins: main_models.CreateTaskDetailAdmins = None,
        allow_append_data: bool = None,
        assign_config: main_models.TaskAssginConfig = None,
        dataset_proxy_relations: List[main_models.DatasetProxyConfig] = None,
        exif: Dict[str, Any] = None,
        tags: List[str] = None,
        task_name: str = None,
        task_template_config: main_models.TaskTemplateConfig = None,
        task_workflow: List[main_models.CreateTaskDetailTaskWorkflow] = None,
        template_id: str = None,
        uuid: str = None,
        vote_configs: Dict[str, main_models.CreateTaskDetailVoteInfo] = None,
    ):
        # Administrators; defaults to the Creator.
        self.admins = admins
        # Indicates whether appending new data is supported. Valid values:
        # - true: Supported
        # - false: Not supported
        self.allow_append_data = allow_append_data
        # Job assignment mechanism.
        # 
        # This parameter is required.
        self.assign_config = assign_config
        # List of dataset configurations.
        # 
        # This parameter is required.
        self.dataset_proxy_relations = dataset_proxy_relations
        # Additional configuration. JSON format.
        self.exif = exif
        # List of job labels.
        self.tags = tags
        # Job name.
        # 
        # This parameter is required.
        self.task_name = task_name
        # Template Configuration.
        self.task_template_config = task_template_config
        # List of pipelines.
        # 
        # This parameter is required.
        self.task_workflow = task_workflow
        # Template ID. For more information, see [ListTemplates](https://help.aliyun.com/document_detail/454654.html).
        # 
        # This parameter is required.
        self.template_id = template_id
        # Unique identifier (UUID), controlled by the business side.
        # 
        # This parameter is required.
        self.uuid = uuid
        # Vote configuration
        self.vote_configs = vote_configs

    def validate(self):
        if self.admins:
            self.admins.validate()
        if self.assign_config:
            self.assign_config.validate()
        if self.dataset_proxy_relations:
            for v1 in self.dataset_proxy_relations:
                 if v1:
                    v1.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for v1 in self.task_workflow:
                 if v1:
                    v1.validate()
        if self.vote_configs:
            for v1 in self.vote_configs.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admins is not None:
            result['Admins'] = self.admins.to_map()

        if self.allow_append_data is not None:
            result['AllowAppendData'] = self.allow_append_data

        if self.assign_config is not None:
            result['AssignConfig'] = self.assign_config.to_map()

        result['DatasetProxyRelations'] = []
        if self.dataset_proxy_relations is not None:
            for k1 in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k1.to_map() if k1 else None)

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_template_config is not None:
            result['TaskTemplateConfig'] = self.task_template_config.to_map()

        result['TaskWorkflow'] = []
        if self.task_workflow is not None:
            for k1 in self.task_workflow:
                result['TaskWorkflow'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.uuid is not None:
            result['UUID'] = self.uuid

        result['VoteConfigs'] = {}
        if self.vote_configs is not None:
            for k1, v1 in self.vote_configs.items():
                result['VoteConfigs'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Admins') is not None:
            temp_model = main_models.CreateTaskDetailAdmins()
            self.admins = temp_model.from_map(m.get('Admins'))

        if m.get('AllowAppendData') is not None:
            self.allow_append_data = m.get('AllowAppendData')

        if m.get('AssignConfig') is not None:
            temp_model = main_models.TaskAssginConfig()
            self.assign_config = temp_model.from_map(m.get('AssignConfig'))

        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k1 in m.get('DatasetProxyRelations'):
                temp_model = main_models.DatasetProxyConfig()
                self.dataset_proxy_relations.append(temp_model.from_map(k1))

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskTemplateConfig') is not None:
            temp_model = main_models.TaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m.get('TaskTemplateConfig'))

        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k1 in m.get('TaskWorkflow'):
                temp_model = main_models.CreateTaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        self.vote_configs = {}
        if m.get('VoteConfigs') is not None:
            for k1, v1 in m.get('VoteConfigs').items():
                temp_model = main_models.CreateTaskDetailVoteInfo()
                self.vote_configs[k1] = temp_model.from_map(v1)

        return self

class CreateTaskDetailTaskWorkflow(DaraModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # Node name. Valid values:
        # - MARK: Annotate.
        # - CHECK: Check.
        # - SAMPLING: Validate.
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self



class CreateTaskDetailAdmins(DaraModel):
    def __init__(
        self,
        users: List[main_models.SimpleUser] = None,
    ):
        # List of administrators.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.SimpleUser()
                self.users.append(temp_model.from_map(k1))

        return self

