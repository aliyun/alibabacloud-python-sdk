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
        self.address_pool_lb_strategy = address_pool_lb_strategy
        self.available_status = available_status
        self.config_id = config_id
        self.enable_status = enable_status
        self.health_status = health_status
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.remark = remark
        self.schedule_domain_name = schedule_domain_name
        self.schedule_hostname = schedule_hostname
        self.schedule_rr_type = schedule_rr_type
        self.schedule_zone_name = schedule_zone_name
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        self.ttl = ttl
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

