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
        # The key for the business space. Omit this parameter to use the default business space. You can get the key from the business management page of your main account.
        self.agent_key = agent_key
        # The identifier for the connection source. You can obtain this value from the channel console.
        # 
        # This parameter is required.
        self.from_ = from_
        # The access token for user authentication.
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

