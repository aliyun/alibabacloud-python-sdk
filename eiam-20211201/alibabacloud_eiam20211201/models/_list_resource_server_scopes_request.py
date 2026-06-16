# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListResourceServerScopesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        authorization_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        resource_server_scope_ids: List[str] = None,
        resource_server_scope_name: str = None,
        resource_server_scope_type: str = None,
        resource_server_scope_value: str = None,
    ):
        # Application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Authorization type.
        self.authorization_type = authorization_type
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Number of rows per page in paginated queries.
        self.max_results = max_results
        # Token for the next page query. Set this to the NextToken value returned by the previous API call. Leave empty for the first query.
        self.next_token = next_token
        # Token for the previous page query. Set this to the PreviousToken value returned by the previous API call.
        self.previous_token = previous_token
        # List of Scope permission IDs.
        self.resource_server_scope_ids = resource_server_scope_ids
        # Scope permission name.
        self.resource_server_scope_name = resource_server_scope_name
        # Scope permission type.
        self.resource_server_scope_type = resource_server_scope_type
        # Scope permission value.
        self.resource_server_scope_value = resource_server_scope_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.resource_server_scope_ids is not None:
            result['ResourceServerScopeIds'] = self.resource_server_scope_ids

        if self.resource_server_scope_name is not None:
            result['ResourceServerScopeName'] = self.resource_server_scope_name

        if self.resource_server_scope_type is not None:
            result['ResourceServerScopeType'] = self.resource_server_scope_type

        if self.resource_server_scope_value is not None:
            result['ResourceServerScopeValue'] = self.resource_server_scope_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('ResourceServerScopeIds') is not None:
            self.resource_server_scope_ids = m.get('ResourceServerScopeIds')

        if m.get('ResourceServerScopeName') is not None:
            self.resource_server_scope_name = m.get('ResourceServerScopeName')

        if m.get('ResourceServerScopeType') is not None:
            self.resource_server_scope_type = m.get('ResourceServerScopeType')

        if m.get('ResourceServerScopeValue') is not None:
            self.resource_server_scope_value = m.get('ResourceServerScopeValue')

        return self

