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
        # The information about the attack types.
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
        # The type of the attack Valid values:
        # 
        # *   **QOTD-Reflect-Flood**: QOTD reflection attacks
        # *   **CharGEN-Reflect-Flood**: CHARGEN reflection attacks
        # *   **DNS-Reflect-Flood**: DNS reflection attacks
        # *   **TFTP-Reflect-Flood**: TFTP reflection attacks
        # *   **Portmap-Reflect-Flood**: Portmap reflection attacks
        # *   **NTP-Reflect-Flood**: NTP reflection attacks
        # *   **NetBIOS-Reflect-Flood**: NetBIOS reflection attacks
        # *   **SNMPv2-Reflect-Flood**: SNMPv2 reflection attacks
        # *   **CLDAP-Reflect-Flood**: CLDAP reflection attacks
        # *   **Ripv1-Reflect-Flood**: RIPv1 reflection attacks
        # *   **OpenVPN-Reflect-Flood**: OpenVPN reflection attacks
        # *   **SSDP-Reflect-Flood**: SSDP reflection attacks
        # *   **NetAssistant-Reflect-Flood**: NetAssistant reflection attacks
        # *   **WSDiscovery-Reflect-Flood**: WS-Discovery reflection attacks
        # *   **Kad-Reflect-Flood**: Kad reflection attacks
        # *   **mDNS-Reflect-Flood**: mDNS reflection attacks
        # *   **10001-Reflect-Flood**: reflection attacks over port 10001
        # *   **Memcached-Reflect-Flood**: Memcached reflection attacks
        # *   **QNP-Reflect-Flood**: QNP reflection attacks
        # *   **DVR-Reflect-Flood**: DVR reflection attacks
        # *   **CoAP-Reflect-Flood**: CoAP reflection attacks
        # *   **ADDP-Reflect-Flood**: ADDP reflection attacks
        # *   **Tcp-Syn**: TCP SYN flood attacks
        # *   **Tcp-Fin**: TCP FIN flood attacks
        # *   **Tcp-Ack**: TCP ACK flood attacks
        # *   **Tcp-Rst**: TCP RST flood attacks
        # *   **Tcp-Pushack**: TCP PSH-ACK flood attacks
        # *   **Tcp-Synack**: TCP SYN-ACK flood attacks
        # *   **Udp-None**: UDP attacks
        # *   **Udp-Ssh**: UDP-based SSH attacks
        # *   **Udp-Dns**: UDP-based DNS attacks
        # *   **Udp-Http**: UDP-based HTTP attacks
        # *   **Udp-Https**: UDP-based HTTPS attacks
        # *   **Udp-Ntp**: UDP-based NTP attacks
        # *   **Udp-Ldap**: UDP-based LDAP attacks
        # *   **Udp-Ssdp**: UDP-based SSDP attacks
        # *   **Udp-Memcached**: Memcached UDP reflection attacks
        # *   **Tcp-Other**: other TCP attacks
        # *   **Icmp**: ICMP flood attacks
        # *   **Igmp**: IGMP flood attacks
        # *   **Ipv6**: IPv6 attacks
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

