# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNatIpCidrRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        nat_gateway_id: str = None,
        nat_ip_cidr: str = None,
        nat_ip_cidr_description: str = None,
        nat_ip_cidr_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without creating the NAT CIDR block. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The instance ID of the VPC NAT gateway for which you want to create the NAT CIDR block.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The NAT CIDR block to create.
        # 
        # The new CIDR block must meet the following conditions:
        # 
        # - It must belong to 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16 and their subnets.
        # - The subnet mask must be 16 to 32 bits in length.
        # - It cannot overlap with the private CIDR block of the VPC to which the VPC NAT gateway belongs. If you want to transform a private endpoint to another address within the VPC private network CIDR block, create a vSwitch in the corresponding VPC private network CIDR block, and then create a new VPC NAT gateway in the vSwitch to provide private network address transform service.
        # - To use a public CIDR block as the NAT CIDR block, the CIDR block must belong to the user CIDR block of the VPC to which the VPC NAT gateway belongs. For more information about user CIDR blocks, see [What is a user CIDR block?](https://help.aliyun.com/document_detail/185311.html).
        # 
        # This parameter is required.
        self.nat_ip_cidr = nat_ip_cidr
        # The description of the NAT CIDR block.
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or Chinese character. It cannot start with `http://` or `https://`.
        self.nat_ip_cidr_description = nat_ip_cidr_description
        # The name of the NAT CIDR block.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.nat_ip_cidr_name = nat_ip_cidr_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway instance to which the NAT CIDR block belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip_cidr is not None:
            result['NatIpCidr'] = self.nat_ip_cidr

        if self.nat_ip_cidr_description is not None:
            result['NatIpCidrDescription'] = self.nat_ip_cidr_description

        if self.nat_ip_cidr_name is not None:
            result['NatIpCidrName'] = self.nat_ip_cidr_name

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIpCidr') is not None:
            self.nat_ip_cidr = m.get('NatIpCidr')

        if m.get('NatIpCidrDescription') is not None:
            self.nat_ip_cidr_description = m.get('NatIpCidrDescription')

        if m.get('NatIpCidrName') is not None:
            self.nat_ip_cidr_name = m.get('NatIpCidrName')

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

