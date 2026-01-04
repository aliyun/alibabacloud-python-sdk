# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateEipAddressRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        client_token: str = None,
        instance_id: str = None,
        instance_region_id: str = None,
        instance_type: str = None,
        mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
    ):
        # The ID of the EIP that you want to associate with an instance.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the instance with which you want to associate the EIP.
        # 
        # You can enter the ID of a NAT gateway, CLB instance, ECS instance, secondary ENI, HAVIP, or IP address.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region in which the instance with which you want to associate the EIP resides.
        # 
        # >  This parameter is required only when the EIP is added to a shared Global Accelerator (GA) instance.
        self.instance_region_id = instance_region_id
        # The type of the instance with which you want to associate the EIP. Valid values:
        # 
        # *   **Nat**: NAT gateway
        # *   **SlbInstance**: CLB instance
        # *   **EcsInstance** (default): ECS instance
        # *   **NetworkInterface**: secondary ENI
        # *   **HaVip**: HAVIP
        # *   **IpAddress**: IP address
        # 
        # >  The default value is **EcsInstance**. If the instance with which you want to associate the EIP is not an ECS instance, this parameter is required.
        self.instance_type = instance_type
        # The association mode. Valid values:
        # 
        # *   **NAT** (default): NAT mode
        # *   **MULTI_BINDED**: multi-EIP-to-ENI mode
        # *   **BINDED**: cut-network interface controller mode
        # 
        # >  This parameter is required only when **InstanceType** is set to **NetworkInterface**.
        self.mode = mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address in the CIDR block of the vSwitch.
        # 
        # If you leave this parameter empty, the system allocates a private IP address based on the VPC ID and vSwitch ID.
        self.private_ip_address = private_ip_address
        # The ID of the region to which the EIP belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VPC in which an IPv4 gateway is created. The VPC and the EIP must be in the same region.
        # 
        # When you associate an EIP with an IP address, the system can enable the IP address to access the Internet based on VPC route configurations.
        # 
        # >  This parameter is required if **InstanceType** is set to **IpAddress**, which indicates that the EIP is to be associated with an IP address.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

