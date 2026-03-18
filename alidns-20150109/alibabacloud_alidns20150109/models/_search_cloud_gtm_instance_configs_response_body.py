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
        config_logging_switch_status: str = None,
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
        self.address_pool_lb_strategy = address_pool_lb_strategy
        self.address_pools = address_pools
        self.available_status = available_status
        self.commodity_code = commodity_code
        self.config_id = config_id
        self.config_logging_switch_status = config_logging_switch_status
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.enable_status = enable_status
        self.health_status = health_status
        self.instance_id = instance_id
        self.remark = remark
        self.schedule_domain_name = schedule_domain_name
        self.schedule_hostname = schedule_hostname
        self.schedule_rr_type = schedule_rr_type
        self.schedule_zone_mode = schedule_zone_mode
        self.schedule_zone_name = schedule_zone_name
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        self.ttl = ttl
        self.update_time = update_time
        self.update_timestamp = update_timestamp
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

        if self.config_logging_switch_status is not None:
            result['ConfigLoggingSwitchStatus'] = self.config_logging_switch_status

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

        if m.get('ConfigLoggingSwitchStatus') is not None:
            self.config_logging_switch_status = m.get('ConfigLoggingSwitchStatus')

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
        self.address_lb_strategy = address_lb_strategy
        self.address_pool_id = address_pool_id
        self.address_pool_name = address_pool_name
        self.address_pool_type = address_pool_type
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

