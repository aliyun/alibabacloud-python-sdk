# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditPluginConfigRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        plugin_config: str = None,
        plugin_desc: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
    ):
        self.biz_id = biz_id
        self.plugin_config = plugin_config
        self.plugin_desc = plugin_desc
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.plugin_config is not None:
            result['PluginConfig'] = self.plugin_config

        if self.plugin_desc is not None:
            result['PluginDesc'] = self.plugin_desc

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PluginConfig') is not None:
            self.plugin_config = m.get('PluginConfig')

        if m.get('PluginDesc') is not None:
            self.plugin_desc = m.get('PluginDesc')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        return self

