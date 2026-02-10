# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListPluginForUuidResponseBody(DaraModel):
    def __init__(
        self,
        aegis_uuid_target_plugin_config_list: List[main_models.ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigList] = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # An array that consists of the information about the plug-ins.
        self.aegis_uuid_target_plugin_config_list = aegis_uuid_target_plugin_config_list
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.aegis_uuid_target_plugin_config_list:
            for v1 in self.aegis_uuid_target_plugin_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AegisUuidTargetPluginConfigList'] = []
        if self.aegis_uuid_target_plugin_config_list is not None:
            for k1 in self.aegis_uuid_target_plugin_config_list:
                result['AegisUuidTargetPluginConfigList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aegis_uuid_target_plugin_config_list = []
        if m.get('AegisUuidTargetPluginConfigList') is not None:
            for k1 in m.get('AegisUuidTargetPluginConfigList'):
                temp_model = main_models.ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigList()
                self.aegis_uuid_target_plugin_config_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigList(DaraModel):
    def __init__(
        self,
        aegis_suspicious_config_list: List[main_models.ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigListAegisSuspiciousConfigList] = None,
        plugin_install_code: str = None,
        plugin_name: str = None,
        plugin_online_installed: bool = None,
        plugin_online_status: bool = None,
        plugin_version: str = None,
    ):
        # An array that consists of the configurations of plug-ins.
        self.aegis_suspicious_config_list = aegis_suspicious_config_list
        # The installation code of the plug-in.
        self.plugin_install_code = plugin_install_code
        # The name of the plug-in. Valid values:
        # 
        # *   **alihips**: trojan-specific prevention
        # *   **alisecguard**: attack-specific prevention
        # *   **alinet**: defense against attacks on servers
        self.plugin_name = plugin_name
        # Indicates whether the plug-in is installed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.plugin_online_installed = plugin_online_installed
        # Indicates whether the plug-in is online. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.plugin_online_status = plugin_online_status
        # The version of the plug-in.
        self.plugin_version = plugin_version

    def validate(self):
        if self.aegis_suspicious_config_list:
            for v1 in self.aegis_suspicious_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AegisSuspiciousConfigList'] = []
        if self.aegis_suspicious_config_list is not None:
            for k1 in self.aegis_suspicious_config_list:
                result['AegisSuspiciousConfigList'].append(k1.to_map() if k1 else None)

        if self.plugin_install_code is not None:
            result['PluginInstallCode'] = self.plugin_install_code

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_online_installed is not None:
            result['PluginOnlineInstalled'] = self.plugin_online_installed

        if self.plugin_online_status is not None:
            result['PluginOnlineStatus'] = self.plugin_online_status

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aegis_suspicious_config_list = []
        if m.get('AegisSuspiciousConfigList') is not None:
            for k1 in m.get('AegisSuspiciousConfigList'):
                temp_model = main_models.ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigListAegisSuspiciousConfigList()
                self.aegis_suspicious_config_list.append(temp_model.from_map(k1))

        if m.get('PluginInstallCode') is not None:
            self.plugin_install_code = m.get('PluginInstallCode')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginOnlineInstalled') is not None:
            self.plugin_online_installed = m.get('PluginOnlineInstalled')

        if m.get('PluginOnlineStatus') is not None:
            self.plugin_online_status = m.get('PluginOnlineStatus')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        return self

class ListPluginForUuidResponseBodyAegisUuidTargetPluginConfigListAegisSuspiciousConfigList(DaraModel):
    def __init__(
        self,
        config: bool = None,
        msg: str = None,
        overall_config: bool = None,
        type: str = None,
    ):
        # Indicates whether the plug-in is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.config = config
        # The message that indicates whether you are authorized to install the plug-in on your server or whether the plug-in is installed on your server. Valid values:
        # 
        # *   **authorized**: authorized
        # *   **unauthorized**: unauthorized
        # *   **unbind**: not installed
        # *   **nonsupport**: not supported
        self.msg = msg
        # Indicates whether the plug-in is globally configured. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.overall_config = overall_config
        # The name of the plug-in. Valid values:
        # 
        # *   **alihips**: trojan-specific prevention
        # *   **alisecguard**: attack-specific prevention
        # *   **alinet**: defense against attacks on servers
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.overall_config is not None:
            result['OverallConfig'] = self.overall_config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('OverallConfig') is not None:
            self.overall_config = m.get('OverallConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

