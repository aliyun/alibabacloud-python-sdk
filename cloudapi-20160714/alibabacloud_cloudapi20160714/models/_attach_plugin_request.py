# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachPluginRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_ids: str = None,
        group_id: str = None,
        plugin_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # The number of the API to be bound.
        self.api_id = api_id
        # The number of the API to be operated. Separate multiple numbers with commas (,). A maximum of 100 numbers can be entered.
        self.api_ids = api_ids
        # The ID of the API group that contains the API to which the plug-in is to be bound.
        self.group_id = group_id
        # The ID of the plug-in to be bound.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **PRE: the pre-release environment**
        # *   **TEST**
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids

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
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

