# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateExternalAgentRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateExternalAgentRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # A reserved idempotency token. The backend does not guarantee idempotency in the current version.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateExternalAgentRequestBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        instruction: str = None,
        model: main_models.UpdateExternalAgentRequestBodyModel = None,
        model_source: str = None,
        name: str = None,
        skills: List[main_models.UpdateExternalAgentRequestBodySkills] = None,
        template: main_models.UpdateExternalAgentRequestBodyTemplate = None,
        tools: List[main_models.UpdateExternalAgentRequestBodyTools] = None,
    ):
        # The description of the external agent.
        self.description = description
        # The agent instruction that guides the behavior of the agent.
        self.instruction = instruction
        # The model configuration. This parameter is available only when modelSource is set to PLATFORM.
        self.model = model
        # The source of the model configuration. Valid values:
        # 
        # - PLATFORM: The model configuration is parsed and distributed by the platform. You can specify the model parameter.
        # - RUNTIME: The model is managed by the external runtime. You cannot specify the model parameter at the same time.
        self.model_source = model_source
        # The name of the external agent.
        self.name = name
        # The list of skill configurations.
        self.skills = skills
        # The agent template configuration.
        self.template = template
        # The list of tool configurations.
        self.tools = tools

    def validate(self):
        if self.model:
            self.model.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.template:
            self.template.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.model_source is not None:
            result['modelSource'] = self.model_source

        if self.name is not None:
            result['name'] = self.name

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        if self.template is not None:
            result['template'] = self.template.to_map()

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('model') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodyModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('modelSource') is not None:
            self.model_source = m.get('modelSource')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.UpdateExternalAgentRequestBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('template') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodyTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.UpdateExternalAgentRequestBodyTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class UpdateExternalAgentRequestBodyTools(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The tool name.
        # 
        # This parameter is required.
        self.name = name
        # The tool type. Valid values:
        # 
        # - MCP: MCP tool.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateExternalAgentRequestBodyTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.UpdateExternalAgentRequestBodyTemplateAiRegistry = None,
    ):
        # The AI Registry template configuration.
        self.ai_registry = ai_registry

    def validate(self):
        if self.ai_registry:
            self.ai_registry.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_registry is not None:
            result['aiRegistry'] = self.ai_registry.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiRegistry') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodyTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class UpdateExternalAgentRequestBodyTemplateAiRegistry(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the template in AI Registry.
        # 
        # This parameter is required.
        self.name = name
        # The version of the template in AI Registry.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class UpdateExternalAgentRequestBodySkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The skill name.
        # 
        # This parameter is required.
        self.name = name
        # The skill version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class UpdateExternalAgentRequestBodyModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
    ):
        # The model connection ID.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        # 
        # This parameter is required.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        return self

