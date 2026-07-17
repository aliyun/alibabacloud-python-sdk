# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAtiAgentRegisterInfoMarketRequest(DaraModel):
    def __init__(
        self,
        agent_host: str = None,
        agent_version: str = None,
        client_token: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.agent_host = agent_host
        self.agent_version = agent_version
        self.client_token = client_token
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

