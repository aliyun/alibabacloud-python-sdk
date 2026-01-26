# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRumAppInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetRumAppInfoResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The application details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRumAppInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRumAppInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        app_config: str = None,
        app_group: str = None,
        app_type: str = None,
        backend_service_trace_region: str = None,
        bonree_sdkconfig: main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfig = None,
        cdn_domain: str = None,
        create_time: str = None,
        description: str = None,
        endpoint: str = None,
        is_subscription: str = None,
        name: str = None,
        nick_name: str = None,
        package_name: str = None,
        pid: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_domain_configs: List[main_models.GetRumAppInfoResponseBodyDataServiceDomainConfigs] = None,
        sls_logstore: str = None,
        sls_project: str = None,
        status: str = None,
        tags: List[main_models.GetRumAppInfoResponseBodyDataTags] = None,
        type: str = None,
        web_sdkconfig_json: str = None,
    ):
        # The application configurations in the JSON format. This parameter is deprecated.
        self.app_config = app_config
        # The group to which the application belongs.
        self.app_group = app_group
        # The application type. Valid values: web, miniapp, ios, and android.
        self.app_type = app_type
        # The region where the backend is deployed.
        self.backend_service_trace_region = backend_service_trace_region
        # The collection configurations.
        self.bonree_sdkconfig = bonree_sdkconfig
        # The domain name of the SDK.
        self.cdn_domain = cdn_domain
        # The time when the application was created. The value is a timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the application.
        self.description = description
        # The endpoint that is used to report application data.
        self.endpoint = endpoint
        # Indicates whether the application is subscribed. Valid values: true and false.
        self.is_subscription = is_subscription
        # The application name.
        self.name = name
        # The alias of the application.
        self.nick_name = nick_name
        # The name of the application package.
        self.package_name = package_name
        # The application ID.
        self.pid = pid
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of service domain configurations. Only mobile applications are supported.
        self.service_domain_configs = service_domain_configs
        # The name of the Simple Log Service Logstore that stores application data.
        self.sls_logstore = sls_logstore
        # The name of the Simple Log Service project that stores application data.
        self.sls_project = sls_project
        # The status of the application. Valid values: created, running, and stopped.
        self.status = status
        # The tags.
        self.tags = tags
        # The type of the application. Valid value: RUM.
        self.type = type
        self.web_sdkconfig_json = web_sdkconfig_json

    def validate(self):
        if self.bonree_sdkconfig:
            self.bonree_sdkconfig.validate()
        if self.service_domain_configs:
            for v1 in self.service_domain_configs:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_group is not None:
            result['AppGroup'] = self.app_group

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.backend_service_trace_region is not None:
            result['BackendServiceTraceRegion'] = self.backend_service_trace_region

        if self.bonree_sdkconfig is not None:
            result['BonreeSDKConfig'] = self.bonree_sdkconfig.to_map()

        if self.cdn_domain is not None:
            result['CdnDomain'] = self.cdn_domain

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.is_subscription is not None:
            result['IsSubscription'] = self.is_subscription

        if self.name is not None:
            result['Name'] = self.name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ServiceDomainConfigs'] = []
        if self.service_domain_configs is not None:
            for k1 in self.service_domain_configs:
                result['ServiceDomainConfigs'].append(k1.to_map() if k1 else None)

        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.web_sdkconfig_json is not None:
            result['WebSDKConfigJson'] = self.web_sdkconfig_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppGroup') is not None:
            self.app_group = m.get('AppGroup')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BackendServiceTraceRegion') is not None:
            self.backend_service_trace_region = m.get('BackendServiceTraceRegion')

        if m.get('BonreeSDKConfig') is not None:
            temp_model = main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfig()
            self.bonree_sdkconfig = temp_model.from_map(m.get('BonreeSDKConfig'))

        if m.get('CdnDomain') is not None:
            self.cdn_domain = m.get('CdnDomain')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('IsSubscription') is not None:
            self.is_subscription = m.get('IsSubscription')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.service_domain_configs = []
        if m.get('ServiceDomainConfigs') is not None:
            for k1 in m.get('ServiceDomainConfigs'):
                temp_model = main_models.GetRumAppInfoResponseBodyDataServiceDomainConfigs()
                self.service_domain_configs.append(temp_model.from_map(k1))

        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetRumAppInfoResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WebSDKConfigJson') is not None:
            self.web_sdkconfig_json = m.get('WebSDKConfigJson')

        return self

class GetRumAppInfoResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetRumAppInfoResponseBodyDataServiceDomainConfigs(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        propagator_types: List[str] = None,
        sampling_rate: int = None,
        tracing: bool = None,
    ):
        # The description.
        self.description = description
        # The domain name or IP address.
        self.domain = domain
        # The trace propagation protocols. This parameter is required if the tracing analysis feature is enabled.
        self.propagator_types = propagator_types
        # The sampling rate of a trace. Valid values: (0, 100].
        self.sampling_rate = sampling_rate
        # Indicates whether the tracing analysis feature is enabled. To enable the tracing analysis feature, you must activate Managed Service for OpenTelemetry. Valid values:
        # 
        # *   `true`: enables the tracing analysis feature. If you enable the tracing analysis feature, related headers are inserted into requests for the domain name.
        # *   `false`: disables the tracing analysis feature.
        self.tracing = tracing

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.propagator_types is not None:
            result['PropagatorTypes'] = self.propagator_types

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.tracing is not None:
            result['Tracing'] = self.tracing

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PropagatorTypes') is not None:
            self.propagator_types = m.get('PropagatorTypes')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')

        return self

class GetRumAppInfoResponseBodyDataBonreeSDKConfig(DaraModel):
    def __init__(
        self,
        module_config: main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfigModuleConfig = None,
        sampling_config: main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfigSamplingConfig = None,
    ):
        # The module configuration.
        self.module_config = module_config
        # Sampling configuration.
        self.sampling_config = sampling_config

    def validate(self):
        if self.module_config:
            self.module_config.validate()
        if self.sampling_config:
            self.sampling_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_config is not None:
            result['moduleConfig'] = self.module_config.to_map()

        if self.sampling_config is not None:
            result['samplingConfig'] = self.sampling_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleConfig') is not None:
            temp_model = main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfigModuleConfig()
            self.module_config = temp_model.from_map(m.get('moduleConfig'))

        if m.get('samplingConfig') is not None:
            temp_model = main_models.GetRumAppInfoResponseBodyDataBonreeSDKConfigSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('samplingConfig'))

        return self

class GetRumAppInfoResponseBodyDataBonreeSDKConfigSamplingConfig(DaraModel):
    def __init__(
        self,
        sampling_rate: int = None,
        sampling_type: int = None,
    ):
        # Sampling rate: between (0, 1000], a thousandth.
        self.sampling_rate = sampling_rate
        # Sampling type, currently only session random sampling is supported, that is, fixed transmission: 1.
        self.sampling_type = sampling_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sampling_rate is not None:
            result['samplingRate'] = self.sampling_rate

        if self.sampling_type is not None:
            result['samplingType'] = self.sampling_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('samplingRate') is not None:
            self.sampling_rate = m.get('samplingRate')

        if m.get('samplingType') is not None:
            self.sampling_type = m.get('samplingType')

        return self

class GetRumAppInfoResponseBodyDataBonreeSDKConfigModuleConfig(DaraModel):
    def __init__(
        self,
        default_config: Dict[str, main_models.DataBonreeSDKConfigModuleConfigDefaultConfigValue] = None,
        enable: bool = None,
        version_configs: Dict[str, main_models.DataBonreeSDKConfigModuleConfigVersionConfigsValue] = None,
    ):
        # The default configuration of the application.
        self.default_config = default_config
        # Indicates whether the configuration is enabled.
        self.enable = enable
        # The version configurations of the application.
        self.version_configs = version_configs

    def validate(self):
        if self.default_config:
            for v1 in self.default_config.values():
                 if v1:
                    v1.validate()
        if self.version_configs:
            for v1 in self.version_configs.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['defaultConfig'] = {}
        if self.default_config is not None:
            for k1, v1 in self.default_config.items():
                result['defaultConfig'][k1] = v1.to_map() if v1 else None

        if self.enable is not None:
            result['enable'] = self.enable

        result['versionConfigs'] = {}
        if self.version_configs is not None:
            for k1, v1 in self.version_configs.items():
                result['versionConfigs'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_config = {}
        if m.get('defaultConfig') is not None:
            for k1, v1 in m.get('defaultConfig').items():
                temp_model = main_models.DataBonreeSDKConfigModuleConfigDefaultConfigValue()
                self.default_config[k1] = temp_model.from_map(v1)

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.version_configs = {}
        if m.get('versionConfigs') is not None:
            for k1, v1 in m.get('versionConfigs').items():
                temp_model = main_models.DataBonreeSDKConfigModuleConfigVersionConfigsValue()
                self.version_configs[k1] = temp_model.from_map(v1)

        return self

