# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrafficMarkingPoliciesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_marking_policy_description: str = None,
        traffic_marking_policy_id: str = None,
        traffic_marking_policy_name: str = None,
        transit_router_id: str = None,
    ):
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query or no subsequent query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description of the traffic marking policy.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.traffic_marking_policy_description = traffic_marking_policy_description
        # The ID of the traffic marking policy.
        self.traffic_marking_policy_id = traffic_marking_policy_id
        # The name of the traffic marking policy.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://.
        self.traffic_marking_policy_name = traffic_marking_policy_name
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description

        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id

        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')

        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')

        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

