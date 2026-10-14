# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDosEventAttackTypeResponseBody(DaraModel):
    def __init__(
        self,
        attack_types: List[main_models.DescribeDDosEventAttackTypeResponseBodyAttackTypes] = None,
        request_id: str = None,
    ):
        # The attack type information.
        self.attack_types = attack_types
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.attack_types:
            for v1 in self.attack_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackTypes'] = []
        if self.attack_types is not None:
            for k1 in self.attack_types:
                result['AttackTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_types = []
        if m.get('AttackTypes') is not None:
            for k1 in m.get('AttackTypes'):
                temp_model = main_models.DescribeDDosEventAttackTypeResponseBodyAttackTypes()
                self.attack_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDDosEventAttackTypeResponseBodyAttackTypes(DaraModel):
    def __init__(
        self,
        attack_type: str = None,
        in_pkts: int = None,
    ):
        # The attack type. Valid values:
        # 
        # - **QOTD-Reflect-Flood**: QOTD reflection attack
        # - **CharGEN-Reflect-Flood**: CharGEN reflection attack
        # - **DNS-Reflect-Flood**: DNS reflection attack
        # - **TFTP-Reflect-Flood**: TFTP reflection attack
        # - **Portmap-Reflect-Flood**: Portmap reflection attack
        # - **NTP-Reflect-Flood**: NTP reflection attack
        # - **NetBIOS-Reflect-Flood**: NetBIOS reflection attack
        # - **SNMPv2-Reflect-Flood**: SNMPv2 reflection attack
        # - **CLDAP-Reflect-Flood**: CLDAP reflection attack
        # - **Ripv1-Reflect-Flood**: Ripv1 reflection attack
        # - **OpenVPN-Reflect-Flood**: OpenVPN reflection attack
        # - **SSDP-Reflect-Flood**: SSDP reflection attack
        # - **NetAssistant-Reflect-Flood**: NetAssistant reflection attack
        # - **WSDiscovery-Reflect-Flood**: WSDiscovery reflection attack
        # - **Kad-Reflect-Flood**: Kad reflection attack
        # - **mDNS-Reflect-Flood**: mDNS reflection attack
        # - **10001-Reflect-Flood**: 10001 reflection attack
        # - **Memcached-Reflect-Flood**: Memcached reflection attack
        # - **QNP-Reflect-Flood**: QNP reflection attack
        # - **DVR-Reflect-Flood**: DVR reflection attack
        # - **CoAP-Reflect-Flood**: CoAP reflection attack
        # - **ADDP-Reflect-Flood**: ADDP reflection attack
        # - **Tcp-Syn**: TCP SYN flood attacks
        # - **Tcp-Fin**: TCP FIN flood attack
        # - **Tcp-Ack**: TCP ACK Flood attacks
        # - **Tcp-Rst**: TCP RST flood attack
        # - **Tcp-Pushack**: TCP PSH+ACK flood attack
        # - **Tcp-Synack**: TCP SYN+ACK flood attack
        # - **Udp-None**: UDP attack
        # - **Udp-Ssh**: UDP SSH protocol attack
        # - **Udp-Dns**: UDP DNS protocol attack
        # - **Udp-Http**: UDP HTTP protocol attack
        # - **Udp-Https**: UDP HTTPS protocol attack
        # - **Udp-Ntp**: UDP NTP protocol attack
        # - **Udp-Ldap**: UDP LDAP protocol attack
        # - **Udp-Ssdp**: UDP SSDP protocol attack
        # - **Udp-Memcached**: Memcache UDP reflection amplification attack
        # - **Tcp-Other**: TCP other type attack
        # - **Icmp**: ICMP flood attack
        # - **Igmp**: IGMP flood attack
        # - **Ipv6**: IPv6 attack
        self.attack_type = attack_type
        # The number of request packets of the attack type.
        self.in_pkts = in_pkts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')

        return self

