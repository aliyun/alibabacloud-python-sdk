# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateForwardEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_name: str = None,
        forward_table_id: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_break: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.dry_run = dry_run
        # *   The EIP that can be accessed over the Internet when you configure a DNAT entry for an Internet NAT gateway.
        # *   The NAT IP address that can be accessed by external networks when you configure a DNAT entry for a VPC NAT gateway.
        # 
        # This parameter is required.
        self.external_ip = external_ip
        # *   The external port range that is used for port forwarding when you configure a DNAT entry for an Internet NAT gateway.
        # 
        #     *   Valid values: **1** to **65535**.
        #     *   To specify a port range, separate the first port and the last port with a forward slash (/), for example, `10/20`.
        #     *   If you set **ExternalPort** to a port range, you must also set **InternalPort** to a port range, and the number of ports specified by these parameters must be the same. For example, if you set **ExternalPort** to `10/20`, you can set **InternalPort** to `80/90`.
        # 
        # *   The port that can be accessed by external networks when you configure a DNAT entry for a VPC NAT gateway. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.external_port = external_port
        # The name of the DNAT entry.
        # 
        # The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.forward_entry_name = forward_entry_name
        # The ID of the DNAT table.
        # 
        # This parameter is required.
        self.forward_table_id = forward_table_id
        # *   The private IP address of the ECS instance that needs to communicate with the Internet when you configure a DNAT entry for an Internet NAT gateway. The private IP address must meet the following requirements:
        # 
        #     *   It must belong to the CIDR block of the VPC where the NAT gateway is deployed.
        #     *   The DNAT entry takes effect only if the private IP address is assigned to an ECS instance and the ECS instance is not associated with an EIP.
        # 
        # *   The private IP address that uses DNAT when you add a DNAT entry to a VPC NAT gateway.
        # 
        # This parameter is required.
        self.internal_ip = internal_ip
        # *   The internal port or port range that is used for port forwarding when you configure a DNAT entry for an Internet NAT gateway. Valid values: **1** to **65535**.
        # *   The port of the destination ECS instance to be mapped when you configure a DNAT entry for a VPC NAT gateway. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.internal_port = internal_port
        # The protocol. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        # *   **Any** If you set **IpProtocol** to **Any**, you must also set **ExternalPort** and **InternalPort** to **Any** to implement DNAT IP mapping.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to remove limits on the port range. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  If a DNAT entry and an SNAT entry have the same public IP address, ou must specify a port that is larger that 1024, and set **PortBreak** to **true**.
        self.port_break = port_break
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
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

        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name

        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_break is not None:
            result['PortBreak'] = self.port_break

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

        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')

        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortBreak') is not None:
            self.port_break = m.get('PortBreak')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

