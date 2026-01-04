# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNatIpCidrsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        max_results: str = None,
        nat_gateway_id: str = None,
        nat_ip_cidr: str = None,
        nat_ip_cidr_name: List[str] = None,
        nat_ip_cidr_status: str = None,
        nat_ip_cidrs: List[str] = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: checks the API request. The CIDR blocks of the NAT gateway are not queried if the API request passes the precheck. The system checks whether your AccessKey pair is valid, whether the Resource Access Management (RAM) user is authorized, and whether the required parameters are set. If the request fails to pass the precheck, the corresponding error message is returned. If the check succeeds, the DryRunOperation error code is returned.
        # *   **false**: sends the API request. If the request passes the precheck, 2xx HTTP status code is returned and the CIDR blocks of the NAT gateway are queried. This is the default value.
        self.dry_run = dry_run
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The ID of the VPC NAT gateway that you want to query.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The CIDR block of the NAT gateway that you want to query.
        self.nat_ip_cidr = nat_ip_cidr
        # The name of the CIDR block that you want to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_cidr_name = nat_ip_cidr_name
        # The status of the CIDR block that you want to query. Set the value to **Available**.
        self.nat_ip_cidr_status = nat_ip_cidr_status
        # The CIDR block of the NAT gateway that you want to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_cidrs = nat_ip_cidrs
        # The token that is used for the next query. Set the value as needed.
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Virtual Private Cloud (VPC) NAT gateway that you want to query.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip_cidr is not None:
            result['NatIpCidr'] = self.nat_ip_cidr

        if self.nat_ip_cidr_name is not None:
            result['NatIpCidrName'] = self.nat_ip_cidr_name

        if self.nat_ip_cidr_status is not None:
            result['NatIpCidrStatus'] = self.nat_ip_cidr_status

        if self.nat_ip_cidrs is not None:
            result['NatIpCidrs'] = self.nat_ip_cidrs

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIpCidr') is not None:
            self.nat_ip_cidr = m.get('NatIpCidr')

        if m.get('NatIpCidrName') is not None:
            self.nat_ip_cidr_name = m.get('NatIpCidrName')

        if m.get('NatIpCidrStatus') is not None:
            self.nat_ip_cidr_status = m.get('NatIpCidrStatus')

        if m.get('NatIpCidrs') is not None:
            self.nat_ip_cidrs = m.get('NatIpCidrs')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

