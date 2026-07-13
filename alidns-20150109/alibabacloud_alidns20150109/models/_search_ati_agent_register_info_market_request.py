# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAtiAgentRegisterInfoMarketRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        protocol: str = None,
        status: str = None,
        trust_level: str = None,
    ):
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length.
        # 
        # If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The keyword for searching. Matches against agent name, domain name, and description.
        self.keyword = keyword
        # The number of entries per batch query.
        self.max_results = max_results
        # The pagination token for the next query.
        self.next_token = next_token
        # The current page number. Minimum value: **1**. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page for the paged query. Settings: maximum value: 100. Default value: 20. This parameter controls paging behavior.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The communication protocol that the agent endpoint follows, which determines how callers interact with the agent.
        # 
        # Valid values:
        # - MCP: Model Context Protocol, an agent tool calling protocol developed by Anthropic.
        # - A2A: Agent-to-Agent Protocol, a cross-agent communication protocol developed by Google.
        # - OpenAPI: Standard RESTful API specification (Swagger/OpenAPI).
        # 
        # Other agents or clients use this protocol identifier to determine how to communicate with the agent. For example, MCP uses the MCP SDK, A2A uses the A2A SDK, and OpenAPI uses standard HTTP requests.
        self.protocol = protocol
        # Queries agents based on the agent status.
        self.status = status
        # Queries agents based on the trust level.
        self.trust_level = trust_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        if self.trust_level is not None:
            result['TrustLevel'] = self.trust_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrustLevel') is not None:
            self.trust_level = m.get('TrustLevel')

        return self

