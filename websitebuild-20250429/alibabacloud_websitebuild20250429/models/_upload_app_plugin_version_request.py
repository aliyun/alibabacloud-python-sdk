# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadAppPluginVersionRequest(DaraModel):
    def __init__(
        self,
        changelog: str = None,
        description: str = None,
        download_url: str = None,
        extend: str = None,
        oss_key: str = None,
        plugin_id: str = None,
        plugin_version: str = None,
    ):
        # The changelog description.
        self.changelog = changelog
        # The description. This parameter is optional. If a non-empty value is specified, the description field in the main table is also updated.
        self.description = description
        # The downloadable ZIP URL. This parameter is mutually exclusive with OssKey.
        self.download_url = download_url
        # The extended JSON. This parameter is optional and uses the same format as the sandbox-synced extend field. If a non-empty value is specified, the extend field in the main table is also updated.
        self.extend = extend
        # The OSS key obtained after frontend direct upload. This parameter is mutually exclusive with DownloadUrl.
        self.oss_key = oss_key
        # The gateway plug-in ID.
        self.plugin_id = plugin_id
        # The new version number in semver format. The version must be greater than the current version.
        self.plugin_version = plugin_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changelog is not None:
            result['Changelog'] = self.changelog

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changelog') is not None:
            self.changelog = m.get('Changelog')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        return self

