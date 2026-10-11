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
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        environment: main_models.GetCustomAgentResponseBodyDataEnvironment = None,
        health_check: main_models.GetCustomAgentResponseBodyDataHealthCheck = None,
        latest_execution_error: main_models.GetCustomAgentResponseBodyDataLatestExecutionError = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        logging: main_models.GetCustomAgentResponseBodyDataLogging = None,
        name: str = None,
        network: main_models.GetCustomAgentResponseBodyDataNetwork = None,
        oss_mounts: List[main_models.GetCustomAgentResponseBodyDataOssMounts] = None,
        protocol: List[main_models.GetCustomAgentResponseBodyDataProtocol] = None,
        region_id: str = None,
        role_arn: str = None,
        runtime: main_models.GetCustomAgentResponseBodyDataRuntime = None,
        sandbox_phase_counts: Dict[str, int] = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        self.agent_id = agent_id
        self.agentic_fs_mounts = agentic_fs_mounts
        self.artifact = artifact
        self.create_mode = create_mode
        self.created_at = created_at
        self.deploy_type = deploy_type
        self.description = description
        self.environment = environment
        self.health_check = health_check
        # 可选。仅解释同一响应 latestSpecVersion/latestVersionStatus 的等待或失败；正常待处理、执行中或成功时省略。消息由 Console 白名单映射，不返回原始运行时诊断、Checkpoint 或凭证。
        self.latest_execution_error = latest_execution_error
        self.latest_spec_version = latest_spec_version
        self.latest_version_status = latest_version_status
        self.logging = logging
        self.name = name
        self.network = network
        self.oss_mounts = oss_mounts
        self.protocol = protocol
        self.region_id = region_id
        self.role_arn = role_arn
        self.runtime = runtime
        self.sandbox_phase_counts = sandbox_phase_counts
        self.status = status
        self.updated_at = updated_at
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

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()

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

        if m.get('environment') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('healthCheck') is not None:
            temp_model = main_models.GetCustomAgentResponseBodyDataHealthCheck()
            self.health_check = temp_model.from_map(m.get('healthCheck'))

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
        # This parameter is required.
        self.compute = compute
        # Agent 当前 spec 版本的 HPA 配置，与 Managed Agent 一致。开启时必须提供最小和最大 Sandbox 数；并发会话上限与会话空闲超时必须一起配置。
        self.hpa = hpa
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
        self.header_name = header_name
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
        # This parameter is required.
        self.enabled = enabled
        # 正整数，必须与 sessionTtlSeconds 同时配置。
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # 开启时为正整数，关闭时为非负整数；不得小于 minSandboxCount。
        self.max_sandbox_count = max_sandbox_count
        # 非负整数。开启弹性时必填；关闭时如提供上下限，必须成对提供。
        self.min_sandbox_count = min_sandbox_count
        # 正整数，必须与 maxConcurrentSessionsPerSandbox 同时配置。
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
        self.headers = headers
        self.paths = paths
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
        self.description = description
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
        self.bucket_name = bucket_name
        self.mount_path = mount_path
        self.path = path
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

class GetCustomAgentResponseBodyDataNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.GetCustomAgentResponseBodyDataNetworkAccessInternet = None,
        access_vpc: main_models.GetCustomAgentResponseBodyDataNetworkAccessVpc = None,
    ):
        self.access_internet = access_internet
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
        self.logstore = logstore
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
        self.code = code
        self.message = message
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
        self.healthy_threshold = healthy_threshold
        self.interval_seconds = interval_seconds
        self.path = path
        self.port = port
        self.timeout_seconds = timeout_seconds
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
        # This parameter is required.
        self.name = name
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
        self.code = code
        self.container = container
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
        self.entrypoint = entrypoint
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.repo = repo
        # This parameter is required.
        self.tag = tag
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
        # This parameter is required.
        self.entrypoint = entrypoint
        # This parameter is required.
        self.language_runtime = language_runtime
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
        self.mount_path = mount_path
        self.path = path
        self.read_only = read_only
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

