# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSmartAccessGatewayDnsForwardRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        master_ip: str = None,
        mode: str = None,
        outbound_port_index: str = None,
        outbound_port_name: str = None,
        outbound_port_type: str = None,
        region_id: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
        slave_ip: str = None,
    ):
        # The domain name.
        # > 
        # >- Wildcard domain names and full match are supported. You can enter an asterisk (*) for the domain name to match all. Examples:
        # *.baidu.com. The allowed input format is baidu.com.
        # 
        # This parameter is required.
        self.domain = domain
        # The primary DNS server.
        # 
        # This parameter is required.
        self.master_ip = master_ip
        # The forwarding mode.
        # 
        # >- This field is invalid. You can ignore it.
        self.mode = mode
        # The outbound port index.
        # >- This parameter is optional when OutboundPortType is set to PhysicalPort, and is not required when OutboundPortType is set to Tunnel.
        # >- OutboundPortIndex and OutboundPortName have a one-to-one mapping: 0 - eth0; 2 - lte.
        self.outbound_port_index = outbound_port_index
        # The outbound port.
        # >- This parameter is optional when OutboundPortType is set to PhysicalPort, and is not required when OutboundPortType is set to Tunnel.
        # >- OutboundPortIndex and OutboundPortName have a one-to-one mapping: 0 - eth0; 2 - lte.
        self.outbound_port_name = outbound_port_name
        # The outbound port type.
        # >- A value of Tunnel indicates a tunnel port, and a value of PhysicalPort indicates a physical port.
        self.outbound_port_type = outbound_port_type
        # The region ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Smart Access Gateway instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number of the device.
        # 
        # This parameter is required.
        self.sag_sn = sag_sn
        # The secondary DNS server.
        self.slave_ip = slave_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.master_ip is not None:
            result['MasterIp'] = self.master_ip

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.outbound_port_index is not None:
            result['OutboundPortIndex'] = self.outbound_port_index

        if self.outbound_port_name is not None:
            result['OutboundPortName'] = self.outbound_port_name

        if self.outbound_port_type is not None:
            result['OutboundPortType'] = self.outbound_port_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        if self.slave_ip is not None:
            result['SlaveIp'] = self.slave_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('MasterIp') is not None:
            self.master_ip = m.get('MasterIp')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OutboundPortIndex') is not None:
            self.outbound_port_index = m.get('OutboundPortIndex')

        if m.get('OutboundPortName') is not None:
            self.outbound_port_name = m.get('OutboundPortName')

        if m.get('OutboundPortType') is not None:
            self.outbound_port_type = m.get('OutboundPortType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        if m.get('SlaveIp') is not None:
            self.slave_ip = m.get('SlaveIp')

        return self

