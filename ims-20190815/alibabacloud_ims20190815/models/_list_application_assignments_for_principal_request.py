# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationAssignmentsForPrincipalRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token used to retrieve the next page of query results. This parameter is not required for the first API call.
        self.next_token = next_token
        # The principal name of the RAM user or the role name.
        # 
        # + User principal name: The format is `<username>@<account-id>.onaliyun.com`. You can query it by calling the GetUser or ListUsers API operation.
        # + Role name: You can query it by calling the RAM ListRoles API operation.
        self.principal_name = principal_name
        # The type of the target principal for the application assignment. Valid values:
        # 
        # + user: The principal type is RAM user. In this case, PrincipalName must be the user principal name.
        # + role: The principal type is RAM role. In this case, PrincipalName must be the role name.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

