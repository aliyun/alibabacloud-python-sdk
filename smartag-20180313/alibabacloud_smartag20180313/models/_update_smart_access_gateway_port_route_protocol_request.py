# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAccessGatewayPortRouteProtocolRequest(DaraModel):
    def __init__(
        self,
        cross_account: bool = None,
        port_name: str = None,
        region_id: str = None,
        remote_as: str = None,
        remote_ip: str = None,
        resource_uid: str = None,
        route_protocol: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
        vlan: str = None,
    ):
        # Specifies whether to query only the SAG instances that belong to another Alibaba Cloud account. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.cross_account = cross_account
        # The port name.
        # 
        # This parameter is required.
        self.port_name = port_name
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The autonomous system number (ASN) of the SAG device.
        # 
        # > When you enable BGP, you must set this parameter.
        self.remote_as = remote_as
        # The IP address of the peer device.
        # 
        # > When you enable BGP, you must set this parameter.
        self.remote_ip = remote_ip
        # The ID of the Alibaba Cloud account to which the SAG instance belongs.
        self.resource_uid = resource_uid
        # The routing protocol. Valid values:
        # 
        # *   **STATIC**
        # *   **OSPF**
        # *   **BGP**
        # 
        # This parameter is required.
        self.route_protocol = route_protocol
        # The ID of the Smart Access Gateway (SAG) instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sag_sn = sag_sn
        # The VLAN ID.
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account is not None:
            result['CrossAccount'] = self.cross_account

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_as is not None:
            result['RemoteAs'] = self.remote_as

        if self.remote_ip is not None:
            result['RemoteIp'] = self.remote_ip

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.route_protocol is not None:
            result['RouteProtocol'] = self.route_protocol

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccount') is not None:
            self.cross_account = m.get('CrossAccount')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteAs') is not None:
            self.remote_as = m.get('RemoteAs')

        if m.get('RemoteIp') is not None:
            self.remote_ip = m.get('RemoteIp')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('RouteProtocol') is not None:
            self.route_protocol = m.get('RouteProtocol')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

