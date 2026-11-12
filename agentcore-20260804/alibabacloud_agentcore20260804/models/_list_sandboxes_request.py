# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSandboxesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_text: str = None,
        service_endpoint_id: str = None,
        session_id: str = None,
    ):
        # The maximum number of entries to return per page. Default value: 20. Valid values: 1 to 100.
        self.max_results = max_results
        # The cursor for querying the next page. When you turn the page, you must keep workspaceId, agentId, searchText, sessionId, and maxResults unchanged.
        self.next_token = next_token
        # Performs a case-insensitive fuzzy search by sandbox ID fragment.
        self.search_text = search_text
        # If this parameter is omitted or left blank, the latest running unit of the agent is queried. If this parameter is specified, the service endpoint must belong to the agent and the target type must be AGENT_VERSION. Otherwise, Resource.NotFound is returned. An independently running service endpoint returns only the sandboxes of its own running unit. If the DEFAULT service endpoint has not taken over independent running, the query falls back to the latest running unit. If a non-DEFAULT service endpoint is not running independently, ServiceEndpointTargetNotReady is returned. If the running unit is not created, an empty list is returned and totalCount is 0, without reporting an error.
        self.service_endpoint_id = service_endpoint_id
        # Performs a case-insensitive fuzzy search by current valid session ID fragment.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.search_text is not None:
            result['searchText'] = self.search_text

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('searchText') is not None:
            self.search_text = m.get('searchText')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

