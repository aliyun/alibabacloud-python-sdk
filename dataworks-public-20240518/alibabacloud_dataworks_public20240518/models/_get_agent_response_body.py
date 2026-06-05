# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent: main_models.GetAgentResponseBodyAgent = None,
        request_id: str = None,
    ):
        self.agent = agent
        self.request_id = request_id

    def validate(self):
        if self.agent:
            self.agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.GetAgentResponseBodyAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentResponseBodyAgent(DaraModel):
    def __init__(
        self,
        callable_agents: List[main_models.GetAgentResponseBodyAgentCallableAgents] = None,
        creator_id: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        metadata: Dict[str, Any] = None,
        model: main_models.GetAgentResponseBodyAgentModel = None,
        modifier_id: str = None,
        name: str = None,
        required_runtime: List[str] = None,
        skills: List[main_models.GetAgentResponseBodyAgentSkills] = None,
        system_prompt: str = None,
        tools: List[main_models.GetAgentResponseBodyAgentTools] = None,
        visibility: str = None,
        visibility_scope: main_models.GetAgentResponseBodyAgentVisibilityScope = None,
    ):
        self.callable_agents = callable_agents
        self.creator_id = creator_id
        self.description = description
        self.display_name = display_name
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        self.metadata = metadata
        self.model = model
        self.modifier_id = modifier_id
        self.name = name
        self.required_runtime = required_runtime
        self.skills = skills
        self.system_prompt = system_prompt
        self.tools = tools
        self.visibility = visibility
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.callable_agents:
            for v1 in self.callable_agents:
                 if v1:
                    v1.validate()
        if self.model:
            self.model.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallableAgents'] = []
        if self.callable_agents is not None:
            for k1 in self.callable_agents:
                result['CallableAgents'].append(k1.to_map() if k1 else None)

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.required_runtime is not None:
            result['RequiredRuntime'] = self.required_runtime

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.callable_agents = []
        if m.get('CallableAgents') is not None:
            for k1 in m.get('CallableAgents'):
                temp_model = main_models.GetAgentResponseBodyAgentCallableAgents()
                self.callable_agents.append(temp_model.from_map(k1))

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Model') is not None:
            temp_model = main_models.GetAgentResponseBodyAgentModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequiredRuntime') is not None:
            self.required_runtime = m.get('RequiredRuntime')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.GetAgentResponseBodyAgentSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.GetAgentResponseBodyAgentTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.GetAgentResponseBodyAgentVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class GetAgentResponseBodyAgentVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.project_ids = project_ids
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

class GetAgentResponseBodyAgentTools(DaraModel):
    def __init__(
        self,
        builtin_name: str = None,
        kind: str = None,
        mcp_items: List[str] = None,
        mcp_server_name: str = None,
    ):
        self.builtin_name = builtin_name
        self.kind = kind
        self.mcp_items = mcp_items
        self.mcp_server_name = mcp_server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.builtin_name is not None:
            result['BuiltinName'] = self.builtin_name

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.mcp_items is not None:
            result['McpItems'] = self.mcp_items

        if self.mcp_server_name is not None:
            result['McpServerName'] = self.mcp_server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinName') is not None:
            self.builtin_name = m.get('BuiltinName')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('McpItems') is not None:
            self.mcp_items = m.get('McpItems')

        if m.get('McpServerName') is not None:
            self.mcp_server_name = m.get('McpServerName')

        return self

class GetAgentResponseBodyAgentSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: int = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAgentResponseBodyAgentModel(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        max_tokens: int = None,
        model_name: str = None,
        stream: bool = None,
        temperature: float = None,
        top_p: float = None,
    ):
        self.config = config
        self.max_tokens = max_tokens
        self.model_name = model_name
        self.stream = stream
        self.temperature = temperature
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class GetAgentResponseBodyAgentCallableAgents(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        source: str = None,
        version: int = None,
    ):
        self.display_name = display_name
        self.name = name
        self.source = source
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

