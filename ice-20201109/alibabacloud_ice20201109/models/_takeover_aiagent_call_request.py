# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TakeoverAIAgentCallRequest(DaraModel):
    def __init__(
        self,
        human_agent_user_id: str = None,
        instance_id: str = None,
        require_token: bool = None,
    ):
        # The ID of the human agent that will take over the AI agent (UserId in ARTC). If you do not specify this parameter, it is automatically generated and returned.
        self.human_agent_user_id = human_agent_user_id
        # The ID of the AI agent that will be taken over.
        self.instance_id = instance_id
        # Specifies whether to return the ARTC token. Default value: false.
        self.require_token = require_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.human_agent_user_id is not None:
            result['HumanAgentUserId'] = self.human_agent_user_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.require_token is not None:
            result['RequireToken'] = self.require_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HumanAgentUserId') is not None:
            self.human_agent_user_id = m.get('HumanAgentUserId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequireToken') is not None:
            self.require_token = m.get('RequireToken')

        return self

