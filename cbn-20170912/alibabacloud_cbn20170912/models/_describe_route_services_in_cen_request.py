# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRouteServicesInCenRequest(DaraModel):
    def __init__(
        self,
        access_region_id: str = None,
        cen_id: str = None,
        host: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the region where the cloud service is accessed.
        self.access_region_id = access_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The service address of the cloud service.
        # 
        # You can enter a domain name, an IP address, or a CIDR block.
        self.host = host
        # The region ID of the cloud service.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.host_region_id = host_region_id
        # The ID of the VPC associated with the cloud service.
        self.host_vpc_id = host_vpc_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. Valid values: **1** to **50**.
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
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.host is not None:
            result['Host'] = self.host

        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id

        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id

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
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')

        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')

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

