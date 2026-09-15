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
        # The business status code. The value SUCCESS is returned if the request is successful.
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
        # The runtime harness of the managed agent. Valid values: qwenpaw and qodercli.
        self.harness = harness
        # The agent instruction that guides the behavior of the agent.
        self.instruction = instruction
        # The latest specification version number.
        self.latest_spec_version = latest_spec_version
        # The status of the latest version.
        self.latest_version_status = latest_version_status
        # The model configuration.
        self.model = model
        # The name of the managed agent.
        self.name = name
        # The network configuration.
        self.network = network
        # The list of OSS mounts. A maximum of 10 entries are supported.
        self.oss_mounts = oss_mounts
        # The region ID.
        self.region_id = region_id
        # The runtime configuration.
        self.runtime = runtime
        # The instance count of the managed agent grouped by sandbox phase. Current keys: PENDING (being created or initialized), RUNNING (running), HIBERNATING (entering hibernation), HIBERNATED (hibernated), RESUMING (resuming), TERMINATING (being terminated), and FAILED (runtime failure). Only phases that actually exist are returned. A missing key indicates a count of 0. This field is a dynamic map and new keys may be added in the future. You can use FAILED > 0 to determine whether abnormal instances exist.
        self.sandbox_phase_counts = sandbox_phase_counts
        # The list of skill configurations.
        self.skills = skills
        # The status of the managed agent.
        self.status = status
        # The list of sub-agent configurations.
        self.sub_agents = sub_agents
        # The template configuration.
        self.template = template
        # The list of tool configurations.
        self.tools = tools
        # The update time in RFC 3339 format.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
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
            temp_model = main_models.UpdateManagedAgentResponseBodyDataTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class UpdateManagedAgentResponseBodyDataTemplateAiRegistry(DaraModel):
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
        # The Sandbox auto scaling and session configuration.
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
        # Specifies whether to enable auto scaling. Required when hpa is present as validated by the backend.
        self.enabled = enabled
        # The maximum number of active sessions per Sandbox. Required when hpa is present as validated by the backend.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of Sandboxes. Required when HPA is enabled and must be no less than the minimum value.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of Sandboxes. Required when HPA is enabled.
        self.min_sandbox_count = min_sandbox_count
        # The session reclamation time after inactivity, in seconds. Required when hpa is present as validated by the backend.
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

class UpdateManagedAgentResponseBodyDataOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The OSS bucket name. Each mount item is validated as required by the backend.
        self.bucket_name = bucket_name
        # The absolute mount path in the container. Each mount item is validated as required by the backend.
        self.mount_path = mount_path
        # The relative object prefix in the bucket. If not specified, the entire bucket is mounted.
        self.path = path
        # Specifies whether to mount as read-only. Default value: false.
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
        # Specifies whether VPC access is allowed.
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
        # Specifies whether public network access is allowed.
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
    ):
        # The model connection ID.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # The upstream model name.
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

class UpdateManagedAgentResponseBodyDataHarness(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateManagedAgentResponseBodyDataHarnessConfiguration = None,
        type: str = None,
    ):
        # The Connector binding configuration for the qodercli harness.
        self.configuration = configuration
        # The type of the runtime harness. Valid values: qwenpaw and qodercli. When the type is qodercli, binding is performed based on configuration.connectorServiceAccountKey, and the name is also populated during queries.
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
        # The Key ID used to bind a Service Account Key of the QoderCLI Connector. This parameter can be omitted when only one key exists, but is required when multiple keys exist.
        self.connector_service_account_key = connector_service_account_key
        # The Connector Key name that is populated during queries. This value is not used as a binding reference during writes.
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

