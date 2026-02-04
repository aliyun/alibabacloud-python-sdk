# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTransitRouterCidrAllocationRequest(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_name: str = None,
        cidr: str = None,
        cidr_block: str = None,
        client_token: str = None,
        dedicated_owner_id: str = None,
        dry_run: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_cidr_id: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the network instance connection.
        self.attachment_id = attachment_id
        # The name of the network instance connection.
        self.attachment_name = attachment_name
        # The CIDR block of the transit router.
        self.cidr = cidr
        # The CIDR blocks that have IP addresses allocated to network instances.
        self.cidr_block = cidr_block
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The CIDR block that is for exclusive use.
        # 
        # Set the value to **VPN**, which specifies the CIDR block that is reserved for VPN connections.
        self.dedicated_owner_id = dedicated_owner_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        # The number of entries per page.
        # 
        # *   If you do not specify a value for **MaxResults**, entries are returned in one response. After you send the request, the value of **MaxResults** includes all entries.
        # 
        # *   If you specify a value for **MaxResults**, entries are returned in batches. Valid values: **1** to **100**. We recommend that you set **MaxResults** to **20**.
        # 
        #     The value of **MaxResults** in the response indicates that number of entries in the current batch.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query or no subsequent query is to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the transit router.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the CIDR block.
        # 
        # You can call the [ListTransitRouterCidr](https://help.aliyun.com/document_detail/462772.html) operation to query the ID of a CIDR block.
        self.transit_router_cidr_id = transit_router_cidr_id
        # The ID of the transit router.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dedicated_owner_id is not None:
            result['DedicatedOwnerId'] = self.dedicated_owner_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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

        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DedicatedOwnerId') is not None:
            self.dedicated_owner_id = m.get('DedicatedOwnerId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

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

        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

