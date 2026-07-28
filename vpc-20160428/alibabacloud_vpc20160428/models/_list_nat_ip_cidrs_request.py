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
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system uses **RequestId** as **ClientToken**. The value of **RequestId** may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without querying the NAT CIDR block list. The system checks the request for potential issues, including missing required parameters, invalid parameter values, and the authorization status of the RAM user. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # 
        # - **false** (default): sends a normal request, and the NAT CIDR block list is returned after the request passes the check with an HTTP 2xx status code.
        self.dry_run = dry_run
        # The number of entries per page for a paged query. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The instance ID of the VPC NAT gateway whose NAT CIDR blocks you want to query.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The NAT CIDR block to query.
        self.nat_ip_cidr = nat_ip_cidr
        # The name of the NAT CIDR block to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_cidr_name = nat_ip_cidr_name
        # The status of the NAT CIDR block to query. Set the value to **Available**, which indicates that the NAT CIDR block is available.
        self.nat_ip_cidr_status = nat_ip_cidr_status
        # The NAT CIDR block to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_cidrs = nat_ip_cidrs
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - If this is the first request or no subsequent requests exist, you do not need to specify this parameter.
        # - If a subsequent request exists, set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the VPC NAT gateway to which the NAT CIDR blocks belong.
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

