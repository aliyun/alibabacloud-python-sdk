# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagGroupRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        client_token: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.agent_key = agent_key
        self.client_token = client_token
        self.group_name = group_name
        self.page_number = page_number
        self.page_size = page_size

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

