# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmAddressResponseBody(DaraModel):
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
        health_tasks: main_models.DescribeCloudGtmAddressResponseBodyHealthTasks = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        request_id: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # IP address or domain name.
        self.address = address
        # The address ID. This ID uniquely identifies the address.
        self.address_id = address_id
        # Address ownership information.
        self.attribute_info = attribute_info
        # The failover method that is used if the address fails health checks. Valid values:
        # 
        # *   auto: the automatic mode. The system determines whether to return an address based on the health check results. If the address fails health checks, the system does not return the address. If the address passes health checks, the system returns the address.
        # *   manual: the manual mode. If an address is in the unavailable state, the address is not returned for Domain Name System (DNS) requests even if the address passes health checks. If an address is in the available state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        self.available_mode = available_mode
        # Address availability status:
        # - available: Available
        # - unavailable: Unavailable
        self.available_status = available_status
        # Address creation time.
        self.create_time = create_time
        # Creation time (timestamp).
        self.create_timestamp = create_timestamp
        # Indicates the current enabled status of the address:
        # enabled: enabled state
        # disabled: disabled state
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
        # *   ok_no_monitor: The address does not reference a health check template.
        # *   exceptional: The address fails some or all health checks of the referenced health check templates and the address is deemed abnormal.
        self.health_status = health_status
        # The health check tasks referenced by the address.
        self.health_tasks = health_tasks
        # The availability state of the address when AvailableMode is set to manual. Valid values:
        # 
        # *   available: The address is normal. In this state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        # *   unavailable: The address is abnormal. In this state, the address is not returned for DNS requests even if the address passes health checks.
        self.manual_available_status = manual_available_status
        # Address name.
        self.name = name
        # Remarks.
        self.remark = remark
        # Unique request identification code.
        self.request_id = request_id
        # Address type:
        # - IPv4
        # - IPv6
        # - domain
        self.type = type
        # The last modification time of the address configuration.
        self.update_time = update_time
        # Modified time (timestamp).
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.health_tasks:
            self.health_tasks.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

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
            temp_model = main_models.DescribeCloudGtmAddressResponseBodyHealthTasks()
            self.health_tasks = temp_model.from_map(m.get('HealthTasks'))

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeCloudGtmAddressResponseBodyHealthTasks(DaraModel):
    def __init__(
        self,
        health_task: List[main_models.DescribeCloudGtmAddressResponseBodyHealthTasksHealthTask] = None,
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
                temp_model = main_models.DescribeCloudGtmAddressResponseBodyHealthTasksHealthTask()
                self.health_task.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmAddressResponseBodyHealthTasksHealthTask(DaraModel):
    def __init__(
        self,
        monitor_status: str = None,
        port: int = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The state of the health check task. Valid values:
        # 
        # *   ok: The task is normal.
        # *   alert: An alert is triggered.
        # *   no_data: No data is available. In most cases, the health check task is newly created and no data is collected.
        self.monitor_status = monitor_status
        # The target service port for health checks. When the Ping protocol is selected for health checks, configuration of the service port is not supported.
        self.port = port
        # The ID of the health check template associated with the address.
        self.template_id = template_id
        # The name of the health check template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status

        if self.port is not None:
            result['Port'] = self.port

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

