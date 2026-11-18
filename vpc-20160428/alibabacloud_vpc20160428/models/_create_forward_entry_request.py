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
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this request. Valid values:
        # 
        # - **true**: performs a dry run without creating the DNAT entry. The system checks whether your AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a Normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the DNAT entry is created.
        self.dry_run = dry_run
        # - If you configure a DNAT entry for an Internet NAT gateway, specify an elastic IP address (EIP) for public network access.
        # - If you configure a DNAT entry for a VPC NAT gateway, specify a NAT IP address for external network access.
        # 
        # This parameter is required.
        self.external_ip = external_ip
        # - If you configure a DNAT entry for an Internet NAT gateway, specify the external port or port range for port forwarding.
        #  
        #     - The port range must be from **1** to **65535**.
        #     - To forward traffic within a port range, separate the start port and the end port with a forward slash (/). Example: `10/20`.
        #     - If **ExternalPort** is set to a port range, **InternalPort** must also be set to a port range with the same number of ports. For example, if **ExternalPort** is set to `10/20`, **InternalPort** must be set to `80/90`.
        # 
        # - If you configure a DNAT entry for a VPC NAT gateway, specify the port on the NAT IP address that is accessed by the external network. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.external_port = external_port
        # The name of the DNAT rule.
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.forward_entry_name = forward_entry_name
        # The ID of the DNAT table.
        # 
        # This parameter is required.
        self.forward_table_id = forward_table_id
        # - If you configure a DNAT entry for an Internet NAT gateway, specify the private IP address of the ECS instance that requires Internet communication. The private IP address must meet the following requirements: 
        #         
        #     - The private IP address must belong to the CIDR block of the VPC where the NAT gateway is deployed. 
        # 
        #     - The private IP address must be used by an ECS instance, and the ECS instance must not be associated with an EIP. Otherwise, the DNAT entry does not take effect. 
        # 
        # - If you configure a DNAT entry for a VPC NAT gateway, specify the private IP address that requires communication through the DNAT rule.
        # 
        # This parameter is required.
        self.internal_ip = internal_ip
        # - If you configure a DNAT entry for an Internet NAT gateway, specify the internal port or port range for port forwarding. Valid values: **1** to **65535**.
        # 
        # - If you configure a DNAT entry for a VPC NAT gateway, specify the destination port of the ECS instance to be mapped. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.internal_port = internal_port
        # The protocol type. Valid values: 
        # 
        # - **TCP**: forwards TCP packets.   
        # 
        # - **UDP**: forwards UDP packets.   
        # 
        # - **Any**: forwards packets of all protocols. If **IpProtocol** is set to **Any**, **ExternalPort** and **InternalPort** must also be set to **Any** to implement DNAT IP mapping.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to enable port breaking. Valid values:
        # 
        # - **true**: enables port breaking.
        # 
        # - **false** (default): disables port breaking.
        # 
        # > If a DNAT entry and an SNAT entry use the same public IP address and you need to configure a port number greater than 1024, you must set **PortBreak** to **true**.
        self.port_break = port_break
        # The region ID of the NAT gateway.
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

