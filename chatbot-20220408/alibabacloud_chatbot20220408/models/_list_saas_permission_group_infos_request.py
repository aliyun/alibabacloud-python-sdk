# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSaasPermissionGroupInfosRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # The key for the business space. If unspecified, the default business space is used. You can find this key on the Business Management page of your main account.
        # 
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        return self

