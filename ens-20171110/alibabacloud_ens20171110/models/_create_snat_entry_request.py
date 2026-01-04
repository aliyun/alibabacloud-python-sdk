# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnatEntryRequest(DaraModel):
    def __init__(
        self,
        eip_affinity: bool = None,
        idle_timeout: int = None,
        isp_affinity: bool = None,
        nat_gateway_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        source_cidr: str = None,
        source_network_id: str = None,
        source_vswitch_id: str = None,
        standby_snat_ip: str = None,
    ):
        # Specifies whether to enable IP affinity. If you do not specify this parameter, IP affinity is enabled by default. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # >  After you enable IP affinity, if multiple EIPs are associated with an SNAT entry, one client uses the same EIP to for communication. If IP affinity is disabled, the client uses a random EIP for communication.
        self.eip_affinity = eip_affinity
        # The timeout period for idle connections. Valid values: **1** to **86400**. Unit: seconds.
        self.idle_timeout = idle_timeout
        # Whether to enable operator affinity. Value taking:
        # 
        # - false:Do not open.
        # - true:Open.
        self.isp_affinity = isp_affinity
        # The ID of the Network Address Translation (NAT) gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The name of the SNAT entry. The name must be 1 to 128 characters in length. The name cannot start with `http://` or `https://`.
        self.snat_entry_name = snat_entry_name
        # The elastic IP address (EIP) in the SNAT entry. Separate multiple EIPs with commas (,).
        # 
        # This parameter is required.
        self.snat_ip = snat_ip
        # The CIDR block. You can specify the CIDR block of a network, a vSwitch, or an instance. You can also specify a custom CIDR block. All instances within the CIDR block can access the Internet or external networks by using SNAT.
        # 
        # >  If you specify **SourceVSwitchId** and **SourceCIDR**, **SourceVSwitchId** does not take effect. The value that you specified for **SourceCIDR** takes precedence.
        self.source_cidr = source_cidr
        # The ID of the network. This parameter specifies that all ENS instances in the network can use the SNAT entry to access the Internet.
        # 
        # >  If you specify **SourceNetworkId** and **SourceVSwitchId** or **SourceCIDR**, **SourceNetworkId** does not take effect. The value that you specified for **SourceCIDR** takes precedence. Priority: **SourceCIDR** > **SourceVSwitchId** > **SourceNetworkId**.
        self.source_network_id = source_network_id
        # The ID of the vSwitch that you need to access over the Internet. This parameter specifies that Edge Node Service (ENS) instances in the vSwitch can use the SNAT entry to access the Internet.
        # 
        # >  If you specify **SourceVSwitchId** and **SourceCIDR**, **SourceVSwitchId** does not take effect. The value that you specified for **SourceCIDR** takes precedence.
        self.source_vswitch_id = source_vswitch_id
        # The secondary EIP in the SNAT entry. Separate multiple secondary EIPs with commas (,).
        self.standby_snat_ip = standby_snat_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.isp_affinity is not None:
            result['IspAffinity'] = self.isp_affinity

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.source_network_id is not None:
            result['SourceNetworkId'] = self.source_network_id

        if self.source_vswitch_id is not None:
            result['SourceVSwitchId'] = self.source_vswitch_id

        if self.standby_snat_ip is not None:
            result['StandbySnatIp'] = self.standby_snat_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('IspAffinity') is not None:
            self.isp_affinity = m.get('IspAffinity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('SourceNetworkId') is not None:
            self.source_network_id = m.get('SourceNetworkId')

        if m.get('SourceVSwitchId') is not None:
            self.source_vswitch_id = m.get('SourceVSwitchId')

        if m.get('StandbySnatIp') is not None:
            self.standby_snat_ip = m.get('StandbySnatIp')

        return self

