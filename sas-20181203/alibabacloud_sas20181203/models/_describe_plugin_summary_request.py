# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePluginSummaryRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        plugin_name: str = None,
    ):
        # The language of the content within the request and response.**** Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The name of the plug-in. Valid values:
        # 
        # *   alinet: AliNet.
        # *   alisecguard: client protection.
        # *   alihips: AliHips.
        self.plugin_name = plugin_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        return self

