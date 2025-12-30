# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainNsResponseBody(DaraModel):
    def __init__(
        self,
        all_ali_dns: bool = None,
        detect_failed_reason_code: str = None,
        dns_servers: main_models.DescribeDomainNsResponseBodyDnsServers = None,
        expect_dns_servers: main_models.DescribeDomainNsResponseBodyExpectDnsServers = None,
        include_ali_dns: bool = None,
        request_id: str = None,
    ):
        # Indicates whether all the name servers are Alibaba Cloud DNS servers.
        self.all_ali_dns = all_ali_dns
        # The cause code of the detection failure.
        self.detect_failed_reason_code = detect_failed_reason_code
        # The DNS server names configured for the domain name.
        self.dns_servers = dns_servers
        # The Domain Name System (DNS) server names assigned by Alibaba Cloud DNS.
        self.expect_dns_servers = expect_dns_servers
        # Indicates whether the name servers include Alibaba Cloud DNS servers.
        self.include_ali_dns = include_ali_dns
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dns_servers:
            self.dns_servers.validate()
        if self.expect_dns_servers:
            self.expect_dns_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_ali_dns is not None:
            result['AllAliDns'] = self.all_ali_dns

        if self.detect_failed_reason_code is not None:
            result['DetectFailedReasonCode'] = self.detect_failed_reason_code

        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()

        if self.expect_dns_servers is not None:
            result['ExpectDnsServers'] = self.expect_dns_servers.to_map()

        if self.include_ali_dns is not None:
            result['IncludeAliDns'] = self.include_ali_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllAliDns') is not None:
            self.all_ali_dns = m.get('AllAliDns')

        if m.get('DetectFailedReasonCode') is not None:
            self.detect_failed_reason_code = m.get('DetectFailedReasonCode')

        if m.get('DnsServers') is not None:
            temp_model = main_models.DescribeDomainNsResponseBodyDnsServers()
            self.dns_servers = temp_model.from_map(m.get('DnsServers'))

        if m.get('ExpectDnsServers') is not None:
            temp_model = main_models.DescribeDomainNsResponseBodyExpectDnsServers()
            self.expect_dns_servers = temp_model.from_map(m.get('ExpectDnsServers'))

        if m.get('IncludeAliDns') is not None:
            self.include_ali_dns = m.get('IncludeAliDns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainNsResponseBodyExpectDnsServers(DaraModel):
    def __init__(
        self,
        expect_dns_server: List[str] = None,
    ):
        self.expect_dns_server = expect_dns_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expect_dns_server is not None:
            result['ExpectDnsServer'] = self.expect_dns_server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectDnsServer') is not None:
            self.expect_dns_server = m.get('ExpectDnsServer')

        return self

class DescribeDomainNsResponseBodyDnsServers(DaraModel):
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

