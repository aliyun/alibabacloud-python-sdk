# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterCidrAllocationResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_cidr_allocations: List[main_models.ListTransitRouterCidrAllocationResponseBodyTransitRouterCidrAllocations] = None,
    ):
        # The number of entries returned per page.
        # 
        # *   If no value is specified for **MaxResults**, query results are returned in one batch. The value of **MaxResults** indicates the total number of entries.
        # *   If a value is specified for **MaxResults**, query results are returned in batches. The value of **MaxResults** in the response indicates the number of entries in the current batch.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** was not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the CIDR blocks that have IP addresses allocated to network instances.
        self.transit_router_cidr_allocations = transit_router_cidr_allocations

    def validate(self):
        if self.transit_router_cidr_allocations:
            for v1 in self.transit_router_cidr_allocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterCidrAllocations'] = []
        if self.transit_router_cidr_allocations is not None:
            for k1 in self.transit_router_cidr_allocations:
                result['TransitRouterCidrAllocations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_cidr_allocations = []
        if m.get('TransitRouterCidrAllocations') is not None:
            for k1 in m.get('TransitRouterCidrAllocations'):
                temp_model = main_models.ListTransitRouterCidrAllocationResponseBodyTransitRouterCidrAllocations()
                self.transit_router_cidr_allocations.append(temp_model.from_map(k1))

        return self

class ListTransitRouterCidrAllocationResponseBodyTransitRouterCidrAllocations(DaraModel):
    def __init__(
        self,
        allocated_cidr_block: str = None,
        attachment_id: str = None,
        attachment_name: str = None,
        cidr: str = None,
        transit_router_cidr_id: str = None,
    ):
        # The CIDR blocks that have IP addresses allocated to network instances.
        self.allocated_cidr_block = allocated_cidr_block
        # The ID of the network instance connection.
        self.attachment_id = attachment_id
        # The name of the network instance connection.
        self.attachment_name = attachment_name
        # The CIDR block of the transit router.
        self.cidr = cidr
        # The ID of the CIDR block.
        self.transit_router_cidr_id = transit_router_cidr_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_cidr_block is not None:
            result['AllocatedCidrBlock'] = self.allocated_cidr_block

        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedCidrBlock') is not None:
            self.allocated_cidr_block = m.get('AllocatedCidrBlock')

        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')

        return self

