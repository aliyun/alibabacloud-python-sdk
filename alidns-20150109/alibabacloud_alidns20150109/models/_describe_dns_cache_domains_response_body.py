# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsCacheDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeDnsCacheDomainsResponseBodyDomains] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names.
        self.domains = domains
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.DescribeDnsCacheDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDnsCacheDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        cache_ttl_max: int = None,
        cache_ttl_min: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        domain_id: str = None,
        domain_name: str = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        instance_id: str = None,
        remark: str = None,
        source_dns_servers: List[main_models.DescribeDnsCacheDomainsResponseBodyDomainsSourceDnsServers] = None,
        source_edns: str = None,
        source_protocol: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        version_code: str = None,
    ):
        # The maximum time-to-live (TTL) period of the cached data retrieved from the origin DNS server. Unit: seconds. Valid values: 30 to 86400.
        self.cache_ttl_max = cache_ttl_max
        # The minimum TTL period of the cached data retrieved from the origin DNS server. Unit: seconds. Valid values: 30 to 86400.
        self.cache_ttl_min = cache_ttl_min
        # The time when the domain name was added. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the domain name was added. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The ID of the cache-accelerated domain name.
        self.domain_id = domain_id
        # The cache-accelerated domain name.
        self.domain_name = domain_name
        # The time when the instance expires. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The time when the instance expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expire_timestamp = expire_timestamp
        # The instance ID of the cache-accelerated domain name.
        self.instance_id = instance_id
        # The description of the domain name.
        self.remark = remark
        # The origin DNS servers.
        self.source_dns_servers = source_dns_servers
        # Specifies whether the origin Domain Name System (DNS) server supports Extension Mechanisms for DNS (EDNS). Valid values: NOT_SUPPORT and SUPPORT.
        self.source_edns = source_edns
        # The origin protocol policy. Valid values: TCP and UDP. Default value: UDP.
        self.source_protocol = source_protocol
        # The time when the configurations of the domain name were updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the configurations of the domain name were updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The edition code of Alibaba Cloud DNS.
        self.version_code = version_code

    def validate(self):
        if self.source_dns_servers:
            for v1 in self.source_dns_servers:
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        result['SourceDnsServers'] = []
        if self.source_dns_servers is not None:
            for k1 in self.source_dns_servers:
                result['SourceDnsServers'].append(k1.to_map() if k1 else None)

        if self.source_edns is not None:
            result['SourceEdns'] = self.source_edns

        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheTtlMax') is not None:
            self.cache_ttl_max = m.get('CacheTtlMax')

        if m.get('CacheTtlMin') is not None:
            self.cache_ttl_min = m.get('CacheTtlMin')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        self.source_dns_servers = []
        if m.get('SourceDnsServers') is not None:
            for k1 in m.get('SourceDnsServers'):
                temp_model = main_models.DescribeDnsCacheDomainsResponseBodyDomainsSourceDnsServers()
                self.source_dns_servers.append(temp_model.from_map(k1))

        if m.get('SourceEdns') is not None:
            self.source_edns = m.get('SourceEdns')

        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class DescribeDnsCacheDomainsResponseBodyDomainsSourceDnsServers(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        # The domain name or IP address of the origin DNS server.
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

