# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListIpamMembersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        member_ids: List[str] = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The maximum number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # A list of IDs of members managed by the IPAM trusted service.
        self.member_ids = member_ids
        # The token that is used to retrieve the next page of results. Valid values:
        # 
        # - If **NextToken** is empty, no more results are available.
        # 
        # - If **NextToken** has a value, the value is the token for the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the hosted region of the IPAM. Call the [DescribeRegions](https://help.aliyun.com/document_detail/448570.html) operation to get the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

