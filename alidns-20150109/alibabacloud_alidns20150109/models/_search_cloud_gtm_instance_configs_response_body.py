# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchCloudGtmInstanceConfigsResponseBody(DaraModel):
    def __init__(
        self,
        instance_configs: main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The instances list.
        self.instance_configs = instance_configs
        # Current page number, starting from 1, default is 1.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of **100**, and a default of **20**.
        self.page_size = page_size
        # Unique request identification code.
        self.request_id = request_id
        # Total number of instance configuration entries.
        self.total_items = total_items
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.instance_configs:
            self.instance_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_configs is not None:
            result['InstanceConfigs'] = self.instance_configs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConfigs') is not None:
            temp_model = main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigs()
            self.instance_configs = temp_model.from_map(m.get('InstanceConfigs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigs(DaraModel):
    def __init__(
        self,
        instance_config: List[main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfig] = None,
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
                temp_model = main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfig()
                self.instance_config.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfig(DaraModel):
    def __init__(
        self,
        address_pool_lb_strategy: str = None,
        address_pools: main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPools = None,
        available_status: str = None,
        commodity_code: str = None,
        config_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_status: str = None,
        instance_id: str = None,
        remark: str = None,
        schedule_domain_name: str = None,
        schedule_hostname: str = None,
        schedule_rr_type: str = None,
        schedule_zone_mode: str = None,
        schedule_zone_name: str = None,
        sequence_lb_strategy_mode: str = None,
        ttl: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        version_code: str = None,
    ):
        # The policy for load balancing between address pools. Valid values:
        # 
        # *   round_robin: All address pools are returned for DNS requests from any source. All address pools are sorted in round-robin mode each time they are returned.
        # *   sequence: The address pool with the smallest sequence number is preferentially returned for DNS requests from any source. The sequence number indicates the priority for returning the address pool. A smaller sequence number indicates a higher priority. If the address pool with the smallest sequence number is unavailable, the address pool with the second smallest sequence number is returned.
        # *   weight: You can set a different weight value for each address pool. This way, address pools are returned based on the weight values.
        # *   source_nearest: Different address pools are returned based on the sources of DNS requests. This way, users can access nearby address pools.
        self.address_pool_lb_strategy = address_pool_lb_strategy
        # The address pools.
        self.address_pools = address_pools
        # The availability state of the access domain name. Valid values:
        # 
        # *   available: If the access domain name is **enabled** and the health state is **normal**, the access domain name is deemed **available**.
        # *   unavailable: If the access domain name is **disabled** or the health state is **abnormal**, the access domain name is deemed **unavailable**.
        self.available_status = available_status
        # The commodity code. Valid values:
        # 
        # *   dns_gtm_public_cn: the commodity code on the China site (aliyun.com)
        # *   dns_gtm_public_intl: the commodity code on the international site (alibabacloud.com)
        self.commodity_code = commodity_code
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        self.config_id = config_id
        # Domain instance creation time.
        self.create_time = create_time
        # Domain instance creation time (timestamp).
        self.create_timestamp = create_timestamp
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
        # The ID of the GTM 3.0 instance.
        self.instance_id = instance_id
        # Remarks for the domain instance.
        self.remark = remark
        # The access domain name. The value of this parameter is composed of the value of ScheduleHostname and the value of ScheduleZoneName.
        self.schedule_domain_name = schedule_domain_name
        # Host record of the domain accessed by GTM.
        self.schedule_hostname = schedule_hostname
        # DNS record types for the scheduling domain:
        # - A: IPv4 address
        # - AAAA: IPv6 address
        # - CNAME: Domain name
        self.schedule_rr_type = schedule_rr_type
        # The allocation mode of the access domain name. Valid values:
        # 
        # *   custom: custom allocation. You must specify a custom hostname and associate the hostname with a zone that is hosted by the Public Authoritative DNS module within the account to which the GTM instance belongs to generate an access domain name.
        # *   sys_assign: system allocation. This mode is not supported. Do not set ScheduleZoneMode to sys_assign.
        self.schedule_zone_mode = schedule_zone_mode
        # The zone such as example.com or subzone such as a.example.com of the access domain name. In most cases, the zone or subzone is hosted by the Public Authoritative DNS module of Alibaba Cloud DNS. This zone belongs to the account to which the GTM instance belongs.
        self.schedule_zone_name = schedule_zone_name
        # The mode used if the address pool with the smallest sequence number is recovered. This parameter is returned when AddressPoolLbStrategy is set to sequence. Valid values:
        # 
        # *   preemptive: The address pool with the smallest sequence number is preferentially used if this address pool is recovered.
        # *   non_preemptive: The current address pool is still used even if the address pool with the smallest sequence number is recovered.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        # Global TTL (in seconds), the TTL value for resolving the access domain name to the address pool, which affects the caching time of DNS records in the operator\\"s LocalDNS. Supports custom TTL values.
        self.ttl = ttl
        # The last modification time of the domain instance.
        self.update_time = update_time
        # The last modification time of the domain instance (timestamp).
        self.update_timestamp = update_timestamp
        # Global Traffic Management version 3.0 instance types:
        # - standard: Standard Edition
        # - ultimate: Ultimate Edition
        self.version_code = version_code

    def validate(self):
        if self.address_pools:
            self.address_pools.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_pool_lb_strategy is not None:
            result['AddressPoolLbStrategy'] = self.address_pool_lb_strategy

        if self.address_pools is not None:
            result['AddressPools'] = self.address_pools.to_map()

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.schedule_domain_name is not None:
            result['ScheduleDomainName'] = self.schedule_domain_name

        if self.schedule_hostname is not None:
            result['ScheduleHostname'] = self.schedule_hostname

        if self.schedule_rr_type is not None:
            result['ScheduleRrType'] = self.schedule_rr_type

        if self.schedule_zone_mode is not None:
            result['ScheduleZoneMode'] = self.schedule_zone_mode

        if self.schedule_zone_name is not None:
            result['ScheduleZoneName'] = self.schedule_zone_name

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolLbStrategy') is not None:
            self.address_pool_lb_strategy = m.get('AddressPoolLbStrategy')

        if m.get('AddressPools') is not None:
            temp_model = main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPools()
            self.address_pools = temp_model.from_map(m.get('AddressPools'))

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScheduleDomainName') is not None:
            self.schedule_domain_name = m.get('ScheduleDomainName')

        if m.get('ScheduleHostname') is not None:
            self.schedule_hostname = m.get('ScheduleHostname')

        if m.get('ScheduleRrType') is not None:
            self.schedule_rr_type = m.get('ScheduleRrType')

        if m.get('ScheduleZoneMode') is not None:
            self.schedule_zone_mode = m.get('ScheduleZoneMode')

        if m.get('ScheduleZoneName') is not None:
            self.schedule_zone_name = m.get('ScheduleZoneName')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPools(DaraModel):
    def __init__(
        self,
        address_pool: List[main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPool] = None,
    ):
        self.address_pool = address_pool

    def validate(self):
        if self.address_pool:
            for v1 in self.address_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressPool'] = []
        if self.address_pool is not None:
            for k1 in self.address_pool:
                result['AddressPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_pool = []
        if m.get('AddressPool') is not None:
            for k1 in m.get('AddressPool'):
                temp_model = main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPool()
                self.address_pool.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPool(DaraModel):
    def __init__(
        self,
        address_lb_strategy: str = None,
        address_pool_id: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        available_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_status: str = None,
        request_source: main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPoolRequestSource = None,
        seq_non_preemptive_schedule: bool = None,
        sequence_lb_strategy_mode: str = None,
        serial_number: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        weight_value: int = None,
    ):
        # Load balancing policy among addresses in the address pool:
        # - round_robin: Round-robin, where for any source of DNS resolution requests, all addresses are returned, with a rotation of the order for every request.
        # - sequence: Sequential, where for any source of DNS resolution requests, the address with the lower sequence number (indicating a higher priority, the smaller the number, the higher the priority) is returned. If the address with the lower sequence number is unavailable, the next address with a lower sequence number is returned.
        # - weight: Weighted, supporting the setting of different weight values for each address to realize returning addresses according to the ratio of weights in DNS query resolutions.
        # - source_nearest: Source-nearest, referring to the intelligent resolution feature, where GTM can return different addresses based on the source of different DNS resolution requests, achieving the effect of users accessing the nearest server.
        self.address_lb_strategy = address_lb_strategy
        # Address pool ID, uniquely identifying the address pool.
        self.address_pool_id = address_pool_id
        # Address pool name.
        self.address_pool_name = address_pool_name
        # Address pool type:
        # - IPv4
        # - IPv6
        # - domain
        self.address_pool_type = address_pool_type
        # Address pool availability status:
        # - available: Available
        # - unavailable: Unavailable
        self.available_status = available_status
        # Address pool creation time.
        self.create_time = create_time
        # Address pool creation time (timestamp).
        self.create_timestamp = create_timestamp
        # Address pool status:
        # - enable: Enabled status
        # - disable: Disabled status
        self.enable_status = enable_status
        # The condition for determining the health status of the address pool. Valid values:
        # 
        # *   any_ok: At least one address in the address pool is available.
        # *   p30_ok: At least 30% of the addresses in the address pool are available.
        # *   p50_ok: At least 50% of the addresses in the address pool are available.
        # *   p70_ok: At least 70% of the addresses in the address pool are available.
        # *   all_ok: All addresses in the address pool are available.
        self.health_judgement = health_judgement
        # The health state of the address pool. Valid values:
        # 
        # *   ok: The health state of the address pool is normal and all addresses that are referenced by the address pool are available.
        # *   ok_alert: The health state of the address pool is warning and some of the addresses that are referenced by the address pool are unavailable. However, the address pool is deemed normal. In this case, only the available addresses are returned for DNS requests.
        # *   exceptional: The health state of the address pool is abnormal and some or all of the addresses that are referenced by the address pool are unavailable. In this case, the address pool is deemed abnormal.
        self.health_status = health_status
        # Parse the request source list.
        self.request_source = request_source
        # Indicates whether it is a sequential (non-preemptive) scheduling object for hybrid cloud management scenarios: 
        # - true: yes 
        # - false: no
        self.seq_non_preemptive_schedule = seq_non_preemptive_schedule
        # The mode used if the address with the smallest sequence number is recovered. This parameter is required only when the policy for load balancing between addresses is sequence. Valid values:
        # 
        # *   preemptive: The address with the smallest sequence number is preferentially used if this address is recovered.
        # *   non_preemptive: The current address is still used even if the address with the smallest sequence number is recovered.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        # Sequence number. For any parsing request, the address pool with the smaller sequence number (indicating the priority of the address pool returned, with smaller numbers having higher priority) will be returned.
        self.serial_number = serial_number
        # Last modification time of the address pool.
        self.update_time = update_time
        # Update time (timestamp).
        self.update_timestamp = update_timestamp
        # Weight value (an integer between 1 and 100, inclusive), allowing different weight values to be set for each address pool, implementing the return of address pools according to weight ratios in resolution queries.
        self.weight_value = weight_value

    def validate(self):
        if self.request_source:
            self.request_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_lb_strategy is not None:
            result['AddressLbStrategy'] = self.address_lb_strategy

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.address_pool_name is not None:
            result['AddressPoolName'] = self.address_pool_name

        if self.address_pool_type is not None:
            result['AddressPoolType'] = self.address_pool_type

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.request_source is not None:
            result['RequestSource'] = self.request_source.to_map()

        if self.seq_non_preemptive_schedule is not None:
            result['SeqNonPreemptiveSchedule'] = self.seq_non_preemptive_schedule

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.weight_value is not None:
            result['WeightValue'] = self.weight_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressLbStrategy') is not None:
            self.address_lb_strategy = m.get('AddressLbStrategy')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('AddressPoolName') is not None:
            self.address_pool_name = m.get('AddressPoolName')

        if m.get('AddressPoolType') is not None:
            self.address_pool_type = m.get('AddressPoolType')

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthJudgement') is not None:
            self.health_judgement = m.get('HealthJudgement')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('RequestSource') is not None:
            temp_model = main_models.SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPoolRequestSource()
            self.request_source = temp_model.from_map(m.get('RequestSource'))

        if m.get('SeqNonPreemptiveSchedule') is not None:
            self.seq_non_preemptive_schedule = m.get('SeqNonPreemptiveSchedule')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('WeightValue') is not None:
            self.weight_value = m.get('WeightValue')

        return self

class SearchCloudGtmInstanceConfigsResponseBodyInstanceConfigsInstanceConfigAddressPoolsAddressPoolRequestSource(DaraModel):
    def __init__(
        self,
        request_source: List[str] = None,
    ):
        self.request_source = request_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        return self

