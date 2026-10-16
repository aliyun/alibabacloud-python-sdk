# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdentityProviderDepartmentsRequest(DaraModel):
    def __init__(
        self,
        identity_provider_type: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_department_id: str = None,
        user_pool_name: str = None,
    ):
        self.identity_provider_type = identity_provider_type
        self.max_results = max_results
        self.next_token = next_token
        self.parent_department_id = parent_department_id
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_department_id is not None:
            result['ParentDepartmentId'] = self.parent_department_id

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentDepartmentId') is not None:
            self.parent_department_id = m.get('ParentDepartmentId')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

