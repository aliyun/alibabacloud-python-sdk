# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateDnsCacheDomainRequest(DaraModel):
    def __init__(
        self,
        cache_ttl_max: int = None,
        cache_ttl_min: int = None,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        source_dns_server: List[main_models.UpdateDnsCacheDomainRequestSourceDnsServer] = None,
        source_edns: str = None,
        source_protocol: str = None,
    ):
        # The maximum TTL for cached data retrieved from the origin server. The value ranges from 30 to 86400.
        self.cache_ttl_max = cache_ttl_max
        # The minimum time-to-live (TTL) for cached data retrieved from the origin server. The value ranges from 30 to 86400.
        self.cache_ttl_min = cache_ttl_min
        # The domain name.<props="china"> To query the domain name, call [DescribeDomains](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c4g.11186623.help-menu-search-29697.d_0).
        # <props="intl">To query the domain name, call [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the authoritative proxy domain name instance.<props="china"> To query the instance ID, call [ListCloudGtmInstances](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-listcloudgtminstances?spm=a2c4g.11186623.help-menu-search-29697.d_0).
        # <props="intl">To query the instance ID, call [ListCloudGtmInstances](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-listcloudgtminstances?spm=a2c63.p38356.help-menu-search-29697.d_0).
        self.instance_id = instance_id
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        # 
        # **zh**
        self.lang = lang
        # A list of origin DNS servers. You can add up to 10 servers.
        self.source_dns_server = source_dns_server
        # Specifies whether the origin server supports Extension Mechanisms for DNS (EDNS).
        # SUPPORT: The origin server supports EDNS.
        # NOT_SUPPORT: The origin server does not support EDNS.
        self.source_edns = source_edns
        # The origin protocol. Valid values: TCP and UDP. Default value: UDP.
        self.source_protocol = source_protocol

    def validate(self):
        if self.source_dns_server:
            for v1 in self.source_dns_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_ttl_max is not None:
            result['CacheTtlMax'] = self.cache_ttl_max

        if self.cache_ttl_min is not None:
            result['CacheTtlMin'] = self.cache_ttl_min

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        result['SourceDnsServer'] = []
        if self.source_dns_server is not None:
            for k1 in self.source_dns_server:
                result['SourceDnsServer'].append(k1.to_map() if k1 else None)

        if self.source_edns is not None:
            result['SourceEdns'] = self.source_edns

        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTtlMax') is not None:
            self.cache_ttl_max = m.get('CacheTtlMax')

        if m.get('CacheTtlMin') is not None:
            self.cache_ttl_min = m.get('CacheTtlMin')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.source_dns_server = []
        if m.get('SourceDnsServer') is not None:
            for k1 in m.get('SourceDnsServer'):
                temp_model = main_models.UpdateDnsCacheDomainRequestSourceDnsServer()
                self.source_dns_server.append(temp_model.from_map(k1))

        if m.get('SourceEdns') is not None:
            self.source_edns = m.get('SourceEdns')

        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')

        return self

class UpdateDnsCacheDomainRequestSourceDnsServer(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        # The domain name or IP address of the origin server.
        self.host = host
        # The port of the origin DNS server.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

