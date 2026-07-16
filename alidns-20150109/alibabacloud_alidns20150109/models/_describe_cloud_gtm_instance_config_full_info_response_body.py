# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmInstanceConfigFullInfoResponseBody(DaraModel):
    def __init__(
        self,
        address_pool_lb_strategy: str = None,
        address_pools: main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPools = None,
        alert_config: str = None,
        alert_group: str = None,
        available_status: str = None,
        commodity_code: str = None,
        config_id: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_status: str = None,
        instance_id: str = None,
        instance_name: str = None,
        remark: str = None,
        request_id: str = None,
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
        # The load balancing policy for the address pools.
        # 
        # - round_robin: Returns all address pools for any DNS request. The address pools are rotated in order for each request.
        # 
        # - sequence: Returns the address pool with the smallest ordinal number for any DNS request. The ordinal number indicates the priority of the address pool. A smaller value indicates a higher priority. If the address pool with the smallest ordinal number is unavailable, the address pool with the next smallest ordinal number is returned.
        # 
        # - weight: Returns address pools based on the specified weight for each address pool.
        # 
        # - source_nearest: Returns different address pools based on the source of the DNS requests. This implements proximity-based access for users.
        self.address_pool_lb_strategy = address_pool_lb_strategy
        # The address pools.
        self.address_pools = address_pools
        # The alert notification configuration.
        self.alert_config = alert_config
        # The alert group.
        self.alert_group = alert_group
        # The service availability status of the instance.
        # 
        # - `available`: The instance is enabled and its health status is Normal. The service is available for the access domain name.
        # 
        # - `unavailable`: The instance is disabled or its health status is abnormal. The service is unavailable for the access domain name.
        self.available_status = available_status
        # The commodity code.
        # 
        # - dns_gtm_public_cn: The commodity code for the China site (aliyun.com).
        # 
        # - dns_gtm_public_intl: The commodity code for the international site (alibabacloud.com).
        self.commodity_code = commodity_code
        # The ID of the instance configuration. You can configure both A and AAAA records for the same access domain name and Global Traffic Manager (GTM) instance. In this case, the GTM instance has two configurations. The ConfigId uniquely identifies an instance configuration.
        self.config_id = config_id
        # The time when the instance was created.
        self.create_time = create_time
        # The UNIX timestamp that indicates when the instance was created.
        self.create_timestamp = create_timestamp
        # The enabled status of the instance.
        # 
        # - enable: The GTM instance is enabled and its intelligent scheduling policy is active.
        # 
        # - disable: The GTM instance is disabled and its intelligent scheduling policy is inactive.
        self.enable_status = enable_status
        # The health status of the instance.
        # 
        # - ok: Normal. All address pools referenced by the access domain name are available.
        # 
        # - ok_alert: Warning. Some of the address pools referenced by the access domain name are unavailable. In this state, DNS requests are resolved to the available address pools, but not to the unavailable ones.
        # 
        # - exceptional: Abnormal. All address pools referenced by the access domain name are unavailable. In this case, DNS requests are resolved to the addresses in the non-empty address pool with the smallest ordinal number as a failover measure. This helps ensure that clients can receive DNS responses.
        self.health_status = health_status
        # The ID of the Global Traffic Manager 3.0 instance.
        self.instance_id = instance_id
        # The name of the GTM instance.
        self.instance_name = instance_name
        # The remarks on the instance configuration.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The GTM access domain name. The format is ScheduleHostname + ScheduleZoneName.
        self.schedule_domain_name = schedule_domain_name
        # The host record of the GTM access domain name.
        self.schedule_hostname = schedule_hostname
        # The DNS record type of the GTM access domain name.
        # 
        # - A: IPv4 address
        # 
        # - AAAA: IPv6 address
        # 
        # - CNAME: canonical name
        self.schedule_rr_type = schedule_rr_type
        # The assignment mode of the access domain name.
        # 
        # - custom: You can customize the host record and associate it with a primary domain name or a subdomain name under the account to which the GTM instance belongs. This generates the access domain name.
        # 
        # - sys_assign: The system assigns a default access domain name. This feature is no longer supported. Do not select this mode.
        self.schedule_zone_mode = schedule_zone_mode
        # The primary domain name (example.com) or subdomain name (a.example.com) of the GTM access domain name. This is typically a domain name hosted in the authoritative zone of the Alibaba Cloud DNS console under the account to which the GTM instance belongs.
        self.schedule_zone_name = schedule_zone_name
        # When the load balancing policy for address pools is sequence, this parameter specifies the service recovery mode for a resource that becomes available again.
        # 
        # - preemptive: The address pool with the smaller ordinal number is preferentially used.
        # 
        # - non_preemptive: The current address pool is still used.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        # The global time to live (TTL) in seconds. This is the TTL value for the DNS records that map the access domain name to the addresses in the address pool. It affects the cache duration of the DNS records on carrier Local DNS servers. You can customize the TTL value.
        self.ttl = ttl
        # The time when the instance was last modified.
        self.update_time = update_time
        # The UNIX timestamp that indicates when the instance was last modified.
        self.update_timestamp = update_timestamp
        # The edition of the Global Traffic Manager 3.0 instance.
        # 
        # - standard: Standard Edition
        # 
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

        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config

        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

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

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPools()
            self.address_pools = temp_model.from_map(m.get('AddressPools'))

        if m.get('AlertConfig') is not None:
            self.alert_config = m.get('AlertConfig')

        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

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

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPools(DaraModel):
    def __init__(
        self,
        address_pool: List[main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPool] = None,
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
                temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPool()
                self.address_pool.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPool(DaraModel):
    def __init__(
        self,
        address_lb_strategy: str = None,
        address_pool_id: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        addresses: main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddresses = None,
        available_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_status: str = None,
        request_source: main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolRequestSource = None,
        seq_non_preemptive_schedule: bool = None,
        sequence_lb_strategy_mode: str = None,
        serial_number: int = None,
        update_time: str = None,
        update_timestamp: int = None,
        weight_value: int = None,
    ):
        self.address_lb_strategy = address_lb_strategy
        self.address_pool_id = address_pool_id
        self.address_pool_name = address_pool_name
        self.address_pool_type = address_pool_type
        self.addresses = addresses
        self.available_status = available_status
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.enable_status = enable_status
        self.health_judgement = health_judgement
        self.health_status = health_status
        self.request_source = request_source
        self.seq_non_preemptive_schedule = seq_non_preemptive_schedule
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        self.serial_number = serial_number
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.weight_value = weight_value

    def validate(self):
        if self.addresses:
            self.addresses.validate()
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

        if self.addresses is not None:
            result['Addresses'] = self.addresses.to_map()

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

        if m.get('Addresses') is not None:
            temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddresses()
            self.addresses = temp_model.from_map(m.get('Addresses'))

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
            temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolRequestSource()
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

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolRequestSource(DaraModel):
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

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddresses(DaraModel):
    def __init__(
        self,
        address: List[main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for v1 in self.address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Address'] = []
        if self.address is not None:
            for k1 in self.address:
                result['Address'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k1 in m.get('Address'):
                temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddress()
                self.address.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddress(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_id: str = None,
        attribute_info: str = None,
        available_mode: str = None,
        available_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_status: str = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        request_source: main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddressRequestSource = None,
        seq_non_preemptive_schedule: bool = None,
        serial_number: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        weight_value: int = None,
    ):
        self.address = address
        self.address_id = address_id
        self.attribute_info = attribute_info
        self.available_mode = available_mode
        self.available_status = available_status
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.enable_status = enable_status
        self.health_judgement = health_judgement
        self.health_status = health_status
        self.manual_available_status = manual_available_status
        self.name = name
        self.remark = remark
        self.request_source = request_source
        self.seq_non_preemptive_schedule = seq_non_preemptive_schedule
        self.serial_number = serial_number
        self.type = type
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.weight_value = weight_value

    def validate(self):
        if self.request_source:
            self.request_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.available_mode is not None:
            result['AvailableMode'] = self.available_mode

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

        if self.manual_available_status is not None:
            result['ManualAvailableStatus'] = self.manual_available_status

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_source is not None:
            result['RequestSource'] = self.request_source.to_map()

        if self.seq_non_preemptive_schedule is not None:
            result['SeqNonPreemptiveSchedule'] = self.seq_non_preemptive_schedule

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.weight_value is not None:
            result['WeightValue'] = self.weight_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')

        if m.get('AvailableMode') is not None:
            self.available_mode = m.get('AvailableMode')

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

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestSource') is not None:
            temp_model = main_models.DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddressRequestSource()
            self.request_source = temp_model.from_map(m.get('RequestSource'))

        if m.get('SeqNonPreemptiveSchedule') is not None:
            self.seq_non_preemptive_schedule = m.get('SeqNonPreemptiveSchedule')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('WeightValue') is not None:
            self.weight_value = m.get('WeightValue')

        return self

class DescribeCloudGtmInstanceConfigFullInfoResponseBodyAddressPoolsAddressPoolAddressesAddressRequestSource(DaraModel):
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

