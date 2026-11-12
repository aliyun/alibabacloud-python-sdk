# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPermissionRulesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        source: str = None,
        target: str = None,
    ):
        # The maximum number of results to return per page.
        self.max_results = max_results
        # The token used to retrieve the next page.
        self.next_token = next_token
        # The principal ID.
        self.principal_id = principal_id
        # The principal name.
        self.principal_name = principal_name
        # The principal type.
        self.principal_type = principal_type
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The rule source.
        self.source = source
        # The rule target.
        self.target = target

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

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_name is not None:
            result['principalName'] = self.principal_name

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalName') is not None:
            self.principal_name = m.get('principalName')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        return self

