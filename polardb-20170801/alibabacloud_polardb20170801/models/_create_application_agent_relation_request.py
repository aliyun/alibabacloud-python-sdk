# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationAgentRelationRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        token: str = None,
    ):
        # The instance ID of the Agent to attach.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The ID of the Squad application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The authentication token.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

