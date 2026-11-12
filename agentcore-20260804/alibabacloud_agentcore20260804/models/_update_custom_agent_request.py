# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateCustomAgentRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateCustomAgentRequestBody = None,
        client_token: str = None,
    ):
        # The update configuration of the custom code or image agent. You must provide at least one top-level field. Omitted top-level fields retain their original values. When submitting `artifact`, specify `port` and the required fields for the corresponding artifact source. When submitting `runtime`, specify `compute` and `sessionPolicy`, and include the complete `hpa` that needs to be retained. `environment.variables` and other arrays are replaced as complete lists.
        self.body = body
        # The idempotency token passed as a query parameter. This parameter is required when you explicitly submit a customImage or set container.type to custom. It is optional when you submit an ACR image or a code package. The token must be 1 to 128 characters in length and can contain letters, digits, periods, underscores, colons, and hyphens. Reuse the same token for retries of the same submission. Requests with the same token but different parameters are rejected.
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
            temp_model = main_models.UpdateCustomAgentRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateCustomAgentRequestBody(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_scope: str = None,
        agentic_fs_mounts: List[main_models.UpdateCustomAgentRequestBodyAgenticFsMounts] = None,
        artifact: main_models.UpdateCustomAgentRequestBodyArtifact = None,
        custom_image: main_models.UpdateCustomAgentRequestBodyCustomImage = None,
        description: str = None,
        environment: main_models.UpdateCustomAgentRequestBodyEnvironment = None,
        health_check: main_models.UpdateCustomAgentRequestBodyHealthCheck = None,
        logging: main_models.UpdateCustomAgentRequestBodyLogging = None,
        name: str = None,
        network: main_models.UpdateCustomAgentRequestBodyNetwork = None,
        observability: main_models.UpdateCustomAgentRequestBodyObservability = None,
        oss_mounts: List[main_models.UpdateCustomAgentRequestBodyOssMounts] = None,
        protocol: List[main_models.UpdateCustomAgentRequestBodyProtocol] = None,
        role_arn: str = None,
        runtime: main_models.UpdateCustomAgentRequestBodyRuntime = None,
        use_image_cache: bool = None,
    ):
        # The inbound access mode.
        self.access_mode = access_mode
        # The user access scope.
        self.access_scope = access_scope
        # The NAS storage mount configuration. Currently, the AgenticFS type is supported and used to mount file directories in access points to agent runtime instances. The AgenticFS directory mount list and `ossMounts` can contain a maximum of 10 items in total. If omitted or set to `[]` during creation, it indicates no mounts. If omitted during an update, the original value is retained. If set to `[]`, the list is cleared. `null` is not accepted.
        self.agentic_fs_mounts = agentic_fs_mounts
        # The update configuration for the deployment artifact. If the entire artifact object is omitted, the original configuration is retained. When submitting this object, specify the port and the required fields for the selected source. Only one source, either code or container, can be specified.
        self.artifact = artifact
        # If omitted, the original source is retained. A complete submission indicates an active update of the custom image. If only the port and startup command change, you do not need to submit this parameter.
        self.custom_image = custom_image
        # The description of the agent purpose. The maximum length is 1024 characters after leading and trailing spaces are removed. If omitted, the original value is retained. Pass `null` to clear the description.
        self.description = description
        # The user environment variable configuration for the agent process. If the entire environment object is omitted, the original values are retained. If variables is provided, the entire list is replaced, and any variables to be retained must be submitted together. Setting variables to an empty array, setting environment to null, or providing environment while omitting variables clears the user-configured environment variables.
        self.environment = environment
        # The optional HTTP health check configuration. When this object is provided, port must be specified. Unspecified items use default values. Omitting this object during creation means no health check is configured. During an update, omitting this top-level field retains the original configuration, while passing null removes the health check.
        self.health_check = health_check
        # The log delivery configuration for the agent. You can specify the Simple Log Service project and Logstore. After a successful creation or update, verify whether the logs are delivered properly.
        self.logging = logging
        # The name of the custom code or image agent. The length is 1 to 128 characters after leading and trailing spaces are removed. The name must be unique within the same workspace. If omitted, the original value is retained. It cannot be `null` or a blank name.
        self.name = name
        # The network access configuration for the agent. When this object is provided, omitted access items are treated as allowed. The actual accessible scope is still restricted by the workspace network configuration. To retain the original restrictions during an update, specify both accessInternet and accessVpc.
        self.network = network
        # The high-code agent observability configuration.
        self.observability = observability
        # The list of OSS directory mounts. A maximum of 10 items can be configured in total for OSS mounts and AgenticFS mounts. When you update this parameter, the entire list is replaced. Pass an empty array to clear the mounts.
        self.oss_mounts = oss_mounts
        # The list of invocation protocols supported by the agent. Each item includes the protocol type and optional paths and request headers. When you update this parameter, the entire list is replaced.
        self.protocol = protocol
        # The ARN of the RAM role used by the agent to access user cloud resources. The role must have the permissions to access the cloud resources.
        self.role_arn = role_arn
        # The runtime configuration. If the entire object is omitted, the original configuration is retained. If provided, you must specify both compute and sessionPolicy. Omitted fields in hpa use default values.
        self.runtime = runtime
        # If this parameter is not passed during an update, the original value is retained. Explicit true or false settings do not automatically default to false. New contracts reject null and invalid types. Existing compatible portals are processed according to migration agreements. In the current phase, the custom source is normalized to false by the console and omitted by the frontend. Explicit true is rejected. Platform copies are still retained.
        self.use_image_cache = use_image_cache

    def validate(self):
        if self.agentic_fs_mounts:
            for v1 in self.agentic_fs_mounts:
                 if v1:
                    v1.validate()
        if self.artifact:
            self.artifact.validate()
        if self.custom_image:
            self.custom_image.validate()
        if self.environment:
            self.environment.validate()
        if self.health_check:
            self.health_check.validate()
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
        if self.access_mode is not None:
            result['accessMode'] = self.access_mode

        if self.access_scope is not None:
            result['accessScope'] = self.access_scope

        result['agenticFsMounts'] = []
        if self.agentic_fs_mounts is not None:
            for k1 in self.agentic_fs_mounts:
                result['agenticFsMounts'].append(k1.to_map() if k1 else None)

        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.custom_image is not None:
            result['customImage'] = self.custom_image.to_map()

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

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.use_image_cache is not None:
            result['useImageCache'] = self.use_image_cache

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
                temp_model = main_models.UpdateCustomAgentRequestBodyAgenticFsMounts()
                self.agentic_fs_mounts.append(temp_model.from_map(k1))

        if m.get('artifact') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyArtifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('customImage') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyCustomImage()
            self.custom_image = temp_model.from_map(m.get('customImage'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environment') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('healthCheck') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyHealthCheck()
            self.health_check = temp_model.from_map(m.get('healthCheck'))

        if m.get('logging') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyLogging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyNetwork()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('observability') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyObservability()
            self.observability = temp_model.from_map(m.get('observability'))

        self.oss_mounts = []
        if m.get('ossMounts') is not None:
            for k1 in m.get('ossMounts'):
                temp_model = main_models.UpdateCustomAgentRequestBodyOssMounts()
                self.oss_mounts.append(temp_model.from_map(k1))

        self.protocol = []
        if m.get('protocol') is not None:
            for k1 in m.get('protocol'):
                temp_model = main_models.UpdateCustomAgentRequestBodyProtocol()
                self.protocol.append(temp_model.from_map(k1))

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('runtime') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyRuntime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('useImageCache') is not None:
            self.use_image_cache = m.get('useImageCache')

        return self

class UpdateCustomAgentRequestBodyRuntime(DaraModel):
    def __init__(
        self,
        compute: main_models.UpdateCustomAgentRequestBodyRuntimeCompute = None,
        hpa: main_models.UpdateCustomAgentRequestBodyRuntimeHpa = None,
        session_policy: main_models.UpdateCustomAgentRequestBodyRuntimeSessionPolicy = None,
    ):
        # The compute resource configuration for the agent runtime instance.
        # 
        # This parameter is required.
        self.compute = compute
        # The elastic and session configuration. Omitted fields use default values. To retain the original policy during an update, submit the complete hpa object or omit the entire runtime object.
        self.hpa = hpa
        # The session policy configuration, which is used to set the session affinity method for requests.
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
            temp_model = main_models.UpdateCustomAgentRequestBodyRuntimeCompute()
            self.compute = temp_model.from_map(m.get('compute'))

        if m.get('hpa') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyRuntimeHpa()
            self.hpa = temp_model.from_map(m.get('hpa'))

        if m.get('sessionPolicy') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyRuntimeSessionPolicy()
            self.session_policy = temp_model.from_map(m.get('sessionPolicy'))

        return self

class UpdateCustomAgentRequestBodyRuntimeSessionPolicy(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        type: str = None,
    ):
        # The name of the request header used for session identification. This parameter is required when type is set to ISOLATED_HEADER_FIELD and must be a valid HTTP request header name. Do not specify this parameter for other policies.
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

class UpdateCustomAgentRequestBodyRuntimeHpa(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_concurrent_sessions_per_sandbox: int = None,
        max_sandbox_count: int = None,
        min_sandbox_count: int = None,
        session_ttl_seconds: int = None,
    ):
        # Specifies whether to enable elastic scaling. Default value: false.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The maximum number of concurrent sessions allowed per instance. Valid values: 1 to 20. Default value: 20.
        self.max_concurrent_sessions_per_sandbox = max_concurrent_sessions_per_sandbox
        # The maximum number of instances. Valid values: 0 to 100. Default value: 10. This value cannot be less than minSandboxCount.
        self.max_sandbox_count = max_sandbox_count
        # The minimum number of instances. Valid values: 0 to 100. Default value: 1. This value cannot be greater than maxSandboxCount.
        self.min_sandbox_count = min_sandbox_count
        # The maximum idle time for a session, in seconds. Valid values: 60 to 86400. Default value: 600.
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

class UpdateCustomAgentRequestBodyRuntimeCompute(DaraModel):
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

class UpdateCustomAgentRequestBodyProtocol(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        paths: List[main_models.UpdateCustomAgentRequestBodyProtocolPaths] = None,
        type: str = None,
    ):
        # The request header configurations for the current protocol. The key is a non-empty request header name, and the value must be a string.
        self.headers = headers
        # The list of API paths corresponding to the current protocol.
        self.paths = paths
        # The invoke Protocol Type. Valid values:
        # - agui: AG-UI protocol.
        # - openai-chat-completion: OpenAI Chat Completions compatible protocol.
        # - custom: custom protocol.
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
                temp_model = main_models.UpdateCustomAgentRequestBodyProtocolPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateCustomAgentRequestBodyProtocolPaths(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The purpose description of the current API path.
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

class UpdateCustomAgentRequestBodyOssMounts(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        # The name of the OSS bucket. This parameter is required for each mount item. The name must be 3 to 63 characters in length and can contain only lowercase letters, digits, and hyphens. It cannot start or end with a hyphen.
        self.bucket_name = bucket_name
        # The absolute mount path in the container, such as `/data/train`. Mount targets must not be duplicated or form parent-child directory overwrites, and must avoid platform reserved directories.
        self.mount_path = mount_path
        # The non-empty relative object directory prefix in the bucket. This parameter is required for each mount item.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and a value of false indicates read and write. If omitted, the default value is false.
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

class UpdateCustomAgentRequestBodyObservability(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable agent observability.
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

class UpdateCustomAgentRequestBodyNetwork(DaraModel):
    def __init__(
        self,
        access_internet: main_models.UpdateCustomAgentRequestBodyNetworkAccessInternet = None,
        access_vpc: main_models.UpdateCustomAgentRequestBodyNetworkAccessVpc = None,
    ):
        # The Internet access configuration. If this access item is omitted, the agent does not restrict Internet access. However, the workspace must still allow Internet access.
        self.access_internet = access_internet
        # The user VPC access configuration. If this access item is omitted, the agent does not restrict VPC access. However, the workspace must still be configured to allow access to the user VPC.
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
            temp_model = main_models.UpdateCustomAgentRequestBodyNetworkAccessInternet()
            self.access_internet = temp_model.from_map(m.get('accessInternet'))

        if m.get('accessVpc') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyNetworkAccessVpc()
            self.access_vpc = temp_model.from_map(m.get('accessVpc'))

        return self

class UpdateCustomAgentRequestBodyNetworkAccessVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow the agent to access the user VPC configured in the workspace. A Boolean value must be provided when configuring accessVpc. For this configuration to take effect, the workspace must also allow VPC access.
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

class UpdateCustomAgentRequestBodyNetworkAccessInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to allow the agent to access the Internet. A Boolean value must be provided when configuring accessInternet. For this configuration to take effect, the workspace must also allow Internet access.
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

class UpdateCustomAgentRequestBodyLogging(DaraModel):
    def __init__(
        self,
        sls: main_models.UpdateCustomAgentRequestBodyLoggingSls = None,
    ):
        # The Simple Log Service log delivery destination. When updating this object, you must specify both project and logstore, and neither can be empty.
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
            temp_model = main_models.UpdateCustomAgentRequestBodyLoggingSls()
            self.sls = temp_model.from_map(m.get('sls'))

        return self

class UpdateCustomAgentRequestBodyLoggingSls(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        # The name of the Simple Log Service Logstore that receives the agent logs.
        self.logstore = logstore
        # The name of the Simple Log Service project that receives the agent logs.
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

class UpdateCustomAgentRequestBodyHealthCheck(DaraModel):
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
        # The interval between two health checks, in seconds. This parameter must be a positive integer. Default value: 10.
        self.interval_seconds = interval_seconds
        # The HTTP health check path. This parameter must start with a forward slash (/). Default value: /healthz.
        self.path = path
        # The port accessed for health checks. This parameter is required when configuring a health check. Valid values: 1 to 65535.
        self.port = port
        # The timeout period for a single health check, in seconds. This parameter must be a positive integer and less than intervalSeconds. Default value: 2.
        self.timeout_seconds = timeout_seconds
        # The number of consecutive health check failures required to mark the instance as unhealthy. This parameter must be a positive integer. Default value: 3.
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

class UpdateCustomAgentRequestBodyEnvironment(DaraModel):
    def __init__(
        self,
        variables: List[main_models.UpdateCustomAgentRequestBodyEnvironmentVariables] = None,
    ):
        # The complete list of user environment variables. A non-empty list replaces the original list entirely, while an empty array clears the list. The name of each item must be non-empty and unique within the list. The value must be a string, and empty strings are allowed.
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
                temp_model = main_models.UpdateCustomAgentRequestBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class UpdateCustomAgentRequestBodyEnvironmentVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable. This parameter cannot be empty and must be unique within the current environment variable list.
        # 
        # This parameter is required.
        self.name = name
        # The value of the environment variable. This parameter must be a string, and empty strings are allowed.
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

class UpdateCustomAgentRequestBodyCustomImage(DaraModel):
    def __init__(
        self,
        image: str = None,
        password: str = None,
        pull_network: main_models.UpdateCustomAgentRequestBodyCustomImagePullNetwork = None,
        skip_tls_verify: bool = None,
        username: str = None,
    ):
        # This parameter is required and verified by the backend when submitting `customImage`. The value is the complete `registry[:port]/repository:tag` or `registry[:port]/repository@sha256:digest`. Multi-level paths are supported. It does not include a protocol or user information.
        self.image = image
        # The password or token for the current repository.
        self.password = password
        # This parameter is required and verified by the backend when submitting `customImage`. It is the complete independent pull network configuration. For public networks, only pass `type=public`.
        self.pull_network = pull_network
        # Specifies whether to skip HTTPS certificate verification.
        self.skip_tls_verify = skip_tls_verify
        # The username for the current repository.
        self.username = username

    def validate(self):
        if self.pull_network:
            self.pull_network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.password is not None:
            result['password'] = self.password

        if self.pull_network is not None:
            result['pullNetwork'] = self.pull_network.to_map()

        if self.skip_tls_verify is not None:
            result['skipTlsVerify'] = self.skip_tls_verify

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('pullNetwork') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyCustomImagePullNetwork()
            self.pull_network = temp_model.from_map(m.get('pullNetwork'))

        if m.get('skipTlsVerify') is not None:
            self.skip_tls_verify = m.get('skipTlsVerify')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class UpdateCustomAgentRequestBodyCustomImagePullNetwork(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required when `type=vpc`. The vSwitch must belong to the selected VPC.
        self.security_group_id = security_group_id
        # This parameter is required and verified by the backend when submitting `pullNetwork`. The default value for new creations is public network, which is independent of the agent runtime network.
        self.type = type
        # This parameter is required when `type=vpc`. The vSwitch must belong to the selected VPC.
        self.v_switch_id = v_switch_id
        # This parameter is required when `type=vpc`. The associated account and region are verified by the backend.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.type is not None:
            result['type'] = self.type

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class UpdateCustomAgentRequestBodyArtifact(DaraModel):
    def __init__(
        self,
        code: main_models.UpdateCustomAgentRequestBodyArtifactCode = None,
        container: main_models.UpdateCustomAgentRequestBodyArtifactContainer = None,
        port: int = None,
    ):
        # The code package deployment configuration. This parameter is mutually exclusive with container. You must specify sourceUri, languageRuntime, and entrypoint, and set artifact.port. ZIP and TAR.GZ formats are supported. Dependencies must be provided by the caller within the package.
        self.code = code
        # The container image deployment configuration. This parameter is mutually exclusive with code. For an ACR source, set type to acr and specify instanceId, namespace, repo, and tag. For a custom source, set type to custom and provide the complete customImage.
        self.container = container
        # The TCP port on which the agent service listens. Valid values: 1 to 65535. This parameter is required when submitting the artifact object. If the entire artifact object is omitted, the original artifact configuration is retained.
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
            temp_model = main_models.UpdateCustomAgentRequestBodyArtifactCode()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('container') is not None:
            temp_model = main_models.UpdateCustomAgentRequestBodyArtifactContainer()
            self.container = temp_model.from_map(m.get('container'))

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class UpdateCustomAgentRequestBodyArtifactContainer(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        instance_id: str = None,
        namespace: str = None,
        repo: str = None,
        tag: str = None,
        type: str = None,
    ):
        # The optional executable program and startup parameters. If specified, this parameter must be a non-empty string. If you submit the container configuration without specifying entrypoint, the default startup method of the image is used. Quotes and escape characters are supported. Variables, pipes, and logical operations are not automatically expanded.
        self.entrypoint = entrypoint
        # The ID of the ACR instance to which the image repository belongs. This parameter cannot be empty.
        self.instance_id = instance_id
        # The namespace to which the ACR image repository belongs. This parameter cannot be empty.
        self.namespace = namespace
        # The name of the image repository in the ACR namespace. This parameter cannot be empty.
        self.repo = repo
        # The ACR image tag. This parameter is required when submitting the ACR container configuration and must be a non-empty string, such as v1.0.1. When updating the tag, you must also specify artifact.port and the type, instanceId, namespace, and repo parameters in the container configuration.
        self.tag = tag
        # The type of the image source. Valid values:
        # - acr: ACR image.
        # - custom: Custom image source.
        # For the corresponding source configurations, refer to the descriptions of artifact.container and customImage.
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

class UpdateCustomAgentRequestBodyArtifactCode(DaraModel):
    def __init__(
        self,
        entrypoint: str = None,
        language_runtime: str = None,
        source_uri: str = None,
    ):
        # The startup command for the code package. This parameter is required in code package mode. The working directory is the root directory of the extracted code, which is /code. Example: python main.py. Quotes and escape characters are supported. Environment variables, pipes, and logical operations are not automatically expanded. For complex commands, use a script within the package.
        self.entrypoint = entrypoint
        # The identifier of the code runtime environment, such as python3.12. When creating or switching environments, use the identifier returned by ListAgentCodeRuntimes. The identifier is validated against the current version catalog and is not a fixed enumeration.
        self.language_runtime = language_runtime
        # The source URI of the code package. OSS URIs (oss://) or HTTPS object URLs of standard OSS public domain names, including OSS signed URLs, are supported. External sites, custom domain names, or additional authentication request headers are not supported. For local uploads, use the sourceUri returned by GetAgentCodePackageUploadUrl. The URI is re-validated and transferred during creation or update. After saving, a fixed oss:// URI provided by the platform is returned. This fixed URI can be reused for regular updates.
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

class UpdateCustomAgentRequestBodyAgenticFsMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The absolute mount path in the container, such as `/data/train`. Mount targets must not be duplicated or form parent-child directory overwrites, and must avoid platform reserved directories.
        self.mount_path = mount_path
        # The existing non-empty relative directory under the access point. This parameter is required for each mount item. Root directories, absolute paths, or parent directory jumps are not allowed.
        self.path = path
        # Specifies whether the mount is read-only. A value of true indicates read-only, and a value of false indicates read and write. If omitted, the default value is false.
        self.read_only = read_only
        # The domain name of the access point. This parameter is required for each mount item. The value is the DomainName in the response of the NAS ListAccessPoints operation. It does not include a protocol, port, or path.
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

