# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateIpamRequest(DaraModel):
    def __init__(
        self,
        add_operating_region: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_description: str = None,
        ipam_id: str = None,
        ipam_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_operating_region: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The effective region that you want to add.
        self.add_operating_region = add_operating_region
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The description of the IPAM.
        # 
        # It must be 2 to 256 characters in length and must start with a letter. It cannot start with `http://` or `https://`. The default value is empty.
        self.ipam_description = ipam_description
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The name of the IPAM.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_name = ipam_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The effective region that you want to remove.
        self.remove_operating_region = remove_operating_region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_operating_region is not None:
            result['AddOperatingRegion'] = self.add_operating_region

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_description is not None:
            result['IpamDescription'] = self.ipam_description

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_name is not None:
            result['IpamName'] = self.ipam_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_operating_region is not None:
            result['RemoveOperatingRegion'] = self.remove_operating_region

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddOperatingRegion') is not None:
            self.add_operating_region = m.get('AddOperatingRegion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamDescription') is not None:
            self.ipam_description = m.get('IpamDescription')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamName') is not None:
            self.ipam_name = m.get('IpamName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveOperatingRegion') is not None:
            self.remove_operating_region = m.get('RemoveOperatingRegion')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

