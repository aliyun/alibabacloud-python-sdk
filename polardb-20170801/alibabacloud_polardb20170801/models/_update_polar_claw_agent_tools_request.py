# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePolarClawAgentToolsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        allow: List[str] = None,
        also_allow: List[str] = None,
        application_id: str = None,
        deny: List[str] = None,
        profile: str = None,
    ):
        # Agent ID
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The list of explicitly allowed tools.
        self.allow = allow
        # The list of additionally allowed tools.
        self.also_allow = also_allow
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The list of denied tools.
        self.deny = deny
        # The tool profile.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.allow is not None:
            result['Allow'] = self.allow

        if self.also_allow is not None:
            result['AlsoAllow'] = self.also_allow

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.deny is not None:
            result['Deny'] = self.deny

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Allow') is not None:
            self.allow = m.get('Allow')

        if m.get('AlsoAllow') is not None:
            self.also_allow = m.get('AlsoAllow')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

