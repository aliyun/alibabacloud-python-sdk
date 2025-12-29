# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationGroupBillRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        billing_cycle: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The billing cycle, in the YYYY-MM format.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The number of entries per page.
        self.max_results = max_results
        # The application group name.
        # 
        # This parameter is required.
        self.name = name
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The type of the cloud resource.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

