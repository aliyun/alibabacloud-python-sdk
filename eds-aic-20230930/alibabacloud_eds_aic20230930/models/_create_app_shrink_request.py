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
        # The application name.
        self.app_name = app_name
        # The region ID.
        self.biz_region_id = biz_region_id
        # The custom application information.
        # 
        # > - If you pass a custom application, pass the `CustomAppInfo` parameter. All six fields in this object parameter are required.
        # >
        # > - Custom applications have a higher priority than applications from the WUYING Workspace app center. If you pass the `CustomAppInfo` parameter, `FileName` and `FilePath`, or `OssAppUrl` will be invalid.
        self.custom_app_info_shrink = custom_app_info_shrink
        # The application description.
        self.description = description
        # The name of the application file stored in Object Storage Service (OSS). This parameter and `FilePath` together determine the unique OSS address.
        # 
        # > - If you pass an application from the WUYING Workspace app center, you must pass `FileName` and `FilePath`, or `OssAppUrl`. The former takes precedence.
        # >
        # > - Log on to the [WUYING Workspace console](https://eds.console.aliyun.com/osshelp). Follow the on-screen instructions to upload your application file to the WUYING Workspace app center to obtain this parameter.
        self.file_name = file_name
        # The storage address of the application file in an OSS bucket. This parameter and `FileName` together determine the unique OSS address.
        # 
        # > - If you pass an application from the WUYING Workspace app center, you must pass `FileName` and `FilePath`, or `OssAppUrl`. The former takes precedence.
        # >
        # > - Log on to the [WUYING Workspace console](https://eds.console.aliyun.com/osshelp). Follow the on-screen instructions to upload your application file to the WUYING Workspace app center to obtain this parameter.
        self.file_path = file_path
        # The URL of the application icon.
        self.icon_url = icon_url
        # The installation parameters. The `-r` installation parameter is included by default when you install the application.
        self.install_param = install_param
        # The OSS address of the application.
        # 
        # > - If you pass an application from the WUYING Workspace app center, you must pass `FileName` and `FilePath`, or `OssAppUrl`. The former takes precedence.
        # >
        # > - Log on to the [WUYING Workspace console](https://eds.console.aliyun.com/osshelp). Follow the on-screen instructions to upload your application file to the WUYING Workspace app center to obtain this parameter.
        self.oss_app_url = oss_app_url
        # Specifies whether to perform a system signature.
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

