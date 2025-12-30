# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ModifyHichinaDomainDNSResponseBody(DaraModel):
    def __init__(
        self,
        new_dns_servers: main_models.ModifyHichinaDomainDNSResponseBodyNewDnsServers = None,
        original_dns_servers: main_models.ModifyHichinaDomainDNSResponseBodyOriginalDnsServers = None,
        request_id: str = None,
    ):
        # The DNS server names after modification.
        self.new_dns_servers = new_dns_servers
        # The DNS server names before modification.
        self.original_dns_servers = original_dns_servers
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.new_dns_servers:
            self.new_dns_servers.validate()
        if self.original_dns_servers:
            self.original_dns_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_dns_servers is not None:
            result['NewDnsServers'] = self.new_dns_servers.to_map()

        if self.original_dns_servers is not None:
            result['OriginalDnsServers'] = self.original_dns_servers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDnsServers') is not None:
            temp_model = main_models.ModifyHichinaDomainDNSResponseBodyNewDnsServers()
            self.new_dns_servers = temp_model.from_map(m.get('NewDnsServers'))

        if m.get('OriginalDnsServers') is not None:
            temp_model = main_models.ModifyHichinaDomainDNSResponseBodyOriginalDnsServers()
            self.original_dns_servers = temp_model.from_map(m.get('OriginalDnsServers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyHichinaDomainDNSResponseBodyOriginalDnsServers(DaraModel):
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

class ModifyHichinaDomainDNSResponseBodyNewDnsServers(DaraModel):
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

