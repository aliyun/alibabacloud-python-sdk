# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UploadCloudAppRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_version: str = None,
        description: str = None,
        download_url: str = None,
        md_5: str = None,
        pkg_format: str = None,
        pkg_labels: List[str] = None,
        pkg_type: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.app_version = app_version
        self.description = description
        # This parameter is required.
        self.download_url = download_url
        # This parameter is required.
        self.md_5 = md_5
        self.pkg_format = pkg_format
        self.pkg_labels = pkg_labels
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

        if self.pkg_labels is not None:
            result['PkgLabels'] = self.pkg_labels

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
            self.pkg_labels = m.get('PkgLabels')

        if m.get('PkgType') is not None:
            self.pkg_type = m.get('PkgType')

        return self

