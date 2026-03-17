# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAccessGatewayDnsForwardRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        master_ip: str = None,
        mode: str = None,
        outbound_port_index: int = None,
        outbound_port_name: str = None,
        outbound_port_type: str = None,
        region_id: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
        slave_ip: str = None,
    ):
        # The domain name.
        # 
        # > 
        # *   Wildcard domain names are supported. You can use the wildcard character asterisk (\\*) to specify a wildcard domain name.
        # 
        # For example, you can enter \\*.baidu.com to specify the domain name baidu.com.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The primary DNS server.
        # 
        # This parameter is required.
        self.master_ip = master_ip
        # The forwarding mode.
        # 
        # > 
        # *   This parameter is not in use. Ignore this parameter.
        self.mode = mode
        # The number of the egress port.
        # 
        # > 
        # *   This parameter is optional if OutboundPortType is set to PhysicalPort. Ignore this parameter if OutboundPortType is set to Tunnel.
        # *   The value of OutboundPortIndex is the unique index of the port name specified by poOutboundPortName. For example, 0 is the index for the port named eth0, and 2 is the index for the port named lte.
        self.outbound_port_index = outbound_port_index
        # The egress port.
        # 
        # > 
        # *   This parameter is optional if OutboundPortType is set to PhysicalPort. Ignore this parameter if OutboundPortType is set to Tunnel.
        # *   The value of OutboundPortIndex is the unique index of the port name specified by poOutboundPortName. For example, 0 is the index for the port named eth0, and 2 is the index for the port named lte.
        self.outbound_port_name = outbound_port_name
        # The type of the egress port.
        # 
        # > 
        # *   A value of Tunnel specifies a tunnel, and a value of PhysicalPort specifies a physical port.
        self.outbound_port_type = outbound_port_type
        # The ID of the region in which the SAG instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number (SN) of the device.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

