# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadCloudAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_version: str = None,
        description: str = None,
        download_url: str = None,
        md_5: str = None,
        pkg_format: str = None,
        pkg_labels_shrink: str = None,
        pkg_type: str = None,
        post_command_path: str = None,
        post_command_timeout_sec: int = None,
    ):
        # The application name. For Android applications, use the package name, such as com.aaa.bbb.
        # 
        # Value rules:
        # 1. Length: 4 to 50 characters.
        # 2. Lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 3. The first and last characters must be letters or digits.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The application version. For Android applications, use the VersionName, such as 1.1.1.
        # 
        # Value rules:
        # 1. Length: 1 to 50 characters.
        # 2. Lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 3. The first and last characters must be letters or digits.
        # 
        # This parameter is required.
        self.app_version = app_version
        # The description of the application.
        self.description = description
        # The download URL of the application package.
        # 
        # This parameter is required.
        self.download_url = download_url
        # The MD5 checksum of the application package, used to verify package integrity.
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The package format. The default value is the file extension of the download URL. Valid values:
        # 1. apk
        # 2. tar.gz
        # 3. tar
        # 4. zip
        # 5. rar
        self.pkg_format = pkg_format
        # The cloud application labels. You can select multiple values. Valid values:
        # 1. hot
        # 2. game
        # 3. app
        self.pkg_labels_shrink = pkg_labels_shrink
        # The package type.
        # 
        # ## Valid values:
        # 
        # 1. android
        # 2. win
        # 3. android_appmarket: corresponds to the Android app marketplace scenario. In this scenario, the actual APK PackageName is restricted:
        # a. Different AppName values cannot share the same PackageName.
        # b. The same AppName with different AppVersion values can be associated with different PackageName values.
        # 
        # ## Default value:
        # If not specified, the package type is automatically mapped based on PkgFormat (or the file extension of DownloadUrl). Default mappings between PkgFormat and package type:
        # 1. android: apk (the apk format is mapped to android by default).
        # 2. win: tar.gz, tar, zip, rar.
        # 3. android_appmarket: apk.
        self.pkg_type = pkg_type
        # The relative path of the post-installation command within the application package. Only supported for win type applications.
        self.post_command_path = post_command_path
        # The timeout period (in seconds) for the post-installation command. Only supported for win type applications.
        self.post_command_timeout_sec = post_command_timeout_sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.pkg_format is not None:
            result['PkgFormat'] = self.pkg_format

        if self.pkg_labels_shrink is not None:
            result['PkgLabels'] = self.pkg_labels_shrink

        if self.pkg_type is not None:
            result['PkgType'] = self.pkg_type

        if self.post_command_path is not None:
            result['PostCommandPath'] = self.post_command_path

        if self.post_command_timeout_sec is not None:
            result['PostCommandTimeoutSec'] = self.post_command_timeout_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('PkgFormat') is not None:
            self.pkg_format = m.get('PkgFormat')

        if m.get('PkgLabels') is not None:
            self.pkg_labels_shrink = m.get('PkgLabels')

        if m.get('PkgType') is not None:
            self.pkg_type = m.get('PkgType')

        if m.get('PostCommandPath') is not None:
            self.post_command_path = m.get('PostCommandPath')

        if m.get('PostCommandTimeoutSec') is not None:
            self.post_command_timeout_sec = m.get('PostCommandTimeoutSec')

        return self

