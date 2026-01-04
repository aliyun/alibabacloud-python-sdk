# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyForwardEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
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
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.dry_run = dry_run
        # *   When you modify DNAT entries of Internet NAT gateways, this parameter specifies the elastic IP addresses (EIPs) that are used to access the Internet.
        # *   When you modify DNAT entries of Virtual Private Cloud (VPC) NAT gateways, this parameter specifies the NAT IP addresses that are accessed by external networks.
        self.external_ip = external_ip
        # *   The external port that is used to forward traffic when you modify DNAT entries of Internet NAT gateways.
        # 
        #     *   Valid values: **1** to **65535**.
        #     *   If you want to modify the port range, separate port numbers with a forward slash (/), such as `10/20`.
        #     *   If you need to modify **ExternalPort** and **InternalPort** at the same time, and **ExternalPort** specifies a port range, make sure that **InternalPort** also specifies a port range, and both ranges specify the same number of ports. For example, you can set **ExternalPort** to `10/20` and **InternalPort** to `80/90`.
        # 
        # *   The port that is accessed by external networks when you modify DNAT entries of VPC NAT gateways. Valid values: **1** to **65535**.
        self.external_port = external_port
        # The ID of the DNAT entry.
        # 
        # This parameter is required.
        self.forward_entry_id = forward_entry_id
        # The new name of the DNAT entry.
        # 
        # The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.forward_entry_name = forward_entry_name
        # The ID of the DNAT table to which the DNAT entry belongs.
        # 
        # This parameter is required.
        self.forward_table_id = forward_table_id
        # *   The private IP address of the ECS instance that uses DNAT entries to communicate with the Internet when you modify DNAT entries of Internet NAT gateways.
        # *   The private IP address that uses DNAT entries to communicate when you modify DNAT entries of VPC NAT gateways.
        self.internal_ip = internal_ip
        # *   The internal port or port range that is used to forward traffic when you modify DNAT entries of Internet NAT gateways. Valid values: **1** to **65535**.
        # *   The port of the destination ECS instance to be mapped when you modify DNAT entries of VPC NAT gateways. Valid values: **1** to **65535**.
        self.internal_port = internal_port
        # The protocol. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        # *   **Any**
        self.ip_protocol = ip_protocol
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to remove limits on the port range. Valid values:
        # 
        # *   **true**
        # *   **false** If an SNAT entry and a DNAT entry use the same public IP address, and you want to specify a port number greater than `1024`, set `PortBreak` to `true`.
        self.port_break = port_break
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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

        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

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

        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

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

