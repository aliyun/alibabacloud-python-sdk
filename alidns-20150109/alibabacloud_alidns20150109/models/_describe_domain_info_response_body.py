# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainInfoResponseBody(DaraModel):
    def __init__(
        self,
        ali_domain: bool = None,
        available_ttls: main_models.DescribeDomainInfoResponseBodyAvailableTtls = None,
        create_time: str = None,
        dns_servers: main_models.DescribeDomainInfoResponseBodyDnsServers = None,
        domain_id: str = None,
        domain_logging_switch_status: str = None,
        domain_name: str = None,
        group_id: str = None,
        group_name: str = None,
        in_black_hole: bool = None,
        in_clean: bool = None,
        instance_id: str = None,
        line_type: str = None,
        min_ttl: int = None,
        puny_code: str = None,
        record_line_tree_json: str = None,
        record_lines: main_models.DescribeDomainInfoResponseBodyRecordLines = None,
        region_lines: bool = None,
        remark: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        slave_dns: bool = None,
        sub_domain: bool = None,
        version_code: str = None,
        version_name: str = None,
    ):
        # Indicates whether the domain name was registered in Alibaba Cloud.
        self.ali_domain = ali_domain
        # The available time to live (TTL) values that can be configured for the domain name. Available TTL values are not returned by default. If you want to query such information, set NeedDetailAttributes to true.
        self.available_ttls = available_ttls
        # The time when the domain name was created.
        self.create_time = create_time
        # The DNS servers that are used to resolve the domain name.
        self.dns_servers = dns_servers
        # The ID of the domain name.
        self.domain_id = domain_id
        # Indicates whether the DNS traffic analysis feature is enabled. Valid values:
        self.domain_logging_switch_status = domain_logging_switch_status
        # The domain name.
        self.domain_name = domain_name
        # The ID of the domain name group.
        self.group_id = group_id
        # The name of the domain name group.
        self.group_name = group_name
        # Indicates whether blackhole filtering was triggered.
        self.in_black_hole = in_black_hole
        # Indicates whether traffic scrubbing was in progress.
        self.in_clean = in_clean
        # The ID of the Alibaba Cloud DNS instance.
        self.instance_id = instance_id
        # The type of the DNS request line.
        self.line_type = line_type
        # The minimum TTL value.
        self.min_ttl = min_ttl
        # The Punycode for the domain name. This parameter is returned only for Chinese domain names.
        self.puny_code = puny_code
        # The tree-structure DNS request lines.
        self.record_line_tree_json = record_line_tree_json
        # The DNS request lines.
        self.record_lines = record_lines
        # Indicates whether the DNS request lines are regional lines.
        self.region_lines = region_lines
        # The description.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether secondary DNS is supported.
        self.slave_dns = slave_dns
        # Indicates whether the queried domain name is a hosted subdomain name. Valid values:
        # 
        # *   true
        # *   false
        self.sub_domain = sub_domain
        # The version ID of Alibaba Cloud DNS.
        self.version_code = version_code
        # The edition of Alibaba Cloud DNS.
        self.version_name = version_name

    def validate(self):
        if self.available_ttls:
            self.available_ttls.validate()
        if self.dns_servers:
            self.dns_servers.validate()
        if self.record_lines:
            self.record_lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_domain is not None:
            result['AliDomain'] = self.ali_domain

        if self.available_ttls is not None:
            result['AvailableTtls'] = self.available_ttls.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.in_black_hole is not None:
            result['InBlackHole'] = self.in_black_hole

        if self.in_clean is not None:
            result['InClean'] = self.in_clean

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line_type is not None:
            result['LineType'] = self.line_type

        if self.min_ttl is not None:
            result['MinTtl'] = self.min_ttl

        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code

        if self.record_line_tree_json is not None:
            result['RecordLineTreeJson'] = self.record_line_tree_json

        if self.record_lines is not None:
            result['RecordLines'] = self.record_lines.to_map()

        if self.region_lines is not None:
            result['RegionLines'] = self.region_lines

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliDomain') is not None:
            self.ali_domain = m.get('AliDomain')

        if m.get('AvailableTtls') is not None:
            temp_model = main_models.DescribeDomainInfoResponseBodyAvailableTtls()
            self.available_ttls = temp_model.from_map(m.get('AvailableTtls'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DnsServers') is not None:
            temp_model = main_models.DescribeDomainInfoResponseBodyDnsServers()
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

        if m.get('InBlackHole') is not None:
            self.in_black_hole = m.get('InBlackHole')

        if m.get('InClean') is not None:
            self.in_clean = m.get('InClean')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LineType') is not None:
            self.line_type = m.get('LineType')

        if m.get('MinTtl') is not None:
            self.min_ttl = m.get('MinTtl')

        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')

        if m.get('RecordLineTreeJson') is not None:
            self.record_line_tree_json = m.get('RecordLineTreeJson')

        if m.get('RecordLines') is not None:
            temp_model = main_models.DescribeDomainInfoResponseBodyRecordLines()
            self.record_lines = temp_model.from_map(m.get('RecordLines'))

        if m.get('RegionLines') is not None:
            self.region_lines = m.get('RegionLines')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class DescribeDomainInfoResponseBodyRecordLines(DaraModel):
    def __init__(
        self,
        record_line: List[main_models.DescribeDomainInfoResponseBodyRecordLinesRecordLine] = None,
    ):
        self.record_line = record_line

    def validate(self):
        if self.record_line:
            for v1 in self.record_line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordLine'] = []
        if self.record_line is not None:
            for k1 in self.record_line:
                result['RecordLine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_line = []
        if m.get('RecordLine') is not None:
            for k1 in m.get('RecordLine'):
                temp_model = main_models.DescribeDomainInfoResponseBodyRecordLinesRecordLine()
                self.record_line.append(temp_model.from_map(k1))

        return self

class DescribeDomainInfoResponseBodyRecordLinesRecordLine(DaraModel):
    def __init__(
        self,
        father_code: str = None,
        line_code: str = None,
        line_display_name: str = None,
        line_name: str = None,
    ):
        # The code of the parent line. This parameter is not returned if the line has no parent line.
        self.father_code = father_code
        # The code of the line.
        self.line_code = line_code
        # The name of the parent line.
        self.line_display_name = line_display_name
        # The name of the line.
        self.line_name = line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.father_code is not None:
            result['FatherCode'] = self.father_code

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_display_name is not None:
            result['LineDisplayName'] = self.line_display_name

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineDisplayName') is not None:
            self.line_display_name = m.get('LineDisplayName')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

class DescribeDomainInfoResponseBodyDnsServers(DaraModel):
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

class DescribeDomainInfoResponseBodyAvailableTtls(DaraModel):
    def __init__(
        self,
        available_ttl: List[str] = None,
    ):
        self.available_ttl = available_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ttl is not None:
            result['AvailableTtl'] = self.available_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableTtl') is not None:
            self.available_ttl = m.get('AvailableTtl')

        return self

