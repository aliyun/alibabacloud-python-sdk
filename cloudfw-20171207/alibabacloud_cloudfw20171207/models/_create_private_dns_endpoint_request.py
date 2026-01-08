# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePrivateDnsEndpointRequest(DaraModel):
    def __init__(
        self,
        access_instance_name: str = None,
        firewall_type: List[str] = None,
        ip_protocol: str = None,
        member_uid: int = None,
        port: int = None,
        primary_dns: str = None,
        primary_vswitch_id: str = None,
        primary_vswitch_ip: str = None,
        private_dns_type: str = None,
        region_no: str = None,
        standby_dns: str = None,
        standby_vswitch_id: str = None,
        standby_vswitch_ip: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.access_instance_name = access_instance_name
        # This parameter is required.
        self.firewall_type = firewall_type
        self.ip_protocol = ip_protocol
        self.member_uid = member_uid
        self.port = port
        self.primary_dns = primary_dns
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_vswitch_ip = primary_vswitch_ip
        # This parameter is required.
        self.private_dns_type = private_dns_type
        # This parameter is required.
        self.region_no = region_no
        self.standby_dns = standby_dns
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_vswitch_ip = standby_vswitch_ip
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_name is not None:
            result['AccessInstanceName'] = self.access_instance_name

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.port is not None:
            result['Port'] = self.port

        if self.primary_dns is not None:
            result['PrimaryDns'] = self.primary_dns

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_vswitch_ip is not None:
            result['PrimaryVSwitchIp'] = self.primary_vswitch_ip

        if self.private_dns_type is not None:
            result['PrivateDnsType'] = self.private_dns_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.standby_dns is not None:
            result['StandbyDns'] = self.standby_dns

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_vswitch_ip is not None:
            result['StandbyVSwitchIp'] = self.standby_vswitch_ip

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceName') is not None:
            self.access_instance_name = m.get('AccessInstanceName')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrimaryDns') is not None:
            self.primary_dns = m.get('PrimaryDns')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryVSwitchIp') is not None:
            self.primary_vswitch_ip = m.get('PrimaryVSwitchIp')

        if m.get('PrivateDnsType') is not None:
            self.private_dns_type = m.get('PrivateDnsType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StandbyDns') is not None:
            self.standby_dns = m.get('StandbyDns')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyVSwitchIp') is not None:
            self.standby_vswitch_ip = m.get('StandbyVSwitchIp')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

