# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppPluginConfigRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        plugin_id: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        return self

