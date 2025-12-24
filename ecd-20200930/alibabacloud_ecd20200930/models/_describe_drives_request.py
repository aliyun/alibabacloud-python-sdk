# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDrivesRequest(DaraModel):
    def __init__(
        self,
        domain_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        # The IDs of the storage resources.
        self.domain_ids = domain_ids
        # The number of entries per page.
        # 
        # *   Maximum value: 500.
        # *   Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        self.region_id = region_id
        # The type of the storage resource.
        # 
        # Valid values:
        # 
        # *   NAS: NAS storage
        # *   PDS: PDS storage
        self.resource_type = resource_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_ids is not None:
            result['DomainIds'] = self.domain_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainIds') is not None:
            self.domain_ids = m.get('DomainIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

