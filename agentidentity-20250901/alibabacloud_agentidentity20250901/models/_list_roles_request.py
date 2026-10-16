# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRolesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        user_pool_name: str = None,
    ):
        # The maximum number of entries to return per page. Valid values: 1 to 1000. Default value: 100.
        self.max_results = max_results
        # The token used to query the next page of data. This parameter is not required for the first call. If a NextToken is returned in the response of a previous call, specify it in the current call to retrieve the next page.
        self.next_token = next_token
        # The name of the user pool.
        self.user_pool_name = user_pool_name

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

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

