# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateManagedAgentRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateManagedAgentRequestBody = None,
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
            temp_model = main_models.UpdateManagedAgentRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateManagedAgentRequestBody(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_scope: str = None,
        agentic_fs_mounts: List[main_models.UpdateManagedAgentRequestBodyAgenticFsMounts] = None,
        description: str = None,
        environment: main_models.UpdateManagedAgentRequestBodyEnvironment = None,
        harness: main_models.UpdateManagedAgentRequestBodyHarness = None,
        instruction: str = None,
        model: main_models.UpdateManagedAgentRequestBodyModel = None,
        name: str = None,
        network: main_models.UpdateManagedAgentRequestBodyNetwork = None,
        oss_mounts: List[main_models.UpdateManagedAgentRequestBodyOssMounts] = None,
        prompt_variables: List[main_models.UpdateManagedAgentRequestBodyPromptVariables] = None,
        runtime: main_models.UpdateManagedAgentRequestBodyRuntime = None,
        skills: List[main_models.UpdateManagedAgentRequestBodySkills] = None,
        sub_agents: List[main_models.UpdateManagedAgentRequestBodySubAgents] = None,
        template: main_models.UpdateManagedAgentRequestBodyTemplate = None,
        tools: List[main_models.UpdateManagedAgentRequestBodyTools] = None,
    ):
        # 省略时保持不变；API_KEY 会清空 accessScope，USER 必须设置访问范围。
        self.access_mode = access_mode
        # 省略时保持不变；仅 accessMode 为 USER 时使用。
        self.access_scope = access_scope
        # If omitted, the existing mounts are retained. An empty array clears the mounts. A non-empty array replaces all existing mounts. Null is rejected. The total number of AgenticFS and OSS mounts cannot exceed 10.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The description of the managed agent.
        self.description = description
        # The environment configuration.
        self.environment = environment
        # The agent runtime framework.
        self.harness = harness
        # The agent instruction, which is used to guide the behavior of the agent.
        self.instruction = instruction
        # The model configuration.
        self.model = model
        # The name of the managed agent.
        self.name = name
        # The network configuration.
        self.network = network
        # The list of OSS mounts. A maximum of 10 items are allowed. Pass an empty array to clear existing mounts.
        self.oss_mounts = oss_mounts
        # The prompt variable declarations.
        self.prompt_variables = prompt_variables
        # The runtime configuration.
        self.runtime = runtime
        # The list of skill configurations.
        self.skills = skills
        # The list of sub-agent configurations.
        self.sub_agents = sub_agents
        # The agent template configuration.
        self.template = template
        # The list of tool configurations.
        self.tools = tools

    def validate(self):
        if self.agentic_fs_mounts:
            for v1 in self.agentic_fs_mounts:
                 if v1:
                    v1.validate()
        if self.environment:
            self.environment.validate()
        if self.harness:
            self.harness.validate()
        if self.model:
            self.model.validate()
        if self.network:
            self.network.validate()
        if self.oss_mounts:
            for v1 in self.oss_mounts:
                 if v1:
                    v1.validate()
        if self.prompt_variables:
            for v1 in self.prompt_variables:
                 if v1:
                    v1.validate()
        if self.runtime:
            self.runtime.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.sub_agents:
            for v1 in self.sub_agents:
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
        if self.access_mode is not None:
            result['accessMode'] = self.access_mode

        if self.access_scope is not None:
            result['accessScope'] = self.access_scope

        result['agenticFsMounts'] = []
        if self.agentic_fs_mounts is not None:
            for k1 in self.agentic_fs_mounts:
                result['agenticFsMounts'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.harness is not None:
            result['harness'] = self.harness.to_map()

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.network is not None:
            result['network'] = self.network.to_map()

        result['ossMounts'] = []
        if self.oss_mounts is not None:
            for k1 in self.oss_mounts:
                result['ossMounts'].append(k1.to_map() if k1 else None)

        result['promptVariables'] = []
        if self.prompt_variables is not None:
            for k1 in self.prompt_variables:
                result['promptVariables'].append(k1.to_map() if k1 else None)

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        result['subAgents'] = []
        if self.sub_agents is not None:
            for k1 in self.sub_agents:
                result['subAgents'].append(k1.to_map() if k1 else None)

        if self.template is not None:
            result['template'] = self.template.to_map()

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessMode') is not None:
            self.access_mode = m.get('accessMode')

        if m.get('accessScope') is not None:
            self.access_scope = m.get('accessScope')

        self.agentic_fs_mounts = []
        if m.get('agenticFsMounts') is not None:
            for k1 in m.get('agenticFsMounts'):
                temp_model = main_models.UpdateManagedAgentRequestBodyAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environment') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('harness') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyHarness()
            self.harness = temp_model.from_map(m.get('harness'))

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('model') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.UpdateManagedAgentRequestBodyOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        self.prompt_variables = []
        if m.get('promptVariables') is not None:
            for k1 in m.get('promptVariables'):
                temp_model = main_models.UpdateManagedAgentRequestBodyPromptVariables()
                self.prompt_variables.append(temp_model.from_map(k1))

        if m.get('runtime') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.UpdateManagedAgentRequestBodySkills()
                self.skills.append(temp_model.from_map(k1))

        self.sub_agents = []
        if m.get('subAgents') is not None:
            for k1 in m.get('subAgents'):
                temp_model = main_models.UpdateManagedAgentRequestBodySubAgents()
                self.sub_agents.append(temp_model.from_map(k1))

        if m.get('template') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.UpdateManagedAgentRequestBodyTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class UpdateManagedAgentRequestBodyTools(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The tool name.
        # 
        # This parameter is required.
        self.name = name
        # The tool type.
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

class UpdateManagedAgentRequestBodyTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.UpdateManagedAgentRequestBodyTemplateAiRegistry = None,
    ):
        # The AI registry template configuration.
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
            temp_model = main_models.UpdateManagedAgentRequestBodyTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class UpdateManagedAgentRequestBodyTemplateAiRegistry(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the template in the AI registry.
        # 
        # This parameter is required.
        self.name = name
        # The version of the template in the AI registry.
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

class UpdateManagedAgentRequestBodySubAgents(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        name: str = None,
        skills: List[main_models.UpdateManagedAgentRequestBodySubAgentsSkills] = None,
    ):
        # The sub-agent instruction.
        # 
        # This parameter is required.
        self.instruction = instruction
        # The sub-agent name.
        # 
        # This parameter is required.
        self.name = name
        # The list of sub-agent skills.
        self.skills = skills

    def validate(self):
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.name is not None:
            result['name'] = self.name

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.UpdateManagedAgentRequestBodySubAgentsSkills()
                self.skills.append(temp_model.from_map(k1))

        return self

class UpdateManagedAgentRequestBodySubAgentsSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The skill name.
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

class UpdateManagedAgentRequestBodySkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_type: str = None,
        version: str = None,
        version_selector: main_models.UpdateManagedAgentRequestBodySkillsVersionSelector = None,
    ):
        # The skill name.
        # 
        # This parameter is required.
        self.name = name
        # The source type of the skill. Valid values: REFERENCE (references the AI registry) and STATIC (provided statically within the package).
        self.source_type = source_type
        # The skill version.
        self.version = version
        # The referenced version selector. If omitted, the default value is LABEL/latest. Currently, only LABEL/latest is supported.
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
            temp_model = main_models.UpdateManagedAgentRequestBodySkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class UpdateManagedAgentRequestBodySkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the version selector. Valid values: LABEL (by tag) and VERSION (by specific version).
        self.type = type
        # The value of the selector. If the type is LABEL, this value is the tag name, such as latest. If the type is VERSION, this value is the specific version number.
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

class UpdateManagedAgentRequestBodyRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.UpdateManagedAgentRequestBodyRuntimeCompute = None,
        hpa: main_models.UpdateManagedAgentRequestBodyRuntimeHpa = None,
        session_policy: main_models.UpdateManagedAgentRequestBodyRuntimeSessionPolicy = None,
    ):
        # The compute configuration.
        # 
        # This parameter is required.
        self.compute = compute
        # The sandbox auto scaling and session configuration.
        self.hpa = hpa
        # The session policy configuration.
        # 
        # This parameter is required.
        self.session_policy = session_policy

    def validate(self):
        if self.compute:
            self.compute.validate()
        if self.hpa:
            self.hpa.validate()
        if self.session_policy:
            self.session_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute is not None:
            result['compute'] = self.compute.to_map()

        if self.hpa is not None:
            result['hpa'] = self.hpa.to_map()

        if self.session_policy is not None:
            result['sessionPolicy'] = self.session_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compute') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class UpdateManagedAgentRequestBodyRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The name of the HTTP header used for session affinity. This parameter takes effect when sessionPolicy.type is set to ISOLATED_HEADER_FIELD.
        self.header_name = header_name
        # The session policy type.
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
        if self.header_name is not None:
            result['headerName'] = self.header_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateManagedAgentRequestBodyRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Specifies whether to enable auto scaling. This parameter is required and validated by the backend when HPA is present.
        self.enabled = enabled
        # The maximum number of active sessions per sandbox. This parameter is required and validated by the backend when HPA is present.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of sandboxes. This parameter is required and must be greater than or equal to the minimum value when HPA is enabled.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of sandboxes. This parameter is required when HPA is enabled.
        self.min_sandbox_count = min_sandbox_count
        # The idle timeout in seconds before an inactive session is reclaimed. This parameter is required and validated by the backend when HPA is present.
        self.session_ttl_seconds = session_ttl_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.max_concurrent_sessions_per_sandbox is not None:
            result['maxConcurrentSessionsPerSandbox'] = self.max_concurrent_sessions_per_sandbox

        if self.max_sandbox_count is not None:
            result['maxSandboxCount'] = self.max_sandbox_count

        if self.min_sandbox_count is not None:
            result['minSandboxCount'] = self.min_sandbox_count

        if self.session_ttl_seconds is not None:
            result['sessionTtlSeconds'] = self.session_ttl_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('maxConcurrentSessionsPerSandbox') is not None:
            self.max_concurrent_sessions_per_sandbox = m.get('maxConcurrentSessionsPerSandbox')

        if m.get('maxSandboxCount') is not None:
            self.max_sandbox_count = m.get('maxSandboxCount')

        if m.get('minSandboxCount') is not None:
            self.min_sandbox_count = m.get('minSandboxCount')

        if m.get('sessionTtlSeconds') is not None:
            self.session_ttl_seconds = m.get('sessionTtlSeconds')

        return self

class UpdateManagedAgentRequestBodyRuntimeCompute(DaraModel):
    def __init__(
        self,
        compute_class: str = None,
    ):
        # The compute class.
        # 
        # This parameter is required.
        self.compute_class = compute_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_class is not None:
            result['computeClass'] = self.compute_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeClass') is not None:
            self.compute_class = m.get('computeClass')

        return self

class UpdateManagedAgentRequestBodyPromptVariables(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
    ):
        # The default value.
        self.default_value = default_value
        # The description of the variable.
        self.description = description
        # The name of the variable.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['defaultValue'] = self.default_value

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class UpdateManagedAgentRequestBodyOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The name of the OSS bucket. This field is required for each mount item and validated by the backend.
        self.bucket_name = bucket_name
        # The absolute mount path in the container. This field is required for each mount item and validated by the backend.
        self.mount_path = mount_path
        # The relative object prefix in the bucket. If not specified, the entire bucket is mounted.
        self.path = path
        # Specifies whether to mount the bucket in read-only mode. If not specified, the default value is false.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.mount_path is not None:
            result['mountPath'] = self.mount_path

        if self.path is not None:
            result['path'] = self.path

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

class UpdateManagedAgentRequestBodyNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.UpdateManagedAgentRequestBodyNetworkAccessInternet = None,
        access_vpc: main_models.UpdateManagedAgentRequestBodyNetworkAccessVpc = None,
    ):
        # The public network access configuration.
        self.access_internet = access_internet
        # The VPC access configuration.
        self.access_vpc = access_vpc

    def validate(self):
        if self.access_internet:
            self.access_internet.validate()
        if self.access_vpc:
            self.access_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_internet is not None:
            result['accessInternet'] = self.access_internet.to_map()

        if self.access_vpc is not None:
            result['accessVpc'] = self.access_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessInternet') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class UpdateManagedAgentRequestBodyNetworkAccessVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow VPC access.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class UpdateManagedAgentRequestBodyNetworkAccessInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow Internet access.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class UpdateManagedAgentRequestBodyModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
        quota: main_models.UpdateManagedAgentRequestBodyModelQuota = None,
    ):
        # The model connection ID.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        self.model_name = model_name
        # The model token quota configuration. If not specified, no quota is configured.
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
            temp_model = main_models.UpdateManagedAgentRequestBodyModelQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class UpdateManagedAgentRequestBodyModelQuota(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_type: str = None,
        period_type: str = None,
        usage_limit: int = None,
    ):
        # Specifies whether to enable the token quota. If not specified, the default value is true. A value of false disables the quota and deletes existing quota rules.
        self.enabled = enabled
        # The quota limit type. This field is required and validated by the backend when the quota is enabled. Fixed value: token.
        self.limit_type = limit_type
        # The statistical period for the quota. This field is required and validated by the backend when the quota is enabled. Valid values: day (daily) and month (monthly).
        self.period_type = period_type
        # The maximum number of tokens allowed to be consumed within a single period. This field is required and validated by the backend when the quota is enabled. The value must be greater than 0.
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

class UpdateManagedAgentRequestBodyHarness(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateManagedAgentRequestBodyHarnessConfiguration = None,
        type: str = None,
    ):
        # The runtime framework configuration.
        self.configuration = configuration
        # The type of the runtime framework.
        self.type = type

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.UpdateManagedAgentRequestBodyHarnessConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateManagedAgentRequestBodyHarnessConfiguration(DaraModel):
    def __init__(
        self,
        connector_service_account_key: str = None,
        connector_service_account_name: str = None,
    ):
        # The connector service account key.
        self.connector_service_account_key = connector_service_account_key
        # The connector service account name.
        self.connector_service_account_name = connector_service_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_service_account_key is not None:
            result['connectorServiceAccountKey'] = self.connector_service_account_key

        if self.connector_service_account_name is not None:
            result['connectorServiceAccountName'] = self.connector_service_account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectorServiceAccountKey') is not None:
            self.connector_service_account_key = m.get('connectorServiceAccountKey')

        if m.get('connectorServiceAccountName') is not None:
            self.connector_service_account_name = m.get('connectorServiceAccountName')

        return self

class UpdateManagedAgentRequestBodyEnvironment(DaraModel):
    def __init__(
        self,
        credential_references: List[main_models.UpdateManagedAgentRequestBodyEnvironmentCredentialReferences] = None,
        variables: List[main_models.UpdateManagedAgentRequestBodyEnvironmentVariables] = None,
    ):
        # The list of credential references.
        self.credential_references = credential_references
        # The list of environment variables.
        self.variables = variables

    def validate(self):
        if self.credential_references:
            for v1 in self.credential_references:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
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

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credential_references = []
        if m.get('credentialReferences') is not None:
            for k1 in m.get('credentialReferences'):
                temp_model = main_models.UpdateManagedAgentRequestBodyEnvironmentCredentialReferences()
                self.credential_references.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.UpdateManagedAgentRequestBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateManagedAgentRequestBodyEnvironmentVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        # 
        # This parameter is required.
        self.name = name
        # The value of the environment variable.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class UpdateManagedAgentRequestBodyEnvironmentCredentialReferences(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
    ):
        # The credential ID.
        # 
        # This parameter is required.
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

class UpdateManagedAgentRequestBodyAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The subdirectory under /mnt/agenticfs/ in the container. This field is required for each mount item and validated by the backend. Mount targets must not overlap or have parent-child overrides.
        self.mount_path = mount_path
        # The existing non-empty relative directory under the access point. This field is required for each mount item and validated by the backend. Root directories, absolute paths, and parent directory segments are not allowed.
        self.path = path
        # Specifies whether to mount the file system in read-only mode. If omitted, the default value is false. This does not apply the read-only policy of the RAM role.
        self.read_only = read_only
        # The domain name of the access point. This field is required for each mount item and validated by the backend. Do not include the protocol, port, or path. Use the DomainName value from the NAS ListAccessPoints response.
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path

        if self.path is not None:
            result['path'] = self.path

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        if self.server is not None:
            result['server'] = self.server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        if m.get('server') is not None:
            self.server = m.get('server')

        return self

