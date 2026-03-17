# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRouteDistributionStrategyRequest(DaraModel):
    def __init__(
        self,
        dest_cidr_block: str = None,
        hc_instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_distribution: str = None,
        route_source: str = None,
        smart_agid: str = None,
        source_type: str = None,
    ):
        # The destination CIDR block.
        # 
        # This parameter is required.
        self.dest_cidr_block = dest_cidr_block
        # The ID of the health check instance.
        self.hc_instance_id = hc_instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Smart Access Gateway (SAG) instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route advertisement policy. Valid values:
        # 
        # *   **publish**: advertises routes.
        # *   **no_publish**: does not advertise routes.
        # *   **no_publish_and_publish_on_health_success**: routes are advertised only when they pass the health check.
        # *   **no_publish_and_publish_on_health_fail**: routes are advertised only when they fail the health check.
        # *   **publish_and_revoke_on_health_success**: advertised routes are withdrawn only when they pass the health check.
        # *   **publish_and_revoke_on_health_fail**: advertised routes are withdrawn only when they fail the health check.
        # 
        # For more information, see [Configure health checks](https://help.aliyun.com/document_detail/163971.html) and [Advertise routes](https://help.aliyun.com/document_detail/163973.html).
        # 
        # This parameter is required.
        self.route_distribution = route_distribution
        # The source of routes. Valid values:
        # 
        # *   **Alibaba Cloud-facing routes**
        # 
        #     *   **The ID of the Virtual Private Cloud (VPC)**: learns routes from the VPC network.
        #     *   **The ID of the virtual border router (VBR)**: learns routes from the VBR.
        #     *   **The ID of the SAG instance**: learns routes from the SAG instance.
        # 
        # *   **Private network-facing routes**
        # 
        #     *   **STATIC**: static routes specified in the SAG console.
        #     *   **OSPF**: learns routes through the Open Shortest Path First (OSPF) protocol.
        #     *   **BGP**: learns routes through Border Gateway Protocol (BGP).
        # 
        # This parameter is required.
        self.route_source = route_source
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The type of the route source. Valid values:
        # 
        # *   **cloud**: Alibaba Cloud-facing routes.
        # *   **local**: private network-facing routes.
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

        if self.hc_instance_id is not None:
            result['HcInstanceId'] = self.hc_instance_id

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

        if self.route_distribution is not None:
            result['RouteDistribution'] = self.route_distribution

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

        if m.get('HcInstanceId') is not None:
            self.hc_instance_id = m.get('HcInstanceId')

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

        if m.get('RouteDistribution') is not None:
            self.route_distribution = m.get('RouteDistribution')

        if m.get('RouteSource') is not None:
            self.route_source = m.get('RouteSource')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

