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
        # The reserved query parameter. The backend does not currently provide idempotence guarantees for deduplication or recovery of original acceptance results based on this identifier.
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
        environment: main_models.UpdateExternalAgentRequestBodyEnvironment = None,
        instruction: str = None,
        model: main_models.UpdateExternalAgentRequestBodyModel = None,
        model_source: str = None,
        name: str = None,
        skills: List[main_models.UpdateExternalAgentRequestBodySkills] = None,
        template: main_models.UpdateExternalAgentRequestBodyTemplate = None,
        tools: List[main_models.UpdateExternalAgentRequestBodyTools] = None,
    ):
        # The description of the managed agent.
        self.description = description
        # The credential binding configuration. If you do not pass this parameter, the original binding is retained. If you pass an object, you must explicitly provide a non-null credentialReferences list, and the list is replaced in its entirety. If the list is empty or environment is null, the binding is cleared. Empty objects and objects that contain only common environment variables are invalid.
        self.environment = environment
        # The agent instruction, which is used to guide the behavior of the agent.
        self.instruction = instruction
        # The model configuration. This parameter is available only when modelSource is set to PLATFORM.
        self.model = model
        # The source of the model configuration. PLATFORM indicates that the platform parses and delivers the model configuration. RUNTIME indicates that the external runtime manages the model itself, and the model parameter cannot be passed at the same time. Valid values: PLATFORM (platform model) and RUNTIME (runtime model).
        self.model_source = model_source
        # The name of the managed agent.
        self.name = name
        # The list of skill configurations.
        self.skills = skills
        # The agent template configuration.
        self.template = template
        # The list of tool configurations.
        self.tools = tools

    def validate(self):
        if self.environment:
            self.environment.validate()
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

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

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

        if m.get('environment') is not None:
            temp_model = main_models.UpdateExternalAgentRequestBodyEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

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
        # The tool type. Valid values: MCP (MCP tool).
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
        # The skill source type. Valid values: REFERENCE (references AI Registry) and STATIC (statically provided with the package).
        self.source_type = source_type
        # The skill version field for compatibility with legacy requests. For new requests, use sourceType and versionSelector. Do not submit this parameter in combination with sourceType.
        self.version = version
        # The skill reference version selector, which supports LABEL tags and VERSION specific versions. If omitted, LABEL/latest is used. Selectors are not provided for STATIC sources.
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
        # The version selector type. Valid values: LABEL (by tag) and VERSION (by specific version).
        self.type = type
        # The selector value. When the type is LABEL, the value is the tag name, such as latest. When the type is VERSION, the value is the specific version number.
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
        # The model token quota configuration. If you do not pass this parameter, no quota is configured.
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
        # Specifies whether to enable the token quota. Default value: true. If you set this parameter to false, the quota is disabled and existing quota rules are deleted.
        self.enabled = enabled
        # The quota limit type. This parameter is required and verified by the backend when the quota is enabled. Fixed value: token.
        self.limit_type = limit_type
        # The statistical period of the quota. This parameter is required and verified by the backend when the quota is enabled. Valid values: day (daily) and month (monthly).
        self.period_type = period_type
        # The maximum number of tokens that can be consumed in a single period. This parameter is required and verified by the backend when the quota is enabled. The value must be greater than 0.
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

class UpdateExternalAgentRequestBodyEnvironment(DaraModel):
    def __init__(
        self,
        credential_references: List[main_models.UpdateExternalAgentRequestBodyEnvironmentCredentialReferences] = None,
    ):
        # The list of credential references. You must explicitly provide this list when passing the environment object, and it cannot be null. The list is replaced in its entirety. If you do not pass environment during an update, the original binding is retained. If you pass an empty list or set environment to null, the binding is cleared. Pass only the credential ID, not the actual key.
        self.credential_references = credential_references

    def validate(self):
        if self.credential_references:
            for v1 in self.credential_references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['credentialReferences'] = []
        if self.credential_references is not None:
            for k1 in self.credential_references:
                result['credentialReferences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credential_references = []
        if m.get('credentialReferences') is not None:
            for k1 in m.get('credentialReferences'):
                temp_model = main_models.UpdateExternalAgentRequestBodyEnvironmentCredentialReferences()
                self.credential_references.append(temp_model.from_map(k1))

        return self

class UpdateExternalAgentRequestBodyEnvironmentCredentialReferences(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
    ):
        # The credential ID. This parameter is required when passing a credential reference item and is verified by the backend.
        self.credential_id = credential_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        return self

