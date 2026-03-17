# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRouteDistributionStrategyRequest(DaraModel):
    def __init__(
        self,
        dest_cidr_block: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_source: str = None,
        smart_agid: str = None,
        source_type: str = None,
    ):
        # The destination CIDR block.
        # 
        # This parameter is required.
        self.dest_cidr_block = dest_cidr_block
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Smart Access Gateway (SAG) instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source of routes. Valid values:
        # 
        # *   **Alibaba Cloud**
        # 
        #     *   **Virtual private cloud (VPC) IDs**: Routes that are learned from VPCs.
        #     *   **Virtual border router (VBR) IDs**: Routes that are learned from VBRs.
        #     *   **SAG instance IDs**: Routes that are learned from SAG instances.
        # 
        # *   **On-premises network**
        # 
        #     *   **STATIC**: Static routes that are specified in the SAG console.
        #     *   **OSPF**: Routes that are learned through the Open Shortest Path First (OSPF) protocol.
        #     *   **BGP**: Routes that are learned through Border Gateway Protocol (BGP).
        # 
        # This parameter is required.
        self.route_source = route_source
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The type of the route source. Valid values:
        # 
        # *   **cloud**: Alibaba Cloud
        # *   **local**: on-premises network
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_cidr_block is not None:
            result['DestCidrBlock'] = self.dest_cidr_block

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

        if self.route_source is not None:
            result['RouteSource'] = self.route_source

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidrBlock') is not None:
            self.dest_cidr_block = m.get('DestCidrBlock')

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

        if m.get('RouteSource') is not None:
            self.route_source = m.get('RouteSource')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

