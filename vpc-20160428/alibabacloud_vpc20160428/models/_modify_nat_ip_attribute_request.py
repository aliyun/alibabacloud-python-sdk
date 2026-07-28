# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNatIpAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        nat_ip_description: str = None,
        nat_ip_id: str = None,
        nat_ip_name: str = None,
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
        # > If you do not specify this parameter, the system uses the **RequestId** as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: sends a check request without modifying the NAT IP address information. The system checks the request for potential issues, including invalid AccessKey pairs, the authorization status of the RAM user, and missing parameter values. If the request fails the dry run, the corresponding error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, a 2xx HTTP status code is returned and the NAT IP address information is modified.
        self.dry_run = dry_run
        # The description of the NAT IP address that you want to modify.
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or Chinese character. It cannot start with `http://` or `https://`.
        self.nat_ip_description = nat_ip_description
        # The instance ID of the NAT IP address that you want to modify.
        # 
        # This parameter is required.
        self.nat_ip_id = nat_ip_id
        # The name of the NAT IP address that you want to modify.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.nat_ip_name = nat_ip_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway instance to which the NAT IP address belongs.
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

        if self.nat_ip_description is not None:
            result['NatIpDescription'] = self.nat_ip_description

        if self.nat_ip_id is not None:
            result['NatIpId'] = self.nat_ip_id

        if self.nat_ip_name is not None:
            result['NatIpName'] = self.nat_ip_name

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

        if m.get('NatIpDescription') is not None:
            self.nat_ip_description = m.get('NatIpDescription')

        if m.get('NatIpId') is not None:
            self.nat_ip_id = m.get('NatIpId')

        if m.get('NatIpName') is not None:
            self.nat_ip_name = m.get('NatIpName')

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

