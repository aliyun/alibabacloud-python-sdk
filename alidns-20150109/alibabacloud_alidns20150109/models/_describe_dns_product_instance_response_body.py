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
        # Indicates whether auto-renewal is enabled for the instance.
        # 
        # - true: Auto-renewal is enabled.
        # 
        # - false: Auto-renewal is disabled.
        self.auto_renewal = auto_renewal
        # The number of times the domain name can be changed for the paid DNS instance. This parameter is available for the Custom Edition.
        self.bind_count = bind_count
        # The number of domain names that can be attached to the paid DNS instance. This parameter is available for the Personal and Ultimate editions.
        self.bind_domain_count = bind_domain_count
        # The number of domain names that are attached to the paid DNS instance. This parameter is available for the Personal and Ultimate editions.
        self.bind_domain_used_count = bind_domain_used_count
        # The number of times the domain name has been changed for the paid DNS instance. This parameter is available for the Custom Edition.
        self.bind_used_count = bind_used_count
        # The DDoS protection bandwidth. Unit: Gbit/s.
        self.ddos_defend_flow = ddos_defend_flow
        # The DDoS protection capacity in queries per second (QPS). The unit is 10,000 QPS. This parameter is available for the Custom Edition.
        self.ddos_defend_query = ddos_defend_query
        # The Server Load Balancer (SLB) capacity. This is the number of IP addresses that can be configured for a domain name on a single line.
        self.dns_slbcount = dns_slbcount
        # The DNS security level. Valid values:
        # 
        # - no: Not required
        # 
        # - basic: Basic DNS attack protection
        # 
        # - advanced: Advanced DNS attack protection
        self.dns_security = dns_security
        self.dns_servers = dns_servers
        # The attached domain name.
        # 
        # If this parameter is empty, no domain name is attached.
        self.domain = domain
        # The type of the instance:
        # 
        # - PUBLIC: An instance for an authoritative domain name.
        # 
        # - CACHE: An instance for a recursive DNS proxy.
        self.domain_type = domain_type
        # The time when the instance expires.
        self.end_time = end_time
        # The time when the instance expires. This is a UNIX timestamp.
        self.end_timestamp = end_timestamp
        # Indicates whether Global Server Load Balancer (GSLB) is allowed.
        # 
        # - true: Allowed
        # 
        # - false: Not allowed
        self.gslb = gslb
        # The carrier line from which the DNS request was initiated. Valid values:
        # 
        # - China Telecom
        # 
        # - China Mobile
        # 
        # - China Unicom
        # 
        # - China Education and Research Network
        # 
        # - China Broadcasting Network
        # 
        # - Dr. Peng Group
        self.isplines = isplines
        # The carrier line and province from which the DNS request was initiated. Valid values:
        # 
        # - China Telecom (by province)
        # 
        # - China Mobile (by province)
        # 
        # - China Unicom (by province)
        # 
        # - China Education and Research Network (by province)
        self.ispregion_lines = ispregion_lines
        # Indicates whether the domain name is in a blackhole filtering status.
        # 
        # - true: The domain name is in a blackhole filtering status.
        # 
        # - false: The domain name is not in a blackhole filtering status.
        self.in_black_hole = in_black_hole
        # Indicates whether the domain name is undergoing traffic scrubbing.
        # 
        # - true: Traffic scrubbing is in progress.
        # 
        # - false: Traffic scrubbing is not in progress.
        self.in_clean = in_clean
        # The ID of the Alibaba Cloud DNS instance.
        self.instance_id = instance_id
        # The monitoring frequency. Unit: minutes.
        self.monitor_frequency = monitor_frequency
        # The number of monitoring nodes.
        self.monitor_node_count = monitor_node_count
        # The number of monitoring jobs.
        self.monitor_task_count = monitor_task_count
        # The DDoS protection bandwidth for regions outside China. Unit: Gbit/s.
        self.oversea_ddos_defend_flow = oversea_ddos_defend_flow
        # The line for regions outside China.
        self.oversea_line = oversea_line
        # The billing method.
        self.payment_type = payment_type
        # Indicates whether regional lines are used.
        # 
        # - true: Regional lines are used.
        # 
        # - false: Regional lines are not used.
        self.region_lines = region_lines
        # The unique ID of the request.
        self.request_id = request_id
        # The search engine line. Valid values:
        # 
        # - Google
        # 
        # - Baidu
        # 
        # - Bing
        # 
        # - Youdao
        self.search_engine_lines = search_engine_lines
        # The time when the instance was purchased.
        self.start_time = start_time
        # The time when the instance was purchased. This is a UNIX timestamp.
        self.start_timestamp = start_timestamp
        # The number of subdomain levels.
        self.sub_domain_level = sub_domain_level
        # The minimum Time to Live (TTL) value. Unit: seconds.
        self.ttlmin_value = ttlmin_value
        # The number of URL forwards.
        self.urlforward_count = urlforward_count
        # The code of the Alibaba Cloud DNS edition.
        self.version_code = version_code
        # The name of the Alibaba Cloud DNS edition.
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

