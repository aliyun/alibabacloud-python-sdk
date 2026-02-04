# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTransitRouteTableAggregationDetailRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_route_table_aggregation_cidr: str = None,
        transit_route_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId may be different for each request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the aggregate route.
        # 
        # This parameter is required.
        self.transit_route_table_aggregation_cidr = transit_route_table_aggregation_cidr
        # The ID of the route table of the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_route_table_id = transit_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_route_table_aggregation_cidr is not None:
            result['TransitRouteTableAggregationCidr'] = self.transit_route_table_aggregation_cidr

        if self.transit_route_table_id is not None:
            result['TransitRouteTableId'] = self.transit_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouteTableAggregationCidr') is not None:
            self.transit_route_table_aggregation_cidr = m.get('TransitRouteTableAggregationCidr')

        if m.get('TransitRouteTableId') is not None:
            self.transit_route_table_id = m.get('TransitRouteTableId')

        return self

