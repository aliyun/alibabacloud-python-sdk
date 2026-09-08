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
        # The transit router CIDR block.
        self.cidr = cidr
        # The allocated CIDR block under the transit router CIDR block.
        self.cidr_block = cidr_block
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The dedicated CIDR block.
        # 
        # Set the value to **VPN**, which specifies that you want to query the CIDR block reserved by the system for creating VPN connections in the backend.
        self.dedicated_owner_id = dedicated_owner_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and business restrictions. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, the transit router CIDR block allocation details are queried.
        self.dry_run = dry_run
        # The number of entries per page.
        # 
        # - If you do not specify a value for **MaxResults**, it indicates that you do not need to query results by page. The value of **MaxResults** in the response indicates the total number of entries.
        # - If you specify a value for **MaxResults**, it indicates that you need to query results by page. Valid values: **1** to **100**. We recommend that you set **MaxResults** to **20**.      
        # 
        #   The value of **MaxResults** in the response indicates the number of entries on the current page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - You do not need to specify this parameter for the first request or if no subsequent request exists.
        # - If a subsequent request exists, set the value to the **NextToken** value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the transit router instance.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the transit router CIDR block.
        # 
        # You can call the [ListTransitRouterCidr](https://help.aliyun.com/document_detail/462772.html) operation to query the transit router CIDR block ID.
        self.transit_router_cidr_id = transit_router_cidr_id
        # The forward router instance ID.
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

