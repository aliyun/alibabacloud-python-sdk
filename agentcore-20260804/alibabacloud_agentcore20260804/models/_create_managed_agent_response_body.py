# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateManagedAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateManagedAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. A value of SUCCESS indicates success.
        self.code = code
        # The information about the managed Harness agent after creation.
        self.data = data
        # The HTTP status code. A value of 200 indicates success.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.CreateManagedAgentResponseBodyData()
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

class CreateManagedAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_scope: str = None,
        agent_id: str = None,
        agentic_fs_mounts: List[main_models.CreateManagedAgentResponseBodyDataAgenticFsMounts] = None,
        configured_skills: List[main_models.CreateManagedAgentResponseBodyDataConfiguredSkills] = None,
        context_configuration: main_models.CreateManagedAgentResponseBodyDataContextConfiguration = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        effective_context_configuration: main_models.CreateManagedAgentResponseBodyDataEffectiveContextConfiguration = None,
        environment: main_models.CreateManagedAgentResponseBodyDataEnvironment = None,
        harness: main_models.CreateManagedAgentResponseBodyDataHarness = None,
        instruction: str = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        model: main_models.CreateManagedAgentResponseBodyDataModel = None,
        name: str = None,
        network: main_models.CreateManagedAgentResponseBodyDataNetwork = None,
        oss_mounts: List[main_models.CreateManagedAgentResponseBodyDataOssMounts] = None,
        prompt_variables: List[main_models.CreateManagedAgentResponseBodyDataPromptVariables] = None,
        region_id: str = None,
        runtime: main_models.CreateManagedAgentResponseBodyDataRuntime = None,
        sandbox_phase_counts: Dict[str, int] = None,
        skills: List[main_models.CreateManagedAgentResponseBodyDataSkills] = None,
        status: str = None,
        sub_agents: List[main_models.CreateManagedAgentResponseBodyDataSubAgents] = None,
        template: main_models.CreateManagedAgentResponseBodyDataTemplate = None,
        tools: List[main_models.CreateManagedAgentResponseBodyDataTools] = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The inbound access mode.
        self.access_mode = access_mode
        # The user access scope.
        self.access_scope = access_scope
        # The managed Harness agent ID.
        self.agent_id = agent_id
        # The NAS storage mount configuration. Currently, the AgenticFS type is supported, which is used to mount file directories in the access point to the agent runtime instance. For NAS mounts, a maximum of 10 items are allowed in total including ossMounts.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The explicitly configured skills.
        self.configured_skills = configured_skills
        # The target configuration accepted by the managed agent, which does not mean it has taken effect at runtime. This field is used in the detail responses of CreateManagedAgent, UpdateManagedAgent, and GetManagedAgent. In the configuration of a fixed version, it represents the configuration snapshot saved for that version. A returned object with enabled:false indicates that the configuration is disabled. The absence of the entire object indicates that the response does not provide the configuration.
        self.context_configuration = context_configuration
        # The creation mode.
        self.create_mode = create_mode
        # The creation time in RFC 3339 format.
        self.created_at = created_at
        # The deployment type.
        self.deploy_type = deploy_type
        # The description of the managed Harness agent.
        self.description = description
        # Read-only. This field is provided only by GetManagedAgent when an effective version exists, and corresponds to the configuration snapshot of effectiveSpecVersion. When a new version is being prepared or fails to be published, it remains the original effective configuration. It is not returned before the first time it takes effect, or in CreateManagedAgent, UpdateManagedAgent, and the configuration of a fixed version. Omission does not mean it is disabled, and the client cannot automatically fill it with enabled:false.
        self.effective_context_configuration = effective_context_configuration
        # The environment configuration information.
        self.environment = environment
        # The agent runtime framework.
        self.harness = harness
        # The agent instruction, which is used to guide the behavior of the agent.
        self.instruction = instruction
        # The latest specification version number.
        self.latest_spec_version = latest_spec_version
        # The status of the latest version.
        self.latest_version_status = latest_version_status
        # The model configuration information.
        self.model = model
        # The name of the managed Harness agent.
        self.name = name
        # The network configuration information.
        self.network = network
        # The list of OSS mounts. A maximum of 10 items are supported.
        self.oss_mounts = oss_mounts
        # The prompt variable declaration.
        self.prompt_variables = prompt_variables
        # The region ID.
        self.region_id = region_id
        # The runtime configuration information.
        self.runtime = runtime
        # The instance counts of managed Harness agents by sandbox phase. Current keys: PENDING (creating or initializing), RUNNING (running), HIBERNATING (hibernating), HIBERNATED (hibernated), RESUMING (resuming), TERMINATING (terminating), and FAILED (failed at runtime). Only phases that actually occur are returned, and missing keys are treated as 0. This field is a dynamic map and new keys may be added in the future. The frontend can use FAILED > 0 to determine whether abnormal instances exist.
        self.sandbox_phase_counts = sandbox_phase_counts
        # The list of skill configurations.
        self.skills = skills
        # The status of the managed Harness agent.
        self.status = status
        # The list of sub-agent configurations.
        self.sub_agents = sub_agents
        # The template configuration information.
        self.template = template
        # The list of tool configurations.
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
        if self.context_configuration:
            self.context_configuration.validate()
        if self.effective_context_configuration:
            self.effective_context_configuration.validate()
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

        if self.context_configuration is not None:
            result['contextConfiguration'] = self.context_configuration.to_map()

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.effective_context_configuration is not None:
            result['effectiveContextConfiguration'] = self.effective_context_configuration.to_map()

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

        result['promptVariables'] = []
        if self.prompt_variables is not None:
            for k1 in self.prompt_variables:
                result['promptVariables'].append(k1.to_map() if k1 else None)

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
        if m.get('accessMode') is not None:
            self.access_mode = m.get('accessMode')

        if m.get('accessScope') is not None:
            self.access_scope = m.get('accessScope')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        self.agentic_fs_mounts = []
        if m.get('agenticFsMounts') is not None:
            for k1 in m.get('agenticFsMounts'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        self.configured_skills = []
        if m.get('configuredSkills') is not None:
            for k1 in m.get('configuredSkills'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataConfiguredSkills()
                self.configured_skills.append(temp_model.from_map(k1))

        if m.get('contextConfiguration') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataContextConfiguration()
            self.context_configuration = temp_model.from_map(m.get('contextConfiguration'))

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveContextConfiguration') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataEffectiveContextConfiguration()
            self.effective_context_configuration = temp_model.from_map(m.get('effectiveContextConfiguration'))

        if m.get('environment') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('harness') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataHarness()
            self.harness = temp_model.from_map(m.get('harness'))

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('model') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        self.prompt_variables = []
        if m.get('promptVariables') is not None:
            for k1 in m.get('promptVariables'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataPromptVariables()
                self.prompt_variables.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('runtime') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('sandboxPhaseCounts') is not None:
            self.sandbox_phase_counts = m.get('sandboxPhaseCounts')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_agents = []
        if m.get('subAgents') is not None:
            for k1 in m.get('subAgents'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataSubAgents()
                self.sub_agents.append(temp_model.from_map(k1))

        if m.get('template') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateManagedAgentResponseBodyDataTools(DaraModel):
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

class CreateManagedAgentResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.CreateManagedAgentResponseBodyDataTemplateAiRegistry = None,
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class CreateManagedAgentResponseBodyDataTemplateAiRegistry(DaraModel):
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

class CreateManagedAgentResponseBodyDataSubAgents(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        name: str = None,
        skills: List[main_models.CreateManagedAgentResponseBodyDataSubAgentsSkills] = None,
    ):
        # The instruction for the sub-agent.
        # 
        # This parameter is required.
        self.instruction = instruction
        # The name of the sub-agent.
        # 
        # This parameter is required.
        self.name = name
        # The list of skills for the sub-agent.
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
                temp_model = main_models.CreateManagedAgentResponseBodyDataSubAgentsSkills()
                self.skills.append(temp_model.from_map(k1))

        return self

class CreateManagedAgentResponseBodyDataSubAgentsSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the skill.
        self.name = name
        # The version of the skill.
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

class CreateManagedAgentResponseBodyDataSkills(DaraModel):
    def __init__(
        self,
        applied_version: str = None,
        from_template: bool = None,
        name: str = None,
        resolved_version: str = None,
        source_type: str = None,
        version: str = None,
        version_selector: main_models.CreateManagedAgentResponseBodyDataSkillsVersionSelector = None,
    ):
        # The effective runtime version. This field is read-only.
        self.applied_version = applied_version
        # Indicates whether the skill is from a fixed template. This field is read-only. Template items cannot be removed.
        self.from_template = from_template
        # The name of the skill.
        self.name = name
        # The current target version. This field is read-only.
        self.resolved_version = resolved_version
        # The source type of the skill.
        self.source_type = source_type
        # The current target version for legacy client compatibility. New clients use resolvedVersion and determine the effective runtime version based on appliedVersion.
        self.version = version
        # The version selector for the skill reference. Supports LABEL for tags and VERSION for specific versions. Defaults to LABEL/latest when omitted. Not applicable for STATIC sources.
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataSkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class CreateManagedAgentResponseBodyDataSkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the version selector.
        self.type = type
        # The value of the selector. For LABEL, specify the tag name, such as latest. For VERSION, specify the exact version number.
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

class CreateManagedAgentResponseBodyDataRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.CreateManagedAgentResponseBodyDataRuntimeCompute = None,
        hpa: main_models.CreateManagedAgentResponseBodyDataRuntimeHpa = None,
        session_policy: main_models.CreateManagedAgentResponseBodyDataRuntimeSessionPolicy = None,
    ):
        # The compute configuration.
        # 
        # This parameter is required.
        self.compute = compute
        # The sandbox auto-scaling and session configuration.
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class CreateManagedAgentResponseBodyDataRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The HTTP header name used for session affinity. This field takes effect when sessionPolicy.type is set to ISOLATED_HEADER_FIELD.
        self.header_name = header_name
        # The type of the session policy.
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

class CreateManagedAgentResponseBodyDataRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Indicates whether elastic auto-scaling is enabled in the current configuration.
        self.enabled = enabled
        # The maximum number of concurrent sessions per instance in the current configuration.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of instances in the current configuration.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of instances in the current configuration.
        self.min_sandbox_count = min_sandbox_count
        # The maximum session idle time in the current configuration, in seconds.
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

class CreateManagedAgentResponseBodyDataRuntimeCompute(DaraModel):
    def __init__(
        self,
        compute_class: str = None,
    ):
        # The compute specification.
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

class CreateManagedAgentResponseBodyDataPromptVariables(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
    ):
        # The default value.
        self.default_value = default_value
        # The variable description.
        self.description = description
        # The variable name.
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

class CreateManagedAgentResponseBodyDataOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The name of the OSS bucket. This field is required for each mount item and is validated by the backend.
        self.bucket_name = bucket_name
        # The absolute mount path in the container, such as `/data/train`. Mount targets cannot be duplicated or form parent-child overwrites, and must avoid platform-reserved directories.
        self.mount_path = mount_path
        # The non-empty relative directory prefix in the configured bucket.
        self.path = path
        # Specifies whether the mount is read-only. Default value: false.
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

class CreateManagedAgentResponseBodyDataNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.CreateManagedAgentResponseBodyDataNetworkAccessInternet = None,
        access_vpc: main_models.CreateManagedAgentResponseBodyDataNetworkAccessVpc = None,
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class CreateManagedAgentResponseBodyDataNetworkAccessVpc(DaraModel):
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

class CreateManagedAgentResponseBodyDataNetworkAccessInternet(DaraModel):
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

class CreateManagedAgentResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
        quota: main_models.CreateManagedAgentResponseBodyDataModelQuota = None,
        thinking_level: str = None,
    ):
        # The model connection ID.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        self.model_name = model_name
        # The model token quota configuration and usage status for the current period. This field is empty if no quota is configured.
        self.quota = quota
        # The thinking level. If not configured, the value defaults to default. Empty strings, null values, or omitted fields are handled according to the default behavior of the model and Harness. Valid values: off, low, medium, high, xhigh, and max. If this parameter is not passed or is null during creation, default is used. When updating and submitting the model configuration, if the thinking level is not passed or is null, it reverts to default. Except for off, which is converted to none, the value is passed to the runtime framework as-is without validating model support or automatically downgrading. If the model does not support the specified level, adjust the level accordingly.
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataModelQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('thinkingLevel') is not None:
            self.thinking_level = m.get('thinkingLevel')

        return self

class CreateManagedAgentResponseBodyDataModelQuota(DaraModel):
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
        # Indicates whether the quota is exceeded in the current period. This field is read-only and returned by the backend.
        self.over_limit = over_limit
        # The quota statistical period. A value of day indicates daily, and a value of month indicates monthly.
        self.period_type = period_type
        # The gateway quota rule status. This field is read-only and returned by the backend.
        self.rule_status = rule_status
        # The maximum number of tokens allowed to be consumed in a single period.
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

class CreateManagedAgentResponseBodyDataHarness(DaraModel):
    def __init__(
        self,
        configuration: main_models.CreateManagedAgentResponseBodyDataHarnessConfiguration = None,
        outdated_instance_count: int = None,
        type: str = None,
        version: str = None,
    ):
        # The runtime framework configuration.
        self.configuration = configuration
        # Returned only in queries. The server calculates this based on the complete instance distribution, which is not affected by the pagination and filtering of the instance list. It is empty when the image tag is missing, pagination is incomplete, or it cannot be confirmed, which is not equivalent to 0.
        self.outdated_instance_count = outdated_instance_count
        # The runtime framework type.
        self.type = type
        # Returned only in queries. Currently returns the pool target image tag. It is empty when it cannot be parsed, and cannot be replaced by the agent configuration version.
        self.version = version

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

        if self.outdated_instance_count is not None:
            result['outdatedInstanceCount'] = self.outdated_instance_count

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.CreateManagedAgentResponseBodyDataHarnessConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('outdatedInstanceCount') is not None:
            self.outdated_instance_count = m.get('outdatedInstanceCount')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class CreateManagedAgentResponseBodyDataHarnessConfiguration(DaraModel):
    def __init__(
        self,
        connector_service_account_key: str = None,
        connector_service_account_name: str = None,
    ):
        # The connector account key record ID bound to qodercli, which is not the original service account key.
        self.connector_service_account_key = connector_service_account_key
        # The connector account name bound to qodercli.
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

class CreateManagedAgentResponseBodyDataEnvironment(DaraModel):
    def __init__(
        self,
        credential_references: List[main_models.CreateManagedAgentResponseBodyDataEnvironmentCredentialReferences] = None,
        variables: List[main_models.CreateManagedAgentResponseBodyDataEnvironmentVariables] = None,
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
                temp_model = main_models.CreateManagedAgentResponseBodyDataEnvironmentCredentialReferences()
                self.credential_references.append(temp_model.from_map(k1))

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class CreateManagedAgentResponseBodyDataEnvironmentVariables(DaraModel):
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

class CreateManagedAgentResponseBodyDataEnvironmentCredentialReferences(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
    ):
        # The ID of the credential.
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

class CreateManagedAgentResponseBodyDataEffectiveContextConfiguration(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.CreateManagedAgentResponseBodyDataEffectiveContextConfigurationBindings] = None,
        enabled: bool = None,
    ):
        # Read-only resource references. This field may be omitted when no selection is made. A disabled configuration can still retain non-empty selections. You cannot determine whether the configuration is enabled solely based on whether the array is empty.
        self.bindings = bindings
        # Read-only. When the configuration object is returned, this field indicates the enabling status of the configuration. A value of false indicates that the configuration is disabled. The absence of the entire configuration object indicates that the response does not provide the configuration, which cannot be treated as false.
        self.enabled = enabled

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['bindings'].append(k1.to_map() if k1 else None)

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('bindings') is not None:
            for k1 in m.get('bindings'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataEffectiveContextConfigurationBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class CreateManagedAgentResponseBodyDataEffectiveContextConfigurationBindings(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        type: str = None,
    ):
        # The context resource ID in the current workspace.
        self.resource_id = resource_id
        # Read-only string. Currently known types are KNOWLEDGE_BASE (knowledge base) and DATA_CONNECTOR (data connector). The response may be extended with new types. The client should retain unknown values and should not fail to parse the entire response due to unknown types. New request types are subject to the actual support scope of the server.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateManagedAgentResponseBodyDataContextConfiguration(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.CreateManagedAgentResponseBodyDataContextConfigurationBindings] = None,
        enabled: bool = None,
    ):
        # Read-only resource references. This field may be omitted when no selection is made. A disabled configuration can still retain non-empty selections. You cannot determine whether the configuration is enabled solely based on whether the array is empty.
        self.bindings = bindings
        # Read-only. When the configuration object is returned, this field indicates the enabling status of the configuration. A value of false indicates that the configuration is disabled. The absence of the entire configuration object indicates that the response does not provide the configuration, which cannot be treated as false.
        self.enabled = enabled

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['bindings'].append(k1.to_map() if k1 else None)

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('bindings') is not None:
            for k1 in m.get('bindings'):
                temp_model = main_models.CreateManagedAgentResponseBodyDataContextConfigurationBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class CreateManagedAgentResponseBodyDataContextConfigurationBindings(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        type: str = None,
    ):
        # The context resource ID in the current workspace.
        self.resource_id = resource_id
        # Read-only string. Currently known types are KNOWLEDGE_BASE (knowledge base) and DATA_CONNECTOR (data connector). The response may be extended with new types. The client should retain unknown values and should not fail to parse the entire response due to unknown types. New request types are subject to the actual support scope of the server.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateManagedAgentResponseBodyDataConfiguredSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_type: str = None,
        version: str = None,
        version_selector: main_models.CreateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector = None,
    ):
        # The name of the skill in the Workspace AI Registry.
        # 
        # This parameter is required.
        self.name = name
        # The source type of the skill.
        self.source_type = source_type
        # The legacy compatibility field. New requests use sourceType and versionSelector.
        self.version = version
        # The version selector for the skill reference. Supports LABEL for tags and VERSION for specific versions. Defaults to LABEL/latest when omitted. Not applicable for STATIC sources.
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
            temp_model = main_models.CreateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector()
            self.version_selector = temp_model.from_map(m.get('versionSelector'))

        return self

class CreateManagedAgentResponseBodyDataConfiguredSkillsVersionSelector(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the version selector.
        self.type = type
        # The value of the selector. For LABEL, specify the tag name, such as latest. For VERSION, specify the exact version number.
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

class CreateManagedAgentResponseBodyDataAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The absolute mount path in the container, such as `/data/train`. Mount targets cannot be duplicated or form parent-child overwrites, and must avoid platform-reserved directories.
        self.mount_path = mount_path
        # The existing non-empty relative directory under the access point. This is a required field validated by the backend for each mount item. Root directories, absolute paths, or parent directory segments are not allowed.
        self.path = path
        # Specifies whether the mount is read-only. If omitted, the default value is false. This is not the read-only policy of a RAM role.
        self.read_only = read_only
        # The access point domain name. This is a required field validated by the backend for each mount item. It does not contain a protocol, port, or path. Use the `DomainName` from the NAS `ListAccessPoints` response.
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

