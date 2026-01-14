# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetPluginConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetPluginConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
            temp_model = main_models.GetPluginConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPluginConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        category: int = None,
        config_check: str = None,
        config_example: str = None,
        domain_config_start_index: int = None,
        gateway_config_list: List[main_models.GetPluginConfigResponseBodyDataGatewayConfigList] = None,
        gateway_config_start_index: int = None,
        id: int = None,
        image_name: str = None,
        mode: int = None,
        name: str = None,
        phase: int = None,
        primary_user: str = None,
        priority: int = None,
        publish_state: int = None,
        readme: str = None,
        readme_en: str = None,
        route_config_start_index: int = None,
        status: str = None,
        summary: str = None,
        summary_en: str = None,
        type: int = None,
        version: str = None,
        version_json: str = None,
        wasm_lang: int = None,
    ):
        # The category of the plug-in. Valid values:
        # 
        # 0: user-defined
        # 
        # 1: permission authentication
        # 
        # 2: security protection
        # 
        # 3: transmission protocol
        # 
        # 4: traffic control
        # 
        # 5: traffic observation
        self.category = category
        # The information about the plug-in configuration used for checking.
        self.config_check = config_check
        self.config_example = config_example
        self.domain_config_start_index = domain_config_start_index
        # The list of gateway plug-in configurations.
        self.gateway_config_list = gateway_config_list
        self.gateway_config_start_index = gateway_config_start_index
        # The ID of the plug-in.
        self.id = id
        # The name of the image.
        self.image_name = image_name
        # The mode.
        self.mode = mode
        # The name of the plug-in.
        self.name = name
        # The execution stage of the plug-in. Valid values:
        # 
        # 0: default stage
        # 
        # 1: authorization stage
        # 
        # 2: authentication stage
        # 
        # 3: statistics stage
        self.phase = phase
        # The ID of the creator.
        self.primary_user = primary_user
        # The execution priority of the plug-in. A larger value indicates a higher priority.
        self.priority = priority
        # The publish status.
        self.publish_state = publish_state
        # The description of the README file.
        self.readme = readme
        # The description of the README file that is edited in English.
        self.readme_en = readme_en
        self.route_config_start_index = route_config_start_index
        # Indicates whether the plug-in is enabled. Valid values:
        # 
        # 0: disabled
        # 
        # 1: enabled
        self.status = status
        # The summary of the plug-in.
        self.summary = summary
        self.summary_en = summary_en
        # The type.
        self.type = type
        # The version of the plug-in.
        self.version = version
        self.version_json = version_json
        # The WebAssembly language. Valid values:
        # 
        # 0: C++
        # 
        # 1: TinyGo
        # 
        # 2: Rust
        # 
        # 3: AssemblyScript
        # 
        # 4: Zig
        self.wasm_lang = wasm_lang

    def validate(self):
        if self.gateway_config_list:
            for v1 in self.gateway_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config_check is not None:
            result['ConfigCheck'] = self.config_check

        if self.config_example is not None:
            result['ConfigExample'] = self.config_example

        if self.domain_config_start_index is not None:
            result['DomainConfigStartIndex'] = self.domain_config_start_index

        result['GatewayConfigList'] = []
        if self.gateway_config_list is not None:
            for k1 in self.gateway_config_list:
                result['GatewayConfigList'].append(k1.to_map() if k1 else None)

        if self.gateway_config_start_index is not None:
            result['GatewayConfigStartIndex'] = self.gateway_config_start_index

        if self.id is not None:
            result['Id'] = self.id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.publish_state is not None:
            result['PublishState'] = self.publish_state

        if self.readme is not None:
            result['Readme'] = self.readme

        if self.readme_en is not None:
            result['ReadmeEn'] = self.readme_en

        if self.route_config_start_index is not None:
            result['RouteConfigStartIndex'] = self.route_config_start_index

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.summary_en is not None:
            result['SummaryEn'] = self.summary_en

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        if self.version_json is not None:
            result['VersionJson'] = self.version_json

        if self.wasm_lang is not None:
            result['WasmLang'] = self.wasm_lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConfigCheck') is not None:
            self.config_check = m.get('ConfigCheck')

        if m.get('ConfigExample') is not None:
            self.config_example = m.get('ConfigExample')

        if m.get('DomainConfigStartIndex') is not None:
            self.domain_config_start_index = m.get('DomainConfigStartIndex')

        self.gateway_config_list = []
        if m.get('GatewayConfigList') is not None:
            for k1 in m.get('GatewayConfigList'):
                temp_model = main_models.GetPluginConfigResponseBodyDataGatewayConfigList()
                self.gateway_config_list.append(temp_model.from_map(k1))

        if m.get('GatewayConfigStartIndex') is not None:
            self.gateway_config_start_index = m.get('GatewayConfigStartIndex')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PublishState') is not None:
            self.publish_state = m.get('PublishState')

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        if m.get('ReadmeEn') is not None:
            self.readme_en = m.get('ReadmeEn')

        if m.get('RouteConfigStartIndex') is not None:
            self.route_config_start_index = m.get('RouteConfigStartIndex')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('SummaryEn') is not None:
            self.summary_en = m.get('SummaryEn')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionJson') is not None:
            self.version_json = m.get('VersionJson')

        if m.get('WasmLang') is not None:
            self.wasm_lang = m.get('WasmLang')

        return self

class GetPluginConfigResponseBodyDataGatewayConfigList(DaraModel):
    def __init__(
        self,
        config: str = None,
        config_level: int = None,
        enable: bool = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        plugin_id: int = None,
        resource_list: List[main_models.GetPluginConfigResponseBodyDataGatewayConfigListResourceList] = None,
    ):
        # The plug-in configuration.
        self.config = config
        # The application scope of the plug-in. Valid values:
        # 
        # 0: global
        # 
        # 1: domain names
        # 
        # 2: routes
        self.config_level = config_level
        # Indicates whether the plug-in is enabled.
        self.enable = enable
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the plug-in configuration.
        self.id = id
        # The ID of the gateway plug-in.
        self.plugin_id = plugin_id
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.GetPluginConfigResponseBodyDataGatewayConfigListResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        return self

class GetPluginConfigResponseBodyDataGatewayConfigListResourceList(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

