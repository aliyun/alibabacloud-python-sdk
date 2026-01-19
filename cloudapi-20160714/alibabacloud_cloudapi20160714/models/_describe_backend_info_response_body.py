# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeBackendInfoResponseBody(DaraModel):
    def __init__(
        self,
        backend_info: main_models.DescribeBackendInfoResponseBodyBackendInfo = None,
        request_id: str = None,
    ):
        # The information about the backend service.
        self.backend_info = backend_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.backend_info:
            self.backend_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_info is not None:
            result['BackendInfo'] = self.backend_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendInfo') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfo()
            self.backend_info = temp_model.from_map(m.get('BackendInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackendInfoResponseBodyBackendInfo(DaraModel):
    def __init__(
        self,
        backend_id: str = None,
        backend_models: List[main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModels] = None,
        backend_name: str = None,
        backend_type: str = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
    ):
        # The ID of the backend service.
        self.backend_id = backend_id
        # The configurations of the backend service in the environment.
        self.backend_models = backend_models
        # The name of the backend service.
        self.backend_name = backend_name
        # The type of the backend service.
        self.backend_type = backend_type
        # The time when the backend service was created.
        self.created_time = created_time
        # The description of the backend service.
        self.description = description
        # The time when the backend service was modified.
        self.modified_time = modified_time

    def validate(self):
        if self.backend_models:
            for v1 in self.backend_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        result['BackendModels'] = []
        if self.backend_models is not None:
            for k1 in self.backend_models:
                result['BackendModels'].append(k1.to_map() if k1 else None)

        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.backend_type is not None:
            result['BackendType'] = self.backend_type

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        self.backend_models = []
        if m.get('BackendModels') is not None:
            for k1 in m.get('BackendModels'):
                temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModels()
                self.backend_models.append(temp_model.from_map(k1))

        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BackendType') is not None:
            self.backend_type = m.get('BackendType')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModels(DaraModel):
    def __init__(
        self,
        backend_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfig = None,
        backend_model_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        stage_mode_id: str = None,
        stage_name: str = None,
    ):
        # The backend service configurations.
        self.backend_config = backend_config
        # The ID of the backend service in the environment.
        self.backend_model_id = backend_model_id
        # The description of the backend service.
        self.description = description
        # The time when the backend service was created.
        self.gmt_create = gmt_create
        # The time when the backend service was modified.
        self.gmt_modified = gmt_modified
        # The ID of the environment.
        self.stage_mode_id = stage_mode_id
        # The environment name.
        self.stage_name = stage_name

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_config is not None:
            result['BackendConfig'] = self.backend_config.to_map()

        if self.backend_model_id is not None:
            result['BackendModelId'] = self.backend_model_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.stage_mode_id is not None:
            result['StageModeId'] = self.stage_mode_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfig()
            self.backend_config = temp_model.from_map(m.get('BackendConfig'))

        if m.get('BackendModelId') is not None:
            self.backend_model_id = m.get('BackendModelId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('StageModeId') is not None:
            self.stage_mode_id = m.get('StageModeId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfig(DaraModel):
    def __init__(
        self,
        discovery_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfig = None,
        edas_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEdasConfig = None,
        event_bridge_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEventBridgeConfig = None,
        function_compute_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigFunctionComputeConfig = None,
        http_target_host_name: str = None,
        mock_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfig = None,
        oss_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigOssConfig = None,
        service_address: str = None,
        service_timeout: int = None,
        type: str = None,
        vpc_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigVpcConfig = None,
    ):
        # The information about the backend service when the backend service is of the Service Discovery type.
        self.discovery_config = discovery_config
        # The EDAS configuration.
        self.edas_config = edas_config
        # The information about the backend service whose type is EventBridge.
        self.event_bridge_config = event_bridge_config
        # The information about the backend service whose type is Function Compute.
        self.function_compute_config = function_compute_config
        # The host of the HTTP backend service.
        self.http_target_host_name = http_target_host_name
        # The information about the backend service when the backend service is of the Mock type.
        self.mock_config = mock_config
        # The information about the backend service whose type is Object Storage Service (OSS).
        self.oss_config = oss_config
        # The URL of the backend service.
        self.service_address = service_address
        # The timeout period of the backend service, in millisecond.
        self.service_timeout = service_timeout
        # The type of the backend service.
        self.type = type
        # The information about the backend service when the backend service is of the VPC type.
        self.vpc_config = vpc_config

    def validate(self):
        if self.discovery_config:
            self.discovery_config.validate()
        if self.edas_config:
            self.edas_config.validate()
        if self.event_bridge_config:
            self.event_bridge_config.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.mock_config:
            self.mock_config.validate()
        if self.oss_config:
            self.oss_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovery_config is not None:
            result['DiscoveryConfig'] = self.discovery_config.to_map()

        if self.edas_config is not None:
            result['EdasConfig'] = self.edas_config.to_map()

        if self.event_bridge_config is not None:
            result['EventBridgeConfig'] = self.event_bridge_config.to_map()

        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()

        if self.http_target_host_name is not None:
            result['HttpTargetHostName'] = self.http_target_host_name

        if self.mock_config is not None:
            result['MockConfig'] = self.mock_config.to_map()

        if self.oss_config is not None:
            result['OssConfig'] = self.oss_config.to_map()

        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address

        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveryConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfig()
            self.discovery_config = temp_model.from_map(m.get('DiscoveryConfig'))

        if m.get('EdasConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEdasConfig()
            self.edas_config = temp_model.from_map(m.get('EdasConfig'))

        if m.get('EventBridgeConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEventBridgeConfig()
            self.event_bridge_config = temp_model.from_map(m.get('EventBridgeConfig'))

        if m.get('FunctionComputeConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m.get('FunctionComputeConfig'))

        if m.get('HttpTargetHostName') is not None:
            self.http_target_host_name = m.get('HttpTargetHostName')

        if m.get('MockConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfig()
            self.mock_config = temp_model.from_map(m.get('MockConfig'))

        if m.get('OssConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigOssConfig()
            self.oss_config = temp_model.from_map(m.get('OssConfig'))

        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')

        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpcConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m.get('VpcConfig'))

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigVpcConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_access_id: str = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
        vpc_target_host_name: str = None,
    ):
        # The ID of the Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance in the VPC.
        self.instance_id = instance_id
        # The name of the VPC configuration.
        self.name = name
        # The port number that corresponds to the instance.
        self.port = port
        # The ID of the VPC access authorization.
        self.vpc_access_id = vpc_access_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # Indicates whether HTTP or HTTPS is used.
        self.vpc_scheme = vpc_scheme
        # The host of the VPC backend service.
        self.vpc_target_host_name = vpc_target_host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_scheme is not None:
            result['VpcScheme'] = self.vpc_scheme

        if self.vpc_target_host_name is not None:
            result['VpcTargetHostName'] = self.vpc_target_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcScheme') is not None:
            self.vpc_scheme = m.get('VpcScheme')

        if m.get('VpcTargetHostName') is not None:
            self.vpc_target_host_name = m.get('VpcTargetHostName')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigOssConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        oss_region_id: str = None,
    ):
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # The region ID of the OSS bucket.
        self.oss_region_id = oss_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfig(DaraModel):
    def __init__(
        self,
        mock_headers: List[main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfigMockHeaders] = None,
        mock_result: str = None,
        mock_status_code: str = None,
    ):
        # The header in the mocked response.
        self.mock_headers = mock_headers
        # The mocked response.
        self.mock_result = mock_result
        # The status code in the mocked response.
        self.mock_status_code = mock_status_code

    def validate(self):
        if self.mock_headers:
            for v1 in self.mock_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MockHeaders'] = []
        if self.mock_headers is not None:
            for k1 in self.mock_headers:
                result['MockHeaders'].append(k1.to_map() if k1 else None)

        if self.mock_result is not None:
            result['MockResult'] = self.mock_result

        if self.mock_status_code is not None:
            result['MockStatusCode'] = self.mock_status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mock_headers = []
        if m.get('MockHeaders') is not None:
            for k1 in m.get('MockHeaders'):
                temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfigMockHeaders()
                self.mock_headers.append(temp_model.from_map(k1))

        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')

        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigMockConfigMockHeaders(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        # The header name.
        self.header_name = header_name
        # The header value.
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header_name is not None:
            result['HeaderName'] = self.header_name

        if self.header_value is not None:
            result['HeaderValue'] = self.header_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')

        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigFunctionComputeConfig(DaraModel):
    def __init__(
        self,
        fc_base_url: str = None,
        fc_region_id: str = None,
        fc_type: str = None,
        function_name: str = None,
        only_business_path: bool = None,
        qualifier: str = None,
        role_arn: str = None,
        service_name: str = None,
        trigger_name: str = None,
    ):
        # The root path of the Function Compute service.
        self.fc_base_url = fc_base_url
        # The region ID of the Function Compute service.
        self.fc_region_id = fc_region_id
        # The type of the service in Function Compute.
        self.fc_type = fc_type
        # The function name that is defined in Function Compute.
        self.function_name = function_name
        # Indicates whether the backend service receives only the service path.
        self.only_business_path = only_business_path
        # The alias of the function.
        self.qualifier = qualifier
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by API Gateway to access Function Compute.
        self.role_arn = role_arn
        # The service name that is defined in Function Compute.
        self.service_name = service_name
        # The name of the trigger.
        # 
        # You can specify the TriggerName or TriggerUrl parameter. The TriggerName parameter is optional.
        self.trigger_name = trigger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fc_base_url is not None:
            result['FcBaseUrl'] = self.fc_base_url

        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id

        if self.fc_type is not None:
            result['FcType'] = self.fc_type

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.only_business_path is not None:
            result['OnlyBusinessPath'] = self.only_business_path

        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FcBaseUrl') is not None:
            self.fc_base_url = m.get('FcBaseUrl')

        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')

        if m.get('FcType') is not None:
            self.fc_type = m.get('FcType')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('OnlyBusinessPath') is not None:
            self.only_business_path = m.get('OnlyBusinessPath')

        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEventBridgeConfig(DaraModel):
    def __init__(
        self,
        event_bridge_region_id: str = None,
        event_bus: str = None,
        event_source: str = None,
        role_arn: str = None,
    ):
        # The region ID of the event bus in EventBridge.
        self.event_bridge_region_id = event_bridge_region_id
        # The event bus.
        self.event_bus = event_bus
        # The event source.
        self.event_source = event_source
        # The ARN of the RAM role to be assumed by API Gateway to access EventBridge.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bridge_region_id is not None:
            result['EventBridgeRegionId'] = self.event_bridge_region_id

        if self.event_bus is not None:
            result['EventBus'] = self.event_bus

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBridgeRegionId') is not None:
            self.event_bridge_region_id = m.get('EventBridgeRegionId')

        if m.get('EventBus') is not None:
            self.event_bus = m.get('EventBus')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigEdasConfig(DaraModel):
    def __init__(
        self,
        edas_app_id: str = None,
        microservice_namespace: str = None,
        microservice_namespace_id: str = None,
        microservice_namespace_name: str = None,
        mse_instance_id: str = None,
        registry_type: str = None,
        service_name: str = None,
    ):
        # The EDAS application ID.
        self.edas_app_id = edas_app_id
        # The ID of the microservices namespace in EDAS.
        self.microservice_namespace = microservice_namespace
        # The ID of the microservices namespace in EDAS.
        self.microservice_namespace_id = microservice_namespace_id
        # The name of the microservices namespace in EDAS.
        self.microservice_namespace_name = microservice_namespace_name
        # The MSE instance ID.
        self.mse_instance_id = mse_instance_id
        # The registration type.
        self.registry_type = registry_type
        # The service name.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edas_app_id is not None:
            result['EdasAppId'] = self.edas_app_id

        if self.microservice_namespace is not None:
            result['MicroserviceNamespace'] = self.microservice_namespace

        if self.microservice_namespace_id is not None:
            result['MicroserviceNamespaceId'] = self.microservice_namespace_id

        if self.microservice_namespace_name is not None:
            result['MicroserviceNamespaceName'] = self.microservice_namespace_name

        if self.mse_instance_id is not None:
            result['MseInstanceId'] = self.mse_instance_id

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasAppId') is not None:
            self.edas_app_id = m.get('EdasAppId')

        if m.get('MicroserviceNamespace') is not None:
            self.microservice_namespace = m.get('MicroserviceNamespace')

        if m.get('MicroserviceNamespaceId') is not None:
            self.microservice_namespace_id = m.get('MicroserviceNamespaceId')

        if m.get('MicroserviceNamespaceName') is not None:
            self.microservice_namespace_name = m.get('MicroserviceNamespaceName')

        if m.get('MseInstanceId') is not None:
            self.mse_instance_id = m.get('MseInstanceId')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfig(DaraModel):
    def __init__(
        self,
        nacos_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigNacosConfig = None,
        rc_type: str = None,
        zookeeper_config: main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigZookeeperConfig = None,
    ):
        # The Nacos configurations.
        self.nacos_config = nacos_config
        # The registry type.
        self.rc_type = rc_type
        # The ZooKeeper configuration.
        self.zookeeper_config = zookeeper_config

    def validate(self):
        if self.nacos_config:
            self.nacos_config.validate()
        if self.zookeeper_config:
            self.zookeeper_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nacos_config is not None:
            result['NacosConfig'] = self.nacos_config.to_map()

        if self.rc_type is not None:
            result['RcType'] = self.rc_type

        if self.zookeeper_config is not None:
            result['ZookeeperConfig'] = self.zookeeper_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NacosConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigNacosConfig()
            self.nacos_config = temp_model.from_map(m.get('NacosConfig'))

        if m.get('RcType') is not None:
            self.rc_type = m.get('RcType')

        if m.get('ZookeeperConfig') is not None:
            temp_model = main_models.DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigZookeeperConfig()
            self.zookeeper_config = temp_model.from_map(m.get('ZookeeperConfig'))

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigZookeeperConfig(DaraModel):
    def __init__(
        self,
        connect_string: str = None,
        namespace: str = None,
        service_name: str = None,
    ):
        # The connection URL of the ZooKeeper server.
        self.connect_string = connect_string
        # The namespace.
        self.namespace = namespace
        # Service name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeBackendInfoResponseBodyBackendInfoBackendModelsBackendConfigDiscoveryConfigNacosConfig(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        auth_type: str = None,
        clusters: str = None,
        group_name: str = None,
        namespace: str = None,
        password: str = None,
        secret_key: str = None,
        server_address: str = None,
        service_name: str = None,
        user_name: str = None,
    ):
        # The AccessKey of the RAM user that has the resource management permissions on Microservices Engine (MSE).
        self.access_key = access_key
        # The authentication method.
        self.auth_type = auth_type
        # The name of the cluster to which the microservice belongs.
        self.clusters = clusters
        # The name of the group to which the microservice that is registered with Nacos belongs.
        self.group_name = group_name
        # The ID of the namespace where the microservice that is registered with Nacos resides.
        self.namespace = namespace
        # The password.
        self.password = password
        # The SecretKey of the RAM user that has the resource management permissions on MSE.
        self.secret_key = secret_key
        # The Nacos service address.
        self.server_address = server_address
        # The microservice name.
        self.service_name = service_name
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.clusters is not None:
            result['Clusters'] = self.clusters

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.password is not None:
            result['Password'] = self.password

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.server_address is not None:
            result['ServerAddress'] = self.server_address

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('ServerAddress') is not None:
            self.server_address = m.get('ServerAddress')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

