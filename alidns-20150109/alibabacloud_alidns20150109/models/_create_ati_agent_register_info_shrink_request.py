# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAtiAgentRegisterInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_description: str = None,
        agent_display_name: str = None,
        agent_host: str = None,
        agent_sub_host: str = None,
        agent_version: str = None,
        client_token: str = None,
        domain_mode: str = None,
        endpoints_shrink: str = None,
        registrant_id: str = None,
    ):
        # The description of the agent capabilities.
        self.agent_description = agent_description
        # The display name of the agent.
        # 
        # This parameter is required.
        self.agent_display_name = agent_display_name
        # The endpoint domain name through which the agent provides services.
        # 
        # This parameter is required.
        self.agent_host = agent_host
        self.agent_sub_host = agent_sub_host
        # The version of the agent.
        # 
        # This parameter is required.
        self.agent_version = agent_version
        # Provides idempotency. Within 3 minutes, the same value takes effect only once.
        self.client_token = client_token
        self.domain_mode = domain_mode
        # The endpoint information of the agent.
        # 
        # This parameter is required.
        self.endpoints_shrink = endpoints_shrink
        # The ID of the verified registrant. Obtain this ID by invoking the identity verification API operation or from the ATS console.
        # 
        # This parameter is required.
        self.registrant_id = registrant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_description is not None:
            result['AgentDescription'] = self.agent_description

        if self.agent_display_name is not None:
            result['AgentDisplayName'] = self.agent_display_name

        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_sub_host is not None:
            result['AgentSubHost'] = self.agent_sub_host

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.domain_mode is not None:
            result['DomainMode'] = self.domain_mode

        if self.endpoints_shrink is not None:
            result['Endpoints'] = self.endpoints_shrink

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDescription') is not None:
            self.agent_description = m.get('AgentDescription')

        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentSubHost') is not None:
            self.agent_sub_host = m.get('AgentSubHost')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DomainMode') is not None:
            self.domain_mode = m.get('DomainMode')

        if m.get('Endpoints') is not None:
            self.endpoints_shrink = m.get('Endpoints')

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        return self

