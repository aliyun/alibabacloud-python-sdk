# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        custom_app_info_shrink: str = None,
        description: str = None,
        file_name: str = None,
        file_path: str = None,
        icon_url: str = None,
        install_param: str = None,
        oss_app_url: str = None,
        sign_apk: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The ID of the region.
        self.biz_region_id = biz_region_id
        # The information about the custom app.
        # 
        # > 
        # 
        # *   If you want to pass in a custom app, configure the `CustomAppInfo` parameter. Take note that the six fields within it are mandatory.
        # 
        # *   A custom app has a higher priority than an app from the Alibaba Cloud Workspace Application Center. If you configure the `CustomAppInfo` parameter, the `FileName` and `FilePath` pair or the `OssAppUrl` will not take effect.
        self.custom_app_info_shrink = custom_app_info_shrink
        # The description of the application.
        self.description = description
        # The name used by the app file in Object Storage Service (OSS). This parameter, combined with `FilePath`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [Elastic Desktop Service (EDS) Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_name = file_name
        # The OSS bucket path to the app file. This parameter, combined with `FileName`, uniquely identifies the OSS path of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.file_path = file_path
        # The icon URL of the application.
        self.icon_url = icon_url
        # The parameters used for installing the application. By default, the `-r` parameter is included when you install an application.
        self.install_param = install_param
        # The OSS bucket endpoint of the app file.
        # 
        # > 
        # 
        # *   If you want to pass in an app from the Alibaba Cloud Workspace Application Center, configure the `FileName` and `FilePath` parameters. Alternatively, configure the `OssAppUrl` parameter. The FileName and FilePath parameters takes precedence over the OssAppUrl parameter.
        # 
        # *   Log on to the [EDS Enterprise](https://eds.console.aliyun.com/osshelp) console, upload the app file to the Application Center according to the on-screen instructions, and then retrieve the parameter value.
        self.oss_app_url = oss_app_url
        self.sign_apk = sign_apk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.custom_app_info_shrink is not None:
            result['CustomAppInfo'] = self.custom_app_info_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.install_param is not None:
            result['InstallParam'] = self.install_param

        if self.oss_app_url is not None:
            result['OssAppUrl'] = self.oss_app_url

        if self.sign_apk is not None:
            result['SignApk'] = self.sign_apk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('CustomAppInfo') is not None:
            self.custom_app_info_shrink = m.get('CustomAppInfo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('InstallParam') is not None:
            self.install_param = m.get('InstallParam')

        if m.get('OssAppUrl') is not None:
            self.oss_app_url = m.get('OssAppUrl')

        if m.get('SignApk') is not None:
            self.sign_apk = m.get('SignApk')

        return self

