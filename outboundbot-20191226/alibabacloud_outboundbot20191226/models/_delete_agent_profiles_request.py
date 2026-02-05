# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAgentProfilesRequest(DaraModel):
    def __init__(
        self,
        agent_profile_ids: List[str] = None,
        app_ip: str = None,
    ):
        self.agent_profile_ids = agent_profile_ids
        self.app_ip = app_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_ids is not None:
            result['AgentProfileIds'] = self.agent_profile_ids

        if self.app_ip is not None:
            result['AppIp'] = self.app_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileIds') is not None:
            self.agent_profile_ids = m.get('AgentProfileIds')

        if m.get('AppIp') is not None:
            self.app_ip = m.get('AppIp')

        return self

