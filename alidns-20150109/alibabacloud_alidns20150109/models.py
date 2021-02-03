# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class DescribeDnsCacheDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDnsCacheDomainsResponseDomainsSourceDnsServers(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = dict()
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


class DescribeDnsCacheDomainsResponseDomains(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
        instance_id: str = None,
        version_code: str = None,
        remark: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        cache_ttl_min: int = None,
        cache_ttl_max: int = None,
        source_protocol: str = None,
        source_edns: str = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        source_dns_servers: List[DescribeDnsCacheDomainsResponseDomainsSourceDnsServers] = None,
    ):
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.version_code = version_code
        self.remark = remark
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.cache_ttl_min = cache_ttl_min
        self.cache_ttl_max = cache_ttl_max
        self.source_protocol = source_protocol
        self.source_edns = source_edns
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.source_dns_servers = source_dns_servers

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.cache_ttl_min, 'cache_ttl_min')
        self.validate_required(self.cache_ttl_max, 'cache_ttl_max')
        self.validate_required(self.source_protocol, 'source_protocol')
        self.validate_required(self.source_edns, 'source_edns')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expire_timestamp, 'expire_timestamp')
        self.validate_required(self.source_dns_servers, 'source_dns_servers')
        if self.source_dns_servers:
            for k in self.source_dns_servers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.cache_ttl_min is not None:
            result['CacheTtlMin'] = self.cache_ttl_min
        if self.cache_ttl_max is not None:
            result['CacheTtlMax'] = self.cache_ttl_max
        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol
        if self.source_edns is not None:
            result['SourceEdns'] = self.source_edns
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        result['SourceDnsServers'] = []
        if self.source_dns_servers is not None:
            for k in self.source_dns_servers:
                result['SourceDnsServers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('CacheTtlMin') is not None:
            self.cache_ttl_min = m.get('CacheTtlMin')
        if m.get('CacheTtlMax') is not None:
            self.cache_ttl_max = m.get('CacheTtlMax')
        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')
        if m.get('SourceEdns') is not None:
            self.source_edns = m.get('SourceEdns')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        self.source_dns_servers = []
        if m.get('SourceDnsServers') is not None:
            for k in m.get('SourceDnsServers'):
                temp_model = DescribeDnsCacheDomainsResponseDomainsSourceDnsServers()
                self.source_dns_servers.append(temp_model.from_map(k))
        return self


class DescribeDnsCacheDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domains: List[DescribeDnsCacheDomainsResponseDomains] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domains = domains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDnsCacheDomainsResponseDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class UpdateDnsCacheDomainRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        remark: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.remark = remark

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateDnsCacheDomainRemarkResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDnsCacheDomainRequestSourceDnsServer(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
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


class UpdateDnsCacheDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        instance_id: str = None,
        cache_ttl_min: int = None,
        cache_ttl_max: int = None,
        source_protocol: str = None,
        source_edns: str = None,
        source_dns_server: List[UpdateDnsCacheDomainRequestSourceDnsServer] = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.cache_ttl_min = cache_ttl_min
        self.cache_ttl_max = cache_ttl_max
        self.source_protocol = source_protocol
        self.source_edns = source_edns
        self.source_dns_server = source_dns_server

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        if self.source_dns_server:
            for k in self.source_dns_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cache_ttl_min is not None:
            result['CacheTtlMin'] = self.cache_ttl_min
        if self.cache_ttl_max is not None:
            result['CacheTtlMax'] = self.cache_ttl_max
        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol
        if self.source_edns is not None:
            result['SourceEdns'] = self.source_edns
        result['SourceDnsServer'] = []
        if self.source_dns_server is not None:
            for k in self.source_dns_server:
                result['SourceDnsServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CacheTtlMin') is not None:
            self.cache_ttl_min = m.get('CacheTtlMin')
        if m.get('CacheTtlMax') is not None:
            self.cache_ttl_max = m.get('CacheTtlMax')
        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')
        if m.get('SourceEdns') is not None:
            self.source_edns = m.get('SourceEdns')
        self.source_dns_server = []
        if m.get('SourceDnsServer') is not None:
            for k in m.get('SourceDnsServer'):
                temp_model = UpdateDnsCacheDomainRequestSourceDnsServer()
                self.source_dns_server.append(temp_model.from_map(k))
        return self


class UpdateDnsCacheDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDnsCacheDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDnsCacheDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDnsCacheDomainRequestSourceDnsServer(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = dict()
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


class AddDnsCacheDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        instance_id: str = None,
        cache_ttl_min: int = None,
        cache_ttl_max: int = None,
        source_protocol: str = None,
        source_edns: str = None,
        remark: str = None,
        source_dns_server: List[AddDnsCacheDomainRequestSourceDnsServer] = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.instance_id = instance_id
        self.cache_ttl_min = cache_ttl_min
        self.cache_ttl_max = cache_ttl_max
        self.source_protocol = source_protocol
        self.source_edns = source_edns
        self.remark = remark
        self.source_dns_server = source_dns_server

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.cache_ttl_min, 'cache_ttl_min')
        self.validate_required(self.cache_ttl_max, 'cache_ttl_max')
        self.validate_required(self.source_protocol, 'source_protocol')
        self.validate_required(self.source_edns, 'source_edns')
        self.validate_required(self.source_dns_server, 'source_dns_server')
        if self.source_dns_server:
            for k in self.source_dns_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cache_ttl_min is not None:
            result['CacheTtlMin'] = self.cache_ttl_min
        if self.cache_ttl_max is not None:
            result['CacheTtlMax'] = self.cache_ttl_max
        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol
        if self.source_edns is not None:
            result['SourceEdns'] = self.source_edns
        if self.remark is not None:
            result['Remark'] = self.remark
        result['SourceDnsServer'] = []
        if self.source_dns_server is not None:
            for k in self.source_dns_server:
                result['SourceDnsServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CacheTtlMin') is not None:
            self.cache_ttl_min = m.get('CacheTtlMin')
        if m.get('CacheTtlMax') is not None:
            self.cache_ttl_max = m.get('CacheTtlMax')
        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')
        if m.get('SourceEdns') is not None:
            self.source_edns = m.get('SourceEdns')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.source_dns_server = []
        if m.get('SourceDnsServer') is not None:
            for k in m.get('SourceDnsServer'):
                temp_model = AddDnsCacheDomainRequestSourceDnsServer()
                self.source_dns_server.append(temp_model.from_map(k))
        return self


class AddDnsCacheDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDnsGtmMonitorAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodesIpv4IspCityNode(TeaModel):
    def __init__(
        self,
        isp_name: str = None,
        isp_code: str = None,
        city_name: str = None,
        city_code: str = None,
        default_selected: bool = None,
        group_type: str = None,
        group_name: str = None,
    ):
        self.isp_name = isp_name
        self.isp_code = isp_code
        self.city_name = city_name
        self.city_code = city_code
        self.default_selected = default_selected
        self.group_type = group_type
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.default_selected, 'default_selected')
        self.validate_required(self.group_type, 'group_type')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodes(TeaModel):
    def __init__(
        self,
        ipv_4isp_city_node: List[DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodesIpv4IspCityNode] = None,
    ):
        self.ipv_4isp_city_node = ipv_4isp_city_node

    def validate(self):
        self.validate_required(self.ipv_4isp_city_node, 'ipv_4isp_city_node')
        if self.ipv_4isp_city_node:
            for k in self.ipv_4isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Ipv4IspCityNode'] = []
        if self.ipv_4isp_city_node is not None:
            for k in self.ipv_4isp_city_node:
                result['Ipv4IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4isp_city_node = []
        if m.get('Ipv4IspCityNode') is not None:
            for k in m.get('Ipv4IspCityNode'):
                temp_model = DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodesIpv4IspCityNode()
                self.ipv_4isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodesIpv6IspCityNode(TeaModel):
    def __init__(
        self,
        isp_name: str = None,
        isp_code: str = None,
        city_name: str = None,
        city_code: str = None,
        default_selected: bool = None,
        group_type: str = None,
        group_name: str = None,
    ):
        self.isp_name = isp_name
        self.isp_code = isp_code
        self.city_name = city_name
        self.city_code = city_code
        self.default_selected = default_selected
        self.group_type = group_type
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.default_selected, 'default_selected')
        self.validate_required(self.group_type, 'group_type')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodes(TeaModel):
    def __init__(
        self,
        ipv_6isp_city_node: List[DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodesIpv6IspCityNode] = None,
    ):
        self.ipv_6isp_city_node = ipv_6isp_city_node

    def validate(self):
        self.validate_required(self.ipv_6isp_city_node, 'ipv_6isp_city_node')
        if self.ipv_6isp_city_node:
            for k in self.ipv_6isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Ipv6IspCityNode'] = []
        if self.ipv_6isp_city_node is not None:
            for k in self.ipv_6isp_city_node:
                result['Ipv6IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6isp_city_node = []
        if m.get('Ipv6IspCityNode') is not None:
            for k in m.get('Ipv6IspCityNode'):
                temp_model = DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodesIpv6IspCityNode()
                self.ipv_6isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodesDomainIpv4IspCityNode(TeaModel):
    def __init__(
        self,
        isp_name: str = None,
        isp_code: str = None,
        city_name: str = None,
        city_code: str = None,
        default_selected: bool = None,
        group_type: str = None,
        group_name: str = None,
    ):
        self.isp_name = isp_name
        self.isp_code = isp_code
        self.city_name = city_name
        self.city_code = city_code
        self.default_selected = default_selected
        self.group_type = group_type
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.default_selected, 'default_selected')
        self.validate_required(self.group_type, 'group_type')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodes(TeaModel):
    def __init__(
        self,
        domain_ipv_4isp_city_node: List[DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodesDomainIpv4IspCityNode] = None,
    ):
        self.domain_ipv_4isp_city_node = domain_ipv_4isp_city_node

    def validate(self):
        self.validate_required(self.domain_ipv_4isp_city_node, 'domain_ipv_4isp_city_node')
        if self.domain_ipv_4isp_city_node:
            for k in self.domain_ipv_4isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainIpv4IspCityNode'] = []
        if self.domain_ipv_4isp_city_node is not None:
            for k in self.domain_ipv_4isp_city_node:
                result['DomainIpv4IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_ipv_4isp_city_node = []
        if m.get('DomainIpv4IspCityNode') is not None:
            for k in m.get('DomainIpv4IspCityNode'):
                temp_model = DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodesDomainIpv4IspCityNode()
                self.domain_ipv_4isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodesDomainIpv6IspCityNode(TeaModel):
    def __init__(
        self,
        isp_name: str = None,
        isp_code: str = None,
        city_name: str = None,
        city_code: str = None,
        default_selected: bool = None,
        group_type: str = None,
        group_name: str = None,
    ):
        self.isp_name = isp_name
        self.isp_code = isp_code
        self.city_name = city_name
        self.city_code = city_code
        self.default_selected = default_selected
        self.group_type = group_type
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.default_selected, 'default_selected')
        self.validate_required(self.group_type, 'group_type')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodes(TeaModel):
    def __init__(
        self,
        domain_ipv_6isp_city_node: List[DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodesDomainIpv6IspCityNode] = None,
    ):
        self.domain_ipv_6isp_city_node = domain_ipv_6isp_city_node

    def validate(self):
        self.validate_required(self.domain_ipv_6isp_city_node, 'domain_ipv_6isp_city_node')
        if self.domain_ipv_6isp_city_node:
            for k in self.domain_ipv_6isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainIpv6IspCityNode'] = []
        if self.domain_ipv_6isp_city_node is not None:
            for k in self.domain_ipv_6isp_city_node:
                result['DomainIpv6IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_ipv_6isp_city_node = []
        if m.get('DomainIpv6IspCityNode') is not None:
            for k in m.get('DomainIpv6IspCityNode'):
                temp_model = DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodesDomainIpv6IspCityNode()
                self.domain_ipv_6isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmMonitorAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ipv_4isp_city_nodes: DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodes = None,
        ipv_6isp_city_nodes: DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodes = None,
        domain_ipv_4isp_city_nodes: DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodes = None,
        domain_ipv_6isp_city_nodes: DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodes = None,
    ):
        self.request_id = request_id
        self.ipv_4isp_city_nodes = ipv_4isp_city_nodes
        self.ipv_6isp_city_nodes = ipv_6isp_city_nodes
        self.domain_ipv_4isp_city_nodes = domain_ipv_4isp_city_nodes
        self.domain_ipv_6isp_city_nodes = domain_ipv_6isp_city_nodes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_4isp_city_nodes, 'ipv_4isp_city_nodes')
        if self.ipv_4isp_city_nodes:
            self.ipv_4isp_city_nodes.validate()
        self.validate_required(self.ipv_6isp_city_nodes, 'ipv_6isp_city_nodes')
        if self.ipv_6isp_city_nodes:
            self.ipv_6isp_city_nodes.validate()
        self.validate_required(self.domain_ipv_4isp_city_nodes, 'domain_ipv_4isp_city_nodes')
        if self.domain_ipv_4isp_city_nodes:
            self.domain_ipv_4isp_city_nodes.validate()
        self.validate_required(self.domain_ipv_6isp_city_nodes, 'domain_ipv_6isp_city_nodes')
        if self.domain_ipv_6isp_city_nodes:
            self.domain_ipv_6isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ipv_4isp_city_nodes is not None:
            result['Ipv4IspCityNodes'] = self.ipv_4isp_city_nodes.to_map()
        if self.ipv_6isp_city_nodes is not None:
            result['Ipv6IspCityNodes'] = self.ipv_6isp_city_nodes.to_map()
        if self.domain_ipv_4isp_city_nodes is not None:
            result['DomainIpv4IspCityNodes'] = self.domain_ipv_4isp_city_nodes.to_map()
        if self.domain_ipv_6isp_city_nodes is not None:
            result['DomainIpv6IspCityNodes'] = self.domain_ipv_6isp_city_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ipv4IspCityNodes') is not None:
            temp_model = DescribeDnsGtmMonitorAvailableConfigResponseIpv4IspCityNodes()
            self.ipv_4isp_city_nodes = temp_model.from_map(m['Ipv4IspCityNodes'])
        if m.get('Ipv6IspCityNodes') is not None:
            temp_model = DescribeDnsGtmMonitorAvailableConfigResponseIpv6IspCityNodes()
            self.ipv_6isp_city_nodes = temp_model.from_map(m['Ipv6IspCityNodes'])
        if m.get('DomainIpv4IspCityNodes') is not None:
            temp_model = DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv4IspCityNodes()
            self.domain_ipv_4isp_city_nodes = temp_model.from_map(m['DomainIpv4IspCityNodes'])
        if m.get('DomainIpv6IspCityNodes') is not None:
            temp_model = DescribeDnsGtmMonitorAvailableConfigResponseDomainIpv6IspCityNodes()
            self.domain_ipv_6isp_city_nodes = temp_model.from_map(m['DomainIpv6IspCityNodes'])
        return self


class UpdateDnsGtmMonitorRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class UpdateDnsGtmMonitorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[UpdateDnsGtmMonitorRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = UpdateDnsGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class UpdateDnsGtmMonitorResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDnsGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        return self


class DeleteDnsGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDnsGtmMonitorStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id
        self.status = status

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDnsGtmMonitorStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDnsGtmMonitorRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class AddDnsGtmMonitorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[AddDnsGtmMonitorRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.evaluation_count, 'evaluation_count')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = AddDnsGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class AddDnsGtmMonitorResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_config_id: str = None,
    ):
        self.request_id = request_id
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class DescribeDnsGtmInstancesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        keyword: str = None,
        resource_group_id: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.keyword = keyword
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDnsGtmInstancesResponseGtmInstancesConfigAlertConfig(TeaModel):
    def __init__(
        self,
        notice_type: str = None,
        sms_notice: str = None,
        email_notice: str = None,
    ):
        self.notice_type = notice_type
        self.sms_notice = sms_notice
        self.email_notice = email_notice

    def validate(self):
        self.validate_required(self.notice_type, 'notice_type')
        self.validate_required(self.sms_notice, 'sms_notice')
        self.validate_required(self.email_notice, 'email_notice')

    def to_map(self):
        result = dict()
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.sms_notice is not None:
            result['SmsNotice'] = self.sms_notice
        if self.email_notice is not None:
            result['EmailNotice'] = self.email_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')
        if m.get('EmailNotice') is not None:
            self.email_notice = m.get('EmailNotice')
        return self


class DescribeDnsGtmInstancesResponseGtmInstancesConfig(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        cname_type: str = None,
        public_user_domain_name: str = None,
        public_cname_mode: str = None,
        public_zone_name: str = None,
        ttl: int = None,
        alert_group: str = None,
        strategy_mode: str = None,
        alert_config: List[DescribeDnsGtmInstancesResponseGtmInstancesConfigAlertConfig] = None,
    ):
        self.instance_name = instance_name
        self.cname_type = cname_type
        self.public_user_domain_name = public_user_domain_name
        self.public_cname_mode = public_cname_mode
        self.public_zone_name = public_zone_name
        self.ttl = ttl
        self.alert_group = alert_group
        self.strategy_mode = strategy_mode
        self.alert_config = alert_config

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.public_user_domain_name, 'public_user_domain_name')
        self.validate_required(self.public_cname_mode, 'public_cname_mode')
        self.validate_required(self.public_zone_name, 'public_zone_name')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.alert_group, 'alert_group')
        self.validate_required(self.strategy_mode, 'strategy_mode')
        self.validate_required(self.alert_config, 'alert_config')
        if self.alert_config:
            for k in self.alert_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.cname_type is not None:
            result['CnameType'] = self.cname_type
        if self.public_user_domain_name is not None:
            result['PublicUserDomainName'] = self.public_user_domain_name
        if self.public_cname_mode is not None:
            result['PublicCnameMode'] = self.public_cname_mode
        if self.public_zone_name is not None:
            result['PublicZoneName'] = self.public_zone_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k in self.alert_config:
                result['AlertConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')
        if m.get('PublicUserDomainName') is not None:
            self.public_user_domain_name = m.get('PublicUserDomainName')
        if m.get('PublicCnameMode') is not None:
            self.public_cname_mode = m.get('PublicCnameMode')
        if m.get('PublicZoneName') is not None:
            self.public_zone_name = m.get('PublicZoneName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k in m.get('AlertConfig'):
                temp_model = DescribeDnsGtmInstancesResponseGtmInstancesConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmInstancesResponseGtmInstancesUsedQuota(TeaModel):
    def __init__(
        self,
        task_used_count: int = None,
        sms_used_count: int = None,
        email_used_count: int = None,
    ):
        self.task_used_count = task_used_count
        self.sms_used_count = sms_used_count
        self.email_used_count = email_used_count

    def validate(self):
        self.validate_required(self.task_used_count, 'task_used_count')
        self.validate_required(self.sms_used_count, 'sms_used_count')
        self.validate_required(self.email_used_count, 'email_used_count')

    def to_map(self):
        result = dict()
        if self.task_used_count is not None:
            result['TaskUsedCount'] = self.task_used_count
        if self.sms_used_count is not None:
            result['SmsUsedCount'] = self.sms_used_count
        if self.email_used_count is not None:
            result['EmailUsedCount'] = self.email_used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUsedCount') is not None:
            self.task_used_count = m.get('TaskUsedCount')
        if m.get('SmsUsedCount') is not None:
            self.sms_used_count = m.get('SmsUsedCount')
        if m.get('EmailUsedCount') is not None:
            self.email_used_count = m.get('EmailUsedCount')
        return self


class DescribeDnsGtmInstancesResponseGtmInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version_code: str = None,
        sms_quota: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        task_quota: int = None,
        resource_group_id: str = None,
        payment_type: str = None,
        config: DescribeDnsGtmInstancesResponseGtmInstancesConfig = None,
        used_quota: DescribeDnsGtmInstancesResponseGtmInstancesUsedQuota = None,
    ):
        self.instance_id = instance_id
        self.version_code = version_code
        self.sms_quota = sms_quota
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.task_quota = task_quota
        self.resource_group_id = resource_group_id
        self.payment_type = payment_type
        self.config = config
        self.used_quota = used_quota

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.sms_quota, 'sms_quota')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expire_timestamp, 'expire_timestamp')
        self.validate_required(self.task_quota, 'task_quota')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.payment_type, 'payment_type')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()
        self.validate_required(self.used_quota, 'used_quota')
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.sms_quota is not None:
            result['SmsQuota'] = self.sms_quota
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.task_quota is not None:
            result['TaskQuota'] = self.task_quota
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('SmsQuota') is not None:
            self.sms_quota = m.get('SmsQuota')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('TaskQuota') is not None:
            self.task_quota = m.get('TaskQuota')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Config') is not None:
            temp_model = DescribeDnsGtmInstancesResponseGtmInstancesConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('UsedQuota') is not None:
            temp_model = DescribeDnsGtmInstancesResponseGtmInstancesUsedQuota()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        return self


class DescribeDnsGtmInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_items: int = None,
        total_pages: int = None,
        gtm_instances: List[DescribeDnsGtmInstancesResponseGtmInstances] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_items = total_items
        self.total_pages = total_pages
        self.gtm_instances = gtm_instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.gtm_instances, 'gtm_instances')
        if self.gtm_instances:
            for k in self.gtm_instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['GtmInstances'] = []
        if self.gtm_instances is not None:
            for k in self.gtm_instances:
                result['GtmInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.gtm_instances = []
        if m.get('GtmInstances') is not None:
            for k in m.get('GtmInstances'):
                temp_model = DescribeDnsGtmInstancesResponseGtmInstances()
                self.gtm_instances.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmInstanceRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDnsGtmInstanceResponseConfigAlertConfigAlertConfig(TeaModel):
    def __init__(
        self,
        notice_type: str = None,
        sms_notice: bool = None,
        email_notice: bool = None,
    ):
        self.notice_type = notice_type
        self.sms_notice = sms_notice
        self.email_notice = email_notice

    def validate(self):
        self.validate_required(self.notice_type, 'notice_type')
        self.validate_required(self.sms_notice, 'sms_notice')
        self.validate_required(self.email_notice, 'email_notice')

    def to_map(self):
        result = dict()
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.sms_notice is not None:
            result['SmsNotice'] = self.sms_notice
        if self.email_notice is not None:
            result['EmailNotice'] = self.email_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')
        if m.get('EmailNotice') is not None:
            self.email_notice = m.get('EmailNotice')
        return self


class DescribeDnsGtmInstanceResponseConfigAlertConfig(TeaModel):
    def __init__(
        self,
        alert_config: List[DescribeDnsGtmInstanceResponseConfigAlertConfigAlertConfig] = None,
    ):
        self.alert_config = alert_config

    def validate(self):
        self.validate_required(self.alert_config, 'alert_config')
        if self.alert_config:
            for k in self.alert_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k in self.alert_config:
                result['AlertConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k in m.get('AlertConfig'):
                temp_model = DescribeDnsGtmInstanceResponseConfigAlertConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmInstanceResponseConfig(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        cname_type: str = None,
        public_user_domain_name: str = None,
        public_cname_mode: str = None,
        pubic_zone_name: str = None,
        ttl: int = None,
        strategy_mode: str = None,
        alert_group: str = None,
        alert_config: DescribeDnsGtmInstanceResponseConfigAlertConfig = None,
    ):
        self.instance_name = instance_name
        self.cname_type = cname_type
        self.public_user_domain_name = public_user_domain_name
        self.public_cname_mode = public_cname_mode
        self.pubic_zone_name = pubic_zone_name
        self.ttl = ttl
        self.strategy_mode = strategy_mode
        self.alert_group = alert_group
        self.alert_config = alert_config

    def validate(self):
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.cname_type, 'cname_type')
        self.validate_required(self.public_user_domain_name, 'public_user_domain_name')
        self.validate_required(self.public_cname_mode, 'public_cname_mode')
        self.validate_required(self.pubic_zone_name, 'pubic_zone_name')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.strategy_mode, 'strategy_mode')
        self.validate_required(self.alert_group, 'alert_group')
        self.validate_required(self.alert_config, 'alert_config')
        if self.alert_config:
            self.alert_config.validate()

    def to_map(self):
        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.cname_type is not None:
            result['CnameType'] = self.cname_type
        if self.public_user_domain_name is not None:
            result['PublicUserDomainName'] = self.public_user_domain_name
        if self.public_cname_mode is not None:
            result['PublicCnameMode'] = self.public_cname_mode
        if self.pubic_zone_name is not None:
            result['PubicZoneName'] = self.pubic_zone_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')
        if m.get('PublicUserDomainName') is not None:
            self.public_user_domain_name = m.get('PublicUserDomainName')
        if m.get('PublicCnameMode') is not None:
            self.public_cname_mode = m.get('PublicCnameMode')
        if m.get('PubicZoneName') is not None:
            self.pubic_zone_name = m.get('PubicZoneName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertConfig') is not None:
            temp_model = DescribeDnsGtmInstanceResponseConfigAlertConfig()
            self.alert_config = temp_model.from_map(m['AlertConfig'])
        return self


class DescribeDnsGtmInstanceResponseUsedQuota(TeaModel):
    def __init__(
        self,
        task_used_count: int = None,
        sms_used_count: int = None,
        email_used_count: int = None,
    ):
        self.task_used_count = task_used_count
        self.sms_used_count = sms_used_count
        self.email_used_count = email_used_count

    def validate(self):
        self.validate_required(self.task_used_count, 'task_used_count')
        self.validate_required(self.sms_used_count, 'sms_used_count')
        self.validate_required(self.email_used_count, 'email_used_count')

    def to_map(self):
        result = dict()
        if self.task_used_count is not None:
            result['TaskUsedCount'] = self.task_used_count
        if self.sms_used_count is not None:
            result['SmsUsedCount'] = self.sms_used_count
        if self.email_used_count is not None:
            result['EmailUsedCount'] = self.email_used_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUsedCount') is not None:
            self.task_used_count = m.get('TaskUsedCount')
        if m.get('SmsUsedCount') is not None:
            self.sms_used_count = m.get('SmsUsedCount')
        if m.get('EmailUsedCount') is not None:
            self.email_used_count = m.get('EmailUsedCount')
        return self


class DescribeDnsGtmInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        version_code: str = None,
        sms_quota: int = None,
        task_quota: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        resource_group_id: str = None,
        payment_type: str = None,
        config: DescribeDnsGtmInstanceResponseConfig = None,
        used_quota: DescribeDnsGtmInstanceResponseUsedQuota = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.version_code = version_code
        self.sms_quota = sms_quota
        self.task_quota = task_quota
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.resource_group_id = resource_group_id
        self.payment_type = payment_type
        self.config = config
        self.used_quota = used_quota

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.sms_quota, 'sms_quota')
        self.validate_required(self.task_quota, 'task_quota')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expire_timestamp, 'expire_timestamp')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.payment_type, 'payment_type')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()
        self.validate_required(self.used_quota, 'used_quota')
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.sms_quota is not None:
            result['SmsQuota'] = self.sms_quota
        if self.task_quota is not None:
            result['TaskQuota'] = self.task_quota
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('SmsQuota') is not None:
            self.sms_quota = m.get('SmsQuota')
        if m.get('TaskQuota') is not None:
            self.task_quota = m.get('TaskQuota')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Config') is not None:
            temp_model = DescribeDnsGtmInstanceResponseConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('UsedQuota') is not None:
            temp_model = DescribeDnsGtmInstanceResponseUsedQuota()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        return self


class DescribeDnsGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeDnsGtmAccessStrategyResponseLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmAccessStrategyResponseLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeDnsGtmAccessStrategyResponseLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeDnsGtmAccessStrategyResponseLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyResponseDefaultAddrPoolsDefaultAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count
        self.lba_weight = lba_weight

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.lba_weight, 'lba_weight')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class DescribeDnsGtmAccessStrategyResponseDefaultAddrPools(TeaModel):
    def __init__(
        self,
        default_addr_pool: List[DescribeDnsGtmAccessStrategyResponseDefaultAddrPoolsDefaultAddrPool] = None,
    ):
        self.default_addr_pool = default_addr_pool

    def validate(self):
        self.validate_required(self.default_addr_pool, 'default_addr_pool')
        if self.default_addr_pool:
            for k in self.default_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DefaultAddrPool'] = []
        if self.default_addr_pool is not None:
            for k in self.default_addr_pool:
                result['DefaultAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_addr_pool = []
        if m.get('DefaultAddrPool') is not None:
            for k in m.get('DefaultAddrPool'):
                temp_model = DescribeDnsGtmAccessStrategyResponseDefaultAddrPoolsDefaultAddrPool()
                self.default_addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyResponseFailoverAddrPoolsFailoverAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count
        self.lba_weight = lba_weight

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.lba_weight, 'lba_weight')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class DescribeDnsGtmAccessStrategyResponseFailoverAddrPools(TeaModel):
    def __init__(
        self,
        failover_addr_pool: List[DescribeDnsGtmAccessStrategyResponseFailoverAddrPoolsFailoverAddrPool] = None,
    ):
        self.failover_addr_pool = failover_addr_pool

    def validate(self):
        self.validate_required(self.failover_addr_pool, 'failover_addr_pool')
        if self.failover_addr_pool:
            for k in self.failover_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FailoverAddrPool'] = []
        if self.failover_addr_pool is not None:
            for k in self.failover_addr_pool:
                result['FailoverAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failover_addr_pool = []
        if m.get('FailoverAddrPool') is not None:
            for k in m.get('FailoverAddrPool'):
                temp_model = DescribeDnsGtmAccessStrategyResponseFailoverAddrPoolsFailoverAddrPool()
                self.failover_addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        strategy_mode: str = None,
        instance_id: str = None,
        default_addr_pool_type: str = None,
        default_lba_strategy: str = None,
        default_min_available_addr_num: int = None,
        default_max_return_addr_num: int = None,
        default_latency_optimization: str = None,
        default_addr_pool_group_status: str = None,
        failover_addr_pool_type: str = None,
        failover_lba_strategy: str = None,
        failover_min_available_addr_num: int = None,
        failover_max_return_addr_num: int = None,
        failover_latency_optimization: str = None,
        failover_addr_pool_group_status: str = None,
        access_mode: str = None,
        effective_addr_pool_group_type: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        default_available_addr_num: int = None,
        failover_available_addr_num: int = None,
        lines: DescribeDnsGtmAccessStrategyResponseLines = None,
        default_addr_pools: DescribeDnsGtmAccessStrategyResponseDefaultAddrPools = None,
        failover_addr_pools: DescribeDnsGtmAccessStrategyResponseFailoverAddrPools = None,
    ):
        self.request_id = request_id
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.strategy_mode = strategy_mode
        self.instance_id = instance_id
        self.default_addr_pool_type = default_addr_pool_type
        self.default_lba_strategy = default_lba_strategy
        self.default_min_available_addr_num = default_min_available_addr_num
        self.default_max_return_addr_num = default_max_return_addr_num
        self.default_latency_optimization = default_latency_optimization
        self.default_addr_pool_group_status = default_addr_pool_group_status
        self.failover_addr_pool_type = failover_addr_pool_type
        self.failover_lba_strategy = failover_lba_strategy
        self.failover_min_available_addr_num = failover_min_available_addr_num
        self.failover_max_return_addr_num = failover_max_return_addr_num
        self.failover_latency_optimization = failover_latency_optimization
        self.failover_addr_pool_group_status = failover_addr_pool_group_status
        self.access_mode = access_mode
        self.effective_addr_pool_group_type = effective_addr_pool_group_type
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.default_available_addr_num = default_available_addr_num
        self.failover_available_addr_num = failover_available_addr_num
        self.lines = lines
        self.default_addr_pools = default_addr_pools
        self.failover_addr_pools = failover_addr_pools

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.strategy_mode, 'strategy_mode')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.default_addr_pool_type, 'default_addr_pool_type')
        self.validate_required(self.default_lba_strategy, 'default_lba_strategy')
        self.validate_required(self.default_min_available_addr_num, 'default_min_available_addr_num')
        self.validate_required(self.default_max_return_addr_num, 'default_max_return_addr_num')
        self.validate_required(self.default_latency_optimization, 'default_latency_optimization')
        self.validate_required(self.default_addr_pool_group_status, 'default_addr_pool_group_status')
        self.validate_required(self.failover_addr_pool_type, 'failover_addr_pool_type')
        self.validate_required(self.failover_lba_strategy, 'failover_lba_strategy')
        self.validate_required(self.failover_min_available_addr_num, 'failover_min_available_addr_num')
        self.validate_required(self.failover_max_return_addr_num, 'failover_max_return_addr_num')
        self.validate_required(self.failover_latency_optimization, 'failover_latency_optimization')
        self.validate_required(self.failover_addr_pool_group_status, 'failover_addr_pool_group_status')
        self.validate_required(self.access_mode, 'access_mode')
        self.validate_required(self.effective_addr_pool_group_type, 'effective_addr_pool_group_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.default_available_addr_num, 'default_available_addr_num')
        self.validate_required(self.failover_available_addr_num, 'failover_available_addr_num')
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()
        self.validate_required(self.default_addr_pools, 'default_addr_pools')
        if self.default_addr_pools:
            self.default_addr_pools.validate()
        self.validate_required(self.failover_addr_pools, 'failover_addr_pools')
        if self.failover_addr_pools:
            self.failover_addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.default_addr_pool_type is not None:
            result['DefaultAddrPoolType'] = self.default_addr_pool_type
        if self.default_lba_strategy is not None:
            result['DefaultLbaStrategy'] = self.default_lba_strategy
        if self.default_min_available_addr_num is not None:
            result['DefaultMinAvailableAddrNum'] = self.default_min_available_addr_num
        if self.default_max_return_addr_num is not None:
            result['DefaultMaxReturnAddrNum'] = self.default_max_return_addr_num
        if self.default_latency_optimization is not None:
            result['DefaultLatencyOptimization'] = self.default_latency_optimization
        if self.default_addr_pool_group_status is not None:
            result['DefaultAddrPoolGroupStatus'] = self.default_addr_pool_group_status
        if self.failover_addr_pool_type is not None:
            result['FailoverAddrPoolType'] = self.failover_addr_pool_type
        if self.failover_lba_strategy is not None:
            result['FailoverLbaStrategy'] = self.failover_lba_strategy
        if self.failover_min_available_addr_num is not None:
            result['FailoverMinAvailableAddrNum'] = self.failover_min_available_addr_num
        if self.failover_max_return_addr_num is not None:
            result['FailoverMaxReturnAddrNum'] = self.failover_max_return_addr_num
        if self.failover_latency_optimization is not None:
            result['FailoverLatencyOptimization'] = self.failover_latency_optimization
        if self.failover_addr_pool_group_status is not None:
            result['FailoverAddrPoolGroupStatus'] = self.failover_addr_pool_group_status
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.effective_addr_pool_group_type is not None:
            result['EffectiveAddrPoolGroupType'] = self.effective_addr_pool_group_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.default_available_addr_num is not None:
            result['DefaultAvailableAddrNum'] = self.default_available_addr_num
        if self.failover_available_addr_num is not None:
            result['FailoverAvailableAddrNum'] = self.failover_available_addr_num
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        if self.default_addr_pools is not None:
            result['DefaultAddrPools'] = self.default_addr_pools.to_map()
        if self.failover_addr_pools is not None:
            result['FailoverAddrPools'] = self.failover_addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DefaultAddrPoolType') is not None:
            self.default_addr_pool_type = m.get('DefaultAddrPoolType')
        if m.get('DefaultLbaStrategy') is not None:
            self.default_lba_strategy = m.get('DefaultLbaStrategy')
        if m.get('DefaultMinAvailableAddrNum') is not None:
            self.default_min_available_addr_num = m.get('DefaultMinAvailableAddrNum')
        if m.get('DefaultMaxReturnAddrNum') is not None:
            self.default_max_return_addr_num = m.get('DefaultMaxReturnAddrNum')
        if m.get('DefaultLatencyOptimization') is not None:
            self.default_latency_optimization = m.get('DefaultLatencyOptimization')
        if m.get('DefaultAddrPoolGroupStatus') is not None:
            self.default_addr_pool_group_status = m.get('DefaultAddrPoolGroupStatus')
        if m.get('FailoverAddrPoolType') is not None:
            self.failover_addr_pool_type = m.get('FailoverAddrPoolType')
        if m.get('FailoverLbaStrategy') is not None:
            self.failover_lba_strategy = m.get('FailoverLbaStrategy')
        if m.get('FailoverMinAvailableAddrNum') is not None:
            self.failover_min_available_addr_num = m.get('FailoverMinAvailableAddrNum')
        if m.get('FailoverMaxReturnAddrNum') is not None:
            self.failover_max_return_addr_num = m.get('FailoverMaxReturnAddrNum')
        if m.get('FailoverLatencyOptimization') is not None:
            self.failover_latency_optimization = m.get('FailoverLatencyOptimization')
        if m.get('FailoverAddrPoolGroupStatus') is not None:
            self.failover_addr_pool_group_status = m.get('FailoverAddrPoolGroupStatus')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('EffectiveAddrPoolGroupType') is not None:
            self.effective_addr_pool_group_type = m.get('EffectiveAddrPoolGroupType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('DefaultAvailableAddrNum') is not None:
            self.default_available_addr_num = m.get('DefaultAvailableAddrNum')
        if m.get('FailoverAvailableAddrNum') is not None:
            self.failover_available_addr_num = m.get('FailoverAvailableAddrNum')
        if m.get('Lines') is not None:
            temp_model = DescribeDnsGtmAccessStrategyResponseLines()
            self.lines = temp_model.from_map(m['Lines'])
        if m.get('DefaultAddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategyResponseDefaultAddrPools()
            self.default_addr_pools = temp_model.from_map(m['DefaultAddrPools'])
        if m.get('FailoverAddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategyResponseFailoverAddrPools()
            self.failover_addr_pools = temp_model.from_map(m['FailoverAddrPools'])
        return self


class DescribeDnsGtmAddrAttributeInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        type: str = None,
        addrs: str = None,
    ):
        self.lang = lang
        self.type = type
        self.addrs = addrs

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.addrs, 'addrs')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.addrs is not None:
            result['Addrs'] = self.addrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Addrs') is not None:
            self.addrs = m.get('Addrs')
        return self


class DescribeDnsGtmAddrAttributeInfoResponseAddrAddrAttributeInfo(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
        father_code: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name
        self.father_code = father_code

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.father_code, 'father_code')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        return self


class DescribeDnsGtmAddrAttributeInfoResponseAddrAddr(TeaModel):
    def __init__(
        self,
        addr: str = None,
        attribute_info: DescribeDnsGtmAddrAttributeInfoResponseAddrAddrAttributeInfo = None,
    ):
        self.addr = addr
        self.attribute_info = attribute_info

    def validate(self):
        self.validate_required(self.addr, 'addr')
        self.validate_required(self.attribute_info, 'attribute_info')
        if self.attribute_info:
            self.attribute_info.validate()

    def to_map(self):
        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('AttributeInfo') is not None:
            temp_model = DescribeDnsGtmAddrAttributeInfoResponseAddrAddrAttributeInfo()
            self.attribute_info = temp_model.from_map(m['AttributeInfo'])
        return self


class DescribeDnsGtmAddrAttributeInfoResponseAddr(TeaModel):
    def __init__(
        self,
        addr: List[DescribeDnsGtmAddrAttributeInfoResponseAddrAddr] = None,
    ):
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = DescribeDnsGtmAddrAttributeInfoResponseAddrAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAddrAttributeInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr: DescribeDnsGtmAddrAttributeInfoResponseAddr = None,
    ):
        self.request_id = request_id
        self.addr = addr

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr, 'addr')
        if self.addr:
            self.addr.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Addr') is not None:
            temp_model = DescribeDnsGtmAddrAttributeInfoResponseAddr()
            self.addr = temp_model.from_map(m['Addr'])
        return self


class DescribeDnsGtmLogsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        return self


class DescribeDnsGtmLogsResponseLogsLog(TeaModel):
    def __init__(
        self,
        oper_time: str = None,
        oper_action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        entity_name: str = None,
        oper_timestamp: int = None,
        id: int = None,
        content: str = None,
    ):
        self.oper_time = oper_time
        self.oper_action = oper_action
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.oper_timestamp = oper_timestamp
        self.id = id
        self.content = content

    def validate(self):
        self.validate_required(self.oper_time, 'oper_time')
        self.validate_required(self.oper_action, 'oper_action')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.entity_name, 'entity_name')
        self.validate_required(self.oper_timestamp, 'oper_timestamp')
        self.validate_required(self.id, 'id')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = dict()
        if self.oper_time is not None:
            result['OperTime'] = self.oper_time
        if self.oper_action is not None:
            result['OperAction'] = self.oper_action
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp
        if self.id is not None:
            result['Id'] = self.id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')
        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeDnsGtmLogsResponseLogs(TeaModel):
    def __init__(
        self,
        log: List[DescribeDnsGtmLogsResponseLogsLog] = None,
    ):
        self.log = log

    def validate(self):
        self.validate_required(self.log, 'log')
        if self.log:
            for k in self.log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Log'] = []
        if self.log is not None:
            for k in self.log:
                result['Log'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k in m.get('Log'):
                temp_model = DescribeDnsGtmLogsResponseLogsLog()
                self.log.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmLogsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        logs: DescribeDnsGtmLogsResponseLogs = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.logs = logs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.logs, 'logs')
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Logs') is not None:
            temp_model = DescribeDnsGtmLogsResponseLogs()
            self.logs = temp_model.from_map(m['Logs'])
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        strategy_mode: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.strategy_mode = strategy_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.strategy_mode, 'strategy_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPoolsIpv4AddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPools(TeaModel):
    def __init__(
        self,
        ipv_4addr_pool: List[DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPoolsIpv4AddrPool] = None,
    ):
        self.ipv_4addr_pool = ipv_4addr_pool

    def validate(self):
        self.validate_required(self.ipv_4addr_pool, 'ipv_4addr_pool')
        if self.ipv_4addr_pool:
            for k in self.ipv_4addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Ipv4AddrPool'] = []
        if self.ipv_4addr_pool is not None:
            for k in self.ipv_4addr_pool:
                result['Ipv4AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4addr_pool = []
        if m.get('Ipv4AddrPool') is not None:
            for k in m.get('Ipv4AddrPool'):
                temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPoolsIpv4AddrPool()
                self.ipv_4addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
        father_code: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name
        self.father_code = father_code

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.father_code, 'father_code')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeDnsGtmAccessStrategyAvailableConfigResponseLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPoolsIpv6AddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPools(TeaModel):
    def __init__(
        self,
        ipv_6addr_pool: List[DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPoolsIpv6AddrPool] = None,
    ):
        self.ipv_6addr_pool = ipv_6addr_pool

    def validate(self):
        self.validate_required(self.ipv_6addr_pool, 'ipv_6addr_pool')
        if self.ipv_6addr_pool:
            for k in self.ipv_6addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Ipv6AddrPool'] = []
        if self.ipv_6addr_pool is not None:
            for k in self.ipv_6addr_pool:
                result['Ipv6AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6addr_pool = []
        if m.get('Ipv6AddrPool') is not None:
            for k in m.get('Ipv6AddrPool'):
                temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPoolsIpv6AddrPool()
                self.ipv_6addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPoolsDomainAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPools(TeaModel):
    def __init__(
        self,
        domain_addr_pool: List[DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPoolsDomainAddrPool] = None,
    ):
        self.domain_addr_pool = domain_addr_pool

    def validate(self):
        self.validate_required(self.domain_addr_pool, 'domain_addr_pool')
        if self.domain_addr_pool:
            for k in self.domain_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainAddrPool'] = []
        if self.domain_addr_pool is not None:
            for k in self.domain_addr_pool:
                result['DomainAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_addr_pool = []
        if m.get('DomainAddrPool') is not None:
            for k in m.get('DomainAddrPool'):
                temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPoolsDomainAddrPool()
                self.domain_addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv4Lines(TeaModel):
    def __init__(
        self,
        selected_ipv_4line: List[str] = None,
    ):
        self.selected_ipv_4line = selected_ipv_4line

    def validate(self):
        self.validate_required(self.selected_ipv_4line, 'selected_ipv_4line')

    def to_map(self):
        result = dict()
        if self.selected_ipv_4line is not None:
            result['SelectedIpv4Line'] = self.selected_ipv_4line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedIpv4Line') is not None:
            self.selected_ipv_4line = m.get('SelectedIpv4Line')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv6Lines(TeaModel):
    def __init__(
        self,
        selected_ipv_6line: List[str] = None,
    ):
        self.selected_ipv_6line = selected_ipv_6line

    def validate(self):
        self.validate_required(self.selected_ipv_6line, 'selected_ipv_6line')

    def to_map(self):
        result = dict()
        if self.selected_ipv_6line is not None:
            result['SelectedIpv6Line'] = self.selected_ipv_6line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedIpv6Line') is not None:
            self.selected_ipv_6line = m.get('SelectedIpv6Line')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedDomainLines(TeaModel):
    def __init__(
        self,
        selected_domain_line: List[str] = None,
    ):
        self.selected_domain_line = selected_domain_line

    def validate(self):
        self.validate_required(self.selected_domain_line, 'selected_domain_line')

    def to_map(self):
        result = dict()
        if self.selected_domain_line is not None:
            result['SelectedDomainLine'] = self.selected_domain_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedDomainLine') is not None:
            self.selected_domain_line = m.get('SelectedDomainLine')
        return self


class DescribeDnsGtmAccessStrategyAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suggest_set_default_line: bool = None,
        ipv_4addr_pools: DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPools = None,
        lines: DescribeDnsGtmAccessStrategyAvailableConfigResponseLines = None,
        ipv_6addr_pools: DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPools = None,
        domain_addr_pools: DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPools = None,
        selected_ipv_4lines: DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv4Lines = None,
        selected_ipv_6lines: DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv6Lines = None,
        selected_domain_lines: DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedDomainLines = None,
    ):
        self.request_id = request_id
        self.suggest_set_default_line = suggest_set_default_line
        self.ipv_4addr_pools = ipv_4addr_pools
        self.lines = lines
        self.ipv_6addr_pools = ipv_6addr_pools
        self.domain_addr_pools = domain_addr_pools
        self.selected_ipv_4lines = selected_ipv_4lines
        self.selected_ipv_6lines = selected_ipv_6lines
        self.selected_domain_lines = selected_domain_lines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.suggest_set_default_line, 'suggest_set_default_line')
        self.validate_required(self.ipv_4addr_pools, 'ipv_4addr_pools')
        if self.ipv_4addr_pools:
            self.ipv_4addr_pools.validate()
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()
        self.validate_required(self.ipv_6addr_pools, 'ipv_6addr_pools')
        if self.ipv_6addr_pools:
            self.ipv_6addr_pools.validate()
        self.validate_required(self.domain_addr_pools, 'domain_addr_pools')
        if self.domain_addr_pools:
            self.domain_addr_pools.validate()
        self.validate_required(self.selected_ipv_4lines, 'selected_ipv_4lines')
        if self.selected_ipv_4lines:
            self.selected_ipv_4lines.validate()
        self.validate_required(self.selected_ipv_6lines, 'selected_ipv_6lines')
        if self.selected_ipv_6lines:
            self.selected_ipv_6lines.validate()
        self.validate_required(self.selected_domain_lines, 'selected_domain_lines')
        if self.selected_domain_lines:
            self.selected_domain_lines.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suggest_set_default_line is not None:
            result['SuggestSetDefaultLine'] = self.suggest_set_default_line
        if self.ipv_4addr_pools is not None:
            result['Ipv4AddrPools'] = self.ipv_4addr_pools.to_map()
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        if self.ipv_6addr_pools is not None:
            result['Ipv6AddrPools'] = self.ipv_6addr_pools.to_map()
        if self.domain_addr_pools is not None:
            result['DomainAddrPools'] = self.domain_addr_pools.to_map()
        if self.selected_ipv_4lines is not None:
            result['SelectedIpv4Lines'] = self.selected_ipv_4lines.to_map()
        if self.selected_ipv_6lines is not None:
            result['SelectedIpv6Lines'] = self.selected_ipv_6lines.to_map()
        if self.selected_domain_lines is not None:
            result['SelectedDomainLines'] = self.selected_domain_lines.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuggestSetDefaultLine') is not None:
            self.suggest_set_default_line = m.get('SuggestSetDefaultLine')
        if m.get('Ipv4AddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv4AddrPools()
            self.ipv_4addr_pools = temp_model.from_map(m['Ipv4AddrPools'])
        if m.get('Lines') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseLines()
            self.lines = temp_model.from_map(m['Lines'])
        if m.get('Ipv6AddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseIpv6AddrPools()
            self.ipv_6addr_pools = temp_model.from_map(m['Ipv6AddrPools'])
        if m.get('DomainAddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseDomainAddrPools()
            self.domain_addr_pools = temp_model.from_map(m['DomainAddrPools'])
        if m.get('SelectedIpv4Lines') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv4Lines()
            self.selected_ipv_4lines = temp_model.from_map(m['SelectedIpv4Lines'])
        if m.get('SelectedIpv6Lines') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedIpv6Lines()
            self.selected_ipv_6lines = temp_model.from_map(m['SelectedIpv6Lines'])
        if m.get('SelectedDomainLines') is not None:
            temp_model = DescribeDnsGtmAccessStrategyAvailableConfigResponseSelectedDomainLines()
            self.selected_domain_lines = temp_model.from_map(m['SelectedDomainLines'])
        return self


class DescribeDnsGtmInstanceAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        return self


class DescribeDnsGtmInstanceAddressPoolResponseAddrsAddr(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        addr: str = None,
        lba_weight: int = None,
        mode: str = None,
        alert_status: str = None,
        remark: str = None,
        attribute_info: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.addr = addr
        self.lba_weight = lba_weight
        self.mode = mode
        self.alert_status = alert_status
        self.remark = remark
        self.attribute_info = attribute_info

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.addr, 'addr')
        self.validate_required(self.lba_weight, 'lba_weight')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.alert_status, 'alert_status')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.attribute_info, 'attribute_info')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')
        return self


class DescribeDnsGtmInstanceAddressPoolResponseAddrs(TeaModel):
    def __init__(
        self,
        addr: List[DescribeDnsGtmInstanceAddressPoolResponseAddrsAddr] = None,
    ):
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = DescribeDnsGtmInstanceAddressPoolResponseAddrsAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmInstanceAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_pool_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        addr_count: int = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        type: str = None,
        lba_strategy: str = None,
        addrs: DescribeDnsGtmInstanceAddressPoolResponseAddrs = None,
    ):
        self.request_id = request_id
        self.addr_pool_id = addr_pool_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.addr_count = addr_count
        self.monitor_config_id = monitor_config_id
        self.monitor_status = monitor_status
        self.name = name
        self.type = type
        self.lba_strategy = lba_strategy
        self.addrs = addrs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.monitor_status, 'monitor_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.lba_strategy, 'lba_strategy')
        self.validate_required(self.addrs, 'addrs')
        if self.addrs:
            self.addrs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        if self.addrs is not None:
            result['Addrs'] = self.addrs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        if m.get('Addrs') is not None:
            temp_model = DescribeDnsGtmInstanceAddressPoolResponseAddrs()
            self.addrs = temp_model.from_map(m['Addrs'])
        return self


class DescribeDnsGtmAddressPoolAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfosAttributeInfo(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
        father_code: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name
        self.father_code = father_code

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.father_code, 'father_code')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        return self


class DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfos(TeaModel):
    def __init__(
        self,
        attribute_info: List[DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfosAttributeInfo] = None,
    ):
        self.attribute_info = attribute_info

    def validate(self):
        self.validate_required(self.attribute_info, 'attribute_info')
        if self.attribute_info:
            for k in self.attribute_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttributeInfo'] = []
        if self.attribute_info is not None:
            for k in self.attribute_info:
                result['AttributeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_info = []
        if m.get('AttributeInfo') is not None:
            for k in m.get('AttributeInfo'):
                temp_model = DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfosAttributeInfo()
                self.attribute_info.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAddressPoolAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        attribute_infos: DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfos = None,
    ):
        self.request_id = request_id
        self.attribute_infos = attribute_infos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.attribute_infos, 'attribute_infos')
        if self.attribute_infos:
            self.attribute_infos.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.attribute_infos is not None:
            result['AttributeInfos'] = self.attribute_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AttributeInfos') is not None:
            temp_model = DescribeDnsGtmAddressPoolAvailableConfigResponseAttributeInfos()
            self.attribute_infos = temp_model.from_map(m['AttributeInfos'])
        return self


class UpdateDnsGtmAddressPoolRequestAddr(TeaModel):
    def __init__(
        self,
        addr: str = None,
        lba_weight: int = None,
        mode: str = None,
        remark: str = None,
        attribute_info: str = None,
    ):
        self.addr = addr
        self.lba_weight = lba_weight
        self.mode = mode
        self.remark = remark
        self.attribute_info = attribute_info

    def validate(self):
        self.validate_required(self.addr, 'addr')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')
        return self


class UpdateDnsGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
        name: str = None,
        lba_strategy: str = None,
        addr: List[UpdateDnsGtmAddressPoolRequestAddr] = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id
        self.name = name
        self.lba_strategy = lba_strategy
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.lba_strategy, 'lba_strategy')
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.name is not None:
            result['Name'] = self.name
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = UpdateDnsGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class UpdateDnsGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig(TeaModel):
    def __init__(
        self,
        notice_type: str = None,
        sms_notice: bool = None,
        email_notice: bool = None,
    ):
        self.notice_type = notice_type
        self.sms_notice = sms_notice
        self.email_notice = email_notice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.sms_notice is not None:
            result['SmsNotice'] = self.sms_notice
        if self.email_notice is not None:
            result['EmailNotice'] = self.email_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('SmsNotice') is not None:
            self.sms_notice = m.get('SmsNotice')
        if m.get('EmailNotice') is not None:
            self.email_notice = m.get('EmailNotice')
        return self


class UpdateDnsGtmInstanceGlobalConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        instance_name: str = None,
        ttl: int = None,
        public_cname_mode: str = None,
        public_user_domain_name: str = None,
        public_zone_name: str = None,
        alert_group: str = None,
        cname_type: str = None,
        alert_config: List[UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig] = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.ttl = ttl
        self.public_cname_mode = public_cname_mode
        self.public_user_domain_name = public_user_domain_name
        self.public_zone_name = public_zone_name
        self.alert_group = alert_group
        self.cname_type = cname_type
        self.alert_config = alert_config

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        if self.alert_config:
            for k in self.alert_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.public_cname_mode is not None:
            result['PublicCnameMode'] = self.public_cname_mode
        if self.public_user_domain_name is not None:
            result['PublicUserDomainName'] = self.public_user_domain_name
        if self.public_zone_name is not None:
            result['PublicZoneName'] = self.public_zone_name
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.cname_type is not None:
            result['CnameType'] = self.cname_type
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k in self.alert_config:
                result['AlertConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('PublicCnameMode') is not None:
            self.public_cname_mode = m.get('PublicCnameMode')
        if m.get('PublicUserDomainName') is not None:
            self.public_user_domain_name = m.get('PublicUserDomainName')
        if m.get('PublicZoneName') is not None:
            self.public_zone_name = m.get('PublicZoneName')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('CnameType') is not None:
            self.cname_type = m.get('CnameType')
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k in m.get('AlertConfig'):
                temp_model = UpdateDnsGtmInstanceGlobalConfigRequestAlertConfig()
                self.alert_config.append(temp_model.from_map(k))
        return self


class UpdateDnsGtmInstanceGlobalConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDnsGtmAccessModeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
        access_mode: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id
        self.access_mode = access_mode

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class SetDnsGtmAccessModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDnsGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DeleteDnsGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchDnsGtmInstanceStrategyModeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        strategy_mode: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.strategy_mode = strategy_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.strategy_mode, 'strategy_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        return self


class SwitchDnsGtmInstanceStrategyModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDnsGtmAvailableAlertGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDnsGtmAvailableAlertGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_alert_group: str = None,
    ):
        self.request_id = request_id
        self.available_alert_group = available_alert_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_alert_group, 'available_alert_group')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_alert_group is not None:
            result['AvailableAlertGroup'] = self.available_alert_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableAlertGroup') is not None:
            self.available_alert_group = m.get('AvailableAlertGroup')
        return self


class AddDnsGtmAccessStrategyRequestDefaultAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class AddDnsGtmAccessStrategyRequestFailoverAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class AddDnsGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        strategy_name: str = None,
        lines: str = None,
        default_addr_pool_type: str = None,
        default_lba_strategy: str = None,
        default_min_available_addr_num: int = None,
        default_max_return_addr_num: int = None,
        default_latency_optimization: str = None,
        failover_addr_pool_type: str = None,
        failover_lba_strategy: str = None,
        failover_min_available_addr_num: int = None,
        failover_max_return_addr_num: int = None,
        failover_latency_optimization: str = None,
        default_addr_pool: List[AddDnsGtmAccessStrategyRequestDefaultAddrPool] = None,
        failover_addr_pool: List[AddDnsGtmAccessStrategyRequestFailoverAddrPool] = None,
        strategy_mode: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.strategy_name = strategy_name
        self.lines = lines
        self.default_addr_pool_type = default_addr_pool_type
        self.default_lba_strategy = default_lba_strategy
        self.default_min_available_addr_num = default_min_available_addr_num
        self.default_max_return_addr_num = default_max_return_addr_num
        self.default_latency_optimization = default_latency_optimization
        self.failover_addr_pool_type = failover_addr_pool_type
        self.failover_lba_strategy = failover_lba_strategy
        self.failover_min_available_addr_num = failover_min_available_addr_num
        self.failover_max_return_addr_num = failover_max_return_addr_num
        self.failover_latency_optimization = failover_latency_optimization
        self.default_addr_pool = default_addr_pool
        self.failover_addr_pool = failover_addr_pool
        self.strategy_mode = strategy_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.default_addr_pool_type, 'default_addr_pool_type')
        self.validate_required(self.default_min_available_addr_num, 'default_min_available_addr_num')
        self.validate_required(self.default_addr_pool, 'default_addr_pool')
        if self.default_addr_pool:
            for k in self.default_addr_pool:
                if k:
                    k.validate()
        if self.failover_addr_pool:
            for k in self.failover_addr_pool:
                if k:
                    k.validate()
        self.validate_required(self.strategy_mode, 'strategy_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.default_addr_pool_type is not None:
            result['DefaultAddrPoolType'] = self.default_addr_pool_type
        if self.default_lba_strategy is not None:
            result['DefaultLbaStrategy'] = self.default_lba_strategy
        if self.default_min_available_addr_num is not None:
            result['DefaultMinAvailableAddrNum'] = self.default_min_available_addr_num
        if self.default_max_return_addr_num is not None:
            result['DefaultMaxReturnAddrNum'] = self.default_max_return_addr_num
        if self.default_latency_optimization is not None:
            result['DefaultLatencyOptimization'] = self.default_latency_optimization
        if self.failover_addr_pool_type is not None:
            result['FailoverAddrPoolType'] = self.failover_addr_pool_type
        if self.failover_lba_strategy is not None:
            result['FailoverLbaStrategy'] = self.failover_lba_strategy
        if self.failover_min_available_addr_num is not None:
            result['FailoverMinAvailableAddrNum'] = self.failover_min_available_addr_num
        if self.failover_max_return_addr_num is not None:
            result['FailoverMaxReturnAddrNum'] = self.failover_max_return_addr_num
        if self.failover_latency_optimization is not None:
            result['FailoverLatencyOptimization'] = self.failover_latency_optimization
        result['DefaultAddrPool'] = []
        if self.default_addr_pool is not None:
            for k in self.default_addr_pool:
                result['DefaultAddrPool'].append(k.to_map() if k else None)
        result['FailoverAddrPool'] = []
        if self.failover_addr_pool is not None:
            for k in self.failover_addr_pool:
                result['FailoverAddrPool'].append(k.to_map() if k else None)
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('DefaultAddrPoolType') is not None:
            self.default_addr_pool_type = m.get('DefaultAddrPoolType')
        if m.get('DefaultLbaStrategy') is not None:
            self.default_lba_strategy = m.get('DefaultLbaStrategy')
        if m.get('DefaultMinAvailableAddrNum') is not None:
            self.default_min_available_addr_num = m.get('DefaultMinAvailableAddrNum')
        if m.get('DefaultMaxReturnAddrNum') is not None:
            self.default_max_return_addr_num = m.get('DefaultMaxReturnAddrNum')
        if m.get('DefaultLatencyOptimization') is not None:
            self.default_latency_optimization = m.get('DefaultLatencyOptimization')
        if m.get('FailoverAddrPoolType') is not None:
            self.failover_addr_pool_type = m.get('FailoverAddrPoolType')
        if m.get('FailoverLbaStrategy') is not None:
            self.failover_lba_strategy = m.get('FailoverLbaStrategy')
        if m.get('FailoverMinAvailableAddrNum') is not None:
            self.failover_min_available_addr_num = m.get('FailoverMinAvailableAddrNum')
        if m.get('FailoverMaxReturnAddrNum') is not None:
            self.failover_max_return_addr_num = m.get('FailoverMaxReturnAddrNum')
        if m.get('FailoverLatencyOptimization') is not None:
            self.failover_latency_optimization = m.get('FailoverLatencyOptimization')
        self.default_addr_pool = []
        if m.get('DefaultAddrPool') is not None:
            for k in m.get('DefaultAddrPool'):
                temp_model = AddDnsGtmAccessStrategyRequestDefaultAddrPool()
                self.default_addr_pool.append(temp_model.from_map(k))
        self.failover_addr_pool = []
        if m.get('FailoverAddrPool') is not None:
            for k in m.get('FailoverAddrPool'):
                temp_model = AddDnsGtmAccessStrategyRequestFailoverAddrPool()
                self.failover_addr_pool.append(temp_model.from_map(k))
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        return self


class AddDnsGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_id: str = None,
    ):
        self.request_id = request_id
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeDnsGtmAccessStrategiesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        strategy_mode: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.strategy_mode = strategy_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.strategy_mode, 'strategy_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        addr_count: int = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.name = name
        self.addr_count = addr_count
        self.lba_weight = lba_weight

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.lba_weight, 'lba_weight')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPools(TeaModel):
    def __init__(
        self,
        effective_addr_pool: List[DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool] = None,
    ):
        self.effective_addr_pool = effective_addr_pool

    def validate(self):
        self.validate_required(self.effective_addr_pool, 'effective_addr_pool')
        if self.effective_addr_pool:
            for k in self.effective_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EffectiveAddrPool'] = []
        if self.effective_addr_pool is not None:
            for k in self.effective_addr_pool:
                result['EffectiveAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_addr_pool = []
        if m.get('EffectiveAddrPool') is not None:
            for k in m.get('EffectiveAddrPool'):
                temp_model = DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPoolsEffectiveAddrPool()
                self.effective_addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategiesStrategy(TeaModel):
    def __init__(
        self,
        strategy_id: str = None,
        strategy_name: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        effective_addr_pool_group_type: str = None,
        effective_addr_pool_type: str = None,
        effective_lba_strategy: str = None,
        lines: DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLines = None,
        effective_addr_pools: DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPools = None,
    ):
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.effective_addr_pool_group_type = effective_addr_pool_group_type
        self.effective_addr_pool_type = effective_addr_pool_type
        self.effective_lba_strategy = effective_lba_strategy
        self.lines = lines
        self.effective_addr_pools = effective_addr_pools

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.effective_addr_pool_group_type, 'effective_addr_pool_group_type')
        self.validate_required(self.effective_addr_pool_type, 'effective_addr_pool_type')
        self.validate_required(self.effective_lba_strategy, 'effective_lba_strategy')
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()
        self.validate_required(self.effective_addr_pools, 'effective_addr_pools')
        if self.effective_addr_pools:
            self.effective_addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.effective_addr_pool_group_type is not None:
            result['EffectiveAddrPoolGroupType'] = self.effective_addr_pool_group_type
        if self.effective_addr_pool_type is not None:
            result['EffectiveAddrPoolType'] = self.effective_addr_pool_type
        if self.effective_lba_strategy is not None:
            result['EffectiveLbaStrategy'] = self.effective_lba_strategy
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        if self.effective_addr_pools is not None:
            result['EffectiveAddrPools'] = self.effective_addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('EffectiveAddrPoolGroupType') is not None:
            self.effective_addr_pool_group_type = m.get('EffectiveAddrPoolGroupType')
        if m.get('EffectiveAddrPoolType') is not None:
            self.effective_addr_pool_type = m.get('EffectiveAddrPoolType')
        if m.get('EffectiveLbaStrategy') is not None:
            self.effective_lba_strategy = m.get('EffectiveLbaStrategy')
        if m.get('Lines') is not None:
            temp_model = DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyLines()
            self.lines = temp_model.from_map(m['Lines'])
        if m.get('EffectiveAddrPools') is not None:
            temp_model = DescribeDnsGtmAccessStrategiesResponseStrategiesStrategyEffectiveAddrPools()
            self.effective_addr_pools = temp_model.from_map(m['EffectiveAddrPools'])
        return self


class DescribeDnsGtmAccessStrategiesResponseStrategies(TeaModel):
    def __init__(
        self,
        strategy: List[DescribeDnsGtmAccessStrategiesResponseStrategiesStrategy] = None,
    ):
        self.strategy = strategy

    def validate(self):
        self.validate_required(self.strategy, 'strategy')
        if self.strategy:
            for k in self.strategy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Strategy'] = []
        if self.strategy is not None:
            for k in self.strategy:
                result['Strategy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.strategy = []
        if m.get('Strategy') is not None:
            for k in m.get('Strategy'):
                temp_model = DescribeDnsGtmAccessStrategiesResponseStrategiesStrategy()
                self.strategy.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmAccessStrategiesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_number: int = None,
        page_size: int = None,
        strategies: DescribeDnsGtmAccessStrategiesResponseStrategies = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_number = page_number
        self.page_size = page_size
        self.strategies = strategies

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.strategies, 'strategies')
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Strategies') is not None:
            temp_model = DescribeDnsGtmAccessStrategiesResponseStrategies()
            self.strategies = temp_model.from_map(m['Strategies'])
        return self


class DescribeDnsGtmInstanceAddressPoolsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDnsGtmInstanceAddressPoolsResponseAddrPoolsAddrPool(TeaModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        addr_count: int = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        type: str = None,
        lba_strategy: str = None,
    ):
        self.addr_pool_id = addr_pool_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.addr_count = addr_count
        self.monitor_config_id = monitor_config_id
        self.monitor_status = monitor_status
        self.name = name
        self.type = type
        self.lba_strategy = lba_strategy

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.monitor_status, 'monitor_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.lba_strategy, 'lba_strategy')

    def to_map(self):
        result = dict()
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        return self


class DescribeDnsGtmInstanceAddressPoolsResponseAddrPools(TeaModel):
    def __init__(
        self,
        addr_pool: List[DescribeDnsGtmInstanceAddressPoolsResponseAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        self.validate_required(self.addr_pool, 'addr_pool')
        if self.addr_pool:
            for k in self.addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k in self.addr_pool:
                result['AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k in m.get('AddrPool'):
                temp_model = DescribeDnsGtmInstanceAddressPoolsResponseAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmInstanceAddressPoolsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_number: int = None,
        page_size: int = None,
        addr_pools: DescribeDnsGtmInstanceAddressPoolsResponseAddrPools = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_number = page_number
        self.page_size = page_size
        self.addr_pools = addr_pools

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.addr_pools, 'addr_pools')
        if self.addr_pools:
            self.addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AddrPools') is not None:
            temp_model = DescribeDnsGtmInstanceAddressPoolsResponseAddrPools()
            self.addr_pools = temp_model.from_map(m['AddrPools'])
        return self


class AddDnsGtmAddressPoolRequestAddr(TeaModel):
    def __init__(
        self,
        addr: str = None,
        lba_weight: int = None,
        mode: str = None,
        remark: str = None,
        attribute_info: str = None,
    ):
        self.addr = addr
        self.lba_weight = lba_weight
        self.mode = mode
        self.remark = remark
        self.attribute_info = attribute_info

    def validate(self):
        self.validate_required(self.addr, 'addr')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.attribute_info, 'attribute_info')

    def to_map(self):
        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')
        return self


class AddDnsGtmAddressPoolRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class AddDnsGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
        lba_strategy: str = None,
        addr: List[AddDnsGtmAddressPoolRequestAddr] = None,
        monitor_status: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[AddDnsGtmAddressPoolRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.name = name
        self.type = type
        self.lba_strategy = lba_strategy
        self.addr = addr
        self.monitor_status = monitor_status
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.lba_strategy, 'lba_strategy')
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = AddDnsGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k))
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = AddDnsGtmAddressPoolRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class AddDnsGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_pool_id: str = None,
        monitor_config_id: str = None,
    ):
        self.request_id = request_id
        self.addr_pool_id = addr_pool_id
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class DescribeDnsGtmMonitorConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class DescribeDnsGtmMonitorConfigResponseIspCityNodesIspCityNode(TeaModel):
    def __init__(
        self,
        country_name: str = None,
        country_code: str = None,
        city_name: str = None,
        city_code: str = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        self.country_name = country_name
        self.country_code = country_code
        self.city_name = city_name
        self.city_code = city_code
        self.isp_code = isp_code
        self.isp_name = isp_name

    def validate(self):
        self.validate_required(self.country_name, 'country_name')
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.isp_name, 'isp_name')

    def to_map(self):
        result = dict()
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class DescribeDnsGtmMonitorConfigResponseIspCityNodes(TeaModel):
    def __init__(
        self,
        isp_city_node: List[DescribeDnsGtmMonitorConfigResponseIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = DescribeDnsGtmMonitorConfigResponseIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeDnsGtmMonitorConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_config_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_nodes: DescribeDnsGtmMonitorConfigResponseIspCityNodes = None,
    ):
        self.request_id = request_id
        self.monitor_config_id = monitor_config_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_nodes = isp_city_nodes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.evaluation_count, 'evaluation_count')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_nodes, 'isp_city_nodes')
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        if m.get('IspCityNodes') is not None:
            temp_model = DescribeDnsGtmMonitorConfigResponseIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m['IspCityNodes'])
        return self


class UpdateDnsGtmAccessStrategyRequestDefaultAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class UpdateDnsGtmAccessStrategyRequestFailoverAddrPool(TeaModel):
    def __init__(
        self,
        id: str = None,
        lba_weight: int = None,
    ):
        self.id = id
        self.lba_weight = lba_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        return self


class UpdateDnsGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        lines: str = None,
        default_addr_pool_type: str = None,
        default_lba_strategy: str = None,
        default_min_available_addr_num: int = None,
        default_max_return_addr_num: int = None,
        default_latency_optimization: str = None,
        failover_addr_pool_type: str = None,
        failover_lba_strategy: str = None,
        failover_min_available_addr_num: int = None,
        failover_max_return_addr_num: int = None,
        failover_latency_optimization: str = None,
        default_addr_pool: List[UpdateDnsGtmAccessStrategyRequestDefaultAddrPool] = None,
        failover_addr_pool: List[UpdateDnsGtmAccessStrategyRequestFailoverAddrPool] = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.lines = lines
        self.default_addr_pool_type = default_addr_pool_type
        self.default_lba_strategy = default_lba_strategy
        self.default_min_available_addr_num = default_min_available_addr_num
        self.default_max_return_addr_num = default_max_return_addr_num
        self.default_latency_optimization = default_latency_optimization
        self.failover_addr_pool_type = failover_addr_pool_type
        self.failover_lba_strategy = failover_lba_strategy
        self.failover_min_available_addr_num = failover_min_available_addr_num
        self.failover_max_return_addr_num = failover_max_return_addr_num
        self.failover_latency_optimization = failover_latency_optimization
        self.default_addr_pool = default_addr_pool
        self.failover_addr_pool = failover_addr_pool

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.default_addr_pool_type, 'default_addr_pool_type')
        self.validate_required(self.default_min_available_addr_num, 'default_min_available_addr_num')
        self.validate_required(self.default_addr_pool, 'default_addr_pool')
        if self.default_addr_pool:
            for k in self.default_addr_pool:
                if k:
                    k.validate()
        if self.failover_addr_pool:
            for k in self.failover_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.default_addr_pool_type is not None:
            result['DefaultAddrPoolType'] = self.default_addr_pool_type
        if self.default_lba_strategy is not None:
            result['DefaultLbaStrategy'] = self.default_lba_strategy
        if self.default_min_available_addr_num is not None:
            result['DefaultMinAvailableAddrNum'] = self.default_min_available_addr_num
        if self.default_max_return_addr_num is not None:
            result['DefaultMaxReturnAddrNum'] = self.default_max_return_addr_num
        if self.default_latency_optimization is not None:
            result['DefaultLatencyOptimization'] = self.default_latency_optimization
        if self.failover_addr_pool_type is not None:
            result['FailoverAddrPoolType'] = self.failover_addr_pool_type
        if self.failover_lba_strategy is not None:
            result['FailoverLbaStrategy'] = self.failover_lba_strategy
        if self.failover_min_available_addr_num is not None:
            result['FailoverMinAvailableAddrNum'] = self.failover_min_available_addr_num
        if self.failover_max_return_addr_num is not None:
            result['FailoverMaxReturnAddrNum'] = self.failover_max_return_addr_num
        if self.failover_latency_optimization is not None:
            result['FailoverLatencyOptimization'] = self.failover_latency_optimization
        result['DefaultAddrPool'] = []
        if self.default_addr_pool is not None:
            for k in self.default_addr_pool:
                result['DefaultAddrPool'].append(k.to_map() if k else None)
        result['FailoverAddrPool'] = []
        if self.failover_addr_pool is not None:
            for k in self.failover_addr_pool:
                result['FailoverAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('DefaultAddrPoolType') is not None:
            self.default_addr_pool_type = m.get('DefaultAddrPoolType')
        if m.get('DefaultLbaStrategy') is not None:
            self.default_lba_strategy = m.get('DefaultLbaStrategy')
        if m.get('DefaultMinAvailableAddrNum') is not None:
            self.default_min_available_addr_num = m.get('DefaultMinAvailableAddrNum')
        if m.get('DefaultMaxReturnAddrNum') is not None:
            self.default_max_return_addr_num = m.get('DefaultMaxReturnAddrNum')
        if m.get('DefaultLatencyOptimization') is not None:
            self.default_latency_optimization = m.get('DefaultLatencyOptimization')
        if m.get('FailoverAddrPoolType') is not None:
            self.failover_addr_pool_type = m.get('FailoverAddrPoolType')
        if m.get('FailoverLbaStrategy') is not None:
            self.failover_lba_strategy = m.get('FailoverLbaStrategy')
        if m.get('FailoverMinAvailableAddrNum') is not None:
            self.failover_min_available_addr_num = m.get('FailoverMinAvailableAddrNum')
        if m.get('FailoverMaxReturnAddrNum') is not None:
            self.failover_max_return_addr_num = m.get('FailoverMaxReturnAddrNum')
        if m.get('FailoverLatencyOptimization') is not None:
            self.failover_latency_optimization = m.get('FailoverLatencyOptimization')
        self.default_addr_pool = []
        if m.get('DefaultAddrPool') is not None:
            for k in m.get('DefaultAddrPool'):
                temp_model = UpdateDnsGtmAccessStrategyRequestDefaultAddrPool()
                self.default_addr_pool.append(temp_model.from_map(k))
        self.failover_addr_pool = []
        if m.get('FailoverAddrPool') is not None:
            for k in m.get('FailoverAddrPool'):
                temp_model = UpdateDnsGtmAccessStrategyRequestFailoverAddrPool()
                self.failover_addr_pool.append(temp_model.from_map(k))
        return self


class UpdateDnsGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_id: str = None,
    ):
        self.request_id = request_id
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeDnsGtmInstanceSystemCnameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDnsGtmInstanceSystemCnameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_cname: str = None,
    ):
        self.request_id = request_id
        self.system_cname = system_cname

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.system_cname, 'system_cname')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_cname is not None:
            result['SystemCname'] = self.system_cname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemCname') is not None:
            self.system_cname = m.get('SystemCname')
        return self


class DescribeDnsGtmInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDnsGtmInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_not_available_num: int = None,
        addr_pool_group_not_available_num: int = None,
        switch_to_failover_strategy_num: int = None,
        strategy_not_available_num: int = None,
        addr_available_num: int = None,
    ):
        self.request_id = request_id
        self.addr_not_available_num = addr_not_available_num
        self.addr_pool_group_not_available_num = addr_pool_group_not_available_num
        self.switch_to_failover_strategy_num = switch_to_failover_strategy_num
        self.strategy_not_available_num = strategy_not_available_num
        self.addr_available_num = addr_available_num

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_not_available_num, 'addr_not_available_num')
        self.validate_required(self.addr_pool_group_not_available_num, 'addr_pool_group_not_available_num')
        self.validate_required(self.switch_to_failover_strategy_num, 'switch_to_failover_strategy_num')
        self.validate_required(self.strategy_not_available_num, 'strategy_not_available_num')
        self.validate_required(self.addr_available_num, 'addr_available_num')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_not_available_num is not None:
            result['AddrNotAvailableNum'] = self.addr_not_available_num
        if self.addr_pool_group_not_available_num is not None:
            result['AddrPoolGroupNotAvailableNum'] = self.addr_pool_group_not_available_num
        if self.switch_to_failover_strategy_num is not None:
            result['SwitchToFailoverStrategyNum'] = self.switch_to_failover_strategy_num
        if self.strategy_not_available_num is not None:
            result['StrategyNotAvailableNum'] = self.strategy_not_available_num
        if self.addr_available_num is not None:
            result['AddrAvailableNum'] = self.addr_available_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrNotAvailableNum') is not None:
            self.addr_not_available_num = m.get('AddrNotAvailableNum')
        if m.get('AddrPoolGroupNotAvailableNum') is not None:
            self.addr_pool_group_not_available_num = m.get('AddrPoolGroupNotAvailableNum')
        if m.get('SwitchToFailoverStrategyNum') is not None:
            self.switch_to_failover_strategy_num = m.get('SwitchToFailoverStrategyNum')
        if m.get('StrategyNotAvailableNum') is not None:
            self.strategy_not_available_num = m.get('StrategyNotAvailableNum')
        if m.get('AddrAvailableNum') is not None:
            self.addr_available_num = m.get('AddrAvailableNum')
        return self


class DescribeDohDomainStatisticsSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        end_date: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDohDomainStatisticsSummaryResponseStatistics(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        v_4http_count: int = None,
        v_6http_count: int = None,
        v_4https_count: int = None,
        v_6https_count: int = None,
        total_count: int = None,
        ip_count: int = None,
        http_count: int = None,
        https_count: int = None,
    ):
        self.domain_name = domain_name
        self.v_4http_count = v_4http_count
        self.v_6http_count = v_6http_count
        self.v_4https_count = v_4https_count
        self.v_6https_count = v_6https_count
        self.total_count = total_count
        self.ip_count = ip_count
        self.http_count = http_count
        self.https_count = https_count

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.v_4http_count, 'v_4http_count')
        self.validate_required(self.v_6http_count, 'v_6http_count')
        self.validate_required(self.v_4https_count, 'v_4https_count')
        self.validate_required(self.v_6https_count, 'v_6https_count')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.http_count, 'http_count')
        self.validate_required(self.https_count, 'https_count')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count
        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count
        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count
        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.http_count is not None:
            result['HttpCount'] = self.http_count
        if self.https_count is not None:
            result['HttpsCount'] = self.https_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')
        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')
        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')
        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')
        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')
        return self


class DescribeDohDomainStatisticsSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        statistics: List[DescribeDohDomainStatisticsSummaryResponseStatistics] = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = DescribeDohDomainStatisticsSummaryResponseStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class DescribeDohAccountStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.lang = lang
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeDohAccountStatisticsResponseStatistics(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        v_4http_count: int = None,
        v_6http_count: int = None,
        v_4https_count: int = None,
        v_6https_count: int = None,
        total_count: int = None,
    ):
        self.timestamp = timestamp
        self.v_4http_count = v_4http_count
        self.v_6http_count = v_6http_count
        self.v_4https_count = v_4https_count
        self.v_6https_count = v_6https_count
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.v_4http_count, 'v_4http_count')
        self.validate_required(self.v_6http_count, 'v_6http_count')
        self.validate_required(self.v_4https_count, 'v_4https_count')
        self.validate_required(self.v_6https_count, 'v_6https_count')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count
        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count
        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count
        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')
        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')
        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')
        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDohAccountStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: List[DescribeDohAccountStatisticsResponseStatistics] = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = DescribeDohAccountStatisticsResponseStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class DescribeDohSubDomainStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        sub_domain: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.lang = lang
        self.sub_domain = sub_domain
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeDohSubDomainStatisticsResponseStatistics(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        v_4http_count: int = None,
        v_4https_count: int = None,
        v_6http_count: int = None,
        v_6https_count: int = None,
        total_count: int = None,
    ):
        self.timestamp = timestamp
        self.v_4http_count = v_4http_count
        self.v_4https_count = v_4https_count
        self.v_6http_count = v_6http_count
        self.v_6https_count = v_6https_count
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.v_4http_count, 'v_4http_count')
        self.validate_required(self.v_4https_count, 'v_4https_count')
        self.validate_required(self.v_6http_count, 'v_6http_count')
        self.validate_required(self.v_6https_count, 'v_6https_count')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count
        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count
        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count
        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')
        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')
        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')
        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDohSubDomainStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: List[DescribeDohSubDomainStatisticsResponseStatistics] = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = DescribeDohSubDomainStatisticsResponseStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class DescribeDohSubDomainStatisticsSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        end_date: str = None,
        sub_domain: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.sub_domain = sub_domain
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDohSubDomainStatisticsSummaryResponseStatistics(TeaModel):
    def __init__(
        self,
        sub_domain: str = None,
        v_4http_count: int = None,
        v_6http_count: int = None,
        v_4https_count: int = None,
        v_6https_count: int = None,
        total_count: int = None,
        ip_count: int = None,
        http_count: int = None,
        https_count: int = None,
    ):
        self.sub_domain = sub_domain
        self.v_4http_count = v_4http_count
        self.v_6http_count = v_6http_count
        self.v_4https_count = v_4https_count
        self.v_6https_count = v_6https_count
        self.total_count = total_count
        self.ip_count = ip_count
        self.http_count = http_count
        self.https_count = https_count

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')
        self.validate_required(self.v_4http_count, 'v_4http_count')
        self.validate_required(self.v_6http_count, 'v_6http_count')
        self.validate_required(self.v_4https_count, 'v_4https_count')
        self.validate_required(self.v_6https_count, 'v_6https_count')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.http_count, 'http_count')
        self.validate_required(self.https_count, 'https_count')

    def to_map(self):
        result = dict()
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count
        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count
        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count
        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.http_count is not None:
            result['HttpCount'] = self.http_count
        if self.https_count is not None:
            result['HttpsCount'] = self.https_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')
        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')
        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')
        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')
        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')
        return self


class DescribeDohSubDomainStatisticsSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        statistics: List[DescribeDohSubDomainStatisticsSummaryResponseStatistics] = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = DescribeDohSubDomainStatisticsSummaryResponseStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class DescribeDohDomainStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeDohDomainStatisticsResponseStatistics(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        v_4http_count: int = None,
        v_6http_count: int = None,
        v_4https_count: int = None,
        v_6https_count: int = None,
        total_count: int = None,
    ):
        self.timestamp = timestamp
        self.v_4http_count = v_4http_count
        self.v_6http_count = v_6http_count
        self.v_4https_count = v_4https_count
        self.v_6https_count = v_6https_count
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.v_4http_count, 'v_4http_count')
        self.validate_required(self.v_6http_count, 'v_6http_count')
        self.validate_required(self.v_4https_count, 'v_4https_count')
        self.validate_required(self.v_6https_count, 'v_6https_count')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.v_4http_count is not None:
            result['V4HttpCount'] = self.v_4http_count
        if self.v_6http_count is not None:
            result['V6HttpCount'] = self.v_6http_count
        if self.v_4https_count is not None:
            result['V4HttpsCount'] = self.v_4https_count
        if self.v_6https_count is not None:
            result['V6HttpsCount'] = self.v_6https_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('V4HttpCount') is not None:
            self.v_4http_count = m.get('V4HttpCount')
        if m.get('V6HttpCount') is not None:
            self.v_6http_count = m.get('V6HttpCount')
        if m.get('V4HttpsCount') is not None:
            self.v_4https_count = m.get('V4HttpsCount')
        if m.get('V6HttpsCount') is not None:
            self.v_6https_count = m.get('V6HttpsCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDohDomainStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: List[DescribeDohDomainStatisticsResponseStatistics] = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = DescribeDohDomainStatisticsResponseStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class DescribeDohUserInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.lang = lang
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeDohUserInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pdns_id: int = None,
        domain_count: int = None,
        sub_domain_count: int = None,
    ):
        self.request_id = request_id
        self.pdns_id = pdns_id
        self.domain_count = domain_count
        self.sub_domain_count = sub_domain_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pdns_id, 'pdns_id')
        self.validate_required(self.domain_count, 'domain_count')
        self.validate_required(self.sub_domain_count, 'sub_domain_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pdns_id is not None:
            result['PdnsId'] = self.pdns_id
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.sub_domain_count is not None:
            result['SubDomainCount'] = self.sub_domain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PdnsId') is not None:
            self.pdns_id = m.get('PdnsId')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('SubDomainCount') is not None:
            self.sub_domain_count = m.get('SubDomainCount')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
        resource_id: List[str] = None,
        next_token: str = None,
    ):
        self.lang = lang
        self.resource_type = resource_type
        self.tag = tag
        self.resource_id = resource_id
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseTagResources] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
        resource_id: List[str] = None,
    ):
        self.lang = lang
        self.resource_type = resource_type
        self.tag = tag
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.lang = lang
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.resource_type = resource_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeTagsResponseTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        tags: List[DescribeTagsResponseTags] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.tags = tags

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagsResponseTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CopyGtmConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_id: str = None,
        target_id: str = None,
        copy_type: str = None,
    ):
        self.lang = lang
        self.source_id = source_id
        self.target_id = target_id
        self.copy_type = copy_type

    def validate(self):
        self.validate_required(self.source_id, 'source_id')
        self.validate_required(self.target_id, 'target_id')
        self.validate_required(self.copy_type, 'copy_type')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.copy_type is not None:
            result['CopyType'] = self.copy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('CopyType') is not None:
            self.copy_type = m.get('CopyType')
        return self


class CopyGtmConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainDnssecInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainDnssecInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        status: str = None,
        ds_record: str = None,
        digest: str = None,
        digest_type: str = None,
        algorithm: str = None,
        public_key: str = None,
        key_tag: str = None,
        flags: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.status = status
        self.ds_record = ds_record
        self.digest = digest
        self.digest_type = digest_type
        self.algorithm = algorithm
        self.public_key = public_key
        self.key_tag = key_tag
        self.flags = flags

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ds_record, 'ds_record')
        self.validate_required(self.digest, 'digest')
        self.validate_required(self.digest_type, 'digest_type')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.public_key, 'public_key')
        self.validate_required(self.key_tag, 'key_tag')
        self.validate_required(self.flags, 'flags')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.ds_record is not None:
            result['DsRecord'] = self.ds_record
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DsRecord') is not None:
            self.ds_record = m.get('DsRecord')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class SetDomainDnssecStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.status = status

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDomainDnssecStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_names: str = None,
        remark: str = None,
        target_user_id: int = None,
    ):
        self.lang = lang
        self.domain_names = domain_names
        self.remark = remark
        self.target_user_id = target_user_id

    def validate(self):
        self.validate_required(self.domain_names, 'domain_names')
        self.validate_required(self.target_user_id, 'target_user_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class TransferDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: int = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTransferDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        transfer_type: str = None,
        domain_name: str = None,
        from_user_id: int = None,
        target_user_id: int = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.transfer_type = transfer_type
        self.domain_name = domain_name
        self.from_user_id = from_user_id
        self.target_user_id = target_user_id

    def validate(self):
        self.validate_required(self.transfer_type, 'transfer_type')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class DescribeTransferDomainsResponseDomainTransfersDomainTransfer(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        from_user_id: int = None,
        target_user_id: int = None,
        id: int = None,
    ):
        self.domain_name = domain_name
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.from_user_id = from_user_id
        self.target_user_id = target_user_id
        self.id = id

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.from_user_id, 'from_user_id')
        self.validate_required(self.target_user_id, 'target_user_id')
        self.validate_required(self.id, 'id')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTransferDomainsResponseDomainTransfers(TeaModel):
    def __init__(
        self,
        domain_transfer: List[DescribeTransferDomainsResponseDomainTransfersDomainTransfer] = None,
    ):
        self.domain_transfer = domain_transfer

    def validate(self):
        self.validate_required(self.domain_transfer, 'domain_transfer')
        if self.domain_transfer:
            for k in self.domain_transfer:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainTransfer'] = []
        if self.domain_transfer is not None:
            for k in self.domain_transfer:
                result['DomainTransfer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_transfer = []
        if m.get('DomainTransfer') is not None:
            for k in m.get('DomainTransfer'):
                temp_model = DescribeTransferDomainsResponseDomainTransfersDomainTransfer()
                self.domain_transfer.append(temp_model.from_map(k))
        return self


class DescribeTransferDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_transfers: DescribeTransferDomainsResponseDomainTransfers = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_transfers = domain_transfers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_transfers, 'domain_transfers')
        if self.domain_transfers:
            self.domain_transfers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_transfers is not None:
            result['DomainTransfers'] = self.domain_transfers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainTransfers') is not None:
            temp_model = DescribeTransferDomainsResponseDomainTransfers()
            self.domain_transfers = temp_model.from_map(m['DomainTransfers'])
        return self


class AddDomainBackupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        period_type: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.period_type = period_type

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.period_type, 'period_type')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        return self


class AddDomainBackupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        period_type: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.period_type = period_type

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.period_type, 'period_type')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        return self


class RetrieveDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class RetrieveDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrsAddr(TeaModel):
    def __init__(
        self,
        id: int = None,
        mode: str = None,
        value: str = None,
    ):
        self.id = id
        self.mode = mode
        self.value = value

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrs(TeaModel):
    def __init__(
        self,
        addr: List[DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrsAddr] = None,
    ):
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrsAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPool(TeaModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        addr_pool_name: str = None,
        instance_id: str = None,
        addrs: DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrs = None,
    ):
        self.addr_pool_id = addr_pool_id
        self.addr_pool_name = addr_pool_name
        self.instance_id = instance_id
        self.addrs = addrs

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.addr_pool_name, 'addr_pool_name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.addrs, 'addrs')
        if self.addrs:
            self.addrs.validate()

    def to_map(self):
        result = dict()
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.addr_pool_name is not None:
            result['AddrPoolName'] = self.addr_pool_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.addrs is not None:
            result['Addrs'] = self.addrs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('AddrPoolName') is not None:
            self.addr_pool_name = m.get('AddrPoolName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Addrs') is not None:
            temp_model = DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPoolAddrs()
            self.addrs = temp_model.from_map(m['Addrs'])
        return self


class DescribeGtmRecoveryPlanResponseFaultAddrPools(TeaModel):
    def __init__(
        self,
        fault_addr_pool: List[DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPool] = None,
    ):
        self.fault_addr_pool = fault_addr_pool

    def validate(self):
        self.validate_required(self.fault_addr_pool, 'fault_addr_pool')
        if self.fault_addr_pool:
            for k in self.fault_addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FaultAddrPool'] = []
        if self.fault_addr_pool is not None:
            for k in self.fault_addr_pool:
                result['FaultAddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fault_addr_pool = []
        if m.get('FaultAddrPool') is not None:
            for k in m.get('FaultAddrPool'):
                temp_model = DescribeGtmRecoveryPlanResponseFaultAddrPoolsFaultAddrPool()
                self.fault_addr_pool.append(temp_model.from_map(k))
        return self


class DescribeGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        recovery_plan_id: int = None,
        name: str = None,
        remark: str = None,
        fault_addr_pool_num: int = None,
        status: str = None,
        last_execute_time: str = None,
        last_execute_timestamp: int = None,
        last_rollback_time: str = None,
        last_rollback_timestamp: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        fault_addr_pools: DescribeGtmRecoveryPlanResponseFaultAddrPools = None,
    ):
        self.request_id = request_id
        self.recovery_plan_id = recovery_plan_id
        self.name = name
        self.remark = remark
        self.fault_addr_pool_num = fault_addr_pool_num
        self.status = status
        self.last_execute_time = last_execute_time
        self.last_execute_timestamp = last_execute_timestamp
        self.last_rollback_time = last_rollback_time
        self.last_rollback_timestamp = last_rollback_timestamp
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.fault_addr_pools = fault_addr_pools

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.fault_addr_pool_num, 'fault_addr_pool_num')
        self.validate_required(self.status, 'status')
        self.validate_required(self.last_execute_time, 'last_execute_time')
        self.validate_required(self.last_execute_timestamp, 'last_execute_timestamp')
        self.validate_required(self.last_rollback_time, 'last_rollback_time')
        self.validate_required(self.last_rollback_timestamp, 'last_rollback_timestamp')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.fault_addr_pools, 'fault_addr_pools')
        if self.fault_addr_pools:
            self.fault_addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.fault_addr_pool_num is not None:
            result['FaultAddrPoolNum'] = self.fault_addr_pool_num
        if self.status is not None:
            result['Status'] = self.status
        if self.last_execute_time is not None:
            result['LastExecuteTime'] = self.last_execute_time
        if self.last_execute_timestamp is not None:
            result['LastExecuteTimestamp'] = self.last_execute_timestamp
        if self.last_rollback_time is not None:
            result['LastRollbackTime'] = self.last_rollback_time
        if self.last_rollback_timestamp is not None:
            result['LastRollbackTimestamp'] = self.last_rollback_timestamp
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.fault_addr_pools is not None:
            result['FaultAddrPools'] = self.fault_addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FaultAddrPoolNum') is not None:
            self.fault_addr_pool_num = m.get('FaultAddrPoolNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastExecuteTime') is not None:
            self.last_execute_time = m.get('LastExecuteTime')
        if m.get('LastExecuteTimestamp') is not None:
            self.last_execute_timestamp = m.get('LastExecuteTimestamp')
        if m.get('LastRollbackTime') is not None:
            self.last_rollback_time = m.get('LastRollbackTime')
        if m.get('LastRollbackTimestamp') is not None:
            self.last_rollback_timestamp = m.get('LastRollbackTimestamp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('FaultAddrPools') is not None:
            temp_model = DescribeGtmRecoveryPlanResponseFaultAddrPools()
            self.fault_addr_pools = temp_model.from_map(m['FaultAddrPools'])
        return self


class AddGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        name: str = None,
        remark: str = None,
        fault_addr_pool: str = None,
    ):
        self.lang = lang
        self.name = name
        self.remark = remark
        self.fault_addr_pool = fault_addr_pool

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.fault_addr_pool, 'fault_addr_pool')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.fault_addr_pool is not None:
            result['FaultAddrPool'] = self.fault_addr_pool
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FaultAddrPool') is not None:
            self.fault_addr_pool = m.get('FaultAddrPool')
        return self


class AddGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        recovery_plan_id: str = None,
    ):
        self.request_id = request_id
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class UpdateGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
        name: str = None,
        remark: str = None,
        fault_addr_pool: str = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id
        self.name = name
        self.remark = remark
        self.fault_addr_pool = fault_addr_pool

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.fault_addr_pool is not None:
            result['FaultAddrPool'] = self.fault_addr_pool
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FaultAddrPool') is not None:
            self.fault_addr_pool = m.get('FaultAddrPool')
        return self


class UpdateGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class DeleteGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGtmRecoveryPlansRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeGtmRecoveryPlansResponseRecoveryPlansRecoveryPlan(TeaModel):
    def __init__(
        self,
        recovery_plan_id: int = None,
        name: str = None,
        remark: str = None,
        fault_addr_pool_num: int = None,
        last_execute_time: str = None,
        last_execute_timestamp: int = None,
        last_rollback_time: str = None,
        last_rollback_timestamp: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        status: str = None,
    ):
        self.recovery_plan_id = recovery_plan_id
        self.name = name
        self.remark = remark
        self.fault_addr_pool_num = fault_addr_pool_num
        self.last_execute_time = last_execute_time
        self.last_execute_timestamp = last_execute_timestamp
        self.last_rollback_time = last_rollback_time
        self.last_rollback_timestamp = last_rollback_timestamp
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.status = status

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.fault_addr_pool_num, 'fault_addr_pool_num')
        self.validate_required(self.last_execute_time, 'last_execute_time')
        self.validate_required(self.last_execute_timestamp, 'last_execute_timestamp')
        self.validate_required(self.last_rollback_time, 'last_rollback_time')
        self.validate_required(self.last_rollback_timestamp, 'last_rollback_timestamp')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.fault_addr_pool_num is not None:
            result['FaultAddrPoolNum'] = self.fault_addr_pool_num
        if self.last_execute_time is not None:
            result['LastExecuteTime'] = self.last_execute_time
        if self.last_execute_timestamp is not None:
            result['LastExecuteTimestamp'] = self.last_execute_timestamp
        if self.last_rollback_time is not None:
            result['LastRollbackTime'] = self.last_rollback_time
        if self.last_rollback_timestamp is not None:
            result['LastRollbackTimestamp'] = self.last_rollback_timestamp
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FaultAddrPoolNum') is not None:
            self.fault_addr_pool_num = m.get('FaultAddrPoolNum')
        if m.get('LastExecuteTime') is not None:
            self.last_execute_time = m.get('LastExecuteTime')
        if m.get('LastExecuteTimestamp') is not None:
            self.last_execute_timestamp = m.get('LastExecuteTimestamp')
        if m.get('LastRollbackTime') is not None:
            self.last_rollback_time = m.get('LastRollbackTime')
        if m.get('LastRollbackTimestamp') is not None:
            self.last_rollback_timestamp = m.get('LastRollbackTimestamp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGtmRecoveryPlansResponseRecoveryPlans(TeaModel):
    def __init__(
        self,
        recovery_plan: List[DescribeGtmRecoveryPlansResponseRecoveryPlansRecoveryPlan] = None,
    ):
        self.recovery_plan = recovery_plan

    def validate(self):
        self.validate_required(self.recovery_plan, 'recovery_plan')
        if self.recovery_plan:
            for k in self.recovery_plan:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RecoveryPlan'] = []
        if self.recovery_plan is not None:
            for k in self.recovery_plan:
                result['RecoveryPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recovery_plan = []
        if m.get('RecoveryPlan') is not None:
            for k in m.get('RecoveryPlan'):
                temp_model = DescribeGtmRecoveryPlansResponseRecoveryPlansRecoveryPlan()
                self.recovery_plan.append(temp_model.from_map(k))
        return self


class DescribeGtmRecoveryPlansResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_number: int = None,
        page_size: int = None,
        recovery_plans: DescribeGtmRecoveryPlansResponseRecoveryPlans = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_number = page_number
        self.page_size = page_size
        self.recovery_plans = recovery_plans

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.recovery_plans, 'recovery_plans')
        if self.recovery_plans:
            self.recovery_plans.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recovery_plans is not None:
            result['RecoveryPlans'] = self.recovery_plans.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecoveryPlans') is not None:
            temp_model = DescribeGtmRecoveryPlansResponseRecoveryPlans()
            self.recovery_plans = temp_model.from_map(m['RecoveryPlans'])
        return self


class DescribeGtmRecoveryPlanAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPoolsAddrPool(TeaModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        name: str = None,
    ):
        self.addr_pool_id = addr_pool_id
        self.name = name

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPools(TeaModel):
    def __init__(
        self,
        addr_pool: List[DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        self.validate_required(self.addr_pool, 'addr_pool')
        if self.addr_pool:
            for k in self.addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k in self.addr_pool:
                result['AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k in m.get('AddrPool'):
                temp_model = DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k))
        return self


class DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        addr_pools: DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPools = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.addr_pools = addr_pools

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.addr_pools, 'addr_pools')
        if self.addr_pools:
            self.addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('AddrPools') is not None:
            temp_model = DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstanceAddrPools()
            self.addr_pools = temp_model.from_map(m['AddrPools'])
        return self


class DescribeGtmRecoveryPlanAvailableConfigResponseInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        self.validate_required(self.instance, 'instance')
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeGtmRecoveryPlanAvailableConfigResponseInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeGtmRecoveryPlanAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instances: DescribeGtmRecoveryPlanAvailableConfigResponseInstances = None,
    ):
        self.request_id = request_id
        self.instances = instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instances') is not None:
            temp_model = DescribeGtmRecoveryPlanAvailableConfigResponseInstances()
            self.instances = temp_model.from_map(m['Instances'])
        return self


class ExecuteGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class ExecuteGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class RollbackGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreviewGtmRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.recovery_plan_id = recovery_plan_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.recovery_plan_id, 'recovery_plan_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfosSwitchInfo(TeaModel):
    def __init__(
        self,
        strategy_name: str = None,
        content: str = None,
    ):
        self.strategy_name = strategy_name
        self.content = content

    def validate(self):
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = dict()
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfos(TeaModel):
    def __init__(
        self,
        switch_info: List[PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfosSwitchInfo] = None,
    ):
        self.switch_info = switch_info

    def validate(self):
        self.validate_required(self.switch_info, 'switch_info')
        if self.switch_info:
            for k in self.switch_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SwitchInfo'] = []
        if self.switch_info is not None:
            for k in self.switch_info:
                result['SwitchInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_info = []
        if m.get('SwitchInfo') is not None:
            for k in m.get('SwitchInfo'):
                temp_model = PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfosSwitchInfo()
                self.switch_info.append(temp_model.from_map(k))
        return self


class PreviewGtmRecoveryPlanResponsePreviewsPreview(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        user_domain_name: str = None,
        switch_infos: PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfos = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.user_domain_name = user_domain_name
        self.switch_infos = switch_infos

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.user_domain_name, 'user_domain_name')
        self.validate_required(self.switch_infos, 'switch_infos')
        if self.switch_infos:
            self.switch_infos.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name
        if self.switch_infos is not None:
            result['SwitchInfos'] = self.switch_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')
        if m.get('SwitchInfos') is not None:
            temp_model = PreviewGtmRecoveryPlanResponsePreviewsPreviewSwitchInfos()
            self.switch_infos = temp_model.from_map(m['SwitchInfos'])
        return self


class PreviewGtmRecoveryPlanResponsePreviews(TeaModel):
    def __init__(
        self,
        preview: List[PreviewGtmRecoveryPlanResponsePreviewsPreview] = None,
    ):
        self.preview = preview

    def validate(self):
        self.validate_required(self.preview, 'preview')
        if self.preview:
            for k in self.preview:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Preview'] = []
        if self.preview is not None:
            for k in self.preview:
                result['Preview'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.preview = []
        if m.get('Preview') is not None:
            for k in m.get('Preview'):
                temp_model = PreviewGtmRecoveryPlanResponsePreviewsPreview()
                self.preview.append(temp_model.from_map(k))
        return self


class PreviewGtmRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        previews: PreviewGtmRecoveryPlanResponsePreviews = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.previews = previews

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.previews, 'previews')
        if self.previews:
            self.previews.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.previews is not None:
            result['Previews'] = self.previews.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Previews') is not None:
            temp_model = PreviewGtmRecoveryPlanResponsePreviews()
            self.previews = temp_model.from_map(m['Previews'])
        return self


class GetTxtRecordForVerifyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        type: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.type = type

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTxtRecordForVerifyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        rr: str = None,
        value: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.rr = rr
        self.value = value

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rr is not None:
            result['RR'] = self.rr
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        start_date: str = None,
        end_date: str = None,
        domain_type: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.start_date = start_date
        self.end_date = end_date
        self.domain_type = domain_type

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeDomainStatisticsResponseStatisticsStatistic(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        count: int = None,
    ):
        self.timestamp = timestamp
        self.count = count

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainStatisticsResponseStatistics(TeaModel):
    def __init__(
        self,
        statistic: List[DescribeDomainStatisticsResponseStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        self.validate_required(self.statistic, 'statistic')
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeDomainStatisticsResponseStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k))
        return self


class DescribeDomainStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: DescribeDomainStatisticsResponseStatistics = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            temp_model = DescribeDomainStatisticsResponseStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        return self


class DescribeRecordStatisticsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        start_date: str = None,
        end_date: str = None,
        domain_name: str = None,
        rr: str = None,
        domain_type: str = None,
    ):
        self.lang = lang
        self.start_date = start_date
        self.end_date = end_date
        self.domain_name = domain_name
        self.rr = rr
        self.domain_type = domain_type

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rr, 'rr')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeRecordStatisticsResponseStatisticsStatistic(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        count: int = None,
    ):
        self.timestamp = timestamp
        self.count = count

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRecordStatisticsResponseStatistics(TeaModel):
    def __init__(
        self,
        statistic: List[DescribeRecordStatisticsResponseStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        self.validate_required(self.statistic, 'statistic')
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRecordStatisticsResponseStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k))
        return self


class DescribeRecordStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: DescribeRecordStatisticsResponseStatistics = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            temp_model = DescribeRecordStatisticsResponseStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        return self


class MoveDomainResourceGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_id: str = None,
        new_resource_group_id: str = None,
    ):
        self.lang = lang
        self.resource_id = resource_id
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.new_resource_group_id, 'new_resource_group_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        return self


class MoveDomainResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveGtmResourceGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_id: str = None,
        new_resource_group_id: str = None,
    ):
        self.lang = lang
        self.resource_id = resource_id
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.new_resource_group_id, 'new_resource_group_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        return self


class MoveGtmResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGtmInstanceSystemCnameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeGtmInstanceSystemCnameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_cname: str = None,
    ):
        self.request_id = request_id
        self.system_cname = system_cname

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.system_cname, 'system_cname')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_cname is not None:
            result['SystemCname'] = self.system_cname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemCname') is not None:
            self.system_cname = m.get('SystemCname')
        return self


class DescribeInstanceDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceDomainsResponseInstanceDomains(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        create_time: str = None,
        create_timestamp: int = None,
    ):
        self.domain_name = domain_name
        self.create_time = create_time
        self.create_timestamp = create_timestamp

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribeInstanceDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        page_number: int = None,
        page_size: int = None,
        total_pages: int = None,
        instance_domains: List[DescribeInstanceDomainsResponseInstanceDomains] = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.page_number = page_number
        self.page_size = page_size
        self.total_pages = total_pages
        self.instance_domains = instance_domains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.instance_domains, 'instance_domains')
        if self.instance_domains:
            for k in self.instance_domains:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['InstanceDomains'] = []
        if self.instance_domains is not None:
            for k in self.instance_domains:
                result['InstanceDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.instance_domains = []
        if m.get('InstanceDomains') is not None:
            for k in m.get('InstanceDomains'):
                temp_model = DescribeInstanceDomainsResponseInstanceDomains()
                self.instance_domains.append(temp_model.from_map(k))
        return self


class BindInstanceDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        domain_names: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.domain_names = domain_names

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.domain_names, 'domain_names')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BindInstanceDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success_count: int = None,
        failed_count: int = None,
    ):
        self.request_id = request_id
        self.success_count = success_count
        self.failed_count = failed_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success_count, 'success_count')
        self.validate_required(self.failed_count, 'failed_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        return self


class UnbindInstanceDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_names: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.domain_names = domain_names
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.domain_names, 'domain_names')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UnbindInstanceDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success_count: int = None,
        failed_count: int = None,
    ):
        self.request_id = request_id
        self.success_count = success_count
        self.failed_count = failed_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success_count, 'success_count')
        self.validate_required(self.failed_count, 'failed_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        return self


class UpdateCustomLineRequestIpSegment(TeaModel):
    def __init__(
        self,
        start_ip: str = None,
        end_ip: str = None,
    ):
        self.start_ip = start_ip
        self.end_ip = end_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_ip is not None:
            result['StartIp'] = self.start_ip
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')
        return self


class UpdateCustomLineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        line_name: str = None,
        ip_segment: List[UpdateCustomLineRequestIpSegment] = None,
        line_id: int = None,
    ):
        self.lang = lang
        self.line_name = line_name
        self.ip_segment = ip_segment
        self.line_id = line_id

    def validate(self):
        if self.ip_segment:
            for k in self.ip_segment:
                if k:
                    k.validate()
        self.validate_required(self.line_id, 'line_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line_name is not None:
            result['LineName'] = self.line_name
        result['IpSegment'] = []
        if self.ip_segment is not None:
            for k in self.ip_segment:
                result['IpSegment'].append(k.to_map() if k else None)
        if self.line_id is not None:
            result['LineId'] = self.line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        self.ip_segment = []
        if m.get('IpSegment') is not None:
            for k in m.get('IpSegment'):
                temp_model = UpdateCustomLineRequestIpSegment()
                self.ip_segment.append(temp_model.from_map(k))
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        return self


class UpdateCustomLineResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCustomLineRequestIpSegment(TeaModel):
    def __init__(
        self,
        start_ip: str = None,
        end_ip: str = None,
    ):
        self.start_ip = start_ip
        self.end_ip = end_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_ip is not None:
            result['StartIp'] = self.start_ip
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')
        return self


class AddCustomLineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        line_name: str = None,
        ip_segment: List[AddCustomLineRequestIpSegment] = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.line_name = line_name
        self.ip_segment = ip_segment

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.ip_segment, 'ip_segment')
        if self.ip_segment:
            for k in self.ip_segment:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.line_name is not None:
            result['LineName'] = self.line_name
        result['IpSegment'] = []
        if self.ip_segment is not None:
            for k in self.ip_segment:
                result['IpSegment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        self.ip_segment = []
        if m.get('IpSegment') is not None:
            for k in m.get('IpSegment'):
                temp_model = AddCustomLineRequestIpSegment()
                self.ip_segment.append(temp_model.from_map(k))
        return self


class AddCustomLineResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        line_id: int = None,
        line_code: str = None,
    ):
        self.request_id = request_id
        self.line_id = line_id
        self.line_code = line_code

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.line_id, 'line_id')
        self.validate_required(self.line_code, 'line_code')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        return self


class DeleteCustomLinesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        line_ids: str = None,
    ):
        self.lang = lang
        self.line_ids = line_ids

    def validate(self):
        self.validate_required(self.line_ids, 'line_ids')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line_ids is not None:
            result['LineIds'] = self.line_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LineIds') is not None:
            self.line_ids = m.get('LineIds')
        return self


class DeleteCustomLinesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCustomLineRequest(TeaModel):
    def __init__(
        self,
        line_id: int = None,
        lang: str = None,
    ):
        self.line_id = line_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.line_id is not None:
            result['LineId'] = self.line_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeCustomLineResponseIpSegmentList(TeaModel):
    def __init__(
        self,
        start_ip: str = None,
        end_ip: str = None,
    ):
        self.start_ip = start_ip
        self.end_ip = end_ip

    def validate(self):
        self.validate_required(self.start_ip, 'start_ip')
        self.validate_required(self.end_ip, 'end_ip')

    def to_map(self):
        result = dict()
        if self.start_ip is not None:
            result['StartIp'] = self.start_ip
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')
        return self


class DescribeCustomLineResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        id: int = None,
        name: str = None,
        domain_name: str = None,
        code: str = None,
        ip_segment_list: List[DescribeCustomLineResponseIpSegmentList] = None,
    ):
        self.request_id = request_id
        self.id = id
        self.name = name
        self.domain_name = domain_name
        self.code = code
        self.ip_segment_list = ip_segment_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ip_segment_list, 'ip_segment_list')
        if self.ip_segment_list:
            for k in self.ip_segment_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.code is not None:
            result['Code'] = self.code
        result['IpSegmentList'] = []
        if self.ip_segment_list is not None:
            for k in self.ip_segment_list:
                result['IpSegmentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.ip_segment_list = []
        if m.get('IpSegmentList') is not None:
            for k in m.get('IpSegmentList'):
                temp_model = DescribeCustomLineResponseIpSegmentList()
                self.ip_segment_list.append(temp_model.from_map(k))
        return self


class DescribeCustomLinesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeCustomLinesResponseCustomLines(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        code: str = None,
    ):
        self.id = id
        self.name = name
        self.code = code

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeCustomLinesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        page_number: int = None,
        page_size: int = None,
        total_pages: int = None,
        custom_lines: List[DescribeCustomLinesResponseCustomLines] = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.page_number = page_number
        self.page_size = page_size
        self.total_pages = total_pages
        self.custom_lines = custom_lines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.custom_lines, 'custom_lines')
        if self.custom_lines:
            for k in self.custom_lines:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['CustomLines'] = []
        if self.custom_lines is not None:
            for k in self.custom_lines:
                result['CustomLines'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.custom_lines = []
        if m.get('CustomLines') is not None:
            for k in m.get('CustomLines'):
                temp_model = DescribeCustomLinesResponseCustomLines()
                self.custom_lines.append(temp_model.from_map(k))
        return self


class DescribeDomainStatisticsSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        end_date: str = None,
        search_mode: str = None,
        keyword: str = None,
        threshold: int = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.search_mode = search_mode
        self.keyword = keyword
        self.threshold = threshold

    def validate(self):
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DescribeDomainStatisticsSummaryResponseStatisticsStatistic(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        count: int = None,
        domain_type: str = None,
    ):
        self.domain_name = domain_name
        self.count = count
        self.domain_type = domain_type

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.count, 'count')
        self.validate_required(self.domain_type, 'domain_type')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.count is not None:
            result['Count'] = self.count
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeDomainStatisticsSummaryResponseStatistics(TeaModel):
    def __init__(
        self,
        statistic: List[DescribeDomainStatisticsSummaryResponseStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        self.validate_required(self.statistic, 'statistic')
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeDomainStatisticsSummaryResponseStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k))
        return self


class DescribeDomainStatisticsSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        statistics: DescribeDomainStatisticsSummaryResponseStatistics = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Statistics') is not None:
            temp_model = DescribeDomainStatisticsSummaryResponseStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        return self


class DescribeRecordStatisticsSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        end_date: str = None,
        domain_name: str = None,
        search_mode: str = None,
        keyword: str = None,
        threshold: int = None,
        domain_type: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.domain_name = domain_name
        self.search_mode = search_mode
        self.keyword = keyword
        self.threshold = threshold
        self.domain_type = domain_type

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeRecordStatisticsSummaryResponseStatisticsStatistic(TeaModel):
    def __init__(
        self,
        sub_domain: str = None,
        count: int = None,
    ):
        self.sub_domain = sub_domain
        self.count = count

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = dict()
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRecordStatisticsSummaryResponseStatistics(TeaModel):
    def __init__(
        self,
        statistic: List[DescribeRecordStatisticsSummaryResponseStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        self.validate_required(self.statistic, 'statistic')
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeRecordStatisticsSummaryResponseStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k))
        return self


class DescribeRecordStatisticsSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        statistics: DescribeRecordStatisticsSummaryResponseStatistics = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.statistics = statistics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.statistics, 'statistics')
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Statistics') is not None:
            temp_model = DescribeRecordStatisticsSummaryResponseStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        return self


class OperateBatchDomainRequestDomainRecordInfo(TeaModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
        rr: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
        new_rr: str = None,
        new_type: str = None,
        new_value: str = None,
    ):
        self.domain = domain
        self.type = type
        self.rr = rr
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line
        self.new_rr = new_rr
        self.new_type = new_type
        self.new_value = new_value

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        if self.new_rr is not None:
            result['NewRr'] = self.new_rr
        if self.new_type is not None:
            result['NewType'] = self.new_type
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('NewRr') is not None:
            self.new_rr = m.get('NewRr')
        if m.get('NewType') is not None:
            self.new_type = m.get('NewType')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        return self


class OperateBatchDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        type: str = None,
        domain_record_info: List[OperateBatchDomainRequestDomainRecordInfo] = None,
    ):
        self.lang = lang
        self.type = type
        self.domain_record_info = domain_record_info

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.domain_record_info, 'domain_record_info')
        if self.domain_record_info:
            for k in self.domain_record_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        result['DomainRecordInfo'] = []
        if self.domain_record_info is not None:
            for k in self.domain_record_info:
                result['DomainRecordInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.domain_record_info = []
        if m.get('DomainRecordInfo') is not None:
            for k in m.get('DomainRecordInfo'):
                temp_model = OperateBatchDomainRequestDomainRecordInfo()
                self.domain_record_info.append(temp_model.from_map(k))
        return self


class OperateBatchDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: int = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeBatchResultDetailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        task_id: int = None,
        batch_type: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.task_id = task_id
        self.batch_type = batch_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBatchResultDetailResponseBatchResultDetailsBatchResultDetail(TeaModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
        rr: str = None,
        value: str = None,
        status: bool = None,
        reason: str = None,
        new_rr: str = None,
        new_value: str = None,
        batch_type: str = None,
        operate_date_str: str = None,
        line: str = None,
        priority: str = None,
        ttl: str = None,
        record_id: str = None,
        remark: str = None,
        rr_status: str = None,
    ):
        self.domain = domain
        self.type = type
        self.rr = rr
        self.value = value
        self.status = status
        self.reason = reason
        self.new_rr = new_rr
        self.new_value = new_value
        self.batch_type = batch_type
        self.operate_date_str = operate_date_str
        self.line = line
        self.priority = priority
        self.ttl = ttl
        self.record_id = record_id
        self.remark = remark
        self.rr_status = rr_status

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.type, 'type')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.value, 'value')
        self.validate_required(self.status, 'status')
        self.validate_required(self.reason, 'reason')
        self.validate_required(self.new_rr, 'new_rr')
        self.validate_required(self.new_value, 'new_value')
        self.validate_required(self.batch_type, 'batch_type')
        self.validate_required(self.operate_date_str, 'operate_date_str')
        self.validate_required(self.line, 'line')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.rr_status, 'rr_status')

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.value is not None:
            result['Value'] = self.value
        if self.status is not None:
            result['Status'] = self.status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.new_rr is not None:
            result['NewRr'] = self.new_rr
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.operate_date_str is not None:
            result['OperateDateStr'] = self.operate_date_str
        if self.line is not None:
            result['Line'] = self.line
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rr_status is not None:
            result['RrStatus'] = self.rr_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('NewRr') is not None:
            self.new_rr = m.get('NewRr')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('OperateDateStr') is not None:
            self.operate_date_str = m.get('OperateDateStr')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RrStatus') is not None:
            self.rr_status = m.get('RrStatus')
        return self


class DescribeBatchResultDetailResponseBatchResultDetails(TeaModel):
    def __init__(
        self,
        batch_result_detail: List[DescribeBatchResultDetailResponseBatchResultDetailsBatchResultDetail] = None,
    ):
        self.batch_result_detail = batch_result_detail

    def validate(self):
        self.validate_required(self.batch_result_detail, 'batch_result_detail')
        if self.batch_result_detail:
            for k in self.batch_result_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BatchResultDetail'] = []
        if self.batch_result_detail is not None:
            for k in self.batch_result_detail:
                result['BatchResultDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_result_detail = []
        if m.get('BatchResultDetail') is not None:
            for k in m.get('BatchResultDetail'):
                temp_model = DescribeBatchResultDetailResponseBatchResultDetailsBatchResultDetail()
                self.batch_result_detail.append(temp_model.from_map(k))
        return self


class DescribeBatchResultDetailResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        batch_result_details: DescribeBatchResultDetailResponseBatchResultDetails = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.batch_result_details = batch_result_details

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.batch_result_details, 'batch_result_details')
        if self.batch_result_details:
            self.batch_result_details.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.batch_result_details is not None:
            result['BatchResultDetails'] = self.batch_result_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BatchResultDetails') is not None:
            temp_model = DescribeBatchResultDetailResponseBatchResultDetails()
            self.batch_result_details = temp_model.from_map(m['BatchResultDetails'])
        return self


class DescribeBatchResultCountRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        task_id: int = None,
        batch_type: str = None,
    ):
        self.lang = lang
        self.task_id = task_id
        self.batch_type = batch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        return self


class DescribeBatchResultCountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
        total_count: int = None,
        success_count: int = None,
        failed_count: int = None,
        reason: str = None,
        batch_type: str = None,
        task_id: int = None,
    ):
        self.request_id = request_id
        self.status = status
        self.total_count = total_count
        self.success_count = success_count
        self.failed_count = failed_count
        self.reason = reason
        self.batch_type = batch_type
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.success_count, 'success_count')
        self.validate_required(self.failed_count, 'failed_count')
        self.validate_required(self.reason, 'reason')
        self.validate_required(self.batch_type, 'batch_type')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SetGtmAccessModeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
        access_mode: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id
        self.access_mode = access_mode

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.access_mode, 'access_mode')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class SetGtmAccessModeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetGtmMonitorStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id
        self.status = status

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetGtmMonitorStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGtmInstanceGlobalConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        instance_name: str = None,
        ttl: int = None,
        user_domain_name: str = None,
        lba_strategy: str = None,
        alert_group: str = None,
        cname_mode: str = None,
        cname_custom_domain_name: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.ttl = ttl
        self.user_domain_name = user_domain_name
        self.lba_strategy = lba_strategy
        self.alert_group = alert_group
        self.cname_mode = cname_mode
        self.cname_custom_domain_name = cname_custom_domain_name

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode
        if self.cname_custom_domain_name is not None:
            result['CnameCustomDomainName'] = self.cname_custom_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')
        if m.get('CnameCustomDomainName') is not None:
            self.cname_custom_domain_name = m.get('CnameCustomDomainName')
        return self


class UpdateGtmInstanceGlobalConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGtmLogsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        return self


class DescribeGtmLogsResponseLogsLog(TeaModel):
    def __init__(
        self,
        oper_time: str = None,
        oper_action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        entity_name: str = None,
        oper_ip: str = None,
        oper_timestamp: int = None,
        id: int = None,
        content: str = None,
    ):
        self.oper_time = oper_time
        self.oper_action = oper_action
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.oper_ip = oper_ip
        self.oper_timestamp = oper_timestamp
        self.id = id
        self.content = content

    def validate(self):
        self.validate_required(self.oper_time, 'oper_time')
        self.validate_required(self.oper_action, 'oper_action')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.entity_id, 'entity_id')
        self.validate_required(self.entity_name, 'entity_name')
        self.validate_required(self.oper_ip, 'oper_ip')
        self.validate_required(self.oper_timestamp, 'oper_timestamp')
        self.validate_required(self.id, 'id')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = dict()
        if self.oper_time is not None:
            result['OperTime'] = self.oper_time
        if self.oper_action is not None:
            result['OperAction'] = self.oper_action
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.oper_ip is not None:
            result['OperIp'] = self.oper_ip
        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp
        if self.id is not None:
            result['Id'] = self.id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')
        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('OperIp') is not None:
            self.oper_ip = m.get('OperIp')
        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeGtmLogsResponseLogs(TeaModel):
    def __init__(
        self,
        log: List[DescribeGtmLogsResponseLogsLog] = None,
    ):
        self.log = log

    def validate(self):
        self.validate_required(self.log, 'log')
        if self.log:
            for k in self.log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Log'] = []
        if self.log is not None:
            for k in self.log:
                result['Log'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k in m.get('Log'):
                temp_model = DescribeGtmLogsResponseLogsLog()
                self.log.append(temp_model.from_map(k))
        return self


class DescribeGtmLogsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_size: int = None,
        page_number: int = None,
        logs: DescribeGtmLogsResponseLogs = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_size = page_size
        self.page_number = page_number
        self.logs = logs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.logs, 'logs')
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Logs') is not None:
            temp_model = DescribeGtmLogsResponseLogs()
            self.logs = temp_model.from_map(m['Logs'])
        return self


class DeleteGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DeleteGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGtmMonitorRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class AddGtmMonitorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[AddGtmMonitorRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.evaluation_count, 'evaluation_count')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = AddGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class AddGtmMonitorResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_config_id: str = None,
    ):
        self.request_id = request_id
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class AddGtmAddressPoolRequestAddr(TeaModel):
    def __init__(
        self,
        value: str = None,
        lba_weight: int = None,
        mode: str = None,
    ):
        self.value = value
        self.lba_weight = lba_weight
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class AddGtmAddressPoolRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class AddGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
        min_available_addr_num: int = None,
        addr: List[AddGtmAddressPoolRequestAddr] = None,
        monitor_status: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[AddGtmAddressPoolRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.name = name
        self.type = type
        self.min_available_addr_num = min_available_addr_num
        self.addr = addr
        self.monitor_status = monitor_status
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_available_addr_num, 'min_available_addr_num')
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = AddGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k))
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = AddGtmAddressPoolRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class AddGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_pool_id: str = None,
        monitor_config_id: str = None,
    ):
        self.request_id = request_id
        self.addr_pool_id = addr_pool_id
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class AddGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        strategy_name: str = None,
        default_addr_pool_id: str = None,
        failover_addr_pool_id: str = None,
        access_lines: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.strategy_name = strategy_name
        self.default_addr_pool_id = default_addr_pool_id
        self.failover_addr_pool_id = failover_addr_pool_id
        self.access_lines = access_lines

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.default_addr_pool_id, 'default_addr_pool_id')
        self.validate_required(self.failover_addr_pool_id, 'failover_addr_pool_id')
        self.validate_required(self.access_lines, 'access_lines')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.default_addr_pool_id is not None:
            result['DefaultAddrPoolId'] = self.default_addr_pool_id
        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id
        if self.access_lines is not None:
            result['AccessLines'] = self.access_lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('DefaultAddrPoolId') is not None:
            self.default_addr_pool_id = m.get('DefaultAddrPoolId')
        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')
        if m.get('AccessLines') is not None:
            self.access_lines = m.get('AccessLines')
        return self


class AddGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_id: str = None,
    ):
        self.request_id = request_id
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeGtmInstancesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        keyword: str = None,
        resource_group_id: str = None,
        need_detail_attributes: bool = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.keyword = keyword
        self.resource_group_id = resource_group_id
        self.need_detail_attributes = need_detail_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')
        return self


class DescribeGtmInstancesResponseGtmInstancesGtmInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        cname: str = None,
        user_domain_name: str = None,
        version_code: str = None,
        ttl: int = None,
        lba_strategy: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        alert_group: str = None,
        cname_mode: str = None,
        access_strategy_num: int = None,
        address_pool_num: int = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.cname = cname
        self.user_domain_name = user_domain_name
        self.version_code = version_code
        self.ttl = ttl
        self.lba_strategy = lba_strategy
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.alert_group = alert_group
        self.cname_mode = cname_mode
        self.access_strategy_num = access_strategy_num
        self.address_pool_num = address_pool_num

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.user_domain_name, 'user_domain_name')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.lba_strategy, 'lba_strategy')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expire_timestamp, 'expire_timestamp')
        self.validate_required(self.alert_group, 'alert_group')
        self.validate_required(self.cname_mode, 'cname_mode')
        self.validate_required(self.access_strategy_num, 'access_strategy_num')
        self.validate_required(self.address_pool_num, 'address_pool_num')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode
        if self.access_strategy_num is not None:
            result['AccessStrategyNum'] = self.access_strategy_num
        if self.address_pool_num is not None:
            result['AddressPoolNum'] = self.address_pool_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')
        if m.get('AccessStrategyNum') is not None:
            self.access_strategy_num = m.get('AccessStrategyNum')
        if m.get('AddressPoolNum') is not None:
            self.address_pool_num = m.get('AddressPoolNum')
        return self


class DescribeGtmInstancesResponseGtmInstances(TeaModel):
    def __init__(
        self,
        gtm_instance: List[DescribeGtmInstancesResponseGtmInstancesGtmInstance] = None,
    ):
        self.gtm_instance = gtm_instance

    def validate(self):
        self.validate_required(self.gtm_instance, 'gtm_instance')
        if self.gtm_instance:
            for k in self.gtm_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['GtmInstance'] = []
        if self.gtm_instance is not None:
            for k in self.gtm_instance:
                result['GtmInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gtm_instance = []
        if m.get('GtmInstance') is not None:
            for k in m.get('GtmInstance'):
                temp_model = DescribeGtmInstancesResponseGtmInstancesGtmInstance()
                self.gtm_instance.append(temp_model.from_map(k))
        return self


class DescribeGtmInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_items: int = None,
        total_pages: int = None,
        gtm_instances: DescribeGtmInstancesResponseGtmInstances = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_items = total_items
        self.total_pages = total_pages
        self.gtm_instances = gtm_instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.gtm_instances, 'gtm_instances')
        if self.gtm_instances:
            self.gtm_instances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.gtm_instances is not None:
            result['GtmInstances'] = self.gtm_instances.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('GtmInstances') is not None:
            temp_model = DescribeGtmInstancesResponseGtmInstances()
            self.gtm_instances = temp_model.from_map(m['GtmInstances'])
        return self


class DeleteGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        return self


class DeleteGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGtmAccessStrategiesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeGtmAccessStrategiesResponseStrategiesStrategyLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeGtmAccessStrategiesResponseStrategiesStrategyLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeGtmAccessStrategiesResponseStrategiesStrategyLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeGtmAccessStrategiesResponseStrategiesStrategyLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeGtmAccessStrategiesResponseStrategiesStrategy(TeaModel):
    def __init__(
        self,
        strategy_id: str = None,
        strategy_name: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        default_addr_pool_id: str = None,
        default_addr_pool_name: str = None,
        failover_addr_pool_id: str = None,
        failover_addr_pool_name: str = None,
        access_mode: str = None,
        access_status: str = None,
        strategy_mode: str = None,
        instance_id: str = None,
        default_addr_pool_status: str = None,
        failover_addr_pool_status: str = None,
        default_addr_pool_monitor_status: str = None,
        failover_addr_pool_monitor_status: str = None,
        lines: DescribeGtmAccessStrategiesResponseStrategiesStrategyLines = None,
    ):
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.default_addr_pool_id = default_addr_pool_id
        self.default_addr_pool_name = default_addr_pool_name
        self.failover_addr_pool_id = failover_addr_pool_id
        self.failover_addr_pool_name = failover_addr_pool_name
        self.access_mode = access_mode
        self.access_status = access_status
        self.strategy_mode = strategy_mode
        self.instance_id = instance_id
        self.default_addr_pool_status = default_addr_pool_status
        self.failover_addr_pool_status = failover_addr_pool_status
        self.default_addr_pool_monitor_status = default_addr_pool_monitor_status
        self.failover_addr_pool_monitor_status = failover_addr_pool_monitor_status
        self.lines = lines

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.default_addr_pool_id, 'default_addr_pool_id')
        self.validate_required(self.default_addr_pool_name, 'default_addr_pool_name')
        self.validate_required(self.failover_addr_pool_id, 'failover_addr_pool_id')
        self.validate_required(self.failover_addr_pool_name, 'failover_addr_pool_name')
        self.validate_required(self.access_mode, 'access_mode')
        self.validate_required(self.access_status, 'access_status')
        self.validate_required(self.strategy_mode, 'strategy_mode')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.default_addr_pool_status, 'default_addr_pool_status')
        self.validate_required(self.failover_addr_pool_status, 'failover_addr_pool_status')
        self.validate_required(self.default_addr_pool_monitor_status, 'default_addr_pool_monitor_status')
        self.validate_required(self.failover_addr_pool_monitor_status, 'failover_addr_pool_monitor_status')
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.default_addr_pool_id is not None:
            result['DefaultAddrPoolId'] = self.default_addr_pool_id
        if self.default_addr_pool_name is not None:
            result['DefaultAddrPoolName'] = self.default_addr_pool_name
        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id
        if self.failover_addr_pool_name is not None:
            result['FailoverAddrPoolName'] = self.failover_addr_pool_name
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_status is not None:
            result['AccessStatus'] = self.access_status
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.default_addr_pool_status is not None:
            result['DefaultAddrPoolStatus'] = self.default_addr_pool_status
        if self.failover_addr_pool_status is not None:
            result['FailoverAddrPoolStatus'] = self.failover_addr_pool_status
        if self.default_addr_pool_monitor_status is not None:
            result['DefaultAddrPoolMonitorStatus'] = self.default_addr_pool_monitor_status
        if self.failover_addr_pool_monitor_status is not None:
            result['FailoverAddrPoolMonitorStatus'] = self.failover_addr_pool_monitor_status
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('DefaultAddrPoolId') is not None:
            self.default_addr_pool_id = m.get('DefaultAddrPoolId')
        if m.get('DefaultAddrPoolName') is not None:
            self.default_addr_pool_name = m.get('DefaultAddrPoolName')
        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')
        if m.get('FailoverAddrPoolName') is not None:
            self.failover_addr_pool_name = m.get('FailoverAddrPoolName')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DefaultAddrPoolStatus') is not None:
            self.default_addr_pool_status = m.get('DefaultAddrPoolStatus')
        if m.get('FailoverAddrPoolStatus') is not None:
            self.failover_addr_pool_status = m.get('FailoverAddrPoolStatus')
        if m.get('DefaultAddrPoolMonitorStatus') is not None:
            self.default_addr_pool_monitor_status = m.get('DefaultAddrPoolMonitorStatus')
        if m.get('FailoverAddrPoolMonitorStatus') is not None:
            self.failover_addr_pool_monitor_status = m.get('FailoverAddrPoolMonitorStatus')
        if m.get('Lines') is not None:
            temp_model = DescribeGtmAccessStrategiesResponseStrategiesStrategyLines()
            self.lines = temp_model.from_map(m['Lines'])
        return self


class DescribeGtmAccessStrategiesResponseStrategies(TeaModel):
    def __init__(
        self,
        strategy: List[DescribeGtmAccessStrategiesResponseStrategiesStrategy] = None,
    ):
        self.strategy = strategy

    def validate(self):
        self.validate_required(self.strategy, 'strategy')
        if self.strategy:
            for k in self.strategy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Strategy'] = []
        if self.strategy is not None:
            for k in self.strategy:
                result['Strategy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.strategy = []
        if m.get('Strategy') is not None:
            for k in m.get('Strategy'):
                temp_model = DescribeGtmAccessStrategiesResponseStrategiesStrategy()
                self.strategy.append(temp_model.from_map(k))
        return self


class DescribeGtmAccessStrategiesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_number: int = None,
        page_size: int = None,
        strategies: DescribeGtmAccessStrategiesResponseStrategies = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_number = page_number
        self.page_size = page_size
        self.strategies = strategies

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.strategies, 'strategies')
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Strategies') is not None:
            temp_model = DescribeGtmAccessStrategiesResponseStrategies()
            self.strategies = temp_model.from_map(m['Strategies'])
        return self


class DescribeGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeGtmAccessStrategyResponseLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeGtmAccessStrategyResponseLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeGtmAccessStrategyResponseLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeGtmAccessStrategyResponseLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        defult_addr_pool_id: str = None,
        default_addr_pool_name: str = None,
        failover_addr_pool_id: str = None,
        failover_addr_pool_name: str = None,
        strategy_mode: str = None,
        access_mode: str = None,
        access_status: str = None,
        instance_id: str = None,
        default_addr_pool_status: str = None,
        failover_addr_pool_status: str = None,
        default_addr_pool_monitor_status: str = None,
        failover_addr_pool_monitor_status: str = None,
        lines: DescribeGtmAccessStrategyResponseLines = None,
    ):
        self.request_id = request_id
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.defult_addr_pool_id = defult_addr_pool_id
        self.default_addr_pool_name = default_addr_pool_name
        self.failover_addr_pool_id = failover_addr_pool_id
        self.failover_addr_pool_name = failover_addr_pool_name
        self.strategy_mode = strategy_mode
        self.access_mode = access_mode
        self.access_status = access_status
        self.instance_id = instance_id
        self.default_addr_pool_status = default_addr_pool_status
        self.failover_addr_pool_status = failover_addr_pool_status
        self.default_addr_pool_monitor_status = default_addr_pool_monitor_status
        self.failover_addr_pool_monitor_status = failover_addr_pool_monitor_status
        self.lines = lines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.strategy_id, 'strategy_id')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.defult_addr_pool_id, 'defult_addr_pool_id')
        self.validate_required(self.default_addr_pool_name, 'default_addr_pool_name')
        self.validate_required(self.failover_addr_pool_id, 'failover_addr_pool_id')
        self.validate_required(self.failover_addr_pool_name, 'failover_addr_pool_name')
        self.validate_required(self.strategy_mode, 'strategy_mode')
        self.validate_required(self.access_mode, 'access_mode')
        self.validate_required(self.access_status, 'access_status')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.default_addr_pool_status, 'default_addr_pool_status')
        self.validate_required(self.failover_addr_pool_status, 'failover_addr_pool_status')
        self.validate_required(self.default_addr_pool_monitor_status, 'default_addr_pool_monitor_status')
        self.validate_required(self.failover_addr_pool_monitor_status, 'failover_addr_pool_monitor_status')
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.defult_addr_pool_id is not None:
            result['DefultAddrPoolId'] = self.defult_addr_pool_id
        if self.default_addr_pool_name is not None:
            result['DefaultAddrPoolName'] = self.default_addr_pool_name
        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id
        if self.failover_addr_pool_name is not None:
            result['FailoverAddrPoolName'] = self.failover_addr_pool_name
        if self.strategy_mode is not None:
            result['StrategyMode'] = self.strategy_mode
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_status is not None:
            result['AccessStatus'] = self.access_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.default_addr_pool_status is not None:
            result['DefaultAddrPoolStatus'] = self.default_addr_pool_status
        if self.failover_addr_pool_status is not None:
            result['FailoverAddrPoolStatus'] = self.failover_addr_pool_status
        if self.default_addr_pool_monitor_status is not None:
            result['DefaultAddrPoolMonitorStatus'] = self.default_addr_pool_monitor_status
        if self.failover_addr_pool_monitor_status is not None:
            result['FailoverAddrPoolMonitorStatus'] = self.failover_addr_pool_monitor_status
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('DefultAddrPoolId') is not None:
            self.defult_addr_pool_id = m.get('DefultAddrPoolId')
        if m.get('DefaultAddrPoolName') is not None:
            self.default_addr_pool_name = m.get('DefaultAddrPoolName')
        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')
        if m.get('FailoverAddrPoolName') is not None:
            self.failover_addr_pool_name = m.get('FailoverAddrPoolName')
        if m.get('StrategyMode') is not None:
            self.strategy_mode = m.get('StrategyMode')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessStatus') is not None:
            self.access_status = m.get('AccessStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DefaultAddrPoolStatus') is not None:
            self.default_addr_pool_status = m.get('DefaultAddrPoolStatus')
        if m.get('FailoverAddrPoolStatus') is not None:
            self.failover_addr_pool_status = m.get('FailoverAddrPoolStatus')
        if m.get('DefaultAddrPoolMonitorStatus') is not None:
            self.default_addr_pool_monitor_status = m.get('DefaultAddrPoolMonitorStatus')
        if m.get('FailoverAddrPoolMonitorStatus') is not None:
            self.failover_addr_pool_monitor_status = m.get('FailoverAddrPoolMonitorStatus')
        if m.get('Lines') is not None:
            temp_model = DescribeGtmAccessStrategyResponseLines()
            self.lines = temp_model.from_map(m['Lines'])
        return self


class DescribeGtmAccessStrategyAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeGtmAccessStrategyAvailableConfigResponseAddrPoolsAddrPool(TeaModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        addr_pool_name: str = None,
    ):
        self.addr_pool_id = addr_pool_id
        self.addr_pool_name = addr_pool_name

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.addr_pool_name, 'addr_pool_name')

    def to_map(self):
        result = dict()
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.addr_pool_name is not None:
            result['AddrPoolName'] = self.addr_pool_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('AddrPoolName') is not None:
            self.addr_pool_name = m.get('AddrPoolName')
        return self


class DescribeGtmAccessStrategyAvailableConfigResponseAddrPools(TeaModel):
    def __init__(
        self,
        addr_pool: List[DescribeGtmAccessStrategyAvailableConfigResponseAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        self.validate_required(self.addr_pool, 'addr_pool')
        if self.addr_pool:
            for k in self.addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k in self.addr_pool:
                result['AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k in m.get('AddrPool'):
                temp_model = DescribeGtmAccessStrategyAvailableConfigResponseAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k))
        return self


class DescribeGtmAccessStrategyAvailableConfigResponseLinesLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        line_name: str = None,
        group_code: str = None,
        group_name: str = None,
        status: str = None,
        father_code: str = None,
    ):
        self.line_code = line_code
        self.line_name = line_name
        self.group_code = group_code
        self.group_name = group_name
        self.status = status
        self.father_code = father_code

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.group_code, 'group_code')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.father_code, 'father_code')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        return self


class DescribeGtmAccessStrategyAvailableConfigResponseLines(TeaModel):
    def __init__(
        self,
        line: List[DescribeGtmAccessStrategyAvailableConfigResponseLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        self.validate_required(self.line, 'line')
        if self.line:
            for k in self.line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Line'] = []
        if self.line is not None:
            for k in self.line:
                result['Line'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k in m.get('Line'):
                temp_model = DescribeGtmAccessStrategyAvailableConfigResponseLinesLine()
                self.line.append(temp_model.from_map(k))
        return self


class DescribeGtmAccessStrategyAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_pools: DescribeGtmAccessStrategyAvailableConfigResponseAddrPools = None,
        lines: DescribeGtmAccessStrategyAvailableConfigResponseLines = None,
    ):
        self.request_id = request_id
        self.addr_pools = addr_pools
        self.lines = lines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_pools, 'addr_pools')
        if self.addr_pools:
            self.addr_pools.validate()
        self.validate_required(self.lines, 'lines')
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()
        if self.lines is not None:
            result['Lines'] = self.lines.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrPools') is not None:
            temp_model = DescribeGtmAccessStrategyAvailableConfigResponseAddrPools()
            self.addr_pools = temp_model.from_map(m['AddrPools'])
        if m.get('Lines') is not None:
            temp_model = DescribeGtmAccessStrategyAvailableConfigResponseLines()
            self.lines = temp_model.from_map(m['Lines'])
        return self


class DescribeGtmAvailableAlertGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeGtmAvailableAlertGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_alert_group: str = None,
    ):
        self.request_id = request_id
        self.available_alert_group = available_alert_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_alert_group, 'available_alert_group')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_alert_group is not None:
            result['AvailableAlertGroup'] = self.available_alert_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableAlertGroup') is not None:
            self.available_alert_group = m.get('AvailableAlertGroup')
        return self


class DescribeGtmInstanceRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        need_detail_attributes: bool = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.need_detail_attributes = need_detail_attributes

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')
        return self


class DescribeGtmInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        version_code: str = None,
        expire_time: str = None,
        expire_timestamp: int = None,
        cname: str = None,
        user_domain_name: str = None,
        ttl: int = None,
        lba_strategy: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        alert_group: str = None,
        cname_mode: str = None,
        access_strategy_num: int = None,
        address_pool_num: int = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.version_code = version_code
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.cname = cname
        self.user_domain_name = user_domain_name
        self.ttl = ttl
        self.lba_strategy = lba_strategy
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.alert_group = alert_group
        self.cname_mode = cname_mode
        self.access_strategy_num = access_strategy_num
        self.address_pool_num = address_pool_num

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expire_timestamp, 'expire_timestamp')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.user_domain_name, 'user_domain_name')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.lba_strategy, 'lba_strategy')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.alert_group, 'alert_group')
        self.validate_required(self.cname_mode, 'cname_mode')
        self.validate_required(self.access_strategy_num, 'access_strategy_num')
        self.validate_required(self.address_pool_num, 'address_pool_num')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode
        if self.access_strategy_num is not None:
            result['AccessStrategyNum'] = self.access_strategy_num
        if self.address_pool_num is not None:
            result['AddressPoolNum'] = self.address_pool_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')
        if m.get('AccessStrategyNum') is not None:
            self.access_strategy_num = m.get('AccessStrategyNum')
        if m.get('AddressPoolNum') is not None:
            self.address_pool_num = m.get('AddressPoolNum')
        return self


class DescribeGtmInstanceAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        return self


class DescribeGtmInstanceAddressPoolResponseAddrsAddr(TeaModel):
    def __init__(
        self,
        addr_id: int = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
        lba_weight: int = None,
        mode: str = None,
        alert_status: str = None,
    ):
        self.addr_id = addr_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.value = value
        self.lba_weight = lba_weight
        self.mode = mode
        self.alert_status = alert_status

    def validate(self):
        self.validate_required(self.addr_id, 'addr_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.lba_weight, 'lba_weight')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.alert_status, 'alert_status')

    def to_map(self):
        result = dict()
        if self.addr_id is not None:
            result['AddrId'] = self.addr_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrId') is not None:
            self.addr_id = m.get('AddrId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        return self


class DescribeGtmInstanceAddressPoolResponseAddrs(TeaModel):
    def __init__(
        self,
        addr: List[DescribeGtmInstanceAddressPoolResponseAddrsAddr] = None,
    ):
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = DescribeGtmInstanceAddressPoolResponseAddrsAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class DescribeGtmInstanceAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_pool_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        addr_count: int = None,
        min_available_addr_num: int = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        addrs: DescribeGtmInstanceAddressPoolResponseAddrs = None,
    ):
        self.request_id = request_id
        self.addr_pool_id = addr_pool_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.addr_count = addr_count
        self.min_available_addr_num = min_available_addr_num
        self.monitor_config_id = monitor_config_id
        self.monitor_status = monitor_status
        self.name = name
        self.status = status
        self.type = type
        self.addrs = addrs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.min_available_addr_num, 'min_available_addr_num')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.monitor_status, 'monitor_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.type, 'type')
        self.validate_required(self.addrs, 'addrs')
        if self.addrs:
            self.addrs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.addrs is not None:
            result['Addrs'] = self.addrs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Addrs') is not None:
            temp_model = DescribeGtmInstanceAddressPoolResponseAddrs()
            self.addrs = temp_model.from_map(m['Addrs'])
        return self


class DescribeGtmInstanceAddressPoolsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeGtmInstanceAddressPoolsResponseAddrPoolsAddrPool(TeaModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        addr_count: int = None,
        min_available_addr_num: int = None,
        monitor_config_id: str = None,
        monitor_status: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.addr_pool_id = addr_pool_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.addr_count = addr_count
        self.min_available_addr_num = min_available_addr_num
        self.monitor_config_id = monitor_config_id
        self.monitor_status = monitor_status
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.addr_count, 'addr_count')
        self.validate_required(self.min_available_addr_num, 'min_available_addr_num')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.monitor_status, 'monitor_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count
        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')
        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeGtmInstanceAddressPoolsResponseAddrPools(TeaModel):
    def __init__(
        self,
        addr_pool: List[DescribeGtmInstanceAddressPoolsResponseAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        self.validate_required(self.addr_pool, 'addr_pool')
        if self.addr_pool:
            for k in self.addr_pool:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k in self.addr_pool:
                result['AddrPool'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k in m.get('AddrPool'):
                temp_model = DescribeGtmInstanceAddressPoolsResponseAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k))
        return self


class DescribeGtmInstanceAddressPoolsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        page_number: int = None,
        page_size: int = None,
        addr_pools: DescribeGtmInstanceAddressPoolsResponseAddrPools = None,
    ):
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages
        self.page_number = page_number
        self.page_size = page_size
        self.addr_pools = addr_pools

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_items, 'total_items')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.addr_pools, 'addr_pools')
        if self.addr_pools:
            self.addr_pools.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AddrPools') is not None:
            temp_model = DescribeGtmInstanceAddressPoolsResponseAddrPools()
            self.addr_pools = temp_model.from_map(m['AddrPools'])
        return self


class DescribeGtmInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeGtmInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        addr_not_available_num: int = None,
        addr_pool_not_available_num: int = None,
        switch_to_failover_strategy_num: int = None,
        strategy_not_available_num: int = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.request_id = request_id
        self.addr_not_available_num = addr_not_available_num
        self.addr_pool_not_available_num = addr_pool_not_available_num
        self.switch_to_failover_strategy_num = switch_to_failover_strategy_num
        self.strategy_not_available_num = strategy_not_available_num
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.addr_not_available_num, 'addr_not_available_num')
        self.validate_required(self.addr_pool_not_available_num, 'addr_pool_not_available_num')
        self.validate_required(self.switch_to_failover_strategy_num, 'switch_to_failover_strategy_num')
        self.validate_required(self.strategy_not_available_num, 'strategy_not_available_num')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.addr_not_available_num is not None:
            result['AddrNotAvailableNum'] = self.addr_not_available_num
        if self.addr_pool_not_available_num is not None:
            result['AddrPoolNotAvailableNum'] = self.addr_pool_not_available_num
        if self.switch_to_failover_strategy_num is not None:
            result['SwitchToFailoverStrategyNum'] = self.switch_to_failover_strategy_num
        if self.strategy_not_available_num is not None:
            result['StrategyNotAvailableNum'] = self.strategy_not_available_num
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddrNotAvailableNum') is not None:
            self.addr_not_available_num = m.get('AddrNotAvailableNum')
        if m.get('AddrPoolNotAvailableNum') is not None:
            self.addr_pool_not_available_num = m.get('AddrPoolNotAvailableNum')
        if m.get('SwitchToFailoverStrategyNum') is not None:
            self.switch_to_failover_strategy_num = m.get('SwitchToFailoverStrategyNum')
        if m.get('StrategyNotAvailableNum') is not None:
            self.strategy_not_available_num = m.get('StrategyNotAvailableNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class DescribeGtmMonitorAvailableConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeGtmMonitorAvailableConfigResponseIspCityNodesIspCityNode(TeaModel):
    def __init__(
        self,
        isp_name: str = None,
        isp_code: str = None,
        city_name: str = None,
        city_code: str = None,
        default_selected: bool = None,
        mainland: bool = None,
        group_type: str = None,
        group_name: str = None,
    ):
        self.isp_name = isp_name
        self.isp_code = isp_code
        self.city_name = city_name
        self.city_code = city_code
        self.default_selected = default_selected
        self.mainland = mainland
        self.group_type = group_type
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.default_selected, 'default_selected')
        self.validate_required(self.mainland, 'mainland')
        self.validate_required(self.group_type, 'group_type')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected
        if self.mainland is not None:
            result['Mainland'] = self.mainland
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')
        if m.get('Mainland') is not None:
            self.mainland = m.get('Mainland')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeGtmMonitorAvailableConfigResponseIspCityNodes(TeaModel):
    def __init__(
        self,
        isp_city_node: List[DescribeGtmMonitorAvailableConfigResponseIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = DescribeGtmMonitorAvailableConfigResponseIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeGtmMonitorAvailableConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        isp_city_nodes: DescribeGtmMonitorAvailableConfigResponseIspCityNodes = None,
    ):
        self.request_id = request_id
        self.isp_city_nodes = isp_city_nodes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.isp_city_nodes, 'isp_city_nodes')
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IspCityNodes') is not None:
            temp_model = DescribeGtmMonitorAvailableConfigResponseIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m['IspCityNodes'])
        return self


class DescribeGtmMonitorConfigRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        return self


class DescribeGtmMonitorConfigResponseIspCityNodesIspCityNode(TeaModel):
    def __init__(
        self,
        country_name: str = None,
        country_code: str = None,
        city_name: str = None,
        city_code: str = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        self.country_name = country_name
        self.country_code = country_code
        self.city_name = city_name
        self.city_code = city_code
        self.isp_code = isp_code
        self.isp_name = isp_name

    def validate(self):
        self.validate_required(self.country_name, 'country_name')
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.city_name, 'city_name')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.isp_code, 'isp_code')
        self.validate_required(self.isp_name, 'isp_name')

    def to_map(self):
        result = dict()
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class DescribeGtmMonitorConfigResponseIspCityNodes(TeaModel):
    def __init__(
        self,
        isp_city_node: List[DescribeGtmMonitorConfigResponseIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = DescribeGtmMonitorConfigResponseIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class DescribeGtmMonitorConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_config_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_nodes: DescribeGtmMonitorConfigResponseIspCityNodes = None,
    ):
        self.request_id = request_id
        self.monitor_config_id = monitor_config_id
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_nodes = isp_city_nodes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.evaluation_count, 'evaluation_count')
        self.validate_required(self.timeout, 'timeout')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_nodes, 'isp_city_nodes')
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        if m.get('IspCityNodes') is not None:
            temp_model = DescribeGtmMonitorConfigResponseIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m['IspCityNodes'])
        return self


class UpdateGtmAccessStrategyRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        default_addr_pool_id: str = None,
        failover_addr_pool_id: str = None,
        access_lines: str = None,
    ):
        self.lang = lang
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.default_addr_pool_id = default_addr_pool_id
        self.failover_addr_pool_id = failover_addr_pool_id
        self.access_lines = access_lines

    def validate(self):
        self.validate_required(self.strategy_id, 'strategy_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.default_addr_pool_id is not None:
            result['DefaultAddrPoolId'] = self.default_addr_pool_id
        if self.failover_addr_pool_id is not None:
            result['FailoverAddrPoolId'] = self.failover_addr_pool_id
        if self.access_lines is not None:
            result['AccessLines'] = self.access_lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('DefaultAddrPoolId') is not None:
            self.default_addr_pool_id = m.get('DefaultAddrPoolId')
        if m.get('FailoverAddrPoolId') is not None:
            self.failover_addr_pool_id = m.get('FailoverAddrPoolId')
        if m.get('AccessLines') is not None:
            self.access_lines = m.get('AccessLines')
        return self


class UpdateGtmAccessStrategyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGtmAddressPoolRequestAddr(TeaModel):
    def __init__(
        self,
        value: str = None,
        lba_weight: int = None,
        mode: str = None,
    ):
        self.value = value
        self.lba_weight = lba_weight
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class UpdateGtmAddressPoolRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        addr_pool_id: str = None,
        name: str = None,
        type: str = None,
        min_available_addr_num: int = None,
        addr: List[UpdateGtmAddressPoolRequestAddr] = None,
    ):
        self.lang = lang
        self.addr_pool_id = addr_pool_id
        self.name = name
        self.type = type
        self.min_available_addr_num = min_available_addr_num
        self.addr = addr

    def validate(self):
        self.validate_required(self.addr_pool_id, 'addr_pool_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.addr, 'addr')
        if self.addr:
            for k in self.addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num
        result['Addr'] = []
        if self.addr is not None:
            for k in self.addr:
                result['Addr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')
        self.addr = []
        if m.get('Addr') is not None:
            for k in m.get('Addr'):
                temp_model = UpdateGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k))
        return self


class UpdateGtmAddressPoolResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGtmMonitorRequestIspCityNode(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        self.city_code = city_code
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.isp_code is not None:
            result['IspCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')
        return self


class UpdateGtmMonitorRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        monitor_config_id: str = None,
        protocol_type: str = None,
        interval: int = None,
        evaluation_count: int = None,
        timeout: int = None,
        monitor_extend_info: str = None,
        isp_city_node: List[UpdateGtmMonitorRequestIspCityNode] = None,
    ):
        self.lang = lang
        self.monitor_config_id = monitor_config_id
        self.protocol_type = protocol_type
        self.interval = interval
        self.evaluation_count = evaluation_count
        self.timeout = timeout
        self.monitor_extend_info = monitor_extend_info
        self.isp_city_node = isp_city_node

    def validate(self):
        self.validate_required(self.monitor_config_id, 'monitor_config_id')
        self.validate_required(self.protocol_type, 'protocol_type')
        self.validate_required(self.monitor_extend_info, 'monitor_extend_info')
        self.validate_required(self.isp_city_node, 'isp_city_node')
        if self.isp_city_node:
            for k in self.isp_city_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k in self.isp_city_node:
                result['IspCityNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k in m.get('IspCityNode'):
                temp_model = UpdateGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k))
        return self


class UpdateGtmMonitorResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDomainRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        remark: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.remark = remark

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateDomainRemarkResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDomainRecordRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
        remark: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id
        self.remark = remark

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateDomainRecordRemarkResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSupportLinesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeSupportLinesResponseRecordLinesRecordLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        father_code: str = None,
        line_name: str = None,
        line_display_name: str = None,
    ):
        self.line_code = line_code
        self.father_code = father_code
        self.line_name = line_name
        self.line_display_name = line_display_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.father_code, 'father_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.line_display_name, 'line_display_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.line_display_name is not None:
            result['LineDisplayName'] = self.line_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('LineDisplayName') is not None:
            self.line_display_name = m.get('LineDisplayName')
        return self


class DescribeSupportLinesResponseRecordLines(TeaModel):
    def __init__(
        self,
        record_line: List[DescribeSupportLinesResponseRecordLinesRecordLine] = None,
    ):
        self.record_line = record_line

    def validate(self):
        self.validate_required(self.record_line, 'record_line')
        if self.record_line:
            for k in self.record_line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RecordLine'] = []
        if self.record_line is not None:
            for k in self.record_line:
                result['RecordLine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_line = []
        if m.get('RecordLine') is not None:
            for k in m.get('RecordLine'):
                temp_model = DescribeSupportLinesResponseRecordLinesRecordLine()
                self.record_line.append(temp_model.from_map(k))
        return self


class DescribeSupportLinesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_lines: DescribeSupportLinesResponseRecordLines = None,
    ):
        self.request_id = request_id
        self.record_lines = record_lines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_lines, 'record_lines')
        if self.record_lines:
            self.record_lines.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_lines is not None:
            result['RecordLines'] = self.record_lines.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordLines') is not None:
            temp_model = DescribeSupportLinesResponseRecordLines()
            self.record_lines = temp_model.from_map(m['RecordLines'])
        return self


class DescribeDomainNsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainNsResponseDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class DescribeDomainNsResponseExpectDnsServers(TeaModel):
    def __init__(
        self,
        expect_dns_server: List[str] = None,
    ):
        self.expect_dns_server = expect_dns_server

    def validate(self):
        self.validate_required(self.expect_dns_server, 'expect_dns_server')

    def to_map(self):
        result = dict()
        if self.expect_dns_server is not None:
            result['ExpectDnsServer'] = self.expect_dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectDnsServer') is not None:
            self.expect_dns_server = m.get('ExpectDnsServer')
        return self


class DescribeDomainNsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        all_ali_dns: bool = None,
        include_ali_dns: bool = None,
        dns_servers: DescribeDomainNsResponseDnsServers = None,
        expect_dns_servers: DescribeDomainNsResponseExpectDnsServers = None,
    ):
        self.request_id = request_id
        self.all_ali_dns = all_ali_dns
        self.include_ali_dns = include_ali_dns
        self.dns_servers = dns_servers
        self.expect_dns_servers = expect_dns_servers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.all_ali_dns, 'all_ali_dns')
        self.validate_required(self.include_ali_dns, 'include_ali_dns')
        self.validate_required(self.dns_servers, 'dns_servers')
        if self.dns_servers:
            self.dns_servers.validate()
        self.validate_required(self.expect_dns_servers, 'expect_dns_servers')
        if self.expect_dns_servers:
            self.expect_dns_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.all_ali_dns is not None:
            result['AllAliDns'] = self.all_ali_dns
        if self.include_ali_dns is not None:
            result['IncludeAliDns'] = self.include_ali_dns
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()
        if self.expect_dns_servers is not None:
            result['ExpectDnsServers'] = self.expect_dns_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AllAliDns') is not None:
            self.all_ali_dns = m.get('AllAliDns')
        if m.get('IncludeAliDns') is not None:
            self.include_ali_dns = m.get('IncludeAliDns')
        if m.get('DnsServers') is not None:
            temp_model = DescribeDomainNsResponseDnsServers()
            self.dns_servers = temp_model.from_map(m['DnsServers'])
        if m.get('ExpectDnsServers') is not None:
            temp_model = DescribeDomainNsResponseExpectDnsServers()
            self.expect_dns_servers = temp_model.from_map(m['ExpectDnsServers'])
        return self


class DescribeDnsProductInstanceRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        instance_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDnsProductInstanceResponseDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class DescribeDnsProductInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        version_code: str = None,
        version_name: str = None,
        start_time: str = None,
        start_timestamp: int = None,
        end_time: str = None,
        end_timestamp: int = None,
        domain: str = None,
        bind_count: int = None,
        bind_used_count: int = None,
        ttlmin_value: int = None,
        sub_domain_level: int = None,
        dns_slbcount: int = None,
        urlforward_count: int = None,
        ddos_defend_flow: int = None,
        ddos_defend_query: int = None,
        oversea_ddos_defend_flow: int = None,
        search_engine_lines: str = None,
        isplines: str = None,
        ispregion_lines: str = None,
        oversea_line: str = None,
        monitor_node_count: int = None,
        monitor_frequency: int = None,
        monitor_task_count: int = None,
        region_lines: bool = None,
        gslb: bool = None,
        in_clean: bool = None,
        in_black_hole: bool = None,
        bind_domain_count: int = None,
        bind_domain_used_count: int = None,
        dns_security: str = None,
        payment_type: str = None,
        domain_type: str = None,
        dns_servers: DescribeDnsProductInstanceResponseDnsServers = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.version_code = version_code
        self.version_name = version_name
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        self.domain = domain
        self.bind_count = bind_count
        self.bind_used_count = bind_used_count
        self.ttlmin_value = ttlmin_value
        self.sub_domain_level = sub_domain_level
        self.dns_slbcount = dns_slbcount
        self.urlforward_count = urlforward_count
        self.ddos_defend_flow = ddos_defend_flow
        self.ddos_defend_query = ddos_defend_query
        self.oversea_ddos_defend_flow = oversea_ddos_defend_flow
        self.search_engine_lines = search_engine_lines
        self.isplines = isplines
        self.ispregion_lines = ispregion_lines
        self.oversea_line = oversea_line
        self.monitor_node_count = monitor_node_count
        self.monitor_frequency = monitor_frequency
        self.monitor_task_count = monitor_task_count
        self.region_lines = region_lines
        self.gslb = gslb
        self.in_clean = in_clean
        self.in_black_hole = in_black_hole
        self.bind_domain_count = bind_domain_count
        self.bind_domain_used_count = bind_domain_used_count
        self.dns_security = dns_security
        self.payment_type = payment_type
        self.domain_type = domain_type
        self.dns_servers = dns_servers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.start_timestamp, 'start_timestamp')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.end_timestamp, 'end_timestamp')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.bind_count, 'bind_count')
        self.validate_required(self.bind_used_count, 'bind_used_count')
        self.validate_required(self.ttlmin_value, 'ttlmin_value')
        self.validate_required(self.sub_domain_level, 'sub_domain_level')
        self.validate_required(self.dns_slbcount, 'dns_slbcount')
        self.validate_required(self.urlforward_count, 'urlforward_count')
        self.validate_required(self.ddos_defend_flow, 'ddos_defend_flow')
        self.validate_required(self.ddos_defend_query, 'ddos_defend_query')
        self.validate_required(self.oversea_ddos_defend_flow, 'oversea_ddos_defend_flow')
        self.validate_required(self.search_engine_lines, 'search_engine_lines')
        self.validate_required(self.isplines, 'isplines')
        self.validate_required(self.ispregion_lines, 'ispregion_lines')
        self.validate_required(self.oversea_line, 'oversea_line')
        self.validate_required(self.monitor_node_count, 'monitor_node_count')
        self.validate_required(self.monitor_frequency, 'monitor_frequency')
        self.validate_required(self.monitor_task_count, 'monitor_task_count')
        self.validate_required(self.region_lines, 'region_lines')
        self.validate_required(self.gslb, 'gslb')
        self.validate_required(self.in_clean, 'in_clean')
        self.validate_required(self.in_black_hole, 'in_black_hole')
        self.validate_required(self.bind_domain_count, 'bind_domain_count')
        self.validate_required(self.bind_domain_used_count, 'bind_domain_used_count')
        self.validate_required(self.dns_security, 'dns_security')
        self.validate_required(self.payment_type, 'payment_type')
        self.validate_required(self.domain_type, 'domain_type')
        self.validate_required(self.dns_servers, 'dns_servers')
        if self.dns_servers:
            self.dns_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.bind_used_count is not None:
            result['BindUsedCount'] = self.bind_used_count
        if self.ttlmin_value is not None:
            result['TTLMinValue'] = self.ttlmin_value
        if self.sub_domain_level is not None:
            result['SubDomainLevel'] = self.sub_domain_level
        if self.dns_slbcount is not None:
            result['DnsSLBCount'] = self.dns_slbcount
        if self.urlforward_count is not None:
            result['URLForwardCount'] = self.urlforward_count
        if self.ddos_defend_flow is not None:
            result['DDosDefendFlow'] = self.ddos_defend_flow
        if self.ddos_defend_query is not None:
            result['DDosDefendQuery'] = self.ddos_defend_query
        if self.oversea_ddos_defend_flow is not None:
            result['OverseaDDosDefendFlow'] = self.oversea_ddos_defend_flow
        if self.search_engine_lines is not None:
            result['SearchEngineLines'] = self.search_engine_lines
        if self.isplines is not None:
            result['ISPLines'] = self.isplines
        if self.ispregion_lines is not None:
            result['ISPRegionLines'] = self.ispregion_lines
        if self.oversea_line is not None:
            result['OverseaLine'] = self.oversea_line
        if self.monitor_node_count is not None:
            result['MonitorNodeCount'] = self.monitor_node_count
        if self.monitor_frequency is not None:
            result['MonitorFrequency'] = self.monitor_frequency
        if self.monitor_task_count is not None:
            result['MonitorTaskCount'] = self.monitor_task_count
        if self.region_lines is not None:
            result['RegionLines'] = self.region_lines
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.in_clean is not None:
            result['InClean'] = self.in_clean
        if self.in_black_hole is not None:
            result['InBlackHole'] = self.in_black_hole
        if self.bind_domain_count is not None:
            result['BindDomainCount'] = self.bind_domain_count
        if self.bind_domain_used_count is not None:
            result['BindDomainUsedCount'] = self.bind_domain_used_count
        if self.dns_security is not None:
            result['DnsSecurity'] = self.dns_security
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('BindUsedCount') is not None:
            self.bind_used_count = m.get('BindUsedCount')
        if m.get('TTLMinValue') is not None:
            self.ttlmin_value = m.get('TTLMinValue')
        if m.get('SubDomainLevel') is not None:
            self.sub_domain_level = m.get('SubDomainLevel')
        if m.get('DnsSLBCount') is not None:
            self.dns_slbcount = m.get('DnsSLBCount')
        if m.get('URLForwardCount') is not None:
            self.urlforward_count = m.get('URLForwardCount')
        if m.get('DDosDefendFlow') is not None:
            self.ddos_defend_flow = m.get('DDosDefendFlow')
        if m.get('DDosDefendQuery') is not None:
            self.ddos_defend_query = m.get('DDosDefendQuery')
        if m.get('OverseaDDosDefendFlow') is not None:
            self.oversea_ddos_defend_flow = m.get('OverseaDDosDefendFlow')
        if m.get('SearchEngineLines') is not None:
            self.search_engine_lines = m.get('SearchEngineLines')
        if m.get('ISPLines') is not None:
            self.isplines = m.get('ISPLines')
        if m.get('ISPRegionLines') is not None:
            self.ispregion_lines = m.get('ISPRegionLines')
        if m.get('OverseaLine') is not None:
            self.oversea_line = m.get('OverseaLine')
        if m.get('MonitorNodeCount') is not None:
            self.monitor_node_count = m.get('MonitorNodeCount')
        if m.get('MonitorFrequency') is not None:
            self.monitor_frequency = m.get('MonitorFrequency')
        if m.get('MonitorTaskCount') is not None:
            self.monitor_task_count = m.get('MonitorTaskCount')
        if m.get('RegionLines') is not None:
            self.region_lines = m.get('RegionLines')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('InClean') is not None:
            self.in_clean = m.get('InClean')
        if m.get('InBlackHole') is not None:
            self.in_black_hole = m.get('InBlackHole')
        if m.get('BindDomainCount') is not None:
            self.bind_domain_count = m.get('BindDomainCount')
        if m.get('BindDomainUsedCount') is not None:
            self.bind_domain_used_count = m.get('BindDomainUsedCount')
        if m.get('DnsSecurity') is not None:
            self.dns_security = m.get('DnsSecurity')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('DnsServers') is not None:
            temp_model = DescribeDnsProductInstanceResponseDnsServers()
            self.dns_servers = temp_model.from_map(m['DnsServers'])
        return self


class UpdateDomainRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
        rr: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class UpdateDomainRecordResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: str = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class UpdateDomainGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.lang = lang
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class UpdateDomainGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class UpdateDNSSLBWeightRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
        weight: int = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id
        self.weight = weight

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateDNSSLBWeightResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: str = None,
        weight: int = None,
    ):
        self.request_id = request_id
        self.record_id = record_id
        self.weight = weight

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SetDomainRecordStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id
        self.status = status

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDomainRecordStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.record_id = record_id
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetDNSSLBStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        sub_domain: str = None,
        open: bool = None,
        domain_name: str = None,
        type: str = None,
        line: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.sub_domain = sub_domain
        self.open = open
        self.domain_name = domain_name
        self.type = type
        self.line = line

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.open is not None:
            result['Open'] = self.open
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.type is not None:
            result['Type'] = self.type
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class SetDNSSLBStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_count: int = None,
        open: bool = None,
    ):
        self.request_id = request_id
        self.record_count = record_count
        self.open = open

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_count, 'record_count')
        self.validate_required(self.open, 'open')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.open is not None:
            result['Open'] = self.open
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        return self


class ModifyHichinaDomainDNSRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ModifyHichinaDomainDNSResponseOriginalDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class ModifyHichinaDomainDNSResponseNewDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class ModifyHichinaDomainDNSResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        original_dns_servers: ModifyHichinaDomainDNSResponseOriginalDnsServers = None,
        new_dns_servers: ModifyHichinaDomainDNSResponseNewDnsServers = None,
    ):
        self.request_id = request_id
        self.original_dns_servers = original_dns_servers
        self.new_dns_servers = new_dns_servers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.original_dns_servers, 'original_dns_servers')
        if self.original_dns_servers:
            self.original_dns_servers.validate()
        self.validate_required(self.new_dns_servers, 'new_dns_servers')
        if self.new_dns_servers:
            self.new_dns_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.original_dns_servers is not None:
            result['OriginalDnsServers'] = self.original_dns_servers.to_map()
        if self.new_dns_servers is not None:
            result['NewDnsServers'] = self.new_dns_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OriginalDnsServers') is not None:
            temp_model = ModifyHichinaDomainDNSResponseOriginalDnsServers()
            self.original_dns_servers = temp_model.from_map(m['OriginalDnsServers'])
        if m.get('NewDnsServers') is not None:
            temp_model = ModifyHichinaDomainDNSResponseNewDnsServers()
            self.new_dns_servers = temp_model.from_map(m['NewDnsServers'])
        return self


class GetMainDomainNameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        input_string: str = None,
    ):
        self.lang = lang
        self.input_string = input_string

    def validate(self):
        self.validate_required(self.input_string, 'input_string')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.input_string is not None:
            result['InputString'] = self.input_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InputString') is not None:
            self.input_string = m.get('InputString')
        return self


class GetMainDomainNameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
        rr: str = None,
        domain_level: int = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name
        self.rr = rr
        self.domain_level = domain_level

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.domain_level, 'domain_level')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rr is not None:
            result['RR'] = self.rr
        if self.domain_level is not None:
            result['DomainLevel'] = self.domain_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('DomainLevel') is not None:
            self.domain_level = m.get('DomainLevel')
        return self


class DescribeSubDomainRecordsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        sub_domain: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
        line: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.sub_domain = sub_domain
        self.page_number = page_number
        self.page_size = page_size
        self.type = type
        self.line = line
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        if self.line is not None:
            result['Line'] = self.line
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeSubDomainRecordsResponseDomainRecordsRecord(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        record_id: str = None,
        rr: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
        status: str = None,
        locked: bool = None,
        weight: int = None,
    ):
        self.domain_name = domain_name
        self.record_id = record_id
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line
        self.status = status
        self.locked = locked
        self.weight = weight

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.line, 'line')
        self.validate_required(self.status, 'status')
        self.validate_required(self.locked, 'locked')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        if self.status is not None:
            result['Status'] = self.status
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeSubDomainRecordsResponseDomainRecords(TeaModel):
    def __init__(
        self,
        record: List[DescribeSubDomainRecordsResponseDomainRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        self.validate_required(self.record, 'record')
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeSubDomainRecordsResponseDomainRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeSubDomainRecordsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_records: DescribeSubDomainRecordsResponseDomainRecords = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_records = domain_records

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_records, 'domain_records')
        if self.domain_records:
            self.domain_records.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_records is not None:
            result['DomainRecords'] = self.domain_records.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainRecords') is not None:
            temp_model = DescribeSubDomainRecordsResponseDomainRecords()
            self.domain_records = temp_model.from_map(m['DomainRecords'])
        return self


class DescribeRecordLogsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
        key_word: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name
        self.page_number = page_number
        self.page_size = page_size
        self.key_word = key_word
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        return self


class DescribeRecordLogsResponseRecordLogsRecordLog(TeaModel):
    def __init__(
        self,
        action_time: str = None,
        action_timestamp: int = None,
        action: str = None,
        message: str = None,
        client_ip: str = None,
    ):
        self.action_time = action_time
        self.action_timestamp = action_timestamp
        self.action = action
        self.message = message
        self.client_ip = client_ip

    def validate(self):
        self.validate_required(self.action_time, 'action_time')
        self.validate_required(self.action_timestamp, 'action_timestamp')
        self.validate_required(self.action, 'action')
        self.validate_required(self.message, 'message')
        self.validate_required(self.client_ip, 'client_ip')

    def to_map(self):
        result = dict()
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        if self.action_timestamp is not None:
            result['ActionTimestamp'] = self.action_timestamp
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        if m.get('ActionTimestamp') is not None:
            self.action_timestamp = m.get('ActionTimestamp')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        return self


class DescribeRecordLogsResponseRecordLogs(TeaModel):
    def __init__(
        self,
        record_log: List[DescribeRecordLogsResponseRecordLogsRecordLog] = None,
    ):
        self.record_log = record_log

    def validate(self):
        self.validate_required(self.record_log, 'record_log')
        if self.record_log:
            for k in self.record_log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RecordLog'] = []
        if self.record_log is not None:
            for k in self.record_log:
                result['RecordLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_log = []
        if m.get('RecordLog') is not None:
            for k in m.get('RecordLog'):
                temp_model = DescribeRecordLogsResponseRecordLogsRecordLog()
                self.record_log.append(temp_model.from_map(k))
        return self


class DescribeRecordLogsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        record_logs: DescribeRecordLogsResponseRecordLogs = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.record_logs = record_logs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.record_logs, 'record_logs')
        if self.record_logs:
            self.record_logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_logs is not None:
            result['RecordLogs'] = self.record_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordLogs') is not None:
            temp_model = DescribeRecordLogsResponseRecordLogs()
            self.record_logs = temp_model.from_map(m['RecordLogs'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        key_word: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        resource_group_id: str = None,
        starmark: bool = None,
    ):
        self.lang = lang
        self.key_word = key_word
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_mode = search_mode
        self.resource_group_id = resource_group_id
        self.starmark = starmark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.starmark is not None:
            result['Starmark'] = self.starmark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Starmark') is not None:
            self.starmark = m.get('Starmark')
        return self


class DescribeDomainsResponseDomainsDomainTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainsResponseDomainsDomainTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeDomainsResponseDomainsDomainTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDomainsResponseDomainsDomainTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseDomainsDomainDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        # DnsServer
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class DescribeDomainsResponseDomainsDomain(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
        puny_code: str = None,
        ali_domain: bool = None,
        record_count: int = None,
        registrant_email: str = None,
        remark: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        version_code: str = None,
        version_name: str = None,
        instance_end_time: str = None,
        instance_expired: bool = None,
        starmark: bool = None,
        create_time: str = None,
        create_timestamp: int = None,
        resource_group_id: str = None,
        tags: DescribeDomainsResponseDomainsDomainTags = None,
        dns_servers: DescribeDomainsResponseDomainsDomainDnsServers = None,
    ):
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.puny_code = puny_code
        self.ali_domain = ali_domain
        self.record_count = record_count
        self.registrant_email = registrant_email
        self.remark = remark
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.version_code = version_code
        self.version_name = version_name
        self.instance_end_time = instance_end_time
        self.instance_expired = instance_expired
        self.starmark = starmark
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.dns_servers = dns_servers

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.puny_code, 'puny_code')
        self.validate_required(self.ali_domain, 'ali_domain')
        self.validate_required(self.record_count, 'record_count')
        self.validate_required(self.registrant_email, 'registrant_email')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.instance_end_time, 'instance_end_time')
        self.validate_required(self.instance_expired, 'instance_expired')
        self.validate_required(self.starmark, 'starmark')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.dns_servers, 'dns_servers')
        if self.dns_servers:
            self.dns_servers.validate()

    def to_map(self):
        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code
        if self.ali_domain is not None:
            result['AliDomain'] = self.ali_domain
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.registrant_email is not None:
            result['RegistrantEmail'] = self.registrant_email
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.instance_end_time is not None:
            result['InstanceEndTime'] = self.instance_end_time
        if self.instance_expired is not None:
            result['InstanceExpired'] = self.instance_expired
        if self.starmark is not None:
            result['Starmark'] = self.starmark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')
        if m.get('AliDomain') is not None:
            self.ali_domain = m.get('AliDomain')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('RegistrantEmail') is not None:
            self.registrant_email = m.get('RegistrantEmail')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('InstanceEndTime') is not None:
            self.instance_end_time = m.get('InstanceEndTime')
        if m.get('InstanceExpired') is not None:
            self.instance_expired = m.get('InstanceExpired')
        if m.get('Starmark') is not None:
            self.starmark = m.get('Starmark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            temp_model = DescribeDomainsResponseDomainsDomainTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('DnsServers') is not None:
            temp_model = DescribeDomainsResponseDomainsDomainDnsServers()
            self.dns_servers = temp_model.from_map(m['DnsServers'])
        return self


class DescribeDomainsResponseDomains(TeaModel):
    def __init__(
        self,
        domain: List[DescribeDomainsResponseDomainsDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = DescribeDomainsResponseDomainsDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domains: DescribeDomainsResponseDomains = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domains = domains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Domains') is not None:
            temp_model = DescribeDomainsResponseDomains()
            self.domains = temp_model.from_map(m['Domains'])
        return self


class DescribeDomainRecordsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
        key_word: str = None,
        rrkey_word: str = None,
        type_key_word: str = None,
        value_key_word: str = None,
        order_by: str = None,
        direction: str = None,
        search_mode: str = None,
        group_id: int = None,
        type: str = None,
        line: str = None,
        status: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.page_number = page_number
        self.page_size = page_size
        self.key_word = key_word
        self.rrkey_word = rrkey_word
        self.type_key_word = type_key_word
        self.value_key_word = value_key_word
        self.order_by = order_by
        self.direction = direction
        self.search_mode = search_mode
        self.group_id = group_id
        self.type = type
        self.line = line
        self.status = status

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.rrkey_word is not None:
            result['RRKeyWord'] = self.rrkey_word
        if self.type_key_word is not None:
            result['TypeKeyWord'] = self.type_key_word
        if self.value_key_word is not None:
            result['ValueKeyWord'] = self.value_key_word
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.type is not None:
            result['Type'] = self.type
        if self.line is not None:
            result['Line'] = self.line
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('RRKeyWord') is not None:
            self.rrkey_word = m.get('RRKeyWord')
        if m.get('TypeKeyWord') is not None:
            self.type_key_word = m.get('TypeKeyWord')
        if m.get('ValueKeyWord') is not None:
            self.value_key_word = m.get('ValueKeyWord')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainRecordsResponseDomainRecordsRecord(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        record_id: str = None,
        rr: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
        status: str = None,
        locked: bool = None,
        weight: int = None,
        remark: str = None,
    ):
        self.domain_name = domain_name
        self.record_id = record_id
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line
        self.status = status
        self.locked = locked
        self.weight = weight
        self.remark = remark

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.line, 'line')
        self.validate_required(self.status, 'status')
        self.validate_required(self.locked, 'locked')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        if self.status is not None:
            result['Status'] = self.status
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeDomainRecordsResponseDomainRecords(TeaModel):
    def __init__(
        self,
        record: List[DescribeDomainRecordsResponseDomainRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        self.validate_required(self.record, 'record')
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeDomainRecordsResponseDomainRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeDomainRecordsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_records: DescribeDomainRecordsResponseDomainRecords = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_records = domain_records

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_records, 'domain_records')
        if self.domain_records:
            self.domain_records.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_records is not None:
            result['DomainRecords'] = self.domain_records.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainRecords') is not None:
            temp_model = DescribeDomainRecordsResponseDomainRecords()
            self.domain_records = temp_model.from_map(m['DomainRecords'])
        return self


class DescribeDomainRecordInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DescribeDomainRecordInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_id: str = None,
        domain_name: str = None,
        puny_code: str = None,
        group_id: str = None,
        group_name: str = None,
        record_id: str = None,
        rr: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
        status: str = None,
        locked: bool = None,
    ):
        self.request_id = request_id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.puny_code = puny_code
        self.group_id = group_id
        self.group_name = group_name
        self.record_id = record_id
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line
        self.status = status
        self.locked = locked

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.puny_code, 'puny_code')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.line, 'line')
        self.validate_required(self.status, 'status')
        self.validate_required(self.locked, 'locked')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        if self.status is not None:
            result['Status'] = self.status
        if self.locked is not None:
            result['Locked'] = self.locked
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        return self


class DescribeDomainLogsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        key_word: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        end_date: str = None,
        type: str = None,
    ):
        self.lang = lang
        self.key_word = key_word
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDomainLogsResponseDomainLogsDomainLog(TeaModel):
    def __init__(
        self,
        action_time: str = None,
        action_timestamp: int = None,
        domain_name: str = None,
        action: str = None,
        message: str = None,
        client_ip: str = None,
        zone_id: str = None,
    ):
        self.action_time = action_time
        self.action_timestamp = action_timestamp
        self.domain_name = domain_name
        self.action = action
        self.message = message
        self.client_ip = client_ip
        self.zone_id = zone_id

    def validate(self):
        self.validate_required(self.action_time, 'action_time')
        self.validate_required(self.action_timestamp, 'action_timestamp')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.action, 'action')
        self.validate_required(self.message, 'message')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = dict()
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        if self.action_timestamp is not None:
            result['ActionTimestamp'] = self.action_timestamp
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.action is not None:
            result['Action'] = self.action
        if self.message is not None:
            result['Message'] = self.message
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        if m.get('ActionTimestamp') is not None:
            self.action_timestamp = m.get('ActionTimestamp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDomainLogsResponseDomainLogs(TeaModel):
    def __init__(
        self,
        domain_log: List[DescribeDomainLogsResponseDomainLogsDomainLog] = None,
    ):
        self.domain_log = domain_log

    def validate(self):
        self.validate_required(self.domain_log, 'domain_log')
        if self.domain_log:
            for k in self.domain_log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainLog'] = []
        if self.domain_log is not None:
            for k in self.domain_log:
                result['DomainLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log = []
        if m.get('DomainLog') is not None:
            for k in m.get('DomainLog'):
                temp_model = DescribeDomainLogsResponseDomainLogsDomainLog()
                self.domain_log.append(temp_model.from_map(k))
        return self


class DescribeDomainLogsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_logs: DescribeDomainLogsResponseDomainLogs = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_logs = domain_logs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_logs, 'domain_logs')
        if self.domain_logs:
            self.domain_logs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_logs is not None:
            result['DomainLogs'] = self.domain_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainLogs') is not None:
            temp_model = DescribeDomainLogsResponseDomainLogs()
            self.domain_logs = temp_model.from_map(m['DomainLogs'])
        return self


class DescribeDomainInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        need_detail_attributes: bool = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.need_detail_attributes = need_detail_attributes

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.need_detail_attributes is not None:
            result['NeedDetailAttributes'] = self.need_detail_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NeedDetailAttributes') is not None:
            self.need_detail_attributes = m.get('NeedDetailAttributes')
        return self


class DescribeDomainInfoResponseRecordLinesRecordLine(TeaModel):
    def __init__(
        self,
        line_code: str = None,
        father_code: str = None,
        line_name: str = None,
        line_display_name: str = None,
    ):
        self.line_code = line_code
        self.father_code = father_code
        self.line_name = line_name
        self.line_display_name = line_display_name

    def validate(self):
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.father_code, 'father_code')
        self.validate_required(self.line_name, 'line_name')
        self.validate_required(self.line_display_name, 'line_display_name')

    def to_map(self):
        result = dict()
        if self.line_code is not None:
            result['LineCode'] = self.line_code
        if self.father_code is not None:
            result['FatherCode'] = self.father_code
        if self.line_name is not None:
            result['LineName'] = self.line_name
        if self.line_display_name is not None:
            result['LineDisplayName'] = self.line_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')
        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')
        if m.get('LineDisplayName') is not None:
            self.line_display_name = m.get('LineDisplayName')
        return self


class DescribeDomainInfoResponseRecordLines(TeaModel):
    def __init__(
        self,
        record_line: List[DescribeDomainInfoResponseRecordLinesRecordLine] = None,
    ):
        self.record_line = record_line

    def validate(self):
        self.validate_required(self.record_line, 'record_line')
        if self.record_line:
            for k in self.record_line:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RecordLine'] = []
        if self.record_line is not None:
            for k in self.record_line:
                result['RecordLine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_line = []
        if m.get('RecordLine') is not None:
            for k in m.get('RecordLine'):
                temp_model = DescribeDomainInfoResponseRecordLinesRecordLine()
                self.record_line.append(temp_model.from_map(k))
        return self


class DescribeDomainInfoResponseDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class DescribeDomainInfoResponseAvailableTtls(TeaModel):
    def __init__(
        self,
        available_ttl: List[str] = None,
    ):
        self.available_ttl = available_ttl

    def validate(self):
        self.validate_required(self.available_ttl, 'available_ttl')

    def to_map(self):
        result = dict()
        if self.available_ttl is not None:
            result['AvailableTtl'] = self.available_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableTtl') is not None:
            self.available_ttl = m.get('AvailableTtl')
        return self


class DescribeDomainInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_id: str = None,
        domain_name: str = None,
        puny_code: str = None,
        ali_domain: bool = None,
        remark: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        version_code: str = None,
        version_name: str = None,
        min_ttl: int = None,
        record_line_tree_json: str = None,
        line_type: str = None,
        region_lines: bool = None,
        in_black_hole: bool = None,
        in_clean: bool = None,
        slave_dns: bool = None,
        resource_group_id: str = None,
        create_time: str = None,
        record_lines: DescribeDomainInfoResponseRecordLines = None,
        dns_servers: DescribeDomainInfoResponseDnsServers = None,
        available_ttls: DescribeDomainInfoResponseAvailableTtls = None,
    ):
        self.request_id = request_id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.puny_code = puny_code
        self.ali_domain = ali_domain
        self.remark = remark
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.version_code = version_code
        self.version_name = version_name
        self.min_ttl = min_ttl
        self.record_line_tree_json = record_line_tree_json
        self.line_type = line_type
        self.region_lines = region_lines
        self.in_black_hole = in_black_hole
        self.in_clean = in_clean
        self.slave_dns = slave_dns
        self.resource_group_id = resource_group_id
        self.create_time = create_time
        self.record_lines = record_lines
        self.dns_servers = dns_servers
        self.available_ttls = available_ttls

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.puny_code, 'puny_code')
        self.validate_required(self.ali_domain, 'ali_domain')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.min_ttl, 'min_ttl')
        self.validate_required(self.record_line_tree_json, 'record_line_tree_json')
        self.validate_required(self.line_type, 'line_type')
        self.validate_required(self.region_lines, 'region_lines')
        self.validate_required(self.in_black_hole, 'in_black_hole')
        self.validate_required(self.in_clean, 'in_clean')
        self.validate_required(self.slave_dns, 'slave_dns')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.record_lines, 'record_lines')
        if self.record_lines:
            self.record_lines.validate()
        self.validate_required(self.dns_servers, 'dns_servers')
        if self.dns_servers:
            self.dns_servers.validate()
        self.validate_required(self.available_ttls, 'available_ttls')
        if self.available_ttls:
            self.available_ttls.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code
        if self.ali_domain is not None:
            result['AliDomain'] = self.ali_domain
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.min_ttl is not None:
            result['MinTtl'] = self.min_ttl
        if self.record_line_tree_json is not None:
            result['RecordLineTreeJson'] = self.record_line_tree_json
        if self.line_type is not None:
            result['LineType'] = self.line_type
        if self.region_lines is not None:
            result['RegionLines'] = self.region_lines
        if self.in_black_hole is not None:
            result['InBlackHole'] = self.in_black_hole
        if self.in_clean is not None:
            result['InClean'] = self.in_clean
        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.record_lines is not None:
            result['RecordLines'] = self.record_lines.to_map()
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()
        if self.available_ttls is not None:
            result['AvailableTtls'] = self.available_ttls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')
        if m.get('AliDomain') is not None:
            self.ali_domain = m.get('AliDomain')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('MinTtl') is not None:
            self.min_ttl = m.get('MinTtl')
        if m.get('RecordLineTreeJson') is not None:
            self.record_line_tree_json = m.get('RecordLineTreeJson')
        if m.get('LineType') is not None:
            self.line_type = m.get('LineType')
        if m.get('RegionLines') is not None:
            self.region_lines = m.get('RegionLines')
        if m.get('InBlackHole') is not None:
            self.in_black_hole = m.get('InBlackHole')
        if m.get('InClean') is not None:
            self.in_clean = m.get('InClean')
        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecordLines') is not None:
            temp_model = DescribeDomainInfoResponseRecordLines()
            self.record_lines = temp_model.from_map(m['RecordLines'])
        if m.get('DnsServers') is not None:
            temp_model = DescribeDomainInfoResponseDnsServers()
            self.dns_servers = temp_model.from_map(m['DnsServers'])
        if m.get('AvailableTtls') is not None:
            temp_model = DescribeDomainInfoResponseAvailableTtls()
            self.available_ttls = temp_model.from_map(m['AvailableTtls'])
        return self


class DescribeDomainGroupsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.lang = lang
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainGroupsResponseDomainGroupsDomainGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        domain_count: int = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.domain_count = domain_count

    def validate(self):
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.domain_count, 'domain_count')

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        return self


class DescribeDomainGroupsResponseDomainGroups(TeaModel):
    def __init__(
        self,
        domain_group: List[DescribeDomainGroupsResponseDomainGroupsDomainGroup] = None,
    ):
        self.domain_group = domain_group

    def validate(self):
        self.validate_required(self.domain_group, 'domain_group')
        if self.domain_group:
            for k in self.domain_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainGroup'] = []
        if self.domain_group is not None:
            for k in self.domain_group:
                result['DomainGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_group = []
        if m.get('DomainGroup') is not None:
            for k in m.get('DomainGroup'):
                temp_model = DescribeDomainGroupsResponseDomainGroupsDomainGroup()
                self.domain_group.append(temp_model.from_map(k))
        return self


class DescribeDomainGroupsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_groups: DescribeDomainGroupsResponseDomainGroups = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_groups = domain_groups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_groups, 'domain_groups')
        if self.domain_groups:
            self.domain_groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_groups is not None:
            result['DomainGroups'] = self.domain_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainGroups') is not None:
            temp_model = DescribeDomainGroupsResponseDomainGroups()
            self.domain_groups = temp_model.from_map(m['DomainGroups'])
        return self


class DescribeDNSSLBSubDomainsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
        rr: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name
        self.page_number = page_number
        self.page_size = page_size
        self.rr = rr

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rr is not None:
            result['Rr'] = self.rr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        return self


class DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm(TeaModel):
    def __init__(
        self,
        line: str = None,
        open: bool = None,
    ):
        self.line = line
        self.open = open

    def validate(self):
        self.validate_required(self.line, 'line')
        self.validate_required(self.open, 'open')

    def to_map(self):
        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        if self.open is not None:
            result['Open'] = self.open
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        return self


class DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithms(TeaModel):
    def __init__(
        self,
        line_algorithm: List[DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm] = None,
    ):
        self.line_algorithm = line_algorithm

    def validate(self):
        self.validate_required(self.line_algorithm, 'line_algorithm')
        if self.line_algorithm:
            for k in self.line_algorithm:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LineAlgorithm'] = []
        if self.line_algorithm is not None:
            for k in self.line_algorithm:
                result['LineAlgorithm'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line_algorithm = []
        if m.get('LineAlgorithm') is not None:
            for k in m.get('LineAlgorithm'):
                temp_model = DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithmsLineAlgorithm()
                self.line_algorithm.append(temp_model.from_map(k))
        return self


class DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomain(TeaModel):
    def __init__(
        self,
        sub_domain: str = None,
        record_count: int = None,
        open: bool = None,
        type: str = None,
        line_algorithms: DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithms = None,
    ):
        self.sub_domain = sub_domain
        self.record_count = record_count
        self.open = open
        self.type = type
        self.line_algorithms = line_algorithms

    def validate(self):
        self.validate_required(self.sub_domain, 'sub_domain')
        self.validate_required(self.record_count, 'record_count')
        self.validate_required(self.open, 'open')
        self.validate_required(self.type, 'type')
        self.validate_required(self.line_algorithms, 'line_algorithms')
        if self.line_algorithms:
            self.line_algorithms.validate()

    def to_map(self):
        result = dict()
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.open is not None:
            result['Open'] = self.open
        if self.type is not None:
            result['Type'] = self.type
        if self.line_algorithms is not None:
            result['LineAlgorithms'] = self.line_algorithms.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('LineAlgorithms') is not None:
            temp_model = DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomainLineAlgorithms()
            self.line_algorithms = temp_model.from_map(m['LineAlgorithms'])
        return self


class DescribeDNSSLBSubDomainsResponseSlbSubDomains(TeaModel):
    def __init__(
        self,
        slb_sub_domain: List[DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomain] = None,
    ):
        self.slb_sub_domain = slb_sub_domain

    def validate(self):
        self.validate_required(self.slb_sub_domain, 'slb_sub_domain')
        if self.slb_sub_domain:
            for k in self.slb_sub_domain:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SlbSubDomain'] = []
        if self.slb_sub_domain is not None:
            for k in self.slb_sub_domain:
                result['SlbSubDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_sub_domain = []
        if m.get('SlbSubDomain') is not None:
            for k in m.get('SlbSubDomain'):
                temp_model = DescribeDNSSLBSubDomainsResponseSlbSubDomainsSlbSubDomain()
                self.slb_sub_domain.append(temp_model.from_map(k))
        return self


class DescribeDNSSLBSubDomainsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        slb_sub_domains: DescribeDNSSLBSubDomainsResponseSlbSubDomains = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.slb_sub_domains = slb_sub_domains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.slb_sub_domains, 'slb_sub_domains')
        if self.slb_sub_domains:
            self.slb_sub_domains.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.slb_sub_domains is not None:
            result['SlbSubDomains'] = self.slb_sub_domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SlbSubDomains') is not None:
            temp_model = DescribeDNSSLBSubDomainsResponseSlbSubDomains()
            self.slb_sub_domains = temp_model.from_map(m['SlbSubDomains'])
        return self


class DescribeDnsProductInstancesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        version_code: str = None,
        domain_type: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.page_number = page_number
        self.page_size = page_size
        self.version_code = version_code
        self.domain_type = domain_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeDnsProductInstancesResponseDnsProductsDnsProduct(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version_code: str = None,
        version_name: str = None,
        start_time: str = None,
        end_time: str = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
        domain: str = None,
        bind_count: int = None,
        bind_used_count: int = None,
        ttlmin_value: int = None,
        sub_domain_level: int = None,
        dns_slbcount: int = None,
        urlforward_count: int = None,
        ddos_defend_flow: int = None,
        ddos_defend_query: int = None,
        oversea_ddos_defend_flow: int = None,
        search_engine_lines: str = None,
        isplines: str = None,
        ispregion_lines: str = None,
        oversea_line: str = None,
        monitor_node_count: int = None,
        monitor_frequency: int = None,
        monitor_task_count: int = None,
        region_lines: bool = None,
        gslb: bool = None,
        in_clean: bool = None,
        in_black_hole: bool = None,
        bind_domain_count: int = None,
        bind_domain_used_count: int = None,
        dns_security: str = None,
        payment_type: str = None,
    ):
        self.instance_id = instance_id
        self.version_code = version_code
        self.version_name = version_name
        self.start_time = start_time
        self.end_time = end_time
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.domain = domain
        self.bind_count = bind_count
        self.bind_used_count = bind_used_count
        self.ttlmin_value = ttlmin_value
        self.sub_domain_level = sub_domain_level
        self.dns_slbcount = dns_slbcount
        self.urlforward_count = urlforward_count
        self.ddos_defend_flow = ddos_defend_flow
        self.ddos_defend_query = ddos_defend_query
        self.oversea_ddos_defend_flow = oversea_ddos_defend_flow
        self.search_engine_lines = search_engine_lines
        self.isplines = isplines
        self.ispregion_lines = ispregion_lines
        self.oversea_line = oversea_line
        self.monitor_node_count = monitor_node_count
        self.monitor_frequency = monitor_frequency
        self.monitor_task_count = monitor_task_count
        self.region_lines = region_lines
        self.gslb = gslb
        self.in_clean = in_clean
        self.in_black_hole = in_black_hole
        self.bind_domain_count = bind_domain_count
        self.bind_domain_used_count = bind_domain_used_count
        self.dns_security = dns_security
        self.payment_type = payment_type

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.version_code, 'version_code')
        self.validate_required(self.version_name, 'version_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_timestamp, 'start_timestamp')
        self.validate_required(self.end_timestamp, 'end_timestamp')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.bind_count, 'bind_count')
        self.validate_required(self.bind_used_count, 'bind_used_count')
        self.validate_required(self.ttlmin_value, 'ttlmin_value')
        self.validate_required(self.sub_domain_level, 'sub_domain_level')
        self.validate_required(self.dns_slbcount, 'dns_slbcount')
        self.validate_required(self.urlforward_count, 'urlforward_count')
        self.validate_required(self.ddos_defend_flow, 'ddos_defend_flow')
        self.validate_required(self.ddos_defend_query, 'ddos_defend_query')
        self.validate_required(self.oversea_ddos_defend_flow, 'oversea_ddos_defend_flow')
        self.validate_required(self.search_engine_lines, 'search_engine_lines')
        self.validate_required(self.isplines, 'isplines')
        self.validate_required(self.ispregion_lines, 'ispregion_lines')
        self.validate_required(self.oversea_line, 'oversea_line')
        self.validate_required(self.monitor_node_count, 'monitor_node_count')
        self.validate_required(self.monitor_frequency, 'monitor_frequency')
        self.validate_required(self.monitor_task_count, 'monitor_task_count')
        self.validate_required(self.region_lines, 'region_lines')
        self.validate_required(self.gslb, 'gslb')
        self.validate_required(self.in_clean, 'in_clean')
        self.validate_required(self.in_black_hole, 'in_black_hole')
        self.validate_required(self.bind_domain_count, 'bind_domain_count')
        self.validate_required(self.bind_domain_used_count, 'bind_domain_used_count')
        self.validate_required(self.dns_security, 'dns_security')
        self.validate_required(self.payment_type, 'payment_type')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.bind_used_count is not None:
            result['BindUsedCount'] = self.bind_used_count
        if self.ttlmin_value is not None:
            result['TTLMinValue'] = self.ttlmin_value
        if self.sub_domain_level is not None:
            result['SubDomainLevel'] = self.sub_domain_level
        if self.dns_slbcount is not None:
            result['DnsSLBCount'] = self.dns_slbcount
        if self.urlforward_count is not None:
            result['URLForwardCount'] = self.urlforward_count
        if self.ddos_defend_flow is not None:
            result['DDosDefendFlow'] = self.ddos_defend_flow
        if self.ddos_defend_query is not None:
            result['DDosDefendQuery'] = self.ddos_defend_query
        if self.oversea_ddos_defend_flow is not None:
            result['OverseaDDosDefendFlow'] = self.oversea_ddos_defend_flow
        if self.search_engine_lines is not None:
            result['SearchEngineLines'] = self.search_engine_lines
        if self.isplines is not None:
            result['ISPLines'] = self.isplines
        if self.ispregion_lines is not None:
            result['ISPRegionLines'] = self.ispregion_lines
        if self.oversea_line is not None:
            result['OverseaLine'] = self.oversea_line
        if self.monitor_node_count is not None:
            result['MonitorNodeCount'] = self.monitor_node_count
        if self.monitor_frequency is not None:
            result['MonitorFrequency'] = self.monitor_frequency
        if self.monitor_task_count is not None:
            result['MonitorTaskCount'] = self.monitor_task_count
        if self.region_lines is not None:
            result['RegionLines'] = self.region_lines
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.in_clean is not None:
            result['InClean'] = self.in_clean
        if self.in_black_hole is not None:
            result['InBlackHole'] = self.in_black_hole
        if self.bind_domain_count is not None:
            result['BindDomainCount'] = self.bind_domain_count
        if self.bind_domain_used_count is not None:
            result['BindDomainUsedCount'] = self.bind_domain_used_count
        if self.dns_security is not None:
            result['DnsSecurity'] = self.dns_security
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('BindUsedCount') is not None:
            self.bind_used_count = m.get('BindUsedCount')
        if m.get('TTLMinValue') is not None:
            self.ttlmin_value = m.get('TTLMinValue')
        if m.get('SubDomainLevel') is not None:
            self.sub_domain_level = m.get('SubDomainLevel')
        if m.get('DnsSLBCount') is not None:
            self.dns_slbcount = m.get('DnsSLBCount')
        if m.get('URLForwardCount') is not None:
            self.urlforward_count = m.get('URLForwardCount')
        if m.get('DDosDefendFlow') is not None:
            self.ddos_defend_flow = m.get('DDosDefendFlow')
        if m.get('DDosDefendQuery') is not None:
            self.ddos_defend_query = m.get('DDosDefendQuery')
        if m.get('OverseaDDosDefendFlow') is not None:
            self.oversea_ddos_defend_flow = m.get('OverseaDDosDefendFlow')
        if m.get('SearchEngineLines') is not None:
            self.search_engine_lines = m.get('SearchEngineLines')
        if m.get('ISPLines') is not None:
            self.isplines = m.get('ISPLines')
        if m.get('ISPRegionLines') is not None:
            self.ispregion_lines = m.get('ISPRegionLines')
        if m.get('OverseaLine') is not None:
            self.oversea_line = m.get('OverseaLine')
        if m.get('MonitorNodeCount') is not None:
            self.monitor_node_count = m.get('MonitorNodeCount')
        if m.get('MonitorFrequency') is not None:
            self.monitor_frequency = m.get('MonitorFrequency')
        if m.get('MonitorTaskCount') is not None:
            self.monitor_task_count = m.get('MonitorTaskCount')
        if m.get('RegionLines') is not None:
            self.region_lines = m.get('RegionLines')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('InClean') is not None:
            self.in_clean = m.get('InClean')
        if m.get('InBlackHole') is not None:
            self.in_black_hole = m.get('InBlackHole')
        if m.get('BindDomainCount') is not None:
            self.bind_domain_count = m.get('BindDomainCount')
        if m.get('BindDomainUsedCount') is not None:
            self.bind_domain_used_count = m.get('BindDomainUsedCount')
        if m.get('DnsSecurity') is not None:
            self.dns_security = m.get('DnsSecurity')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class DescribeDnsProductInstancesResponseDnsProducts(TeaModel):
    def __init__(
        self,
        dns_product: List[DescribeDnsProductInstancesResponseDnsProductsDnsProduct] = None,
    ):
        self.dns_product = dns_product

    def validate(self):
        self.validate_required(self.dns_product, 'dns_product')
        if self.dns_product:
            for k in self.dns_product:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DnsProduct'] = []
        if self.dns_product is not None:
            for k in self.dns_product:
                result['DnsProduct'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_product = []
        if m.get('DnsProduct') is not None:
            for k in m.get('DnsProduct'):
                temp_model = DescribeDnsProductInstancesResponseDnsProductsDnsProduct()
                self.dns_product.append(temp_model.from_map(k))
        return self


class DescribeDnsProductInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        domain_type: str = None,
        dns_products: DescribeDnsProductInstancesResponseDnsProducts = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.domain_type = domain_type
        self.dns_products = dns_products

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.domain_type, 'domain_type')
        self.validate_required(self.dns_products, 'dns_products')
        if self.dns_products:
            self.dns_products.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.dns_products is not None:
            result['DnsProducts'] = self.dns_products.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('DnsProducts') is not None:
            temp_model = DescribeDnsProductInstancesResponseDnsProducts()
            self.dns_products = temp_model.from_map(m['DnsProducts'])
        return self


class DeleteSubDomainRecordsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
        rr: str = None,
        type: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name
        self.rr = rr
        self.type = type

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rr, 'rr')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteSubDomainRecordsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rr: str = None,
        total_count: str = None,
    ):
        self.request_id = request_id
        self.rr = rr
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rr is not None:
            result['RR'] = self.rr
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteDomainRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        record_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteDomainRecordResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: str = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteDomainGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        group_id: str = None,
    ):
        self.lang = lang
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteDomainGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_name: str = None,
    ):
        self.request_id = request_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_name: str = None,
    ):
        self.request_id = request_id
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ChangeDomainOfDnsProductRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        instance_id: str = None,
        new_domain: str = None,
        force: bool = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.instance_id = instance_id
        self.new_domain = new_domain
        self.force = force

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.new_domain is not None:
            result['NewDomain'] = self.new_domain
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NewDomain') is not None:
            self.new_domain = m.get('NewDomain')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class ChangeDomainOfDnsProductResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        original_domain: str = None,
    ):
        self.request_id = request_id
        self.original_domain = original_domain

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.original_domain, 'original_domain')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.original_domain is not None:
            result['OriginalDomain'] = self.original_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OriginalDomain') is not None:
            self.original_domain = m.get('OriginalDomain')
        return self


class ChangeDomainGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ChangeDomainGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddDomainRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        domain_name: str = None,
        rr: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        priority: int = None,
        line: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.domain_name = domain_name
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.priority = priority
        self.line = line

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rr, 'rr')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.rr is not None:
            result['RR'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RR') is not None:
            self.rr = m.get('RR')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class AddDomainRecordResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: str = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class AddDomainGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        group_name: str = None,
    ):
        self.lang = lang
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddDomainGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddDomainRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        domain_name: str = None,
        group_id: str = None,
        resource_group_id: str = None,
    ):
        self.lang = lang
        self.domain_name = domain_name
        self.group_id = group_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AddDomainResponseDnsServers(TeaModel):
    def __init__(
        self,
        dns_server: List[str] = None,
    ):
        self.dns_server = dns_server

    def validate(self):
        self.validate_required(self.dns_server, 'dns_server')

    def to_map(self):
        result = dict()
        if self.dns_server is not None:
            result['DnsServer'] = self.dns_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServer') is not None:
            self.dns_server = m.get('DnsServer')
        return self


class AddDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_id: str = None,
        domain_name: str = None,
        puny_code: str = None,
        group_id: str = None,
        group_name: str = None,
        dns_servers: AddDomainResponseDnsServers = None,
    ):
        self.request_id = request_id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.puny_code = puny_code
        self.group_id = group_id
        self.group_name = group_name
        self.dns_servers = dns_servers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.puny_code, 'puny_code')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.dns_servers, 'dns_servers')
        if self.dns_servers:
            self.dns_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('DnsServers') is not None:
            temp_model = AddDomainResponseDnsServers()
            self.dns_servers = temp_model.from_map(m['DnsServers'])
        return self


