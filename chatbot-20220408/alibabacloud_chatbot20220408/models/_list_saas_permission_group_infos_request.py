# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSaasPermissionGroupInfosRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # The business workspace key. If this parameter is not specified, the default business workspace is accessed. You can obtain the key value on the business management page of the Alibaba Cloud account.
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

