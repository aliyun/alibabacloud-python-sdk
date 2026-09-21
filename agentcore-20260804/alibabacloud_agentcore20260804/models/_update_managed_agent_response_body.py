# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateManagedAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateManagedAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value is SUCCESS when the operation succeeds.
        self.code = code
        # The details of the managed agent.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The message returned for the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateManagedAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agentic_fs_mounts: List[main_models.UpdateManagedAgentResponseBodyDataAgenticFsMounts] = None,
        configured_skills: List[main_models.UpdateManagedAgentResponseBodyDataConfiguredSkills] = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        environment: main_models.UpdateManagedAgentResponseBodyDataEnvironment = None,
        harness: main_models.UpdateManagedAgentResponseBodyDataHarness = None,
        instruction: str = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        model: main_models.UpdateManagedAgentResponseBodyDataModel = None,
        name: str = None,
        network: main_models.UpdateManagedAgentResponseBodyDataNetwork = None,
        oss_mounts: List[main_models.UpdateManagedAgentResponseBodyDataOssMounts] = None,
        region_id: str = None,
        runtime: main_models.UpdateManagedAgentResponseBodyDataRuntime = None,
        sandbox_phase_counts: Dict[str, int] = None,
        skills: List[main_models.UpdateManagedAgentResponseBodyDataSkills] = None,
        status: str = None,
        sub_agents: List[main_models.UpdateManagedAgentResponseBodyDataSubAgents] = None,
        template: main_models.UpdateManagedAgentResponseBodyDataTemplate = None,
        tools: List[main_models.UpdateManagedAgentResponseBodyDataTools] = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The managed agent ID.
        self.agent_id = agent_id
        # The AgenticFS additional mount list. The total number of items combined with ossMounts cannot exceed 10.
        self.agentic_fs_mounts = agentic_fs_mounts
        # Contains only skills that are added or overridden by the user. Skills inherited from templates are not included. The resource model reads this field to preserve update semantics. The skills field in the request is still used for creation and update operations.
        self.configured_skills = configured_skills
        # The creation mode.
        self.create_mode = create_mode
        # The creation time in RFC 3339 format.
        self.created_at = created_at
        # The deployment type.
        self.deploy_type = deploy_type
        # The description of the managed agent.
        self.description = description
        # The environment configuration.
        self.environment = environment
        # The agent runtime harness.
        self.harness = harness
        # The agent instruction that guides the behavior of the agent.
        self.instruction = instruction
        # The latest specification version number.
        self.latest_spec_version = latest_spec_version
        # The latest version status.
        self.latest_version_status = latest_version_status
        # The model configuration.
        self.model = model
        # The name of the managed agent.
        self.name = name
        # The network configuration.
        self.network = network
        # The OSS mount list. A maximum of 10 items are supported.
        self.oss_mounts = oss_mounts
        # The region ID.
        self.region_id = region_id
        # The runtime configuration information.
        self.runtime = runtime
        # The instance counts of the managed agent grouped by sandbox phase. Current keys: PENDING (being created or initialized), RUNNING (running), HIBERNATING (entering hibernation), HIBERNATED (hibernated), RESUMING (resuming), TERMINATING (being terminated), FAILED (runtime failure). Only phases that actually occur are returned. Missing keys are treated as 0. This field is a dynamic mapping and new keys may be added in the future. The frontend can use FAILED > 0 to determine whether abnormal instances exist.
        self.sandbox_phase_counts = sandbox_phase_counts
        # The skill configuration list.
        self.skills = skills
        # The status of the managed agent.
        self.status = status
        # The sub-agent configuration list.
        self.sub_agents = sub_agents
        # The template configuration information.
        self.template = template
        # The tool configuration list.
        self.tools = tools
        # The update time in RFC 3339 format.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.agentic_fs_mounts:
            for v1 in self.agentic_fs_mounts:
                 if v1:
                    v1.validate()
        if self.configured_skills:
            for v1 in self.configured_skills:
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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        result['agenticFsMounts'] = []
        if self.agentic_fs_mounts is not None:
            for k1 in self.agentic_fs_mounts:
                result['agenticFsMounts'].append(k1.to_map() if k1 else None)

        result['configuredSkills'] = []
        if self.configured_skills is not None:
            for k1 in self.configured_skills:
                result['configuredSkills'].append(k1.to_map() if k1 else None)

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.harness is not None:
            result['harness'] = self.harness.to_map()

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.latest_version_status is not None:
            result['latestVersionStatus'] = self.latest_version_status

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

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.sandbox_phase_counts is not None:
            result['sandboxPhaseCounts'] = self.sandbox_phase_counts

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

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

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        self.agentic_fs_mounts = []
        if m.get('agenticFsMounts') is not None:
            for k1 in m.get('agenticFsMounts'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        self.configured_skills = []
        if m.get('configuredSkills') is not None:
            for k1 in m.get('configuredSkills'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataConfiguredSkills()
                self.configured_skills.append(temp_model.from_map(k1))

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environment') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('harness') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataHarness()
            self.harness = temp_model.from_map(m.get('harness'))

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('model') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('runtime') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('sandboxPhaseCounts') is not None:
            self.sandbox_phase_counts = m.get('sandboxPhaseCounts')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_agents = []
        if m.get('subAgents') is not None:
            for k1 in m.get('subAgents'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataSubAgents()
                self.sub_agents.append(temp_model.from_map(k1))

        if m.get('template') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateManagedAgentResponseBodyDataTools(DaraModel):
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

class UpdateManagedAgentResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.UpdateManagedAgentResponseBodyDataTemplateAiRegistry = None,
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class UpdateManagedAgentResponseBodyDataTemplateAiRegistry(DaraModel):
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

class UpdateManagedAgentResponseBodyDataSubAgents(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        name: str = None,
    ):
        # The sub-agent instruction.
        # 
        # This parameter is required.
        self.instruction = instruction
        # The sub-agent name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class UpdateManagedAgentResponseBodyDataSkills(DaraModel):
    def __init__(
        self,
        applied_version: str = None,
        from_template: bool = None,
        name: str = None,
        resolved_version: str = None,
        source_type: str = None,
        version: str = None,
        version_selector: main_models.UpdateManagedAgentResponseBodyDataSkillsVersionSelector = None,
    ):
        # The version that has taken effect at runtime. This field is read-only.
        self.applied_version = applied_version
        # Indicates whether the skill originates from a fixed template. This field is read-only. Template items cannot be removed.
        self.from_template = from_template
        # The skill name.
        self.name = name
        # The current target version. This field is read-only.
        self.resolved_version = resolved_version
        # The skill source type. Valid values:
        # - REFERENCE: references AI Registry.
        # - STATIC: statically bundled with the package.
        self.source_type = source_type
        # The skill version.
        self.version = version
        # The referenced version selector. Defaults to LABEL/latest if omitted.
        self.version_selector = version_selector

    def validate(self):
        if self.version_selector:
            self.version_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_version is not None:
            result['appliedVersion'] = self.applied_version

        if self.from_template is not None:
            result['fromTemplate'] = self.from_template

        if self.name is not None:
            result['name'] = self.name

        if self.resolved_version is not None:
            result['resolvedVersion'] = self.resolved_version

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.version is not None:
            result['version'] = self.version

        if self.version_selector is not None:
            result['versionSelector'] = self.version_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appliedVersion') is not None:
            self.applied_version = m.get('appliedVersion')

        if m.get('fromTemplate') is not None:
            self.from_template = m.get('fromTemplate')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resolvedVersion') is not None:
            self.resolved_version = m.get('resolvedVersion')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionSelector') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataSkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class UpdateManagedAgentResponseBodyDataSkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The version selector type. Valid values:
        # - LABEL: selects by label.
        # - VERSION: selects by specific version.
        self.type = type
        # The selector value. If the type is LABEL, specify a label name such as latest. If the type is VERSION, specify a specific version number.
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

class UpdateManagedAgentResponseBodyDataRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.UpdateManagedAgentResponseBodyDataRuntimeCompute = None,
        hpa: main_models.UpdateManagedAgentResponseBodyDataRuntimeHpa = None,
        session_policy: main_models.UpdateManagedAgentResponseBodyDataRuntimeSessionPolicy = None,
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class UpdateManagedAgentResponseBodyDataRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The HTTP header name used for session affinity. Takes effect when sessionPolicy.type is set to ISOLATED_HEADER_FIELD.
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

class UpdateManagedAgentResponseBodyDataRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Specifies whether to enable auto scaling. Required when hpa is present, as validated by the backend.
        self.enabled = enabled
        # The maximum number of active sessions per sandbox. Required when hpa is present, as validated by the backend.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of sandboxes. Required when HPA is enabled and must be no less than the minimum value.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of sandboxes. Required when HPA is enabled.
        self.min_sandbox_count = min_sandbox_count
        # The time in seconds before an inactive session is reclaimed. Required when hpa is present, as validated by the backend.
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

class UpdateManagedAgentResponseBodyDataRuntimeCompute(DaraModel):
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

class UpdateManagedAgentResponseBodyDataOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The OSS bucket name. Required for each mount entry as validated by the backend.
        self.bucket_name = bucket_name
        # The absolute mount path in the container. Required for each mount entry as validated by the backend.
        self.mount_path = mount_path
        # The relative object prefix within the bucket. If not specified, the entire bucket is mounted.
        self.path = path
        # Specifies whether to mount in read-only mode. Default value: false.
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

class UpdateManagedAgentResponseBodyDataNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.UpdateManagedAgentResponseBodyDataNetworkAccessInternet = None,
        access_vpc: main_models.UpdateManagedAgentResponseBodyDataNetworkAccessVpc = None,
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.UpdateManagedAgentResponseBodyDataNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class UpdateManagedAgentResponseBodyDataNetworkAccessVpc(DaraModel):
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

class UpdateManagedAgentResponseBodyDataNetworkAccessInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow public network access.
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

class UpdateManagedAgentResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
        quota: main_models.UpdateManagedAgentResponseBodyDataModelQuota = None,
    ):
        # The model connection ID.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        self.model_name = model_name
        # The model token quota configuration and the quota usage status for the current period. This field is empty if no quota is configured.
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataModelQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class UpdateManagedAgentResponseBodyDataModelQuota(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_type: str = None,
        over_limit: bool = None,
        period_type: str = None,
        rule_status: str = None,
        usage_limit: int = None,
        used_amount: int = None,
    ):
        # Indicates whether the quota is enabled. This field is not returned if no quota is configured.
        self.enabled = enabled
        # The quota limit type. Currently, only token is supported.
        self.limit_type = limit_type
        # Indicates whether the quota has been exceeded in the current period. This field is read-only and returned by the backend.
        self.over_limit = over_limit
        # The quota statistical period. A value of day indicates daily. A value of month indicates monthly.
        self.period_type = period_type
        # The gateway quota rule status. This field is read-only and returned by the backend.
        self.rule_status = rule_status
        # The maximum number of tokens that can be consumed in a single period.
        self.usage_limit = usage_limit
        # The number of tokens consumed in the current period. This field is read-only and returned by the backend.
        self.used_amount = used_amount

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

        if self.over_limit is not None:
            result['overLimit'] = self.over_limit

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        if self.used_amount is not None:
            result['usedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('overLimit') is not None:
            self.over_limit = m.get('overLimit')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        if m.get('usedAmount') is not None:
            self.used_amount = m.get('usedAmount')

        return self

class UpdateManagedAgentResponseBodyDataHarness(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateManagedAgentResponseBodyDataHarnessConfiguration = None,
        type: str = None,
    ):
        # The runtime harness configuration.
        self.configuration = configuration
        # The runtime harness type.
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataHarnessConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateManagedAgentResponseBodyDataHarnessConfiguration(DaraModel):
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

class UpdateManagedAgentResponseBodyDataEnvironment(DaraModel):
    def __init__(
        self,
        credential_references: List[main_models.UpdateManagedAgentResponseBodyDataEnvironmentCredentialReferences] = None,
        variables: List[main_models.UpdateManagedAgentResponseBodyDataEnvironmentVariables] = None,
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
                temp_model = main_models.UpdateManagedAgentResponseBodyDataEnvironmentCredentialReferences()
                self.credential_references.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.UpdateManagedAgentResponseBodyDataEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateManagedAgentResponseBodyDataEnvironmentVariables(DaraModel):
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

class UpdateManagedAgentResponseBodyDataEnvironmentCredentialReferences(DaraModel):
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

class UpdateManagedAgentResponseBodyDataConfiguredSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_type: str = None,
        version: str = None,
        version_selector: main_models.UpdateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector = None,
    ):
        # The skill name in the Workspace AI Registry.
        # 
        # This parameter is required.
        self.name = name
        # The skill source type. Valid values:
        # - REFERENCE: references AI Registry.
        # - STATIC: statically bundled with the package.
        self.source_type = source_type
        # A legacy compatibility field. Use sourceType and versionSelector for new requests.
        self.version = version
        # The referenced version selector. Defaults to LABEL/latest if omitted. Currently supports LABEL/latest.
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class UpdateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The version selector type. Valid values:
        # - LABEL: selects by label.
        # - VERSION: selects by specific version.
        self.type = type
        # The selector value. If the type is LABEL, specify a label name such as latest. If the type is VERSION, specify a specific version number.
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

class UpdateManagedAgentResponseBodyDataAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The subdirectory under /mnt/agenticfs/ in the container. Required for each mount entry as validated by the backend. Mount targets must not be duplicated or have parent-child overlaps.
        self.mount_path = mount_path
        # The non-empty relative directory that exists under the AccessPoint. Required for each mount entry as validated by the backend. Root directory, absolute paths, and parent directory segments are not allowed.
        self.path = path
        # Specifies whether to mount in read-only mode. Default value: false. This is not the RAM role read-only policy.
        self.read_only = read_only
        # The AccessPoint domain name. Required for each mount entry as validated by the backend. Do not include the protocol, port, or path. Use the DomainName from the NAS ListAccessPoints response.
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

