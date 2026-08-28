# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceEndpointsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        collaboration_component: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_binding_id: str = None,
        status: str = None,
        target_type: str = None,
    ):
        # Filters by target agent ID.
        self.agent_id = agent_id
        # Filters by target agent version number.
        self.agent_version = agent_version
        # Filters by collaboration component type. Valid values: MATRIX_CLIENT, MATRIX_FEDERATION, ELEMENT_WEB.
        self.collaboration_component = collaboration_component
        # The maximum number of records per page. Valid values: 1 to 100. If this parameter is not specified, 20 records are returned by default.
        self.max_results = max_results
        # The pagination token for the next page. Do not specify this parameter for the first request. For subsequent requests, specify the nextToken value returned in the previous response.
        self.next_token = next_token
        # Filters by the workspace resource binding ID of the target collaboration component.
        self.resource_binding_id = resource_binding_id
        # Filters by service endpoint status. Valid values: CREATING, READY, UPDATING, DEGRADED, DISABLED, DELETING.
        self.status = status
        # Filters by target type. Valid values: AGENT_VERSION, TEAM_COLLABORATION.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.collaboration_component is not None:
            result['collaborationComponent'] = self.collaboration_component

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.resource_binding_id is not None:
            result['resourceBindingId'] = self.resource_binding_id

        if self.status is not None:
            result['status'] = self.status

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('collaborationComponent') is not None:
            self.collaboration_component = m.get('collaborationComponent')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceBindingId') is not None:
            self.resource_binding_id = m.get('resourceBindingId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

