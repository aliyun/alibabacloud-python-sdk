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
        trust_level: str = None,
    ):
        # The endpoint domain name through which the agent provides services externally.
        self.agent_host = agent_host
        # The agent version.
        self.agent_version = agent_version
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query.
        self.next_token = next_token
        self.trust_level = trust_level

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

        if self.trust_level is not None:
            result['TrustLevel'] = self.trust_level

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

        if m.get('TrustLevel') is not None:
            self.trust_level = m.get('TrustLevel')

        return self

