# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRouteConflictRequest(DaraModel):
    def __init__(
        self,
        child_instance_id: str = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        child_instance_type: str = None,
        destination_cidr_block: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the network instance that you want to query.
        # 
        # This parameter is required.
        self.child_instance_id = child_instance_id
        # The ID of the region where the network instance is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.child_instance_region_id = child_instance_region_id
        # The ID of the route table that is configured on the network instance.
        # 
        # This parameter is required.
        self.child_instance_route_table_id = child_instance_route_table_id
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC)
        # *   **VBR**: virtual border router (VBR)
        # *   **CCN**: Cloud Connect Network (CCN) instance
        # 
        # This parameter is required.
        self.child_instance_type = child_instance_type
        # The destination CIDR block of the conflicting route.
        self.destination_cidr_block = destination_cidr_block
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

