# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentEndpointConfig(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        custom_domain_url: str = None,
        endpoint_url: str = None,
    ):
        self.agent_name = agent_name
        self.custom_domain_url = custom_domain_url
        self.endpoint_url = endpoint_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.custom_domain_url is not None:
            result['customDomainUrl'] = self.custom_domain_url

        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('customDomainUrl') is not None:
            self.custom_domain_url = m.get('customDomainUrl')

        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')

        return self

