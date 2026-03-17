# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagPortRouteProtocolRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        port_name: str = None,
        region_id: str = None,
        remote_as: str = None,
        remote_ip: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_protocol: str = None,
        smart_agid: str = None,
        smart_agsn: str = None,
        vlan: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the port.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The ID of the region where the Smart Access Gateway (SAG) instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The BGP autonomous system number (ASN) of the peer device.
        # 
        # >  You must set this parameter when you enable BGP.
        self.remote_as = remote_as
        # The IP address of the peer device.
        # 
        # >  You must set this parameter when you enable BGP.
        self.remote_ip = remote_ip
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The routing protocol. Valid values:
        # 
        # *   **STATIC**: uses a static routing protocol.
        # *   **OSPF**: uses the Open Shortest Path First protocol (OSPF).
        # *   **BGP**: uses the Border Gateway Protocol (BGP).
        # 
        # This parameter is required.
        self.route_protocol = route_protocol
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn
        # The VLAN ID.
        self.vlan = vlan

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

        if self.remote_as is not None:
            result['RemoteAs'] = self.remote_as

        if self.remote_ip is not None:
            result['RemoteIp'] = self.remote_ip

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_protocol is not None:
            result['RouteProtocol'] = self.route_protocol

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        if self.vlan is not None:
            result['Vlan'] = self.vlan

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

        if m.get('RemoteAs') is not None:
            self.remote_as = m.get('RemoteAs')

        if m.get('RemoteIp') is not None:
            self.remote_ip = m.get('RemoteIp')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteProtocol') is not None:
            self.route_protocol = m.get('RouteProtocol')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

