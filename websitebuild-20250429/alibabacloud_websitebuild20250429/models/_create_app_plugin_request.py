# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppPluginRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        download_url: str = None,
        extend: str = None,
        icon: str = None,
        oss_key: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_version: str = None,
        tags: str = None,
        visibility: str = None,
    ):
        # The category of the skill.
        self.category = category
        # The description of the skill. The description must be 10 to 512 characters in length.
        self.description = description
        # The URL of the downloadable ZIP file. Specify either this parameter or OssKey.
        self.download_url = download_url
        # The extended JSON data. The format is the same as the extend parameter synchronized with the sandbox. If this parameter is not empty, it is saved to the database. This parameter is optional.
        self.extend = extend
        # The URL of the icon.
        self.icon = icon
        # The Object Storage Service (OSS) key generated after a direct upload from the frontend. Specify either this parameter or DownloadUrl.
        self.oss_key = oss_key
        # The unique identifier of the skill. The identifier must be 3 to 64 characters in length and can contain only lowercase letters, digits, and hyphens (-).
        self.plugin_id = plugin_id
        # The name of the skill. The name must be 2 to 64 characters in length.
        self.plugin_name = plugin_name
        # The version number of the plug-in. The version number must be in the Semantic Versioning (SemVer) format. Default value: 0.1.0.
        self.plugin_version = plugin_version
        # The tags of the skill. Separate multiple tags with commas (,).
        self.tags = tags
        # The visibility of the skill. Default value: private.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

