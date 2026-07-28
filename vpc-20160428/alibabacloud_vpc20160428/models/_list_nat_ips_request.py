# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNatIpsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ip_origin: str = None,
        ipv_4prefix: str = None,
        max_results: str = None,
        nat_gateway_id: str = None,
        nat_ip_cidr: str = None,
        nat_ip_ids: List[str] = None,
        nat_ip_name: List[str] = None,
        nat_ip_status: str = None,
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
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The origin of the NAT IP address to query. Valid values:
        # - prefix: a NAT IP address that belongs to an IP prefix.
        # 
        # - cidr: a standalone NAT IP address that does not belong to any IP prefix.
        # 
        # - Empty: queries all NAT IP addresses.
        self.ip_origin = ip_origin
        # The CIDR block of the IP prefix to query.
        self.ipv_4prefix = ipv_4prefix
        # The number of entries per page for a paged query. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The instance ID of the NAT gateway to which the NAT IP addresses belong.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The CIDR block to which the NAT IP addresses belong.
        self.nat_ip_cidr = nat_ip_cidr
        # The instance ID of the NAT IP address to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_ids = nat_ip_ids
        # The name of the NAT IP address to query. Valid values of **N**: **1** to **20**.
        self.nat_ip_name = nat_ip_name
        # The status of the NAT IP addresses to query. Valid values:
        # 
        # - **Available**: available.
        # - **Deleting**: being deleted.
        # - **Creating**: being created.
        self.nat_ip_status = nat_ip_status
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - You do not need to specify this parameter for the first request or if no subsequent query exists.
        # - If a next query exists, set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway instance to which the NAT IP addresses belong.
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

        if self.ip_origin is not None:
            result['IpOrigin'] = self.ip_origin

        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip_cidr is not None:
            result['NatIpCidr'] = self.nat_ip_cidr

        if self.nat_ip_ids is not None:
            result['NatIpIds'] = self.nat_ip_ids

        if self.nat_ip_name is not None:
            result['NatIpName'] = self.nat_ip_name

        if self.nat_ip_status is not None:
            result['NatIpStatus'] = self.nat_ip_status

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

        if m.get('IpOrigin') is not None:
            self.ip_origin = m.get('IpOrigin')

        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIpCidr') is not None:
            self.nat_ip_cidr = m.get('NatIpCidr')

        if m.get('NatIpIds') is not None:
            self.nat_ip_ids = m.get('NatIpIds')

        if m.get('NatIpName') is not None:
            self.nat_ip_name = m.get('NatIpName')

        if m.get('NatIpStatus') is not None:
            self.nat_ip_status = m.get('NatIpStatus')

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

