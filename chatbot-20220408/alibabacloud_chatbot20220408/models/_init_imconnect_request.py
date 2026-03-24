# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitIMConnectRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        from_: str = None,
        user_access_token: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.from_ = from_
        self.user_access_token = user_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.from_ is not None:
            result['From'] = self.from_

        if self.user_access_token is not None:
            result['UserAccessToken'] = self.user_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('UserAccessToken') is not None:
            self.user_access_token = m.get('UserAccessToken')

        return self

