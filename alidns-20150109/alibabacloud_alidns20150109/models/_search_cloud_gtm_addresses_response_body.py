# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchCloudGtmAddressesResponseBody(DaraModel):
    def __init__(
        self,
        addresses: main_models.SearchCloudGtmAddressesResponseBodyAddresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.addresses = addresses
        # Current page number, starting from **1**, default is **1**.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of **100** and a default of **20**.
        self.page_size = page_size
        # Unique request identification code.
        self.request_id = request_id
        # Total number of address entries that meet the query conditions.
        self.total_items = total_items
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.addresses:
            self.addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses is not None:
            result['Addresses'] = self.addresses.to_map()

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
        if m.get('Addresses') is not None:
            temp_model = main_models.SearchCloudGtmAddressesResponseBodyAddresses()
            self.addresses = temp_model.from_map(m.get('Addresses'))

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

class SearchCloudGtmAddressesResponseBodyAddresses(DaraModel):
    def __init__(
        self,
        address: List[main_models.SearchCloudGtmAddressesResponseBodyAddressesAddress] = None,
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
                temp_model = main_models.SearchCloudGtmAddressesResponseBodyAddressesAddress()
                self.address.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmAddressesResponseBodyAddressesAddress(DaraModel):
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
        health_tasks: main_models.SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasks = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
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
        self.health_tasks = health_tasks
        self.manual_available_status = manual_available_status
        self.name = name
        self.remark = remark
        self.type = type
        self.update_time = update_time
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
            temp_model = main_models.SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasks()
            self.health_tasks = temp_model.from_map(m.get('HealthTasks'))

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasks(DaraModel):
    def __init__(
        self,
        health_task: List[main_models.SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasksHealthTask] = None,
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
                temp_model = main_models.SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasksHealthTask()
                self.health_task.append(temp_model.from_map(k1))

        return self

class SearchCloudGtmAddressesResponseBodyAddressesAddressHealthTasksHealthTask(DaraModel):
    def __init__(
        self,
        monitor_status: str = None,
        port: int = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.monitor_status = monitor_status
        self.port = port
        self.template_id = template_id
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

