# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMultiAccountResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_ids: List[str] = None,
    ):
        # The ID of the management account or a member in the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource group IDs.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

