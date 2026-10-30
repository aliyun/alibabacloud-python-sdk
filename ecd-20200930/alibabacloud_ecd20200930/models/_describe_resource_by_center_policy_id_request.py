# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceByCenterPolicyIdRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: str = None,
        product_type: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The number of entries per page for a paged query.    
        # 
        # - Maximum value: 100.    
        # - Default value: 10.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The policy ID.
        # 
        # This parameter is required.
        self.policy_group_id = policy_group_id
        # The product type.
        self.product_type = product_type
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name

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

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

