# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAtiAgentRegisterInfosRequest(DaraModel):
    def __init__(
        self,
        agent_display_name: str = None,
        agent_host: str = None,
        agent_id: str = None,
        agent_version: str = None,
        client_token: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The display name of the Agent.
        self.agent_display_name = agent_display_name
        # The host address of the Agent.
        self.agent_host = agent_host
        # The Agent ID, which is uniformly assigned by CNNIC after real-name verification through CNNIC. The AgentID serves as the unique identifier that binds the Agent to the real-name verified registrant.
        self.agent_id = agent_id
        # The version of the Agent.
        self.agent_version = agent_version
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The current page number. Minimum value: 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The page size for the paged query. This parameter specifies the number of entries per page for paging.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the Agent.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_display_name is not None:
            result['AgentDisplayName'] = self.agent_display_name

        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

