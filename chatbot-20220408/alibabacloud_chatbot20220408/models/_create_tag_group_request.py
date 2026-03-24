# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTagGroupRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

