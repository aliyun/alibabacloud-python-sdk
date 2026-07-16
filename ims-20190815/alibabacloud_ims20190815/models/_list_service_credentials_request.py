# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceCredentialsRequest(DaraModel):
    def __init__(
        self,
        all_users: bool = None,
        max_results: int = None,
        next_token: str = None,
        service_name: str = None,
        user_principal_name: str = None,
    ):
        # Specifies whether to query service credentials for all Resource Access Management (RAM) users under the Alibaba Cloud account.
        # 
        # If this parameter is set to true, you cannot specify UserPrincipalName at the same time.
        self.all_users = all_users
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. You do not need to specify this parameter for the first API call.
        self.next_token = next_token
        # The service name of the Alibaba Cloud service.
        self.service_name = service_name
        # The logon name of the Resource Access Management (RAM) user.
        # 
        # Queries the service credentials of the specified RAM user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_users is not None:
            result['AllUsers'] = self.all_users

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUsers') is not None:
            self.all_users = m.get('AllUsers')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

