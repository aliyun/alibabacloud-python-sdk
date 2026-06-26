# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CreateFunctionInput(DaraModel):
    def __init__(
        self,
        code: main_models.InputCodeLocation = None,
        cpu: float = None,
        custom_container_config: main_models.CustomContainerConfig = None,
        custom_dns: main_models.CustomDNS = None,
        custom_runtime_config: main_models.CustomRuntimeConfig = None,
        description: str = None,
        disable_inject_credentials: str = None,
        disable_ondemand: bool = None,
        disk_size: int = None,
        enable_long_living: bool = None,
        environment_variables: Dict[str, str] = None,
        function_name: str = None,
        gpu_config: main_models.GPUConfig = None,
        handler: str = None,
        idle_timeout: int = None,
        instance_concurrency: int = None,
        instance_isolation_mode: str = None,
        instance_lifecycle_config: main_models.InstanceLifecycleConfig = None,
        internet_access: bool = None,
        juice_fs_config: main_models.JuiceFsConfig = None,
        layers: List[str] = None,
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
        tags: List[main_models.Tag] = None,
        timeout: int = None,
        tracing_config: main_models.TracingConfig = None,
        vpc_config: main_models.VPCConfig = None,
    ):
        # The ZIP package of the function code. Specify either code or customContainerConfig.
        self.code = code
        # The CPU specification of the function, in vCPUs. The value must be a multiple of 0.05 vCPU. Minimum value: 0.05. Maximum value: 16. The ratio of cpu to memorySize (in GB) must be between 1:1 and 1:4.
        self.cpu = cpu
        # The configuration for the custom container runtime. After this parameter is configured, the function can use a custom container image for execution. Specify either code or customContainerConfig.
        self.custom_container_config = custom_container_config
        # The custom DNS configuration.
        self.custom_dns = custom_dns
        # The custom runtime configuration.
        self.custom_runtime_config = custom_runtime_config
        # The description of the function.
        self.description = description
        # Specifies whether to disable STS token injection. Valid values:
        # - None: STS tokens are injected in all methods.
        # - Env: STS tokens are not injected through environment variables.
        # - Request: STS tokens are not injected in requests, including context and headers.
        # - All: STS tokens are not injected in any method.
        self.disable_inject_credentials = disable_inject_credentials
        # Specifies whether to disable the creation of on-demand instances. If this feature is enabled, on-demand instances are not created and only provisioned instances can be used.
        self.disable_ondemand = disable_ondemand
        # The disk specification of the function, in MB. Valid values: 512 and 10240.
        self.disk_size = disk_size
        # Specifies whether to allow provisioned instances of GPU functions to be long-running. When this feature is enabled, function instances are not injected with STS tokens.
        self.enable_long_living = enable_long_living
        # The environment variables of the function. You can access the configured environment variables in the runtime environment.
        self.environment_variables = environment_variables
        # The name of the function. The name can contain only letters, digits, underscores (_), and hyphens (-). The name cannot start with a digit or hyphen (-). The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.function_name = function_name
        # The GPU configuration of the function.
        self.gpu_config = gpu_config
        # The function entry point. The specific format depends on the runtime.
        # 
        # This parameter is required.
        self.handler = handler
        # The deferred release time of the instance.
        self.idle_timeout = idle_timeout
        # The maximum concurrency of an instance.
        self.instance_concurrency = instance_concurrency
        # The instance isolation mode.
        self.instance_isolation_mode = instance_isolation_mode
        # The instance lifecycle hook configuration.
        self.instance_lifecycle_config = instance_lifecycle_config
        # Specifies whether the function can access the Internet. Default value: true.
        self.internet_access = internet_access
        self.juice_fs_config = juice_fs_config
        # The list of layers. Multiple layers are merged in descending order of array index. Files in a layer with a smaller index overwrite files with the same name in a layer with a larger index.
        self.layers = layers
        # The log configuration. Logs generated by the function are written to the configured Logstore.
        self.log_config = log_config
        # The memory specification of the function, in MB. The value must be a multiple of 64 MB. Minimum value: 128. Maximum value: 32768 (32 GB). The ratio of cpu to memorySize (in GB) must be between 1:1 and 1:4.
        self.memory_size = memory_size
        self.micro_sandbox_config = micro_sandbox_config
        # The NAS configuration. After this parameter is configured, the function can access the specified NAS resources.
        self.nas_config = nas_config
        # The OSS mount configuration.
        self.oss_mount_config = oss_mount_config
        # The PolarFs configuration. After this parameter is configured, the function can access the specified PolarFs resources.
        self.polar_fs_config = polar_fs_config
        self.resource_group_id = resource_group_id
        # The RAM role that the user grants to Function Compute. After this parameter is set, Function Compute assumes this role to generate temporary access credentials. You can use the temporary access credentials of this role in the function to access specified Alibaba Cloud services, such as OSS and OTS.
        self.role = role
        # The runtime environment of the function. Supported runtimes: nodejs12, nodejs14, nodejs16, nodejs18, nodejs20, go1, python3, python3.9, python3.10, python3.12, java8, java11, php7.2, dotnetcore3.1, custom, custom.debian10, custom.debian11, custom.debian12, and custom-container.
        # 
        # This parameter is required.
        self.runtime = runtime
        # The affinity policy for Function Compute invocation requests. To implement request affinity for the MCP SSE protocol, set this parameter to MCP_SSE. To use cookie-based affinity, set this parameter to GENERATED_COOKIE. To use header-based affinity, set this parameter to HEADER_FIELD. If this parameter is not set or is set to NONE, no affinity is applied and requests are routed based on the default scheduling policy of Function Compute.
        self.session_affinity = session_affinity
        # The affinity configuration that corresponds to the sessionAffinity type. For MCP_SSE affinity, specify MCPSSESessionAffinityConfig. For cookie-based affinity, specify CookieSessionAffinityConfig. For header field affinity, specify HeaderFieldSessionAffinityConfig.
        self.session_affinity_config = session_affinity_config
        # The list of tags.
        self.tags = tags
        # The timeout period for function execution, in seconds. Minimum value: 1. Maximum value: 86400. Default value: 3. The function is terminated if it exceeds this time limit.
        self.timeout = timeout
        # The Tracing Analysis configuration. After Function Compute is integrated with Tracing Analysis, you can record the time consumed by requests in Function Compute, view the cold start time of functions, and record the time consumed within functions.
        self.tracing_config = tracing_config
        # The VPC configuration. After this parameter is configured, the function can access the specified VPC resources.
        self.vpc_config = vpc_config

    def validate(self):
        if self.code:
            self.code.validate()
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
        if self.juice_fs_config:
            self.juice_fs_config.validate()
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
        if self.code is not None:
            result['code'] = self.code.to_map()

        if self.cpu is not None:
            result['cpu'] = self.cpu

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

        if self.juice_fs_config is not None:
            result['juiceFsConfig'] = self.juice_fs_config.to_map()

        if self.layers is not None:
            result['layers'] = self.layers

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
        if m.get('code') is not None:
            temp_model = main_models.InputCodeLocation()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

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

        if m.get('juiceFsConfig') is not None:
            temp_model = main_models.JuiceFsConfig()
            self.juice_fs_config = temp_model.from_map(m.get('juiceFsConfig'))

        if m.get('layers') is not None:
            self.layers = m.get('layers')

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

