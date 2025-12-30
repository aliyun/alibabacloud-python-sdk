# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmAddressPoolReferenceResponseBody(DaraModel):
    def __init__(
        self,
        address_pool_id: str = None,
        address_pool_name: str = None,
        instance_configs: main_models.DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigs = None,
        request_id: str = None,
    ):
        # The ID of the address pool. This ID uniquely identifies the address pool.
        self.address_pool_id = address_pool_id
        # Address pool name.
        self.address_pool_name = address_pool_name
        # The access domain names that reference the address pool.
        self.instance_configs = instance_configs
        # Unique request identification code.
        self.request_id = request_id

    def validate(self):
        if self.instance_configs:
            self.instance_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.address_pool_name is not None:
            result['AddressPoolName'] = self.address_pool_name

        if self.instance_configs is not None:
            result['InstanceConfigs'] = self.instance_configs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('AddressPoolName') is not None:
            self.address_pool_name = m.get('AddressPoolName')

        if m.get('InstanceConfigs') is not None:
            temp_model = main_models.DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigs()
            self.instance_configs = temp_model.from_map(m.get('InstanceConfigs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigs(DaraModel):
    def __init__(
        self,
        instance_config: List[main_models.DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigsInstanceConfig] = None,
    ):
        self.instance_config = instance_config

    def validate(self):
        if self.instance_config:
            for v1 in self.instance_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceConfig'] = []
        if self.instance_config is not None:
            for k1 in self.instance_config:
                result['InstanceConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_config = []
        if m.get('InstanceConfig') is not None:
            for k1 in m.get('InstanceConfig'):
                temp_model = main_models.DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigsInstanceConfig()
                self.instance_config.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmAddressPoolReferenceResponseBodyInstanceConfigsInstanceConfig(DaraModel):
    def __init__(
        self,
        address_pool_lb_strategy: str = None,
        available_status: str = None,
        config_id: str = None,
        enable_status: str = None,
        health_status: str = None,
        instance_id: str = None,
        instance_name: str = None,
        remark: str = None,
        schedule_domain_name: str = None,
        schedule_hostname: str = None,
        schedule_rr_type: str = None,
        schedule_zone_name: str = None,
        sequence_lb_strategy_mode: str = None,
        ttl: int = None,
        version_code: str = None,
    ):
        # The policy for load balancing between address pools. Valid values:
        # 
        # *   round_robin: All address pools are returned for Domain Name System (DNS) requests from any source. All address pools are sorted in round-robin mode each time they are returned.
        # *   sequence: The address pool with the smallest sequence number is preferentially returned for DNS requests from any source. The sequence number indicates the priority for returning the address pool. A smaller sequence number indicates a higher priority. If the address pool with the smallest sequence number is unavailable, the address pool with the second smallest sequence number is returned.
        # *   weight: You can set a different weight value for each address pool. This way, address pools are returned based on the weight values.
        # *   source_nearest: Different address pools are returned based on the sources of DNS requests. This way, users can access nearby address pools.
        self.address_pool_lb_strategy = address_pool_lb_strategy
        # The availability state of the access domain name. Valid values:
        # 
        # *   available: If the access domain name is **enabled** and the health state is **normal**, the access domain name is deemed **available**.
        # *   unavailable: If the access domain name is **disabled** or the health state is **abnormal**, the access domain name is deemed **unavailable**.
        self.available_status = available_status
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        self.config_id = config_id
        # The enabling state of the access domain name. Valid values:
        # 
        # *   enable: The access domain name is enabled and the intelligent scheduling policy of the corresponding GTM instance takes effect.
        # *   disable: The access domain name is disabled and the intelligent scheduling policy of the corresponding GTM instance does not take effect.
        self.enable_status = enable_status
        # The health state of the access domain name. Valid values:
        # 
        # *   ok: The health state of the access domain name is normal and all address pools that are referenced by the access domain name are available.
        # *   ok_alert: The health state of the access domain name is warning and some of the address pools that are referenced by the access domain name are unavailable. In this case, only the available address pools are returned for DNS requests.
        # *   exceptional: The health state of the access domain name is abnormal and all address pools that are referenced by the access domain name are unavailable. In this case, addresses in the non-empty address pool with the smallest sequence number are preferentially used for fallback resolution. This returns DNS results for clients as much as possible.
        self.health_status = health_status
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # Instance name.
        self.instance_name = instance_name
        # Remarks.
        self.remark = remark
        # The access domain name. The value of this parameter is composed of the value of ScheduleHostname and the value of ScheduleZoneName.
        self.schedule_domain_name = schedule_domain_name
        # Host record of the domain accessed by GTM.
        self.schedule_hostname = schedule_hostname
        # DNS record types for scheduling domains:
        # - A: IPv4 address
        # - AAAA: IPv6 address
        # - CNAME: Domain name
        self.schedule_rr_type = schedule_rr_type
        # The zone such as example.com or subzone such as a.example.com of the access domain name. In most cases, the zone or subzone is hosted by the Public Authoritative DNS module of Alibaba Cloud DNS. This zone belongs to the account to which the GTM instance belongs.
        self.schedule_zone_name = schedule_zone_name
        # The mode used if the address pool with the smallest sequence number is recovered. This parameter is returned when AddressPoolLbStrategy is set to sequence. Valid values:
        # 
        # *   preemptive: The address pool with the smallest sequence number is preferentially used if this address pool is recovered.
        # *   non_preemptive: The current address pool is still used even if the address pool with the smallest sequence number is recovered.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        # Global TTL, the TTL value for resolving the accessed domain name to addresses in the address pool, which affects the caching time of DNS records in the operator\\"s LocalDNS. Supports custom TTL values.
        self.ttl = ttl
        # Global Traffic Management version 3.0 instance types:
        # - standard: Standard Edition
        # - ultimate: Ultimate Edition
        self.version_code = version_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_pool_lb_strategy is not None:
            result['AddressPoolLbStrategy'] = self.address_pool_lb_strategy

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.schedule_domain_name is not None:
            result['ScheduleDomainName'] = self.schedule_domain_name

        if self.schedule_hostname is not None:
            result['ScheduleHostname'] = self.schedule_hostname

        if self.schedule_rr_type is not None:
            result['ScheduleRrType'] = self.schedule_rr_type

        if self.schedule_zone_name is not None:
            result['ScheduleZoneName'] = self.schedule_zone_name

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolLbStrategy') is not None:
            self.address_pool_lb_strategy = m.get('AddressPoolLbStrategy')

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScheduleDomainName') is not None:
            self.schedule_domain_name = m.get('ScheduleDomainName')

        if m.get('ScheduleHostname') is not None:
            self.schedule_hostname = m.get('ScheduleHostname')

        if m.get('ScheduleRrType') is not None:
            self.schedule_rr_type = m.get('ScheduleRrType')

        if m.get('ScheduleZoneName') is not None:
            self.schedule_zone_name = m.get('ScheduleZoneName')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

