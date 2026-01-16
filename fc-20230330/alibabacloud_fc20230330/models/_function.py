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
        last_modified_time: str = None,
        last_update_status: str = None,
        last_update_status_reason: str = None,
        last_update_status_reason_code: str = None,
        layers: List[main_models.FunctionLayer] = None,
        log_config: main_models.LogConfig = None,
        memory_size: int = None,
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
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.cpu = cpu
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        self.custom_dns = custom_dns
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disable_inject_credentials = disable_inject_credentials
        self.disable_ondemand = disable_ondemand
        self.disk_size = disk_size
        self.enable_long_living = enable_long_living
        self.environment_variables = environment_variables
        self.function_arn = function_arn
        self.function_id = function_id
        self.function_name = function_name
        self.gpu_config = gpu_config
        self.handler = handler
        self.idle_timeout = idle_timeout
        self.instance_concurrency = instance_concurrency
        self.instance_isolation_mode = instance_isolation_mode
        self.instance_lifecycle_config = instance_lifecycle_config
        self.internet_access = internet_access
        self.invocation_restriction = invocation_restriction
        self.last_modified_time = last_modified_time
        self.last_update_status = last_update_status
        self.last_update_status_reason = last_update_status_reason
        self.last_update_status_reason_code = last_update_status_reason_code
        self.layers = layers
        self.log_config = log_config
        self.memory_size = memory_size
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.polar_fs_config = polar_fs_config
        self.resource_group_id = resource_group_id
        self.role = role
        self.runtime = runtime
        self.session_affinity = session_affinity
        self.session_affinity_config = session_affinity_config
        self.state = state
        self.state_reason = state_reason
        self.state_reason_code = state_reason_code
        self.tags = tags
        self.timeout = timeout
        self.tracing_config = tracing_config
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
        if self.layers:
            for v1 in self.layers:
                 if v1:
                    v1.validate()
        if self.log_config:
            self.log_config.validate()
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

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

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

        if m.get('logConfig') is not None:
            temp_model = main_models.LogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

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

