# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateGatewayServiceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        dns_server_list: List[str] = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: str = None,
        ip_list: List[str] = None,
        name: str = None,
        service_port: str = None,
        service_protocol: str = None,
        tls_setting: str = None,
    ):
        self.accept_language = accept_language
        self.dns_server_list = dns_server_list
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.id = id
        self.ip_list = ip_list
        self.name = name
        self.service_port = service_port
        self.service_protocol = service_protocol
        self.tls_setting = tls_setting

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.dns_server_list is not None:
            result['DnsServerList'] = self.dns_server_list

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.name is not None:
            result['Name'] = self.name

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.tls_setting is not None:
            result['TlsSetting'] = self.tls_setting

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DnsServerList') is not None:
            self.dns_server_list = m.get('DnsServerList')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('TlsSetting') is not None:
            self.tls_setting = m.get('TlsSetting')

        return self

