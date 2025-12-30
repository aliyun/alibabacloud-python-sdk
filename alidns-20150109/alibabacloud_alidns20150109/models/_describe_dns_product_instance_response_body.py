# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsProductInstanceResponseBody(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        bind_count: int = None,
        bind_domain_count: int = None,
        bind_domain_used_count: int = None,
        bind_used_count: int = None,
        ddos_defend_flow: int = None,
        ddos_defend_query: int = None,
        dns_slbcount: int = None,
        dns_security: str = None,
        dns_servers: main_models.DescribeDnsProductInstanceResponseBodyDnsServers = None,
        domain: str = None,
        domain_type: str = None,
        end_time: str = None,
        end_timestamp: int = None,
        gslb: bool = None,
        isplines: str = None,
        ispregion_lines: str = None,
        in_black_hole: bool = None,
        in_clean: bool = None,
        instance_id: str = None,
        monitor_frequency: int = None,
        monitor_node_count: int = None,
        monitor_task_count: int = None,
        oversea_ddos_defend_flow: int = None,
        oversea_line: str = None,
        payment_type: str = None,
        region_lines: bool = None,
        request_id: str = None,
        search_engine_lines: str = None,
        start_time: str = None,
        start_timestamp: int = None,
        sub_domain_level: int = None,
        ttlmin_value: int = None,
        urlforward_count: int = None,
        version_code: str = None,
        version_name: str = None,
    ):
        # Indicates whether auto-renewal was enabled. Valid values:
        # 
        # *   true: Auto-renewal was enabled.
        # *   false: Auto-renewal was not enabled.
        self.auto_renewal = auto_renewal
        # The number of times that you can change the domain names that are bound to the paid Alibaba Cloud DNS instance. This parameter applies to Alibaba Cloud DNS instances of the custom edition.
        self.bind_count = bind_count
        # The number of domain names that can be bound to the paid Alibaba Cloud DNS instance. This parameter applies to Alibaba Cloud DNS instances of Personal Edition, Enterprise Standard Edition, and Enterprise Ultimate Edition.
        self.bind_domain_count = bind_domain_count
        # The number of domain names that are bound to the paid Alibaba Cloud DNS instance. This parameter applies to Alibaba Cloud DNS instances of Personal Edition, Enterprise Standard Edition, and Enterprise Ultimate Edition.
        self.bind_domain_used_count = bind_domain_used_count
        # The number of times that you have changed the domain names that are bound to the paid Alibaba Cloud DNS instance. This parameter applies to Alibaba Cloud DNS instances of the custom edition.
        self.bind_used_count = bind_used_count
        # The DDoS protection traffic. Unit: GB.
        self.ddos_defend_flow = ddos_defend_flow
        # The DDoS protection frequency. Unit: 10,000 QPS. This parameter applies to Alibaba Cloud DNS instances of the custom edition.
        self.ddos_defend_query = ddos_defend_query
        # The maximum number of IP addresses that are used for load balancing in a single line of a domain name.
        self.dns_slbcount = dns_slbcount
        # The level of DNS protection. Valid values:
        # 
        # *   no: No DNS protection is provided.
        # *   basic: Basic DNS protection is provided.
        # *   advanced: Advanced DNS protection is provided.
        self.dns_security = dns_security
        # The DNS servers configured for the domain names.
        self.dns_servers = dns_servers
        # The domain name that is bound to the paid instance.
        # 
        # If no value is returned for this parameter, no domain name is bound to the paid instance.
        self.domain = domain
        # The type of the instance. Valid values:
        # 
        # *   PUBLIC: authoritative domain name
        # *   CACHE: cache-accelerated domain name
        self.domain_type = domain_type
        # The time when the instance expired. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The time when the instance expired. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_timestamp = end_timestamp
        # Indicates whether global server load balancing (GSLB) is supported. Valid values:
        # 
        # *   true: GSLB is supported.
        # *   false: GSLB is not supported.
        self.gslb = gslb
        # The ISP resolution lines. Valid values:
        # 
        # *   China Telecom
        # *   China Mobile
        # *   China Unicom
        # *   China Education and Research Network (CERNET)
        # *   China Broadcasting Network (CBN)
        # *   Dr Peng Telecom & Media Group
        self.isplines = isplines
        # The regional ISP resolution lines. Valid values:
        # 
        # *   China Telecom (province)
        # *   China Mobile (province)
        # *   China Unicom (province)
        # *   CERNET (province)
        self.ispregion_lines = ispregion_lines
        # Indicates whether the Domain Name System (DNS) servers stopped responding to all DNS requests. Valid values:
        # 
        # *   true: The DNS servers stopped responding to all DNS requests.
        # *   false: The DNS servers did not stop responding to all DNS requests.
        self.in_black_hole = in_black_hole
        # Indicates whether the DNS servers stopped responding to abnormal requests sent to the domain names.
        # 
        # *   true: The DNS servers stopped responding to abnormal requests sent to the domain names.
        # *   false: The DNS servers did not stop responding to abnormal requests sent to the domain names.
        self.in_clean = in_clean
        # The ID of the Alibaba Cloud DNS instance.
        self.instance_id = instance_id
        # The interval at which the instance is monitored. Unit: minutes.
        self.monitor_frequency = monitor_frequency
        # The number of monitoring nodes.
        self.monitor_node_count = monitor_node_count
        # The number of monitoring tasks.
        self.monitor_task_count = monitor_task_count
        # The DDoS protection traffic outside the Chinese mainland. Unit: GB.
        self.oversea_ddos_defend_flow = oversea_ddos_defend_flow
        # The line outside the Chinese mainland.
        self.oversea_line = oversea_line
        # The billing method.
        self.payment_type = payment_type
        # Indicates whether the DNS request lines are regional lines. Valid values:
        # 
        # *   true: The DNS request lines are regional lines.
        # *   false: The DNS request lines are not regional lines.
        self.region_lines = region_lines
        # The request ID.
        self.request_id = request_id
        # The search engine resolution lines. Valid values:
        # 
        # *   Google
        # *   Baidu
        # *   Bing
        # *   Youdao
        self.search_engine_lines = search_engine_lines
        # The time when the instance was purchased. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The time when the instance was purchased. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_timestamp = start_timestamp
        # The number of subdomain name levels.
        self.sub_domain_level = sub_domain_level
        # The minimum time-to-live (TTL) period. Unit: seconds.
        self.ttlmin_value = ttlmin_value
        # The number of the forwarded URLs.
        self.urlforward_count = urlforward_count
        # The version code of Alibaba Cloud DNS.
        self.version_code = version_code
        # The edition of Alibaba Cloud DNS.
        self.version_name = version_name

    def validate(self):
        if self.dns_servers:
            self.dns_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.bind_domain_count is not None:
            result['BindDomainCount'] = self.bind_domain_count

        if self.bind_domain_used_count is not None:
            result['BindDomainUsedCount'] = self.bind_domain_used_count

        if self.bind_used_count is not None:
            result['BindUsedCount'] = self.bind_used_count

        if self.ddos_defend_flow is not None:
            result['DDosDefendFlow'] = self.ddos_defend_flow

        if self.ddos_defend_query is not None:
            result['DDosDefendQuery'] = self.ddos_defend_query

        if self.dns_slbcount is not None:
            result['DnsSLBCount'] = self.dns_slbcount

        if self.dns_security is not None:
            result['DnsSecurity'] = self.dns_security

        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers.to_map()

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.gslb is not None:
            result['Gslb'] = self.gslb

        if self.isplines is not None:
            result['ISPLines'] = self.isplines

        if self.ispregion_lines is not None:
            result['ISPRegionLines'] = self.ispregion_lines

        if self.in_black_hole is not None:
            result['InBlackHole'] = self.in_black_hole

        if self.in_clean is not None:
            result['InClean'] = self.in_clean

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.monitor_frequency is not None:
            result['MonitorFrequency'] = self.monitor_frequency

        if self.monitor_node_count is not None:
            result['MonitorNodeCount'] = self.monitor_node_count

        if self.monitor_task_count is not None:
            result['MonitorTaskCount'] = self.monitor_task_count

        if self.oversea_ddos_defend_flow is not None:
            result['OverseaDDosDefendFlow'] = self.oversea_ddos_defend_flow

        if self.oversea_line is not None:
            result['OverseaLine'] = self.oversea_line

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_lines is not None:
            result['RegionLines'] = self.region_lines

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_engine_lines is not None:
            result['SearchEngineLines'] = self.search_engine_lines

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.sub_domain_level is not None:
            result['SubDomainLevel'] = self.sub_domain_level

        if self.ttlmin_value is not None:
            result['TTLMinValue'] = self.ttlmin_value

        if self.urlforward_count is not None:
            result['URLForwardCount'] = self.urlforward_count

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('BindDomainCount') is not None:
            self.bind_domain_count = m.get('BindDomainCount')

        if m.get('BindDomainUsedCount') is not None:
            self.bind_domain_used_count = m.get('BindDomainUsedCount')

        if m.get('BindUsedCount') is not None:
            self.bind_used_count = m.get('BindUsedCount')

        if m.get('DDosDefendFlow') is not None:
            self.ddos_defend_flow = m.get('DDosDefendFlow')

        if m.get('DDosDefendQuery') is not None:
            self.ddos_defend_query = m.get('DDosDefendQuery')

        if m.get('DnsSLBCount') is not None:
            self.dns_slbcount = m.get('DnsSLBCount')

        if m.get('DnsSecurity') is not None:
            self.dns_security = m.get('DnsSecurity')

        if m.get('DnsServers') is not None:
            temp_model = main_models.DescribeDnsProductInstanceResponseBodyDnsServers()
            self.dns_servers = temp_model.from_map(m.get('DnsServers'))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')

        if m.get('ISPLines') is not None:
            self.isplines = m.get('ISPLines')

        if m.get('ISPRegionLines') is not None:
            self.ispregion_lines = m.get('ISPRegionLines')

        if m.get('InBlackHole') is not None:
            self.in_black_hole = m.get('InBlackHole')

        if m.get('InClean') is not None:
            self.in_clean = m.get('InClean')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MonitorFrequency') is not None:
            self.monitor_frequency = m.get('MonitorFrequency')

        if m.get('MonitorNodeCount') is not None:
            self.monitor_node_count = m.get('MonitorNodeCount')

        if m.get('MonitorTaskCount') is not None:
            self.monitor_task_count = m.get('MonitorTaskCount')

        if m.get('OverseaDDosDefendFlow') is not None:
            self.oversea_ddos_defend_flow = m.get('OverseaDDosDefendFlow')

        if m.get('OverseaLine') is not None:
            self.oversea_line = m.get('OverseaLine')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionLines') is not None:
            self.region_lines = m.get('RegionLines')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchEngineLines') is not None:
            self.search_engine_lines = m.get('SearchEngineLines')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('SubDomainLevel') is not None:
            self.sub_domain_level = m.get('SubDomainLevel')

        if m.get('TTLMinValue') is not None:
            self.ttlmin_value = m.get('TTLMinValue')

        if m.get('URLForwardCount') is not None:
            self.urlforward_count = m.get('URLForwardCount')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class DescribeDnsProductInstanceResponseBodyDnsServers(DaraModel):
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

