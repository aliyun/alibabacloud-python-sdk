# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNatGatewayRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        nat_gateway_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to forcefully delete the NAT gateway. Valid values:
        # 
        # - **true**: forcefully deletes the NAT gateway. If you set this parameter to **true**:
        # 
        #     - If the NAT gateway has SNAT rules, the system force deletes the SNAT rules.
        # 
        #     - If the NAT gateway has DNAT rules, the system force deletes the DNAT rules.
        # 
        #     - If the NAT gateway has associated elastic IP addresses (EIPs), the system automatically disassociates the EIPs.
        # 
        #     - If the NAT gateway has NAT service plans that are not deleted, the system force deletes the NAT service plans.
        # 
        # - **false** (default): does not forcefully delete the NAT gateway. If you set this parameter to **false**:
        # 
        #     - If the NAT gateway has NAT service plans that are not deleted, delete the NAT service plans first.
        # 
        #     - If the NAT gateway has SNAT rules, delete the SNAT rules first.
        # 
        #     - If the NAT gateway has DNAT rules, delete the DNAT rules first.
        # 
        #     - If the NAT gateway has associated EIPs, disassociate the EIPs first.
        self.force = force
        # The instance ID of the NAT gateway that you want to delete.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the region ID.
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
        if self.force is not None:
            result['Force'] = self.force

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

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
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

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

