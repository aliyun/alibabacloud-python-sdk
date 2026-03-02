# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class AppPluginInfo(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_version: str = None,
        app_version_id: int = None,
        config: main_models.MobiPluginConfig = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        plugin_key: str = None,
        plugin_type: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.app_version_id = app_version_id
        self.config = config
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.plugin_key = plugin_key
        self.plugin_type = plugin_type
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_version is not None:
            result['appVersion'] = self.app_version

        if self.app_version_id is not None:
            result['appVersionId'] = self.app_version_id

        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.plugin_key is not None:
            result['pluginKey'] = self.plugin_key

        if self.plugin_type is not None:
            result['pluginType'] = self.plugin_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')

        if m.get('appVersionId') is not None:
            self.app_version_id = m.get('appVersionId')

        if m.get('config') is not None:
            temp_model = main_models.MobiPluginConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pluginKey') is not None:
            self.plugin_key = m.get('pluginKey')

        if m.get('pluginType') is not None:
            self.plugin_type = m.get('pluginType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

