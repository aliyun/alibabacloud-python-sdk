# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetTestResultsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        net_test_type: str = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # The number of entries per page in a paged query. Maximum value: 100.
        # 
        # Default value:
        # 
        # - If this parameter is not specified or is set to a value less than 20, the default value is 20.
        # 
        # - If this parameter is set to a value greater than 100, the default value is 100.
        self.max_results = max_results
        # The network test type.
        self.net_test_type = net_test_type
        # The pagination token. Set this parameter to the value of NextToken that is returned from the previous API call.
        self.next_token = next_token
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

