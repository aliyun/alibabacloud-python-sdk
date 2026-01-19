# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachGroupPluginRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        plugin_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the plug-in to be bound.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        self.security_token = security_token
        # The environment in which the API is requested. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the pre-release environment
        # *   **TEST**: the test environment
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

