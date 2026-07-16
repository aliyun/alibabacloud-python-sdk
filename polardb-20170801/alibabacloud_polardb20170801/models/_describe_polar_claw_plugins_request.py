# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePolarClawPluginsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        plugin_list: List[str] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # A list of plugin IDs. If omitted, all plugins are returned.
        self.plugin_list = plugin_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.plugin_list is not None:
            result['PluginList'] = self.plugin_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('PluginList') is not None:
            self.plugin_list = m.get('PluginList')

        return self

