# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListServerGroupServersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        server_group_id: str = None,
        server_ids: List[str] = None,
        server_ips: List[str] = None,
        skip: int = None,
    ):
        # The number of entries per page.
        # 
        # Valid values: 1 to 1000.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The server group ID.
        self.server_group_id = server_group_id
        # The server IDs.
        # 
        # You can specify at most 200 servers in each call.
        self.server_ids = server_ids
        # The server IP addresses.
        # 
        # You can specify at most 200 servers in each call.
        self.server_ips = server_ips
        # The number of entries to be skipped in the call.
        self.skip = skip

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

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids

        if self.server_ips is not None:
            result['ServerIps'] = self.server_ips

        if self.skip is not None:
            result['Skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')

        if m.get('ServerIps') is not None:
            self.server_ips = m.get('ServerIps')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        return self

