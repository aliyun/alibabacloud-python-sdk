# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamPoolCidrsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_pool_cidrs: List[main_models.ListIpamPoolCidrsResponseBodyIpamPoolCidrs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # A list of provisioned CIDR blocks of the IPAM pool.
        self.ipam_pool_cidrs = ipam_pool_cidrs
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        # 
        # - If this parameter is empty, no more results are to be returned.
        # 
        # - If a value is returned, the value is the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that match the query.
        self.total_count = total_count

    def validate(self):
        if self.ipam_pool_cidrs:
            for v1 in self.ipam_pool_cidrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamPoolCidrs'] = []
        if self.ipam_pool_cidrs is not None:
            for k1 in self.ipam_pool_cidrs:
                result['IpamPoolCidrs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ipam_pool_cidrs = []
        if m.get('IpamPoolCidrs') is not None:
            for k1 in m.get('IpamPoolCidrs'):
                temp_model = main_models.ListIpamPoolCidrsResponseBodyIpamPoolCidrs()
                self.ipam_pool_cidrs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamPoolCidrsResponseBodyIpamPoolCidrs(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_id: str = None,
        status: str = None,
    ):
        # The provisioned CIDR block.
        self.cidr = cidr
        # The instance ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The instance status of the provisioned CIDR block of the IPAM pool. Valid values:
        # 
        # - **Created**: The CIDR block is created.
        # 
        # - **Deleted**: The CIDR block is deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

