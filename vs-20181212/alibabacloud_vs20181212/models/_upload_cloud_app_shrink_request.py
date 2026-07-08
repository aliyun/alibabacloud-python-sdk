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
    ):
        # The application name. For Android apps, use the package name, such as com.aaa.bbb.
        # 
        # Value requirements:
        # 
        # 1. Length: 4–50 characters
        # 
        # 2. Allowed characters: lowercase letters, digits, underscores (_), hyphens (-), and dots (.)
        # 
        # 3. The first and last characters must be a letter or digit
        # 
        # This parameter is required.
        self.app_name = app_name
        # Value requirements:
        # 
        # 1. Length: 1–50 characters
        # 
        # 2. Allowed characters: lowercase letters, digits, underscores (_), hyphens (-), and dots (.)
        # 
        # 3. The first and last characters must be a letter or digit
        # 
        # This parameter is required.
        self.app_version = app_version
        # A description of the application.
        self.description = description
        # The download URL of the application package.
        # 
        # This parameter is required.
        self.download_url = download_url
        # The MD5 hash of the application package, used to verify package integrity.
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The package format. By default, this is inferred from the file extension in the DownloadUrl. Valid values:
        # 
        # 1. apk
        # 
        # 2. tar.gz
        # 
        # 3. tar
        # 
        # 4. zip
        # 
        # 5. rar
        self.pkg_format = pkg_format
        # Cloud application labels. You can select multiple. Valid values:
        # 
        # 1. hot
        # 
        # 2. game
        # 
        # 3. app
        self.pkg_labels_shrink = pkg_labels_shrink
        # The package type.
        # 
        # ## Valid values:
        # 
        # 1. android
        # 
        # 2. win
        # 
        # 3. android_appmarket: for Android app marketplace scenarios. This scenario enforces real APK PackageName restrictions:
        #    a. PackageNames must be unique across different AppNames.
        #    b. The same AppName with different AppVersions can map to different PackageNames.
        # 
        # ## Default behavior:
        # 
        # If not specified, the system automatically maps the package type based on PkgFormat (or infers PkgFormat from the DownloadUrl file extension). The default mapping is:
        # 
        # 1. android: apk
        # 
        # 2. win: tar.gz, tar, zip, rar
        # 
        # 3. android_appmarket: apk
        self.pkg_type = pkg_type

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

        return self

