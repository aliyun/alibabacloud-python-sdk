# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagWanRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        gateway: str = None,
        ip: str = None,
        iptype: str = None,
        isp: str = None,
        mask: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        port_name: str = None,
        priority: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        smart_agsn: str = None,
        username: str = None,
        weight: int = None,
    ):
        # The maximum bandwidth of the WAN port. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The IP address of the gateway.
        # 
        # > 
        # *   If the WAN port uses a static IP address, you must set this parameter.
        # *   After this parameter is set, the SAG device generates a default route.
        self.gateway = gateway
        # The IP address of the WAN port.
        # 
        # >  If the WAN port uses a static IP address, you must set this parameter.
        self.ip = ip
        # The connection type of the WAN port: Valid values:
        # 
        # *   **DHCP**: The WAN port connects to the Internet through an IP address that is dynamically assigned by the Dynamic Host Configuration Protocol (DHCP) server.
        # *   **STATIC**: The WAN port connects to the Internet through a static IP address. If you set this value, you must configure a static IP address, a subnet mask, and a gateway IP address for the WAN port.
        # *   **PPPOE**: The WAN port connects to the Internet through dial-up connections. If you set this value, you must enter the username and password of the PPPoE account provided by the Internet service provider (ISP).
        # 
        # This parameter is required.
        self.iptype = iptype
        # The ISP used by the WAN port. Valid values:
        # 
        # *   **CT**: China Telecom
        # *   **CM**: China Mobile
        # *   **CU**: China Unicom
        # *   **Other**: Other ISPs.
        self.isp = isp
        # The subnet mask of the WAN port IP address.
        # 
        # >  If the WAN port uses a static IP address, you must set this parameter.
        self.mask = mask
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the PPPoE account.
        # 
        # The username must be 6 to 30 characters in length, and can contain digits and letters.
        # 
        # >  If the connection type of the WAN port is PPPoE, you must set this parameter. If you do not need to modify the password, you can ignore this parameter.
        self.password = password
        # The number of the WAN port.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The priority of the WAN port.
        # 
        # Valid values: **-1** and **1 to 50**.
        # 
        # A smaller value indicates a higher priority. A value of **-1** indicates that traffic forwarding is disabled on the WAN port.
        self.priority = priority
        # The ID of the region where the SAG instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn
        # The username of the PPPoE account.
        # 
        # The username must be 6 to 30 characters in length, and can contain digits and letters.
        # 
        # >  If the connection type of the WAN port is PPPoE, you must set this parameter.
        self.username = username
        # The weight of the WAN port.
        # 
        # Valid values: **1 to 100**. Default value: **100**.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.ip is not None:
            result['IP'] = self.ip

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        if self.username is not None:
            result['Username'] = self.username

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

