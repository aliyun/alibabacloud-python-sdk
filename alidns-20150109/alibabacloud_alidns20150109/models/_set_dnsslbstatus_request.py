# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDNSSLBStatusRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        line: str = None,
        open: bool = None,
        sub_domain: str = None,
        type: str = None,
        user_client_ip: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The language of the content within the request and response. Default: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The DNS resolution line. The line can be the default line, China Telecom, and China Mobile.
        self.line = line
        # Specifies whether to enable or disable weighted round-robin. Valid values:
        # 
        # *   **true** (default): enables weighted round-robin.
        # *   **false**: disables weighted round-robin.
        self.open = open
        # The subdomain name for which you want to enable weighted round-robin. Set the parameter to @.example.com instead of example.com.
        # 
        # This parameter is required.
        self.sub_domain = sub_domain
        # The type of the Domain Name System (DNS) record. Valid values: A and AAAA. Default value: A.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line is not None:
            result['Line'] = self.line

        if self.open is not None:
            result['Open'] = self.open

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.type is not None:
            result['Type'] = self.type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

