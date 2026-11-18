# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIpv4GatewayRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        internet_mode: str = None,
        ipv_4gateway_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without deleting the IPv4 gateway. The system checks whether the required parameters are specified, the request format is valid, and the service limits are met. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, the HTTP 2xx status code is returned and the IPv4 gateway is deleted.
        self.dry_run = dry_run
        # The public network pattern of the VPC after the IPv4 gateway is deleted. Valid values:
        # 
        # - **private**: the default value. After the IPv4 gateway is deleted, the VPC becomes a purely private network VPC and does not have public network access capabilities.
        # - **public**: After the IPv4 gateway is deleted, public network access to the VPC is no longer centrally controlled by the IPv4 gateway. By default, after a public IP address is associated with an instance, the instance can directly access the public network.
        self.internet_mode = internet_mode
        # The instance ID of the IPv4 gateway to delete.
        # 
        # This parameter is required.
        self.ipv_4gateway_id = ipv_4gateway_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IPv4 gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
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

        if self.internet_mode is not None:
            result['InternetMode'] = self.internet_mode

        if self.ipv_4gateway_id is not None:
            result['Ipv4GatewayId'] = self.ipv_4gateway_id

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

        if m.get('InternetMode') is not None:
            self.internet_mode = m.get('InternetMode')

        if m.get('Ipv4GatewayId') is not None:
            self.ipv_4gateway_id = m.get('Ipv4GatewayId')

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

