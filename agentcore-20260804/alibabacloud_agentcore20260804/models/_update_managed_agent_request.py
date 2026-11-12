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
        # The reserved query parameter. The backend currently does not provide idempotency guarantees for deduplication or restoring original acceptance results based on this identifier.
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
        # The inbound access mode.
        self.access_mode = access_mode
        # The user access scope.
        self.access_scope = access_scope
        # The NAS storage mount configuration. Currently, only the AgenticFS type is supported, which is used to mount file directories in access points to agent runtime instances. This is the list of AgenticFS directory mounts. The total number of AgenticFS mounts and OSS mounts cannot exceed 10. If omitted or set to `[]` during creation, no mounts are configured. During an update, omitting this field retains the original configuration, and setting it to `[]` clears the mounts. `null` is not accepted.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The description of the managed Harness agent.
        self.description = description
        # The environment configuration.
        self.environment = environment
        # The runtime harness object. If omitted, the original harness is retained. If provided, the `type` must be the same as the one specified during creation. You can update the account binding for the same type of harness.
        self.harness = harness
        # The agent instruction, which is used to guide the behavior of the agent.
        self.instruction = instruction
        # The model configuration.
        self.model = model
        # The name of the managed Harness agent.
        self.name = name
        # The runtime network configuration. If provided, both accessInternet.enabled and accessVpc.enabled must be included. Actual access is subject to workspace network restrictions.
        self.network = network
        # The OSS directory mount list. A maximum of 10 items in total with agenticFsMounts. The entire list is replaced during an update. Pass [] to clear the list.
        self.oss_mounts = oss_mounts
        # The prompt variable declarations.
        self.prompt_variables = prompt_variables
        # The runtime configuration. If the entire object is omitted, the original configuration is retained. If provided, both compute and sessionPolicy must be specified. Omitted fields in hpa use default values.
        self.runtime = runtime
        # The skill configuration list.
        self.skills = skills
        # The sub-agent configuration list.
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
        # The name of the tool.
        # 
        # This parameter is required.
        self.name = name
        # The type of the tool.
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
        # The sub-agent skill list.
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
        # The skill source type. REFERENCE references the AI Registry. STATIC is statically provided with the package.
        self.source_type = source_type
        # The skill version field for legacy request compatibility. For new requests, use sourceType and versionSelector. Do not submit this field in combination with sourceType.
        self.version = version
        # The skill reference version selector. Supports LABEL for tags and VERSION for specific versions. Defaults to LABEL/latest when omitted. Selectors are not provided for STATIC sources.
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
        # The version selector type. LABEL selects by tag. VERSION selects by specific version.
        self.type = type
        # The selector value. For LABEL, it is the tag name (such as latest). For VERSION, it is the specific version number.
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
        # The elastic scaling and session configuration. Omitted fields use default values. To retain the original policy during an update, submit the complete hpa object or omit the entire runtime object.
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
        # The name of the request header for session identification. Required when type is ISOLATED_HEADER_FIELD. Must be a valid HTTP request header name. Do not specify for other policies.
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
        # Specifies whether to enable elastic scaling. Defaults to false when omitted.
        self.enabled = enabled
        # The maximum number of concurrent sessions allowed per instance. Valid values: 1 to 20. Defaults to 20 when omitted.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The upper limit of the number of instances. Valid values: 0 to 100. Defaults to 10 when omitted. Cannot be less than minSandboxCount.
        self.max_sandbox_count = max_sandbox_count
        # The lower limit of the number of instances. Valid values: 0 to 100. Defaults to 1 when omitted. Cannot be greater than maxSandboxCount.
        self.min_sandbox_count = min_sandbox_count
        # The maximum idle time for a session, in seconds. Valid values: 60 to 86400. Defaults to 600 when omitted.
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
        # The compute specifications.
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
        # The OSS bucket name. Required and validated by the backend for each mount item.
        self.bucket_name = bucket_name
        # The absolute mount path in the container, such as `/data/train`. Mount targets cannot be duplicated or form parent-child overwrites, and must avoid platform reserved directories.
        self.mount_path = mount_path
        # The non-empty relative object directory prefix within the bucket. Required for each mount item.
        self.path = path
        # Specifies whether to mount as read-only. Defaults to false if not specified.
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
        # Specifies whether to allow access to the VPC.
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
        # Specifies whether to allow access to the Internet.
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
        thinking_level: str = None,
    ):
        # For qwenpaw, use the workspace model connection ID. For qodercli, use the available model identifier returned by ListConnectorModels.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # For qwenpaw, use the name of the upstream model created under the model connection. This field is required. For qodercli, this field can be omitted.
        self.model_name = model_name
        # The model token quota configuration. If not provided, no quota is configured.
        self.quota = quota
        # Valid values: `off`, `low`, `medium`, `high`, `xhigh`, and `max`. If not provided or set to `null` during creation, `default` is used. When updating and submitting the model configuration, if the thinking level is not provided or is `null`, it reverts to `default`. Except for `off` which is converted to `none`, the value is passed to the runtime harness as-is. The system does not validate model support or automatically downgrade the level. If the model does not support the specified level, adjust the level accordingly.
        self.thinking_level = thinking_level

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

        if self.thinking_level is not None:
            result['thinkingLevel'] = self.thinking_level

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

        if m.get('thinkingLevel') is not None:
            self.thinking_level = m.get('thinkingLevel')

        return self

class UpdateManagedAgentRequestBodyModelQuota(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_type: str = None,
        period_type: str = None,
        usage_limit: int = None,
    ):
        # Specifies whether to enable the token quota. If not specified, the default value is `true`. Setting this field to `false` disables the quota and deletes existing quota rules.
        self.enabled = enabled
        # The quota limit type. This field is required and validated by the backend when the quota is enabled. Fixed value: `token`.
        self.limit_type = limit_type
        # The statistical period for the quota. This field is required and validated by the backend when the quota is enabled. Valid values: `day` (daily) and `month` (monthly).
        self.period_type = period_type
        # The maximum number of tokens allowed to be consumed in a single period. This field is required and validated by the backend when the quota is enabled. The value must be greater than 0.
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
        # The runtime harness configuration.
        self.configuration = configuration
        # The type of the runtime harness. This field is required when `harness` is provided, and must be consistent with the one specified during creation.
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
        # The account key record ID in the qodercli connector. You can query it by calling ListConnectors. It is not the original key. This field can be omitted if there is only one record, but must be specified if there are multiple records. Do not specify this field for qwenpaw.
        self.connector_service_account_key = connector_service_account_key
        # The name of the connector account bound to qodercli. Do not specify this field for qwenpaw.
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
        # The credential reference list.
        self.credential_references = credential_references
        # The environment variable list.
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
        # The environment variable name.
        # 
        # This parameter is required.
        self.name = name
        # The environment variable value.
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
        # The absolute mount path in the container, such as `/data/train`. Mount targets cannot be duplicated or form parent-child overwrites, and must avoid platform reserved directories.
        self.mount_path = mount_path
        # An existing non-empty relative directory under the access point. This field is required and validated by the backend for each mount item. Root directories, absolute paths, and parent directory segments are not allowed.
        self.path = path
        # Specifies whether the mount is read-only. If omitted, the default value is `false`. This is not a RAM role read-only policy.
        self.read_only = read_only
        # The domain name of the access point. This field is required and validated by the backend for each mount item. It must not contain a protocol, port, or path. Use the DomainName value from the NAS ListAccessPoints response.
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

