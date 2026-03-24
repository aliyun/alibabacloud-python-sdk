# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTagRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_id: int = None,
        tag_name: str = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        # This parameter is required.
        self.group_id = group_id
        # This parameter is required.
        self.tag_name = tag_name

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

