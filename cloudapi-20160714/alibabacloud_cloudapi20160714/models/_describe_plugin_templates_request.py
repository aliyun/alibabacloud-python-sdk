# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePluginTemplatesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        plugin_name: str = None,
        security_token: str = None,
    ):
        # The language that is used to return the description of the system policy. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese.
        # *   ja: Japanese
        self.language = language
        # The name of the plug-in.
        self.plugin_name = plugin_name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

