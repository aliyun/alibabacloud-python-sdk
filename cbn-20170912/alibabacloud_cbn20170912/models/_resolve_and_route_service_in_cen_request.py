# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResolveAndRouteServiceInCenRequest(DaraModel):
    def __init__(
        self,
        access_region_ids: List[str] = None,
        cen_id: str = None,
        client_token: str = None,
        description: str = None,
        host: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the regions where the cloud service is accessed.
        # 
        # This parameter is required.
        self.access_region_ids = access_region_ids
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # The description of the cloud service.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The IP addresses or CIDR blocks of the cloud service.
        # 
        # > In most cases, multiple IP addresses or CIDR blocks are assigned to a cloud service. We recommend that you call this operation multiple times to add all IP addresses and CIDR blocks of the cloud service.
        # 
        # This parameter is required.
        self.host = host
        # The ID of the region in which the cloud service is deployed.
        # 
        # This parameter is required.
        self.host_region_id = host_region_id
        # The ID of the VPC that is associated with the cloud service.
        # 
        # This parameter is required.
        self.host_vpc_id = host_vpc_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_region_ids is not None:
            result['AccessRegionIds'] = self.access_region_ids

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRegionIds') is not None:
            self.access_region_ids = m.get('AccessRegionIds')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

