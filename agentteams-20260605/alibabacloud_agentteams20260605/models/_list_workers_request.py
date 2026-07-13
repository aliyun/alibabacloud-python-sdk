# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class ListWorkersRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        credential: str = None,
        group: main_models.ListWorkersRequestGroup = None,
        instance_id: str = None,
        max_results: int = None,
        mcp: str = None,
        model_name: str = None,
        model_provider: str = None,
        name_like: str = None,
        next_token: str = None,
        template: main_models.ListWorkersRequestTemplate = None,
        version_code: str = None,
    ):
        self.agent_type = agent_type
        self.credential = credential
        self.group = group
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.mcp = mcp
        self.model_name = model_name
        self.model_provider = model_provider
        self.name_like = name_like
        self.next_token = next_token
        self.template = template
        self.version_code = version_code

    def validate(self):
        if self.group:
            self.group.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.credential is not None:
            result['Credential'] = self.credential

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.mcp is not None:
            result['Mcp'] = self.mcp

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_provider is not None:
            result['ModelProvider'] = self.model_provider

        if self.name_like is not None:
            result['NameLike'] = self.name_like

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.template is not None:
            result['Template'] = self.template.to_map()

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('Group') is not None:
            temp_model = main_models.ListWorkersRequestGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Mcp') is not None:
            self.mcp = m.get('Mcp')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelProvider') is not None:
            self.model_provider = m.get('ModelProvider')

        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Template') is not None:
            temp_model = main_models.ListWorkersRequestTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class ListWorkersRequestTemplate(DaraModel):
    def __init__(
        self,
        label: str = None,
        name: str = None,
        version: str = None,
    ):
        self.label = label
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListWorkersRequestGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
        type: str = None,
    ):
        self.name = name
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

