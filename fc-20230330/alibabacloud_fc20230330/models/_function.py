# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class Function(DaraModel):
    def __init__(
        self,
        code_checksum: str = None,
        code_size: int = None,
        cpu: float = None,
        created_time: str = None,
        custom_container_config: main_models.CustomContainerConfig = None,
        custom_dns: main_models.CustomDNS = None,
        custom_runtime_config: main_models.CustomRuntimeConfig = None,
        description: str = None,
        disable_inject_credentials: str = None,
        disable_ondemand: bool = None,
        disk_size: int = None,
        enable_long_living: bool = None,
        environment_variables: Dict[str, str] = None,
        function_arn: str = None,
        function_id: str = None,
        function_name: str = None,
        gpu_config: main_models.GPUConfig = None,
        handler: str = None,
        idle_timeout: int = None,
        instance_concurrency: int = None,
        instance_isolation_mode: str = None,
        instance_lifecycle_config: main_models.InstanceLifecycleConfig = None,
        internet_access: bool = None,
        invocation_restriction: main_models.FunctionRestriction = None,
        juice_fs_config: main_models.JuiceFsConfig = None,
        last_modified_time: str = None,
        last_update_status: str = None,
        last_update_status_reason: str = None,
        last_update_status_reason_code: str = None,
        layers: List[main_models.FunctionLayer] = None,
        lock_info: main_models.FunctionLockInfo = None,
        log_config: main_models.LogConfig = None,
        memory_size: int = None,
        micro_sandbox_config: main_models.MicroSandboxConfig = None,
        nas_config: main_models.NASConfig = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        polar_fs_config: main_models.PolarFsConfig = None,
        resource_group_id: str = None,
        role: str = None,
        runtime: str = None,
        session_affinity: str = None,
        session_affinity_config: str = None,
        state: str = None,
        state_reason: str = None,
        state_reason_code: str = None,
        tags: List[main_models.Tag] = None,
        timeout: int = None,
        tracing_config: main_models.TracingConfig = None,
        vpc_config: main_models.VPCConfig = None,
    ):
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum
        # The size of the function code package returned by the system. Unit: bytes.
        self.code_size = code_size
        # The CPU specification of the function. Unit: vCPU. The value must be a multiple of 0.05 vCPU. Minimum value: 0.05. Maximum value: 16. The ratio of cpu to memorySize (in GB) must be between 1:1 and 1:4.
        self.cpu = cpu
        # The time when the function was created.
        self.created_time = created_time
        # The custom container runtime configuration. After this parameter is configured, the function can use a custom container image to execute the function. Specify either code or customContainerConfig.
        self.custom_container_config = custom_container_config
        # The custom DNS configuration.
        self.custom_dns = custom_dns
        # The custom runtime configuration.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # Specifies whether to disable STS token injection. Valid values:
        # - None: injects STS tokens in all methods.
        # - Env: does not inject STS tokens through environment variables.
        # - Request: does not inject STS tokens through requests, including context and headers.
        # - All: does not inject STS tokens in any method.
        self.disable_inject_credentials = disable_inject_credentials
        # Specifies whether to disable the creation of on-demand instances. If this feature is enabled, on-demand instances are not created, and only provisioned instances can be used.
        self.disable_ondemand = disable_ondemand
        # The disk specification of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # When a sessionAffinity type is set, configure the corresponding affinity settings. For MCP_SSE affinity, populate the MCPSSESessionAffinityConfig configuration. For cookie-based affinity, populate the CookieSessionAffinityConfig configuration. For header field affinity, populate the HeaderFieldSessionAffinityConfig configuration.
        self.enable_long_living = enable_long_living
        # The environment variables of the function. You can access the configured environment variables in the runtime environment.
        self.environment_variables = environment_variables
        # The Alibaba Cloud Resource Name (ARN) of the function.
        self.function_arn = function_arn
        # The globally unique ID generated by the system for the function.
        self.function_id = function_id
        # The name of the function.
        self.function_name = function_name
        # The GPU configuration of the function.
        self.gpu_config = gpu_config
        # The function entry point. The specific format depends on the runtime.
        self.handler = handler
        # The deferred instance release time.
        self.idle_timeout = idle_timeout
        # The maximum concurrency per instance.
        self.instance_concurrency = instance_concurrency
        # The instance isolation mode.
        self.instance_isolation_mode = instance_isolation_mode
        # The instance lifecycle hook method configuration.
        self.instance_lifecycle_config = instance_lifecycle_config
        # Specifies whether the function can access the Internet. Default value: true.
        self.internet_access = internet_access
        self.invocation_restriction = invocation_restriction
        self.juice_fs_config = juice_fs_config
        # The time when the function was last updated.
        self.last_modified_time = last_modified_time
        # The status of the most recent function update operation. When a function is created, this value is Successful. Valid values:
        # - Successful
        # - Failed
        # - InProgress.
        self.last_update_status = last_update_status
        # The reason that caused the most recent function update operation to have the current status.
        self.last_update_status_reason = last_update_status_reason
        # The status code of the reason that caused the most recent function update operation to have the current status.
        self.last_update_status_reason_code = last_update_status_reason_code
        # The list of layers.
        self.layers = layers
        self.lock_info = lock_info
        # The log configuration. Logs generated by the function are written to the configured Logstore.
        self.log_config = log_config
        # The memory specification of the function. Unit: MB. The value must be a multiple of 64 MB. Minimum value: 128. Maximum value: 32768 (32 GB). The ratio of cpu to memorySize (in GB) must be between 1:1 and 1:4.
        self.memory_size = memory_size
        self.micro_sandbox_config = micro_sandbox_config
        # The NAS configuration. After this parameter is configured, the function can access the specified NAS resources.
        self.nas_config = nas_config
        # The OSS mount configuration.
        self.oss_mount_config = oss_mount_config
        # The PolarFs configuration. After this parameter is configured, the function can access the specified PolarFs resources.
        self.polar_fs_config = polar_fs_config
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The RAM role that the user grants to Function Compute. After this parameter is configured, Function Compute assumes this role to generate temporary access credentials. You can use the temporary access credentials of this role in the function to access specified Alibaba Cloud services such as OSS and OTS.
        self.role = role
        # The runtime environment of the function. Currently supported runtime environments include: nodejs12, nodejs14, nodejs16, nodejs18, nodejs20, go1, python3, python3.9, python3.10, python3.12, java8, java11, php7.2, dotnetcore3.1, custom, custom.debian10, custom.debian11, custom.debian12, and custom-container.
        self.runtime = runtime
        # The affinity policy for Function Compute invocation requests. To implement request affinity for the MCP SSE protocol, set this parameter to MCP_SSE. To use cookie-based affinity, set this parameter to GENERATED_COOKIE. To use header-based affinity, set this parameter to HEADER_FIELD. If this parameter is not set or is set to NONE, no affinity is applied, and requests are routed based on the default scheduling policy of Function Compute.
        self.session_affinity = session_affinity
        # When a sessionAffinity type is set, configure the corresponding affinity settings. For MCP_SSE affinity, populate the MCPSSESessionAffinityConfig configuration. For cookie-based affinity, populate the CookieSessionAffinityConfig configuration. For header field affinity, populate the HeaderFieldSessionAffinityConfig configuration.
        self.session_affinity_config = session_affinity_config
        # The current state of the function.
        self.state = state
        # The reason why the function is in the current state.
        self.state_reason = state_reason
        # The status code of the reason why the function is in the current state.
        self.state_reason_code = state_reason_code
        # The list of tags.
        self.tags = tags
        # The timeout period for the function execution. Unit: seconds. Minimum value: 1. Maximum value: 86400. Default value: 3. The function is terminated if it exceeds this time limit.
        self.timeout = timeout
        # The Tracing Analysis configuration. After Function Compute is integrated with Tracing Analysis, you can record the time consumed by requests in Function Compute, view the cold start time of functions, and record the time consumed by internal operations of functions.
        self.tracing_config = tracing_config
        # The VPC configuration. After this parameter is configured, the function can access the specified VPC resources.
        self.vpc_config = vpc_config

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.invocation_restriction:
            self.invocation_restriction.validate()
        if self.juice_fs_config:
            self.juice_fs_config.validate()
        if self.layers:
            for v1 in self.layers:
                 if v1:
                    v1.validate()
        if self.lock_info:
            self.lock_info.validate()
        if self.log_config:
            self.log_config.validate()
        if self.micro_sandbox_config:
            self.micro_sandbox_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.polar_fs_config:
            self.polar_fs_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum

        if self.code_size is not None:
            result['codeSize'] = self.code_size

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()

        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()

        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.disable_inject_credentials is not None:
            result['disableInjectCredentials'] = self.disable_inject_credentials

        if self.disable_ondemand is not None:
            result['disableOndemand'] = self.disable_ondemand

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.enable_long_living is not None:
            result['enableLongLiving'] = self.enable_long_living

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        if self.function_id is not None:
            result['functionId'] = self.function_id

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()

        if self.handler is not None:
            result['handler'] = self.handler

        if self.idle_timeout is not None:
            result['idleTimeout'] = self.idle_timeout

        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency

        if self.instance_isolation_mode is not None:
            result['instanceIsolationMode'] = self.instance_isolation_mode

        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()

        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access

        if self.invocation_restriction is not None:
            result['invocationRestriction'] = self.invocation_restriction.to_map()

        if self.juice_fs_config is not None:
            result['juiceFsConfig'] = self.juice_fs_config.to_map()

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.last_update_status is not None:
            result['lastUpdateStatus'] = self.last_update_status

        if self.last_update_status_reason is not None:
            result['lastUpdateStatusReason'] = self.last_update_status_reason

        if self.last_update_status_reason_code is not None:
            result['lastUpdateStatusReasonCode'] = self.last_update_status_reason_code

        result['layers'] = []
        if self.layers is not None:
            for k1 in self.layers:
                result['layers'].append(k1.to_map() if k1 else None)

        if self.lock_info is not None:
            result['lockInfo'] = self.lock_info.to_map()

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.micro_sandbox_config is not None:
            result['microSandboxConfig'] = self.micro_sandbox_config.to_map()

        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.polar_fs_config is not None:
            result['polarFsConfig'] = self.polar_fs_config.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.role is not None:
            result['role'] = self.role

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity

        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config

        if self.state is not None:
            result['state'] = self.state

        if self.state_reason is not None:
            result['stateReason'] = self.state_reason

        if self.state_reason_code is not None:
            result['stateReasonCode'] = self.state_reason_code

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()

        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')

        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('customContainerConfig') is not None:
            temp_model = main_models.CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m.get('customContainerConfig'))

        if m.get('customDNS') is not None:
            temp_model = main_models.CustomDNS()
            self.custom_dns = temp_model.from_map(m.get('customDNS'))

        if m.get('customRuntimeConfig') is not None:
            temp_model = main_models.CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m.get('customRuntimeConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disableInjectCredentials') is not None:
            self.disable_inject_credentials = m.get('disableInjectCredentials')

        if m.get('disableOndemand') is not None:
            self.disable_ondemand = m.get('disableOndemand')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('enableLongLiving') is not None:
            self.enable_long_living = m.get('enableLongLiving')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('gpuConfig') is not None:
            temp_model = main_models.GPUConfig()
            self.gpu_config = temp_model.from_map(m.get('gpuConfig'))

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('idleTimeout') is not None:
            self.idle_timeout = m.get('idleTimeout')

        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')

        if m.get('instanceIsolationMode') is not None:
            self.instance_isolation_mode = m.get('instanceIsolationMode')

        if m.get('instanceLifecycleConfig') is not None:
            temp_model = main_models.InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m.get('instanceLifecycleConfig'))

        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')

        if m.get('invocationRestriction') is not None:
            temp_model = main_models.FunctionRestriction()
            self.invocation_restriction = temp_model.from_map(m.get('invocationRestriction'))

        if m.get('juiceFsConfig') is not None:
            temp_model = main_models.JuiceFsConfig()
            self.juice_fs_config = temp_model.from_map(m.get('juiceFsConfig'))

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('lastUpdateStatus') is not None:
            self.last_update_status = m.get('lastUpdateStatus')

        if m.get('lastUpdateStatusReason') is not None:
            self.last_update_status_reason = m.get('lastUpdateStatusReason')

        if m.get('lastUpdateStatusReasonCode') is not None:
            self.last_update_status_reason_code = m.get('lastUpdateStatusReasonCode')

        self.layers = []
        if m.get('layers') is not None:
            for k1 in m.get('layers'):
                temp_model = main_models.FunctionLayer()
                self.layers.append(temp_model.from_map(k1))

        if m.get('lockInfo') is not None:
            temp_model = main_models.FunctionLockInfo()
            self.lock_info = temp_model.from_map(m.get('lockInfo'))

        if m.get('logConfig') is not None:
            temp_model = main_models.LogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('microSandboxConfig') is not None:
            temp_model = main_models.MicroSandboxConfig()
            self.micro_sandbox_config = temp_model.from_map(m.get('microSandboxConfig'))

        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('polarFsConfig') is not None:
            temp_model = main_models.PolarFsConfig()
            self.polar_fs_config = temp_model.from_map(m.get('polarFsConfig'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')

        if m.get('sessionAffinityConfig') is not None:
            self.session_affinity_config = m.get('sessionAffinityConfig')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('stateReason') is not None:
            self.state_reason = m.get('stateReason')

        if m.get('stateReasonCode') is not None:
            self.state_reason_code = m.get('stateReasonCode')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('tracingConfig') is not None:
            temp_model = main_models.TracingConfig()
            self.tracing_config = temp_model.from_map(m.get('tracingConfig'))

        if m.get('vpcConfig') is not None:
            temp_model = main_models.VPCConfig()
            self.vpc_config = temp_model.from_map(m.get('vpcConfig'))

        return self

