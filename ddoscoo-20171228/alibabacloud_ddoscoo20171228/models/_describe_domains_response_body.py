# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeDomainsResponseBodyDomains] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.domains = domains
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.DescribeDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        black_list: List[str] = None,
        cc_enabled: bool = None,
        cc_rule_enabled: bool = None,
        cc_template: str = None,
        cert_name: str = None,
        cert_region: str = None,
        cname: str = None,
        domain: str = None,
        http_2enable: bool = None,
        proxy_type_list: List[main_models.DescribeDomainsResponseBodyDomainsProxyTypeList] = None,
        real_servers: List[main_models.DescribeDomainsResponseBodyDomainsRealServers] = None,
        ssl_ciphers: str = None,
        ssl_protocols: str = None,
        white_list: List[str] = None,
    ):
        self.black_list = black_list
        self.cc_enabled = cc_enabled
        self.cc_rule_enabled = cc_rule_enabled
        self.cc_template = cc_template
        self.cert_name = cert_name
        self.cert_region = cert_region
        self.cname = cname
        self.domain = domain
        self.http_2enable = http_2enable
        self.proxy_type_list = proxy_type_list
        self.real_servers = real_servers
        self.ssl_ciphers = ssl_ciphers
        self.ssl_protocols = ssl_protocols
        self.white_list = white_list

    def validate(self):
        if self.proxy_type_list:
            for v1 in self.proxy_type_list:
                 if v1:
                    v1.validate()
        if self.real_servers:
            for v1 in self.real_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list is not None:
            result['BlackList'] = self.black_list

        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled

        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled

        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable

        result['ProxyTypeList'] = []
        if self.proxy_type_list is not None:
            for k1 in self.proxy_type_list:
                result['ProxyTypeList'].append(k1.to_map() if k1 else None)

        result['RealServers'] = []
        if self.real_servers is not None:
            for k1 in self.real_servers:
                result['RealServers'].append(k1.to_map() if k1 else None)

        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers

        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')

        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')

        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')

        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')

        self.proxy_type_list = []
        if m.get('ProxyTypeList') is not None:
            for k1 in m.get('ProxyTypeList'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsProxyTypeList()
                self.proxy_type_list.append(temp_model.from_map(k1))

        self.real_servers = []
        if m.get('RealServers') is not None:
            for k1 in m.get('RealServers'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsRealServers()
                self.real_servers.append(temp_model.from_map(k1))

        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')

        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class DescribeDomainsResponseBodyDomainsRealServers(DaraModel):
    def __init__(
        self,
        real_server: str = None,
        rs_type: int = None,
    ):
        self.real_server = real_server
        self.rs_type = rs_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.real_server is not None:
            result['RealServer'] = self.real_server

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        return self

class DescribeDomainsResponseBodyDomainsProxyTypeList(DaraModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        return self

