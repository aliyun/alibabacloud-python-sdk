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
        # The reserved idempotency token. The backend does not provide idempotency guarantees in the current phase.
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
        # The agent instructions used to guide the behavior of the agent.
        self.instruction = instruction
        # The model configuration. Available only when modelSource is set to PLATFORM.
        self.model = model
        # The source of the model configuration. PLATFORM indicates that the platform parses and delivers the model configuration. RUNTIME indicates that the external runtime manages the model independently, and the model parameter cannot be passed at the same time. Valid values:
        # - PLATFORM: Platform model.
        # - RUNTIME: Runtime model.
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
        # The name of the template in the AI Registry.
        # 
        # This parameter is required.
        self.name = name
        # The version of the template in the AI Registry.
        # 
        # This parameter is required.
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
        source_type: str = None,
        version: str = None,
        version_selector: main_models.UpdateExternalAgentRequestBodySkillsVersionSelector = None,
    ):
        # The skill name.
        # 
        # This parameter is required.
        self.name = name
        # The source type of the skill. Valid values:
        # - REFERENCE: References the AI Registry.
        # - STATIC: Statically provided with the package.
        self.source_type = source_type
        # The skill version.
        self.version = version
        # The referenced version selector. If omitted, the default is LABEL/latest. Currently, only LABEL/latest is supported.
        self.version_selector = version_selector

    def validate(self):
        if self.version_selector:
            self.version_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.version is not None:
            result['version'] = self.version

        if self.version_selector is not None:
            result['versionSelector'] = self.version_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionSelector') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodySkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class UpdateExternalAgentRequestBodySkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the version selector. Valid values:
        # - LABEL: By label.
        # - VERSION: By specific version.
        self.type = type
        # The value of the selector. When the type is LABEL, this is the label name, such as latest. When the type is VERSION, this is the specific version number.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateExternalAgentRequestBodyModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
        quota: main_models.UpdateExternalAgentRequestBodyModelQuota = None,
    ):
        # The model connection ID.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model token quota configuration. If not passed, no quota is configured.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('quota') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodyModelQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class UpdateExternalAgentRequestBodyModelQuota(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_type: str = None,
        period_type: str = None,
        usage_limit: int = None,
    ):
        # Specifies whether to enable the token quota. Default value: true. If set to false, the quota is disabled and existing quota rules are deleted.
        self.enabled = enabled
        # The quota limit type. Required and validated by the backend when the quota is enabled. Fixed value: token.
        self.limit_type = limit_type
        # The statistical period for the quota. Required and validated by the backend when the quota is enabled. Valid values:
        # - day: Daily.
        # - month: Monthly.
        self.period_type = period_type
        # The maximum number of tokens allowed to be consumed within a single period. Required and validated by the backend when the quota is enabled. The value must be greater than 0.
        self.usage_limit = usage_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.limit_type is not None:
            result['limitType'] = self.limit_type

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        return self

