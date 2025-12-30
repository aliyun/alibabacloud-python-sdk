# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddDomainResponseBody(DaraModel):
    def __init__(
        self,
        dns_servers: main_models.AddDomainResponseBodyDnsServers = None,
        domain_id: str = None,
        domain_name: str = None,
        group_id: str = None,
        group_name: str = None,
        puny_code: str = None,
        request_id: str = None,
    ):
        # The Domain Name System (DNS) servers configured for the domain name.
        self.dns_servers = dns_servers
        # The ID of the domain name.
        self.domain_id = domain_id
        # The domain name.
        self.domain_name = domain_name
        # The ID of the domain name group.
        self.group_id = group_id
        # The name of the domain name group.
        self.group_name = group_name
        # The Punycode for the domain name. This parameter is returned only for Chinese domain names.
        self.puny_code = puny_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dns_servers:
            self.dns_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServers') is not None:
            temp_model = main_models.AddDomainResponseBodyDnsServers()
            self.dns_servers = temp_model.from_map(m.get('DnsServers'))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddDomainResponseBodyDnsServers(DaraModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')

        return self

