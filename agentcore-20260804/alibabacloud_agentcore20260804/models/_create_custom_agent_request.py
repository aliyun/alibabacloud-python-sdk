# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateCustomAgentRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateCustomAgentRequestBody = None,
        client_token: str = None,
    ):
        # The JSON configuration of the custom agent. You must specify name, artifact, roleArn, and runtime.
        self.body = body
        # Idempotency is not currently guaranteed. Do not rely on this parameter to prevent duplicate requests.
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
            temp_model = main_models.CreateCustomAgentRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateCustomAgentRequestBody(DaraModel):
    def __init__(
        self,
        agentic_fs_mounts: List[main_models.CreateCustomAgentRequestBodyAgenticFsMounts] = None,
        artifact: main_models.CreateCustomAgentRequestBodyArtifact = None,
        description: str = None,
        environment: main_models.CreateCustomAgentRequestBodyEnvironment = None,
        health_check: main_models.CreateCustomAgentRequestBodyHealthCheck = None,
        logging: main_models.CreateCustomAgentRequestBodyLogging = None,
        name: str = None,
        network: main_models.CreateCustomAgentRequestBodyNetwork = None,
        oss_mounts: List[main_models.CreateCustomAgentRequestBodyOssMounts] = None,
        protocol: List[main_models.CreateCustomAgentRequestBodyProtocol] = None,
        role_arn: str = None,
        runtime: main_models.CreateCustomAgentRequestBodyRuntime = None,
    ):
        # The list of additional AgenticFS mounts. The total number of AgenticFS and OSS mounts cannot exceed 10. If you omit this parameter or pass an empty array [] during creation, no additional mounts are configured. If you omit this parameter during an update, the original value is retained. If you pass an empty array [], the list is cleared. You cannot pass null.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The deployment artifact configuration. Currently, only ACR container images are supported. Specify container and the service listening port in port, and omit code.
        # 
        # This parameter is required.
        self.artifact = artifact
        # The description of the agent purpose. The maximum length is 1,024 characters after leading and trailing whitespace is removed.
        self.description = description
        # The environment variable configuration passed to the agent runtime process.
        self.environment = environment
        # The optional HTTP health check configuration. If this object is provided, you must specify port. Unspecified items use default values. If omitted during creation, no health check is configured. If this top-level field is omitted during an update, the original configuration is retained. If null is passed, the health check is removed.
        self.health_check = health_check
        # The agent log delivery configuration. You can specify the Simple Log Service project and Logstore. After a successful creation or update, verify that logs are delivered properly.
        self.logging = logging
        # The name of the custom agent. The length must be 1 to 128 characters after leading and trailing whitespace is removed. The name must be unique within the same workspace.
        # 
        # This parameter is required.
        self.name = name
        # The network access configuration of the agent. If this object is provided, omitted access items are treated as allowed. The actual accessible range is still limited by the workspace network configuration. To retain the original restrictions during an update, specify both accessInternet and accessVpc.
        self.network = network
        # The list of OSS mounts. The total number of OSS and AgenticFS mounts cannot exceed 10. You must specify bucketName, path, and mountPath for each item. Mount targets must not be duplicated or overlap. The entire list is replaced during an update. Pass an empty array [] to clear the list.
        self.oss_mounts = oss_mounts
        # The list of invocation protocols supported by the agent. Each item includes the protocol type and optional paths and request headers. The entire list is replaced during an update.
        self.protocol = protocol
        # The ARN of the RAM role used when the agent accesses user cloud resources. The role must have permissions to access the cloud resources.
        # 
        # This parameter is required.
        self.role_arn = role_arn
        # The runtime configuration, including compute specifications, session policies, and an optional elastic policy. Both compute and sessionPolicy must be specified.
        # 
        # This parameter is required.
        self.runtime = runtime

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
        result['agenticFsMounts'] = []
        if self.agentic_fs_mounts is not None:
            for k1 in self.agentic_fs_mounts:
                result['agenticFsMounts'].append(k1.to_map() if k1 else None)

        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()

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

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agentic_fs_mounts = []
        if m.get('agenticFsMounts') is not None:
            for k1 in m.get('agenticFsMounts'):
                temp_model = main_models.CreateCustomAgentRequestBodyAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        if m.get('artifact') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyArtifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environment') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('healthCheck') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyHealthCheck()
            self.health_check = temp_model.from_map(m.get('healthCheck'))

        if m.get('logging') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyLogging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyNetwork()
            self.network = temp_model.from_map(m.get('network'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.CreateCustomAgentRequestBodyOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        self.protocol = []
        if m.get('protocol') is not None:
            for k1 in m.get('protocol'):
                temp_model = main_models.CreateCustomAgentRequestBodyProtocol()
                self.protocol.append(temp_model.from_map(k1))

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('runtime') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        return self

class CreateCustomAgentRequestBodyRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.CreateCustomAgentRequestBodyRuntimeCompute = None,
        hpa: main_models.CreateCustomAgentRequestBodyRuntimeHpa = None,
        session_policy: main_models.CreateCustomAgentRequestBodyRuntimeSessionPolicy = None,
    ):
        # The compute resource configuration for the agent runtime instance.
        # 
        # This parameter is required.
        self.compute = compute
        # The optional elastic policy. When runtime is provided, if hpa or its fields are omitted, the default values are used: enabled is false, the minimum number of instances is 1, the maximum number of instances is 10, the maximum number of concurrent sessions per instance is 100, and the session idle timeout is 600 seconds. To retain the original policy during an update, provide the complete hpa configuration.
        self.hpa = hpa
        # The session policy configuration, which is used to set the session association method for requests.
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
            temp_model = main_models.CreateCustomAgentRequestBodyRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class CreateCustomAgentRequestBodyRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The name of the HTTP request header used by the session policy. This parameter is required when type is set to ISOLATED_HEADER_FIELD and must be a valid HTTP request header name. Omit this parameter for other policies.
        self.header_name = header_name
        # The session policy type. Valid values:
        # - AFFINITY: Session affinity.
        # - ISOLATED_HEADER_FIELD: Associates sessions by using the request header specified by headerName.
        # - ISOLATED_COOKIE: Not recommended.
        # - DISABLED: A compatibility option. The response returns AFFINITY.
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

class CreateCustomAgentRequestBodyRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Specifies whether to enable elastic scaling. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # Default value: false.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The maximum number of concurrent sessions for a single runtime instance. Valid values: 1 to 100. Default value: 100.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of runtime instances. Valid values: 1 to 100. The value cannot be less than minSandboxCount. Default value: 10.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of runtime instances. Valid values: 1 to 100. The value cannot be greater than maxSandboxCount. Default value: 1.
        self.min_sandbox_count = min_sandbox_count
        # The session idle timeout in seconds. Valid values: 60 to 86400. Default value: 600.
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

class CreateCustomAgentRequestBodyRuntimeCompute(DaraModel):
    def __init__(
        self,
        compute_class: str = None,
    ):
        # The compute specification. Valid values:
        # - INTERACTIVE: 1 vCPU and 2 GiB of memory.
        # - STANDARD: 2 vCPUs and 4 GiB of memory.
        # - HEAVY: 4 vCPUs and 8 GiB of memory.
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

class CreateCustomAgentRequestBodyProtocol(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        paths: List[main_models.CreateCustomAgentRequestBodyProtocolPaths] = None,
        type: str = None,
    ):
        # The request header configuration for the current protocol. The key is a non-empty request header name, and the value must be a string.
        self.headers = headers
        # The list of API paths corresponding to the current protocol.
        self.paths = paths
        # The invocation protocol type. Valid values:
        # - agui: AG-UI protocol.
        # - openai-chat-completion: OpenAI Chat Completions compatible protocol.
        # - custom: Custom protocol.
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
                temp_model = main_models.CreateCustomAgentRequestBodyProtocolPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateCustomAgentRequestBodyProtocolPaths(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The usage description of the current API path.
        self.description = description
        # The non-empty API path corresponding to the current protocol.
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

class CreateCustomAgentRequestBodyOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The name of the OSS bucket. This parameter is required for each mount item. The name must be 3 to 63 characters in length and can contain only lowercase letters, digits, and hyphens. It cannot start or end with a hyphen.
        self.bucket_name = bucket_name
        # The subdirectory under /mnt/oss/ in the container. This parameter is required for each mount item. Mount targets must not be duplicated or overlap in a parent-child relationship.
        self.mount_path = mount_path
        # The non-empty object directory prefix in the bucket, such as datasets/train. Leading and trailing forward slashes (/) are removed. Root directories are not supported. Do not use parent directory traversals.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and a value of false indicates read and write. If this parameter is omitted, the default value is false.
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

class CreateCustomAgentRequestBodyNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.CreateCustomAgentRequestBodyNetworkAccessInternet = None,
        access_vpc: main_models.CreateCustomAgentRequestBodyNetworkAccessVpc = None,
    ):
        # The Internet access configuration. If this access item is omitted, Internet access is not restricted on the agent side. However, the workspace must still allow Internet access.
        self.access_internet = access_internet
        # The user VPC access configuration. If this access item is omitted, VPC access is not restricted on the agent side. However, the workspace must still be configured to allow access to the user VPC.
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
            temp_model = main_models.CreateCustomAgentRequestBodyNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class CreateCustomAgentRequestBodyNetworkAccessVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow the agent to access the user VPC configured for the workspace. A Boolean value must be provided when configuring accessVpc. For this setting to take effect, the workspace must also allow VPC access.
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

class CreateCustomAgentRequestBodyNetworkAccessInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow the agent to access the Internet. A Boolean value must be provided when configuring accessInternet. For this setting to take effect, the workspace must also allow Internet access.
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

class CreateCustomAgentRequestBodyLogging(DaraModel):
    def __init__(
        self,
        sls: main_models.CreateCustomAgentRequestBodyLoggingSls = None,
    ):
        # The Simple Log Service log delivery destination. When configuring this object, neither project nor logstore can be empty.
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
            temp_model = main_models.CreateCustomAgentRequestBodyLoggingSls()
            self.sls = temp_model.from_map(m.get('sls'))

        return self

class CreateCustomAgentRequestBodyLoggingSls(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        # The name of the Simple Log Service Logstore that receives agent logs.
        self.logstore = logstore
        # The name of the Simple Log Service project that receives agent logs.
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

class CreateCustomAgentRequestBodyHealthCheck(DaraModel):
    def __init__(
        self,
        healthy_threshold: int = None,
        interval_seconds: int = None,
        path: str = None,
        port: int = None,
        timeout_seconds: int = None,
        unhealthy_threshold: int = None,
    ):
        # This parameter does not take effect. Omit this parameter.
        self.healthy_threshold = healthy_threshold
        # The interval between two health checks, in seconds. It must be a positive integer. If omitted, the default value is 10.
        self.interval_seconds = interval_seconds
        # The HTTP health check path. It must start with a forward slash (/). If omitted, the default value is /healthz.
        self.path = path
        # The port accessed for health checks. This parameter is required when configuring health checks. Valid values: 1 to 65535.
        self.port = port
        # The timeout period for a single health check, in seconds. It must be a positive integer and less than intervalSeconds. If omitted, the default value is 2.
        self.timeout_seconds = timeout_seconds
        # The number of consecutive health check failures required to mark the target as unhealthy. It must be a positive integer. If omitted, the default value is 3.
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

class CreateCustomAgentRequestBodyEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.CreateCustomAgentRequestBodyEnvironmentVariables] = None,
    ):
        # The list of environment variables. Each item includes a name and a value. The entire list is replaced during an update.
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
                temp_model = main_models.CreateCustomAgentRequestBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class CreateCustomAgentRequestBodyEnvironmentVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable. This parameter cannot be empty and must be unique within the current environment variable list.
        # 
        # This parameter is required.
        self.name = name
        # The value of the environment variable. It must be a string. Empty strings are allowed.
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

class CreateCustomAgentRequestBodyArtifact(DaraModel):
    def __init__(
        self,
        code: main_models.CreateCustomAgentRequestBodyArtifactCode = None,
        container: main_models.CreateCustomAgentRequestBodyArtifactContainer = None,
        port: int = None,
    ):
        # The code package deployment configuration. This feature is currently not supported. Omit this parameter and use artifact.container.
        self.code = code
        # The ACR container image configuration. You must specify type, instanceId, namespace, repo, and tag. Do not configure code at the same time.
        self.container = container
        # The TCP port on which the agent service listens. Valid values: 1 to 65535.
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
            temp_model = main_models.CreateCustomAgentRequestBodyArtifactCode()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('container') is not None:
            temp_model = main_models.CreateCustomAgentRequestBodyArtifactContainer()
            self.container = temp_model.from_map(m.get('container'))

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class CreateCustomAgentRequestBodyArtifactContainer(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        instance_id: str = None,
        namespace: str = None,
        repo: str = None,
        tag: str = None,
        type: str = None,
    ):
        # The optional image startup command. If specified, it must be a non-empty string. If omitted, the default startup method of the image is used.
        self.entrypoint = entrypoint
        # The ID of the ACR instance to which the image repository belongs. This parameter cannot be empty.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace to which the ACR image repository belongs. This parameter cannot be empty.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The name of the image repository in the ACR namespace. This parameter cannot be empty.
        # 
        # This parameter is required.
        self.repo = repo
        # The image tag used for deployment. This parameter cannot be empty. When updating the tag, you must also specify artifact.port and other required image fields.
        # 
        # This parameter is required.
        self.tag = tag
        # The source type of the image. Currently, only acr is supported, which indicates Alibaba Cloud Container Registry (ACR).
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

class CreateCustomAgentRequestBodyArtifactCode(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        language_runtime: str = None,
        source_uri: str = None,
    ):
        # The startup entry point of the code package. Code package deployment is currently not supported. Omit this parameter.
        # 
        # This parameter is required.
        self.entrypoint = entrypoint
        # The language runtime identifier of the code package. Code package deployment is currently not supported. Omit this parameter.
        # 
        # This parameter is required.
        self.language_runtime = language_runtime
        # The source URI of the code package. Code package deployment is currently not supported. Omit this parameter.
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

class CreateCustomAgentRequestBodyAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The subdirectory under /mnt/agenticfs/ in the container. This parameter is required for each mount item. Mount targets must not be duplicated or overlap in a parent-child relationship.
        self.mount_path = mount_path
        # The existing non-empty relative directory under the access point. This parameter is required for each mount item. Root directories, absolute paths, and parent directory traversals are not allowed.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and a value of false indicates read and write. If this parameter is omitted, the default value is false.
        self.read_only = read_only
        # The domain name of the access point. This parameter is required for each mount item. Use the DomainName value from the NAS ListAccessPoints response. Do not include the protocol, port, or path.
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

