# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDasAgentSSERequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        instance_id: str = None,
        query: str = None,
        session_id: str = None,
    ):
        # Optional. By default, the default agent is used. You can also specify an agent that was generated after enabling the DAS Agent service or an agent that you manually created.
        self.agent_id = agent_id
        # Deprecated parameter. The instance ID is passed through the Query field.
        self.instance_id = instance_id
        # The natural language description for the query.
        # 
        # This parameter is required.
        self.query = query
        # Optional. The session ID in UUID string format. If not specified, a new session is created. To maintain context across conversations, use the same session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.query is not None:
            result['Query'] = self.query

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

