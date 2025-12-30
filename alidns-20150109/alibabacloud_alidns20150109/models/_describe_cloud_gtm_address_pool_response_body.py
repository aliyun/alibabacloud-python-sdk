# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmAddressPoolResponseBody(DaraModel):
    def __init__(
        self,
        address_lb_strategy: str = None,
        address_pool_id: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        addresses: main_models.DescribeCloudGtmAddressPoolResponseBodyAddresses = None,
        available_status: str = None,
        create_time: str = None,
        create_timestamp: int = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_status: str = None,
        remark: str = None,
        request_id: str = None,
        sequence_lb_strategy_mode: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # Load balancing policy among addresses in the address pool:
        # - round_robin: Round-robin, where for any source of DNS resolution requests, all addresses are returned, with a rotation of the order for every request.
        # - sequence: Sequential, where for any source of DNS resolution requests, the address with the lower sequence number (indicating a higher priority, the smaller the number, the higher the priority) is returned. If the address with the lower sequence number is unavailable, the next address with a lower sequence number is returned.
        # - weight: Weighted, supporting the setting of different weight values for each address to realize returning addresses according to the weight ratio of query resolutions.
        # - source_nearest: Source-nearest, also known as intelligent resolution, where GTM can return different addresses based on the source of different DNS resolution requests, achieving the effect of users accessing nearby servers.
        self.address_lb_strategy = address_lb_strategy
        # The ID of the address pool. This ID uniquely identifies the address pool.
        self.address_pool_id = address_pool_id
        # Address pool name.
        self.address_pool_name = address_pool_name
        # Address pool type:
        # - IPv4
        # - IPv6
        # - domain
        self.address_pool_type = address_pool_type
        # The addresses.
        self.addresses = addresses
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
        # *   ok_alert: The health state of the address pool is warning and some of the addresses that are referenced by the address pool are unavailable. However, the address pool is deemed normal. In this case, only the available addresses are returned for Domain Name System (DNS) requests.
        # *   exceptional: The health state of the address pool is abnormal and some or all of the addresses that are referenced by the address pool are unavailable. In this case, the address pool is deemed abnormal.
        self.health_status = health_status
        # Remarks for the address.
        self.remark = remark
        # Unique request identification code.
        self.request_id = request_id
        # The mode used if the address with the smallest sequence number is recovered. This parameter is returned only when the policy for load balancing between addresses is sequence. Valid values:
        # 
        # *   preemptive: The address with the smallest sequence number is preferentially used if this address is recovered.
        # *   non_preemptive: The current address is still used even if the address with the smallest sequence number is recovered.
        self.sequence_lb_strategy_mode = sequence_lb_strategy_mode
        # The last modification time of the address pool.
        self.update_time = update_time
        # Last modification time of the address pool (timestamp).
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.addresses:
            self.addresses.validate()

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

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sequence_lb_strategy_mode is not None:
            result['SequenceLbStrategyMode'] = self.sequence_lb_strategy_mode

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

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
            temp_model = main_models.DescribeCloudGtmAddressPoolResponseBodyAddresses()
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

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SequenceLbStrategyMode') is not None:
            self.sequence_lb_strategy_mode = m.get('SequenceLbStrategyMode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeCloudGtmAddressPoolResponseBodyAddresses(DaraModel):
    def __init__(
        self,
        address: List[main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddress] = None,
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
                temp_model = main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddress()
                self.address.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmAddressPoolResponseBodyAddressesAddress(DaraModel):
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
        health_tasks: main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasks = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        request_source: main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressRequestSource = None,
        seq_non_preemptive_schedule: bool = None,
        serial_number: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        weight_value: int = None,
    ):
        # IP address or domain name.
        self.address = address
        # The address ID. This ID uniquely identifies the address.
        self.address_id = address_id
        # Address ownership information, not supported in the current version.
        self.attribute_info = attribute_info
        # The failover method that is used if the address fails health checks. Valid values:
        # 
        # *   auto: the automatic mode. The system determines whether to return an address based on the health check results. If the address fails health checks, the system does not return the address. If the address passes health checks, the system returns the address.
        # *   manual: the manual mode. If an address is in the unavailable state, the address is not returned for DNS requests even if the address passes health checks. If an address is in the available state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        self.available_mode = available_mode
        # Address availability status:
        # - available: Address available
        # - unavailable: Address unavailable
        self.available_status = available_status
        # Address creation time.
        self.create_time = create_time
        # Address creation time (timestamp).
        self.create_timestamp = create_timestamp
        # Address enable status, indicating whether the address is currently available:
        # - enable: Enabled status
        # - disable: Disabled status
        self.enable_status = enable_status
        # The condition for determining the health status of the address. Valid values:
        # 
        # *   any_ok: The health check results of at least one health check template are normal.
        # *   p30_ok: The health check results of at least 30% of health check templates are normal.
        # *   p50_ok: The health check results of at least 50% of health check templates are normal.
        # *   p70_ok: The health check results of at least 70% of health check templates are normal.
        # *   all_ok: The health check results of all health check templates are normal.
        self.health_judgement = health_judgement
        # The health check state of the address. Valid values:
        # 
        # *   ok: The address passes all health checks of the referenced health check templates.
        # *   ok_alert: The address fails some health checks of the referenced health check templates but the address is deemed normal.
        # *   ok_no_monitor: The address does not reference a health check template and is normal.
        # *   exceptional: The address fails some or all health checks of the referenced health check templates and the address is deemed abnormal.
        self.health_status = health_status
        # Health check task list.
        self.health_tasks = health_tasks
        # The availability state of the address when AvailableMode is set to manual. Valid values:
        # 
        # *   available: The address is normal. In this state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        # *   unavailable: The address is abnormal. In this state, the address is not returned for DNS requests even if the address passes health checks.
        self.manual_available_status = manual_available_status
        # Address name.
        self.name = name
        # Remarks for the address.
        self.remark = remark
        # The request source list.
        self.request_source = request_source
        # Indicates whether it is a sequential (non-preemptive) scheduling object for hybrid cloud management scenarios: - true: yes - false: no
        self.seq_non_preemptive_schedule = seq_non_preemptive_schedule
        # Sequence number, indicating the priority of address return, where smaller numbers have higher priority.
        self.serial_number = serial_number
        # The address type. Valid values:
        # 
        # *   IPv4: IPv4 address
        # *   IPv6: IPv6 address
        # *   domain: domain name
        self.type = type
        # The last time the address was modified.
        self.update_time = update_time
        # The last modification time of the address (timestamp).
        self.update_timestamp = update_timestamp
        # Weight value (an integer between 1 and 100, inclusive), allowing different weight values to be set for each address, enabling resolution queries to return addresses according to the weighted ratio.
        self.weight_value = weight_value

    def validate(self):
        if self.health_tasks:
            self.health_tasks.validate()
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

        if self.health_tasks is not None:
            result['HealthTasks'] = self.health_tasks.to_map()

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

        if m.get('HealthTasks') is not None:
            temp_model = main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasks()
            self.health_tasks = temp_model.from_map(m.get('HealthTasks'))

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestSource') is not None:
            temp_model = main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressRequestSource()
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

class DescribeCloudGtmAddressPoolResponseBodyAddressesAddressRequestSource(DaraModel):
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

class DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasks(DaraModel):
    def __init__(
        self,
        health_task: List[main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasksHealthTask] = None,
    ):
        self.health_task = health_task

    def validate(self):
        if self.health_task:
            for v1 in self.health_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HealthTask'] = []
        if self.health_task is not None:
            for k1 in self.health_task:
                result['HealthTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_task = []
        if m.get('HealthTask') is not None:
            for k1 in m.get('HealthTask'):
                temp_model = main_models.DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasksHealthTask()
                self.health_task.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmAddressPoolResponseBodyAddressesAddressHealthTasksHealthTask(DaraModel):
    def __init__(
        self,
        port: int = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The target service port for health check probes. When the health check protocol is set to Ping, configuration of the service port is not supported.
        self.port = port
        # ID of the health check template associated with the address.
        self.template_id = template_id
        # Health check template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

