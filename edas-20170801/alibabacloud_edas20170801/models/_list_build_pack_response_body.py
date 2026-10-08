# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListBuildPackResponseBody(DaraModel):
    def __init__(
        self,
        build_pack_list: main_models.ListBuildPackResponseBodyBuildPackList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.build_pack_list = build_pack_list
        # code
        self.code = code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.build_pack_list:
            self.build_pack_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_pack_list is not None:
            result['BuildPackList'] = self.build_pack_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildPackList') is not None:
            temp_model = main_models.ListBuildPackResponseBodyBuildPackList()
            self.build_pack_list = temp_model.from_map(m.get('BuildPackList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBuildPackResponseBodyBuildPackList(DaraModel):
    def __init__(
        self,
        build_pack: List[main_models.ListBuildPackResponseBodyBuildPackListBuildPack] = None,
    ):
        self.build_pack = build_pack

    def validate(self):
        if self.build_pack:
            for v1 in self.build_pack:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildPack'] = []
        if self.build_pack is not None:
            for k1 in self.build_pack:
                result['BuildPack'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_pack = []
        if m.get('BuildPack') is not None:
            for k1 in m.get('BuildPack'):
                temp_model = main_models.ListBuildPackResponseBodyBuildPackListBuildPack()
                self.build_pack.append(temp_model.from_map(k1))

        return self

class ListBuildPackResponseBodyBuildPackListBuildPack(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        disabled: bool = None,
        feature: str = None,
        image_id: str = None,
        multiple_tenant: bool = None,
        pack_version: str = None,
        pandora_desc: str = None,
        pandora_download_url: str = None,
        pandora_version: str = None,
        plugin_info: str = None,
        script_name: str = None,
        script_version: str = None,
        support_features: str = None,
        tengine_download_url: str = None,
        tengine_image_id: str = None,
        tomcat_desc: str = None,
        tomcat_download_url: str = None,
        tomcat_path: str = None,
        tomcat_version: str = None,
        with_tengine: bool = None,
    ):
        self.config_id = config_id
        self.disabled = disabled
        self.feature = feature
        self.image_id = image_id
        self.multiple_tenant = multiple_tenant
        self.pack_version = pack_version
        self.pandora_desc = pandora_desc
        self.pandora_download_url = pandora_download_url
        self.pandora_version = pandora_version
        self.plugin_info = plugin_info
        self.script_name = script_name
        self.script_version = script_version
        self.support_features = support_features
        self.tengine_download_url = tengine_download_url
        self.tengine_image_id = tengine_image_id
        self.tomcat_desc = tomcat_desc
        self.tomcat_download_url = tomcat_download_url
        self.tomcat_path = tomcat_path
        self.tomcat_version = tomcat_version
        self.with_tengine = with_tengine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.feature is not None:
            result['Feature'] = self.feature

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.multiple_tenant is not None:
            result['MultipleTenant'] = self.multiple_tenant

        if self.pack_version is not None:
            result['PackVersion'] = self.pack_version

        if self.pandora_desc is not None:
            result['PandoraDesc'] = self.pandora_desc

        if self.pandora_download_url is not None:
            result['PandoraDownloadUrl'] = self.pandora_download_url

        if self.pandora_version is not None:
            result['PandoraVersion'] = self.pandora_version

        if self.plugin_info is not None:
            result['PluginInfo'] = self.plugin_info

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version

        if self.support_features is not None:
            result['SupportFeatures'] = self.support_features

        if self.tengine_download_url is not None:
            result['TengineDownloadUrl'] = self.tengine_download_url

        if self.tengine_image_id is not None:
            result['TengineImageId'] = self.tengine_image_id

        if self.tomcat_desc is not None:
            result['TomcatDesc'] = self.tomcat_desc

        if self.tomcat_download_url is not None:
            result['TomcatDownloadUrl'] = self.tomcat_download_url

        if self.tomcat_path is not None:
            result['TomcatPath'] = self.tomcat_path

        if self.tomcat_version is not None:
            result['TomcatVersion'] = self.tomcat_version

        if self.with_tengine is not None:
            result['WithTengine'] = self.with_tengine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Feature') is not None:
            self.feature = m.get('Feature')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('MultipleTenant') is not None:
            self.multiple_tenant = m.get('MultipleTenant')

        if m.get('PackVersion') is not None:
            self.pack_version = m.get('PackVersion')

        if m.get('PandoraDesc') is not None:
            self.pandora_desc = m.get('PandoraDesc')

        if m.get('PandoraDownloadUrl') is not None:
            self.pandora_download_url = m.get('PandoraDownloadUrl')

        if m.get('PandoraVersion') is not None:
            self.pandora_version = m.get('PandoraVersion')

        if m.get('PluginInfo') is not None:
            self.plugin_info = m.get('PluginInfo')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')

        if m.get('SupportFeatures') is not None:
            self.support_features = m.get('SupportFeatures')

        if m.get('TengineDownloadUrl') is not None:
            self.tengine_download_url = m.get('TengineDownloadUrl')

        if m.get('TengineImageId') is not None:
            self.tengine_image_id = m.get('TengineImageId')

        if m.get('TomcatDesc') is not None:
            self.tomcat_desc = m.get('TomcatDesc')

        if m.get('TomcatDownloadUrl') is not None:
            self.tomcat_download_url = m.get('TomcatDownloadUrl')

        if m.get('TomcatPath') is not None:
            self.tomcat_path = m.get('TomcatPath')

        if m.get('TomcatVersion') is not None:
            self.tomcat_version = m.get('TomcatVersion')

        if m.get('WithTengine') is not None:
            self.with_tengine = m.get('WithTengine')

        return self

