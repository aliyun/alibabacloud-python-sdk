# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPublishTaskStateRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # The key of the business space. If this parameter is not specified, the default business space is accessed. Obtain the key value from the business management page of the primary account.
        self.agent_key = agent_key
        # The ID of the publish task.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

