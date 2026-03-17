# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagPortRoleRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        port_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
        smart_agid: str = None,
        smart_agsn: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the port.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The ID of the region where the Smart Access Gateway (SAG) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role of the port. Valid values:
        # 
        # *   **NONE**: No role is assigned to the port.
        # *   **WAN**: The port is used as a WAN port. By default, port 5 of an SAG device is used as a WAN port and supports access to the Internet by using a Dynamic Host Configuration Protocol (DHCP) client, PPPoE, or a static IP address.
        # *   **LAN**: The port is used as a LAN port. The LAN port allows a DHCP server or a static IP address to connect to an on-premises terminal or switch.
        # *   **ECC**: The port is used as a port to connect to an Express Connect circuit.
        # *   **MGT**: The port is used as the management port. By default, port 2 of an SAG device is used as the management port.
        # 
        # > 
        # 
        # *   In exclusive mode, the management traffic is separated from the workload traffic. The management port is only used to access the SAG web console and cannot be used to transfer your workload data. You can access the SAG web console only through the management port.
        # *   A WAN port can be used when it is connected. If a port is the first one that obtains an IP address over DHCP and can access the Internet, it is set as a WAN port. In the SAG web console, you can set another port as a WAN port.
        # 
        # This parameter is required.
        self.role = role
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role is not None:
            result['Role'] = self.role

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        return self

