# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetCustomAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request result code. The value is SUCCESS if the request is successful.
        # 
        # This parameter is required.
        self.code = code
        # The latest submitted configuration and status of the custom agent. To determine whether the configuration has taken effect, refer to latestVersionStatus.
        # 
        # This parameter is required.
        self.data = data
        # The HTTP status code of the request. A value of 200 indicates success.
        # 
        # This parameter is required.
        self.http_status_code = http_status_code
        # The processing result description of the request. A value of success indicates success.
        # 
        # This parameter is required.
        self.message = message
        # The unique identifier of the request, which is used to locate and troubleshoot issues.
        # 
        # This parameter is required.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of true indicates that the request was successful. A successful creation, update, or deletion does not mean that the background operation is complete.
        # 
        # This parameter is required.
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
            temp_model = main_models.GetCustomAgentResponseBodyData()
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

class GetCustomAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agentic_fs_mounts: List[main_models.GetCustomAgentResponseBodyDataAgenticFsMounts] = None,
        artifact: main_models.GetCustomAgentResponseBodyDataArtifact = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        effective_spec_version: int = None,
        environment: main_models.GetCustomAgentResponseBodyDataEnvironment = None,
        health_check: main_models.GetCustomAgentResponseBodyDataHealthCheck = None,
        image_cache_id: str = None,
        latest_execution_error: main_models.GetCustomAgentResponseBodyDataLatestExecutionError = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        logging: main_models.GetCustomAgentResponseBodyDataLogging = None,
        name: str = None,
        network: main_models.GetCustomAgentResponseBodyDataNetwork = None,
        observability: main_models.GetCustomAgentResponseBodyDataObservability = None,
        oss_mounts: List[main_models.GetCustomAgentResponseBodyDataOssMounts] = None,
        protocol: List[main_models.GetCustomAgentResponseBodyDataProtocol] = None,
        region_id: str = None,
        role_arn: str = None,
        runtime: main_models.GetCustomAgentResponseBodyDataRuntime = None,
        sandbox_phase_counts: Dict[str, int] = None,
        status: str = None,
        updated_at: str = None,
        use_image_cache: bool = None,
        workspace_id: str = None,
    ):
        # The unique identifier of the custom agent. You can obtain this identifier from the response of CreateCustomAgent or ListCustomAgents.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The latest submitted list of additional AgenticFS mounts.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The latest submitted deployment artifact configuration, including the service listening port and ACR container image. To determine whether the configuration has taken effect, refer to latestVersionStatus.
        self.artifact = artifact
        # The creation method of the agent. CUSTOM is returned for custom agents.
        self.create_mode = create_mode
        # The creation time of the agent. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.created_at = created_at
        # The deployment method of the agent. MANAGED is returned for custom agents because they are deployed and managed by the platform.
        self.deploy_type = deploy_type
        # The description of the agent\\"s purpose.
        self.description = description
        # The value is null if no effective version exists. Do not use latestSpecVersion as a substitute. This field cannot be used to release the occupation protection of old cached instances.
        # 
        # This parameter is required.
        self.effective_spec_version = effective_spec_version
        # The environment variable configuration for the agent process.
        self.environment = environment
        # The HTTP health check configuration of the agent. The value is empty if not configured.
        self.health_check = health_check
        # This field is always returned. If useImageCache is true, the value is the non-empty logical ID of the current workspace. If useImageCache is false, the value is null. The occupation of old instances after disabling is independently protected by the backend and is not backfilled as the current configuration association.
        # 
        # This parameter is required.
        self.image_cache_id = image_cache_id
        # The wait or execution error of the latest configuration version. This field is returned only when the version is waiting for a retry or fails to execute.
        self.latest_execution_error = latest_execution_error
        # The current latest configuration version number. Updates with the same configuration may retain the original version number. This field does not indicate that the configuration has taken effect.
        # 
        # This parameter is required.
        self.latest_spec_version = latest_spec_version
        # The execution status corresponding to latestSpecVersion. Valid values: pending (waiting for execution), processing (executing), waiting_retry (waiting for a retry), succeeded (execution successful), failed (execution failed), and superseded (replaced by a subsequent version).
        self.latest_version_status = latest_version_status
        # The latest submitted log delivery configuration.
        self.logging = logging
        # The custom agent name.
        # 
        # This parameter is required.
        self.name = name
        # The network access configuration of the agent. The actual access scope is also restricted by the workspace network configuration.
        self.network = network
        # The high-code agent observability configuration.
        self.observability = observability
        # The list of recently submitted OSS directory mounts.
        self.oss_mounts = oss_mounts
        # The list of invocation protocol configurations for the agent.
        self.protocol = protocol
        # The region ID of the workspace to which the agent belongs.
        self.region_id = region_id
        # The ARN of the RAM role used by the agent to access user cloud resources.
        self.role_arn = role_arn
        # The latest committed runtime configuration, including compute specifications, session policy, and elastic policy.
        self.runtime = runtime
        # The number of instances by runtime instance phase. Keys include PENDING (creating or initializing), RUNNING (running), HIBERNATING (hibernating), HIBERNATED (hibernated), RESUMING (resuming), TERMINATING (terminating), and FAILED (failed). Only phases that actually occur are returned. Missing keys are treated as 0.
        self.sandbox_phase_counts = sandbox_phase_counts
        # The overall status of the agent. Valid values: Creating: creating; Running: running; Failed: failed; Updating: updating; Deleting: deleting; Deleted: deleted. To query the execution progress of the latest configuration, check latestVersionStatus.
        # 
        # This parameter is required.
        self.status = status
        # The time when the agent was last updated. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.updated_at = updated_at
        # Required. Reflects the accepted final configuration. If this field is missing in historical data, false is returned. Do not infer based on the cache status.
        # 
        # This parameter is required.
        self.use_image_cache = use_image_cache
        # The ID of the workspace to which the custom agent belongs.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.agentic_fs_mounts:
            for v1 in self.agentic_fs_mounts:
                 if v1:
                    v1.validate()
        if self.artifact:
            self.artifact.validate()
        if self.environment:
            self.environment.validate()
        if self.health_check:
            self.health_check.validate()
        if self.latest_execution_error:
            self.latest_execution_error.validate()
        if self.logging:
            self.logging.validate()
        if self.network:
            self.network.validate()
        if self.observability:
            self.observability.validate()
        if self.oss_mounts:
            for v1 in self.oss_mounts:
                 if v1:
                    v1.validate()
        if self.protocol:
            for v1 in self.protocol:
                 if v1:
                    v1.validate()
        if self.runtime:
            self.runtime.validate()

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

        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.effective_spec_version is not None:
            result['effectiveSpecVersion'] = self.effective_spec_version

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()

        if self.image_cache_id is not None:
            result['imageCacheId'] = self.image_cache_id

        if self.latest_execution_error is not None:
            result['latestExecutionError'] = self.latest_execution_error.to_map()

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.latest_version_status is not None:
            result['latestVersionStatus'] = self.latest_version_status

        if self.logging is not None:
            result['logging'] = self.logging.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.network is not None:
            result['network'] = self.network.to_map()

        if self.observability is not None:
            result['observability'] = self.observability.to_map()

        result['ossMounts'] = []
        if self.oss_mounts is not None:
            for k1 in self.oss_mounts:
                result['ossMounts'].append(k1.to_map() if k1 else None)

        result['protocol'] = []
        if self.protocol is not None:
            for k1 in self.protocol:
                result['protocol'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.sandbox_phase_counts is not None:
            result['sandboxPhaseCounts'] = self.sandbox_phase_counts

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.use_image_cache is not None:
            result['useImageCache'] = self.use_image_cache

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
                temp_model = main_models.GetCustomAgentResponseBodyDataAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        if m.get('artifact') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataArtifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveSpecVersion') is not None:
            self.effective_spec_version = m.get('effectiveSpecVersion')

        if m.get('environment') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('healthCheck') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataHealthCheck()
            self.health_check = temp_model.from_map(m.get('healthCheck'))

        if m.get('imageCacheId') is not None:
            self.image_cache_id = m.get('imageCacheId')

        if m.get('latestExecutionError') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataLatestExecutionError()
            self.latest_execution_error = temp_model.from_map(m.get('latestExecutionError'))

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('logging') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataLogging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataNetwork()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('observability') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataObservability()
            self.observability = temp_model.from_map(m.get('observability'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.GetCustomAgentResponseBodyDataOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        self.protocol = []
        if m.get('protocol') is not None:
            for k1 in m.get('protocol'):
                temp_model = main_models.GetCustomAgentResponseBodyDataProtocol()
                self.protocol.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('runtime') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('sandboxPhaseCounts') is not None:
            self.sandbox_phase_counts = m.get('sandboxPhaseCounts')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('useImageCache') is not None:
            self.use_image_cache = m.get('useImageCache')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetCustomAgentResponseBodyDataRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.GetCustomAgentResponseBodyDataRuntimeCompute = None,
        hpa: main_models.GetCustomAgentResponseBodyDataRuntimeHpa = None,
        session_policy: main_models.GetCustomAgentResponseBodyDataRuntimeSessionPolicy = None,
    ):
        # The compute resource configuration of the agent runtime instance.
        # 
        # This parameter is required.
        self.compute = compute
        # The elastic policy configuration of the agent.
        self.hpa = hpa
        # The session policy configuration of the agent.
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
            temp_model = main_models.GetCustomAgentResponseBodyDataRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class GetCustomAgentResponseBodyDataRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The name of the HTTP request header used by the session policy. This parameter is applicable to ISOLATED_HEADER_FIELD.
        self.header_name = header_name
        # The session policy type. Valid values: AFFINITY: session affinity; ISOLATED_HEADER_FIELD: uses the request header specified by headerName to associate sessions. ISOLATED_COOKIE is not recommended. The compatible value DISABLED in requests is returned as AFFINITY.
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

class GetCustomAgentResponseBodyDataRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Specifies whether to enable elastic scaling. A value of true indicates that elastic scaling is enabled. A value of false indicates that elastic scaling is disabled.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The configured maximum number of concurrent sessions for a single runtime instance.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The configured maximum number of runtime instances.
        self.max_sandbox_count = max_sandbox_count
        # The configured minimum number of runtime instances.
        self.min_sandbox_count = min_sandbox_count
        # The configured session idle timeout limit, in seconds.
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

class GetCustomAgentResponseBodyDataRuntimeCompute(DaraModel):
    def __init__(
        self,
        compute_class: str = None,
    ):
        # The compute specification. Valid values: INTERACTIVE: 1 vCPU and 2 GiB of memory; STANDARD: 2 vCPUs and 4 GiB of memory; HEAVY: 4 vCPUs and 8 GiB of memory.
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

class GetCustomAgentResponseBodyDataProtocol(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        paths: List[main_models.GetCustomAgentResponseBodyDataProtocolPaths] = None,
        type: str = None,
    ):
        # The request header configuration for the current protocol. The key is the name and the value is a string.
        self.headers = headers
        # The list of API paths corresponding to the current protocol.
        self.paths = paths
        # The invocation protocol type. Valid values: agui: AG-UI protocol; openai-chat-completion: OpenAI Chat Completions compatible protocol; custom: custom protocol.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        result['paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['paths'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        self.paths = []
        if m.get('paths') is not None:
            for k1 in m.get('paths'):
                temp_model = main_models.GetCustomAgentResponseBodyDataProtocolPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetCustomAgentResponseBodyDataProtocolPaths(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The usage description of the current API path.
        self.description = description
        # The API path corresponding to the current protocol.
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
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetCustomAgentResponseBodyDataOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The name of the mounted OSS bucket.
        self.bucket_name = bucket_name
        # The OSS mount directory in the container, located under /mnt/oss/.
        self.mount_path = mount_path
        # The object directory prefix in the mounted bucket.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and false indicates read and write.
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

class GetCustomAgentResponseBodyDataObservability(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Default value: true. If set to false, the platform Python probe is not loaded at runtime, and you must collect observability data yourself.
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

class GetCustomAgentResponseBodyDataNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.GetCustomAgentResponseBodyDataNetworkAccessInternet = None,
        access_vpc: main_models.GetCustomAgentResponseBodyDataNetworkAccessVpc = None,
    ):
        # The Internet access configuration of the agent. If this parameter is not configured, Internet access is allowed on the agent side but remains restricted by the workspace.
        self.access_internet = access_internet
        # The user VPC access configuration of the agent. If this parameter is not configured, user VPC access is allowed on the agent side but remains restricted by the workspace.
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
            temp_model = main_models.GetCustomAgentResponseBodyDataNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class GetCustomAgentResponseBodyDataNetworkAccessVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether access to the user VPC configured for the workspace is allowed on the agent side. The actual access remains restricted by the workspace.
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

class GetCustomAgentResponseBodyDataNetworkAccessInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether Internet access is allowed on the agent side. The actual access remains restricted by the workspace.
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

class GetCustomAgentResponseBodyDataLogging(DaraModel):
    def __init__(
        self,
        sls: main_models.GetCustomAgentResponseBodyDataLoggingSls = None,
    ):
        # The Simple Log Service (SLS) log delivery destination.
        self.sls = sls

    def validate(self):
        if self.sls:
            self.sls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls is not None:
            result['sls'] = self.sls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sls') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataLoggingSls()
            self.sls = temp_model.from_map(m.get('sls'))

        return self

class GetCustomAgentResponseBodyDataLoggingSls(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        # The name of the SLS Logstore that receives agent logs.
        self.logstore = logstore
        # The name of the SLS project that receives agent logs.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

class GetCustomAgentResponseBodyDataLatestExecutionError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        retryable: bool = None,
    ):
        # The reason code for the wait or execution failure of the latest configuration. This code is used to determine the subsequent handling method.
        # 
        # This parameter is required.
        self.code = code
        # The description of the reason why the latest configuration is waiting or failed to execute. Refer to code and retryable to determine what to do next.
        # 
        # This parameter is required.
        self.message = message
        # Specifies whether automatic retries are performed. If the value is true, you can query again later. If the value is false, check and fix the configuration based on the reason, and then resubmit.
        # 
        # This parameter is required.
        self.retryable = retryable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.retryable is not None:
            result['retryable'] = self.retryable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        return self

class GetCustomAgentResponseBodyDataHealthCheck(DaraModel):
    def __init__(
        self,
        healthy_threshold: int = None,
        interval_seconds: int = None,
        path: str = None,
        port: int = None,
        timeout_seconds: int = None,
        unhealthy_threshold: int = None,
    ):
        # This parameter does not take effect.
        self.healthy_threshold = healthy_threshold
        # The interval between two health checks, in seconds.
        self.interval_seconds = interval_seconds
        # The HTTP health check path.
        self.path = path
        # The port accessed for the HTTP health check.
        self.port = port
        # The timeout period for a single health check, in seconds.
        self.timeout_seconds = timeout_seconds
        # The number of consecutive health check failures required to mark the instance as unhealthy.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold

        if self.interval_seconds is not None:
            result['intervalSeconds'] = self.interval_seconds

        if self.path is not None:
            result['path'] = self.path

        if self.port is not None:
            result['port'] = self.port

        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds

        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')

        if m.get('intervalSeconds') is not None:
            self.interval_seconds = m.get('intervalSeconds')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')

        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')

        return self

class GetCustomAgentResponseBodyDataEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.GetCustomAgentResponseBodyDataEnvironmentVariables] = None,
    ):
        # The latest submitted list of environment variables.
        self.variables = variables

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.GetCustomAgentResponseBodyDataEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetCustomAgentResponseBodyDataEnvironmentVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        # 
        # This parameter is required.
        self.name = name
        # The string value of the environment variable. Empty strings are allowed.
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

class GetCustomAgentResponseBodyDataArtifact(DaraModel):
    def __init__(
        self,
        code: main_models.GetCustomAgentResponseBodyDataArtifactCode = None,
        container: main_models.GetCustomAgentResponseBodyDataArtifactContainer = None,
        port: int = None,
    ):
        # The code package configuration field. Code package deployment is not supported.
        self.code = code
        # The latest submitted ACR container image configuration.
        self.container = container
        # The TCP port listened by the agent service.
        # 
        # This parameter is required.
        self.port = port

    def validate(self):
        if self.code:
            self.code.validate()
        if self.container:
            self.container.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code.to_map()

        if self.container is not None:
            result['container'] = self.container.to_map()

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataArtifactCode()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('container') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataArtifactContainer()
            self.container = temp_model.from_map(m.get('container'))

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class GetCustomAgentResponseBodyDataArtifactContainer(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        instance_id: str = None,
        namespace: str = None,
        repo: str = None,
        tag: str = None,
        type: str = None,
    ):
        # The custom executable program and startup parameters. If not configured, the default startup method of the image is used.
        self.entrypoint = entrypoint
        # The ID of the ACR instance to which the image repository belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace to which the ACR image repository belongs.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the image repository in the ACR namespace.
        # 
        # This parameter is required.
        self.repo = repo
        # The latest submitted image tag.
        # 
        # This parameter is required.
        self.tag = tag
        # The image source type. A value of acr indicates Alibaba Cloud Container Registry (ACR).
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
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.repo is not None:
            result['repo'] = self.repo

        if self.tag is not None:
            result['tag'] = self.tag

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('repo') is not None:
            self.repo = m.get('repo')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetCustomAgentResponseBodyDataArtifactCode(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        language_runtime: str = None,
        source_uri: str = None,
    ):
        # The startup entry point of the code package. Code package deployment is not supported.
        # 
        # This parameter is required.
        self.entrypoint = entrypoint
        # The language runtime identifier of the code package. Code package deployment is not supported.
        # 
        # This parameter is required.
        self.language_runtime = language_runtime
        # The source URI of the code package. Code package deployment is not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.language_runtime is not None:
            result['languageRuntime'] = self.language_runtime

        if self.source_uri is not None:
            result['sourceUri'] = self.source_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('languageRuntime') is not None:
            self.language_runtime = m.get('languageRuntime')

        if m.get('sourceUri') is not None:
            self.source_uri = m.get('sourceUri')

        return self

class GetCustomAgentResponseBodyDataAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The AgenticFS mount directory in the container, located under /mnt/agenticfs/.
        self.mount_path = mount_path
        # The relative directory within the mounted access point.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and false indicates read and write.
        self.read_only = read_only
        # The AgenticFS access point domain name used for the mount.
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

