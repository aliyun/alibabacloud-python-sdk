# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyAtiAgentRegisterInfoAcmeChallengeRecordRequest(DaraModel):
    def __init__(
        self,
        agent_register_info_id: str = None,
        client_token: str = None,
    ):
        # This parameter is required.
        self.agent_register_info_id = agent_register_info_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_register_info_id is not None:
            result['AgentRegisterInfoId'] = self.agent_register_info_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentRegisterInfoId') is not None:
            self.agent_register_info_id = m.get('AgentRegisterInfoId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

