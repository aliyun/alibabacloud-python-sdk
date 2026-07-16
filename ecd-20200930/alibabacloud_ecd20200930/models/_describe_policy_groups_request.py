# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePolicyGroupsRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        external_policy_group_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_group_id: List[str] = None,
        region_id: str = None,
        scope: str = None,
    ):
        self.business_channel = business_channel
        # The list of cloud computer policy IDs to exclude from the query results.
        self.external_policy_group_ids = external_policy_group_ids
        # The number of entries per page.
        # 
        # - Maximum value: 100
        # 
        # - Default value: 10
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous response. Do not set this parameter for the first request.
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        # The list of cloud computer policy IDs.
        self.policy_group_id = policy_group_id
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The effective scope of the cloud computer policy.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.external_policy_group_ids is not None:
            result['ExternalPolicyGroupIds'] = self.external_policy_group_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('ExternalPolicyGroupIds') is not None:
            self.external_policy_group_ids = m.get('ExternalPolicyGroupIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

