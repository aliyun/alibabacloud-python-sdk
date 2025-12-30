# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: main_models.DescribeDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names.
        self.domains = domains
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of domain names.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

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
        if m.get('Domains') is not None:
            temp_model = main_models.DescribeDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        domain: List[main_models.DescribeDomainsResponseBodyDomainsDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for v1 in self.domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domain'] = []
        if self.domain is not None:
            for k1 in self.domain:
                result['Domain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k1 in m.get('Domain'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsDomain()
                self.domain.append(temp_model.from_map(k1))

        return self

class DescribeDomainsResponseBodyDomainsDomain(DaraModel):
    def __init__(
        self,
        ali_domain: bool = None,
        create_time: str = None,
        create_timestamp: int = None,
        dns_servers: main_models.DescribeDomainsResponseBodyDomainsDomainDnsServers = None,
        domain_id: str = None,
        domain_logging_switch_status: str = None,
        domain_name: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_end_time: str = None,
        instance_expired: bool = None,
        instance_id: str = None,
        puny_code: str = None,
        record_count: int = None,
        registrant_email: str = None,
        remark: str = None,
        resource_group_id: str = None,
        slave_dns_status: str = None,
        starmark: bool = None,
        tags: main_models.DescribeDomainsResponseBodyDomainsDomainTags = None,
        version_code: str = None,
        version_name: str = None,
    ):
        # Indicates whether the domain name was registered with Alibaba Cloud.
        self.ali_domain = ali_domain
        # The time when the domain name was added. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the domain name was added. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The names of the DNS servers configured for the domain name assigned by Alibaba Cloud DNS.
        self.dns_servers = dns_servers
        # The ID of the domain name.
        self.domain_id = domain_id
        # Indicates whether the DNS traffic analysis feature is enabled for the domain name. Valid values:
        # 
        # *   OPEN
        # *   CLOSE
        self.domain_logging_switch_status = domain_logging_switch_status
        # The domain name.
        self.domain_name = domain_name
        # The ID of the domain name group.
        self.group_id = group_id
        # The name of the domain name group.
        self.group_name = group_name
        # The time when the Alibaba Cloud DNS instance expires. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.instance_end_time = instance_end_time
        # Indicates whether the Alibaba Cloud DNS instance expires.
        self.instance_expired = instance_expired
        # The ID of the Alibaba Cloud DNS instance.
        self.instance_id = instance_id
        # The Punycode for the domain name. This parameter is returned only for Chinese domain names.
        self.puny_code = puny_code
        # The number of Domain Name System (DNS) records added for the domain name.
        self.record_count = record_count
        # The email address of the registrant.
        self.registrant_email = registrant_email
        # The description of the domain name.
        self.remark = remark
        # The ID of the resource group to which the domain name belongs.
        self.resource_group_id = resource_group_id
        self.slave_dns_status = slave_dns_status
        # Indicates whether the domain name was added to favorites.
        self.starmark = starmark
        # The tags added to the resource.
        self.tags = tags
        # The edition code of Alibaba Cloud DNS.
        self.version_code = version_code
        # The edition of Alibaba Cloud DNS.
        self.version_name = version_name

    def validate(self):
        if self.dns_servers:
            self.dns_servers.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_domain is not None:
            result['AliDomain'] = self.ali_domain

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_logging_switch_status is not None:
            result['DomainLoggingSwitchStatus'] = self.domain_logging_switch_status

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_end_time is not None:
            result['InstanceEndTime'] = self.instance_end_time

        if self.instance_expired is not None:
            result['InstanceExpired'] = self.instance_expired

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.registrant_email is not None:
            result['RegistrantEmail'] = self.registrant_email

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_dns_status is not None:
            result['SlaveDnsStatus'] = self.slave_dns_status

        if self.starmark is not None:
            result['Starmark'] = self.starmark

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliDomain') is not None:
            self.ali_domain = m.get('AliDomain')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DnsServers') is not None:
            temp_model = main_models.DescribeDomainsResponseBodyDomainsDomainDnsServers()
            self.dns_servers = temp_model.from_map(m.get('DnsServers'))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainLoggingSwitchStatus') is not None:
            self.domain_logging_switch_status = m.get('DomainLoggingSwitchStatus')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceEndTime') is not None:
            self.instance_end_time = m.get('InstanceEndTime')

        if m.get('InstanceExpired') is not None:
            self.instance_expired = m.get('InstanceExpired')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('RegistrantEmail') is not None:
            self.registrant_email = m.get('RegistrantEmail')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDnsStatus') is not None:
            self.slave_dns_status = m.get('SlaveDnsStatus')

        if m.get('Starmark') is not None:
            self.starmark = m.get('Starmark')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDomainsResponseBodyDomainsDomainTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class DescribeDomainsResponseBodyDomainsDomainTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDomainsResponseBodyDomainsDomainTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDomainsResponseBodyDomainsDomainTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDomainsResponseBodyDomainsDomainTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeDomainsResponseBodyDomainsDomainDnsServers(DaraModel):
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

