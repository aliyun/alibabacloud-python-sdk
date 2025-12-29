# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class Application(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        application_id: str = None,
        application_name: str = None,
        args: str = None,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        command: str = None,
        cpu: float = None,
        created_time: str = None,
        custom_dns: main_models.CustomDNS = None,
        custom_domain_name: str = None,
        custom_health_check_config: main_models.CustomHealthCheckConfig = None,
        custom_host_alias: main_models.CustomHostAlias = None,
        custom_runtime_config: main_models.CustomRuntimeConfig = None,
        description: str = None,
        disk_size: int = None,
        enable_app_metric: bool = None,
        enable_arms_advanced: bool = None,
        environment_variables: Dict[str, str] = None,
        gpu_memory_size: int = None,
        handler: str = None,
        http_trigger_config: main_models.HTTPTriggerConfig = None,
        image_config: main_models.ImageConfig = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: main_models.InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        layers_arn_v2: List[str] = None,
        liveness_probe: main_models.Probe = None,
        log_config: main_models.LogConfig = None,
        memory_size: int = None,
        namespace: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        nas_config: main_models.NASConfig = None,
        oss_mount_config: main_models.OSSMountConfig = None,
        programming_language: str = None,
        runtime: str = None,
        scale_config: main_models.ScaleConfig = None,
        sls_config: main_models.SLSConfig = None,
        startup_probe: main_models.Probe = None,
        timeout: int = None,
        tracing_config: main_models.TracingConfig = None,
        url_internet: str = None,
        url_intranet: str = None,
        version: main_models.Version = None,
        vpc_config: main_models.VPCConfig = None,
    ):
        self.request_id = request_id
        self.application_id = application_id
        self.application_name = application_name
        self.args = args
        self.ca_port = ca_port
        self.code_checksum = code_checksum
        self.code_size = code_size
        self.command = command
        self.cpu = cpu
        self.created_time = created_time
        self.custom_dns = custom_dns
        self.custom_domain_name = custom_domain_name
        self.custom_health_check_config = custom_health_check_config
        self.custom_host_alias = custom_host_alias
        self.custom_runtime_config = custom_runtime_config
        self.description = description
        self.disk_size = disk_size
        self.enable_app_metric = enable_app_metric
        self.enable_arms_advanced = enable_arms_advanced
        self.environment_variables = environment_variables
        self.gpu_memory_size = gpu_memory_size
        self.handler = handler
        self.http_trigger_config = http_trigger_config
        self.image_config = image_config
        self.initialization_timeout = initialization_timeout
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        self.internet_access = internet_access
        self.last_modified_time = last_modified_time
        self.layers = layers
        self.layers_arn_v2 = layers_arn_v2
        self.liveness_probe = liveness_probe
        self.log_config = log_config
        self.memory_size = memory_size
        self.namespace = namespace
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.nas_config = nas_config
        self.oss_mount_config = oss_mount_config
        self.programming_language = programming_language
        self.runtime = runtime
        self.scale_config = scale_config
        self.sls_config = sls_config
        self.startup_probe = startup_probe
        self.timeout = timeout
        self.tracing_config = tracing_config
        self.url_internet = url_internet
        self.url_intranet = url_intranet
        self.version = version
        self.vpc_config = vpc_config

    def validate(self):
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_host_alias:
            self.custom_host_alias.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.http_trigger_config:
            self.http_trigger_config.validate()
        if self.image_config:
            self.image_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.scale_config:
            self.scale_config.validate()
        if self.sls_config:
            self.sls_config.validate()
        if self.startup_probe:
            self.startup_probe.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.version:
            self.version.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.application_id is not None:
            result['applicationId'] = self.application_id

        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.args is not None:
            result['args'] = self.args

        if self.ca_port is not None:
            result['caPort'] = self.ca_port

        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum

        if self.code_size is not None:
            result['codeSize'] = self.code_size

        if self.command is not None:
            result['command'] = self.command

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()

        if self.custom_domain_name is not None:
            result['customDomainName'] = self.custom_domain_name

        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()

        if self.custom_host_alias is not None:
            result['customHostAlias'] = self.custom_host_alias.to_map()

        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.disk_size is not None:
            result['diskSize'] = self.disk_size

        if self.enable_app_metric is not None:
            result['enableAppMetric'] = self.enable_app_metric

        if self.enable_arms_advanced is not None:
            result['enableArmsAdvanced'] = self.enable_arms_advanced

        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables

        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size

        if self.handler is not None:
            result['handler'] = self.handler

        if self.http_trigger_config is not None:
            result['httpTriggerConfig'] = self.http_trigger_config.to_map()

        if self.image_config is not None:
            result['imageConfig'] = self.image_config.to_map()

        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout

        if self.initializer is not None:
            result['initializer'] = self.initializer

        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency

        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()

        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.layers is not None:
            result['layers'] = self.layers

        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2

        if self.liveness_probe is not None:
            result['livenessProbe'] = self.liveness_probe.to_map()

        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.namespace_id is not None:
            result['namespaceID'] = self.namespace_id

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()

        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()

        if self.programming_language is not None:
            result['programmingLanguage'] = self.programming_language

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.scale_config is not None:
            result['scaleConfig'] = self.scale_config.to_map()

        if self.sls_config is not None:
            result['slsConfig'] = self.sls_config.to_map()

        if self.startup_probe is not None:
            result['startupProbe'] = self.startup_probe.to_map()

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()

        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet

        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet

        if self.version is not None:
            result['version'] = self.version.to_map()

        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')

        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')

        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')

        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('customDNS') is not None:
            temp_model = main_models.CustomDNS()
            self.custom_dns = temp_model.from_map(m.get('customDNS'))

        if m.get('customDomainName') is not None:
            self.custom_domain_name = m.get('customDomainName')

        if m.get('customHealthCheckConfig') is not None:
            temp_model = main_models.CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m.get('customHealthCheckConfig'))

        if m.get('customHostAlias') is not None:
            temp_model = main_models.CustomHostAlias()
            self.custom_host_alias = temp_model.from_map(m.get('customHostAlias'))

        if m.get('customRuntimeConfig') is not None:
            temp_model = main_models.CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m.get('customRuntimeConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')

        if m.get('enableAppMetric') is not None:
            self.enable_app_metric = m.get('enableAppMetric')

        if m.get('enableArmsAdvanced') is not None:
            self.enable_arms_advanced = m.get('enableArmsAdvanced')

        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')

        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('httpTriggerConfig') is not None:
            temp_model = main_models.HTTPTriggerConfig()
            self.http_trigger_config = temp_model.from_map(m.get('httpTriggerConfig'))

        if m.get('imageConfig') is not None:
            temp_model = main_models.ImageConfig()
            self.image_config = temp_model.from_map(m.get('imageConfig'))

        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')

        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')

        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')

        if m.get('instanceLifecycleConfig') is not None:
            temp_model = main_models.InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m.get('instanceLifecycleConfig'))

        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('layers') is not None:
            self.layers = m.get('layers')

        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')

        if m.get('livenessProbe') is not None:
            temp_model = main_models.Probe()
            self.liveness_probe = temp_model.from_map(m.get('livenessProbe'))

        if m.get('logConfig') is not None:
            temp_model = main_models.LogConfig()
            self.log_config = temp_model.from_map(m.get('logConfig'))

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('namespaceID') is not None:
            self.namespace_id = m.get('namespaceID')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('nasConfig') is not None:
            temp_model = main_models.NASConfig()
            self.nas_config = temp_model.from_map(m.get('nasConfig'))

        if m.get('ossMountConfig') is not None:
            temp_model = main_models.OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m.get('ossMountConfig'))

        if m.get('programmingLanguage') is not None:
            self.programming_language = m.get('programmingLanguage')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('scaleConfig') is not None:
            temp_model = main_models.ScaleConfig()
            self.scale_config = temp_model.from_map(m.get('scaleConfig'))

        if m.get('slsConfig') is not None:
            temp_model = main_models.SLSConfig()
            self.sls_config = temp_model.from_map(m.get('slsConfig'))

        if m.get('startupProbe') is not None:
            temp_model = main_models.Probe()
            self.startup_probe = temp_model.from_map(m.get('startupProbe'))

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('tracingConfig') is not None:
            temp_model = main_models.TracingConfig()
            self.tracing_config = temp_model.from_map(m.get('tracingConfig'))

        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')

        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')

        if m.get('version') is not None:
            temp_model = main_models.Version()
            self.version = temp_model.from_map(m.get('version'))

        if m.get('vpcConfig') is not None:
            temp_model = main_models.VPCConfig()
            self.vpc_config = temp_model.from_map(m.get('vpcConfig'))

        return self

