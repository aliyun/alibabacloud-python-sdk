# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachGroupPluginRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        plugin_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # API group ID
        # 
        # This parameter is required.
        self.group_id = group_id
        # API Gateway plugin ID
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        self.security_token = security_token
        # Specify the environment of the API to operate on.
        # 
        # - **RELEASE**: Production
        # - **PRE**: Pre-release
        # - **TEST**: Test
        # 
        # This parameter is required.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

