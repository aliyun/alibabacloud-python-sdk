# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceMaintenanceAttributesResponseBody(DaraModel):
    def __init__(
        self,
        maintenance_attributes: main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maintenance attributes.
        self.maintenance_attributes = maintenance_attributes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of queried maintenance attributes.
        self.total_count = total_count

    def validate(self):
        if self.maintenance_attributes:
            self.maintenance_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maintenance_attributes is not None:
            result['MaintenanceAttributes'] = self.maintenance_attributes.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaintenanceAttributes') is not None:
            temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributes()
            self.maintenance_attributes = temp_model.from_map(m.get('MaintenanceAttributes'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributes(DaraModel):
    def __init__(
        self,
        maintenance_attribute: List[main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttribute] = None,
    ):
        self.maintenance_attribute = maintenance_attribute

    def validate(self):
        if self.maintenance_attribute:
            for v1 in self.maintenance_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MaintenanceAttribute'] = []
        if self.maintenance_attribute is not None:
            for k1 in self.maintenance_attribute:
                result['MaintenanceAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.maintenance_attribute = []
        if m.get('MaintenanceAttribute') is not None:
            for k1 in m.get('MaintenanceAttribute'):
                temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttribute()
                self.maintenance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttribute(DaraModel):
    def __init__(
        self,
        action_on_maintenance: main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenance = None,
        instance_id: str = None,
        maintenance_windows: main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindows = None,
        notify_on_maintenance: bool = None,
    ):
        # The attributes of the maintenance action of the instance.
        self.action_on_maintenance = action_on_maintenance
        # The instance ID.
        self.instance_id = instance_id
        # The maintenance windows.
        self.maintenance_windows = maintenance_windows
        # Indicates whether an event notification was sent before maintenance.
        self.notify_on_maintenance = notify_on_maintenance

    def validate(self):
        if self.action_on_maintenance:
            self.action_on_maintenance.validate()
        if self.maintenance_windows:
            self.maintenance_windows.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.maintenance_windows is not None:
            result['MaintenanceWindows'] = self.maintenance_windows.to_map()

        if self.notify_on_maintenance is not None:
            result['NotifyOnMaintenance'] = self.notify_on_maintenance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionOnMaintenance') is not None:
            temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenance()
            self.action_on_maintenance = temp_model.from_map(m.get('ActionOnMaintenance'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaintenanceWindows') is not None:
            temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindows()
            self.maintenance_windows = temp_model.from_map(m.get('MaintenanceWindows'))

        if m.get('NotifyOnMaintenance') is not None:
            self.notify_on_maintenance = m.get('NotifyOnMaintenance')

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindows(DaraModel):
    def __init__(
        self,
        maintenance_window: List[main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindowsMaintenanceWindow] = None,
    ):
        self.maintenance_window = maintenance_window

    def validate(self):
        if self.maintenance_window:
            for v1 in self.maintenance_window:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MaintenanceWindow'] = []
        if self.maintenance_window is not None:
            for k1 in self.maintenance_window:
                result['MaintenanceWindow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.maintenance_window = []
        if m.get('MaintenanceWindow') is not None:
            for k1 in m.get('MaintenanceWindow'):
                temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindowsMaintenanceWindow()
                self.maintenance_window.append(temp_model.from_map(k1))

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeMaintenanceWindowsMaintenanceWindow(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time of the maintenance window.
        self.end_time = end_time
        # The start time of the maintenance window.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenance(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        supported_values: main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenanceSupportedValues = None,
        value: str = None,
    ):
        # The default maintenance action.
        self.default_value = default_value
        # The supported maintenance actions.
        self.supported_values = supported_values
        # The current maintenance action. Valid values:
        # 
        # *   Stop: stops the instance.
        # *   AutoRecover: automatically recovers the instance.
        # *   AutoRedeploy: redeploys the instance, which may damage the data disks attached to the instance.
        self.value = value

    def validate(self):
        if self.supported_values:
            self.supported_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.supported_values is not None:
            result['SupportedValues'] = self.supported_values.to_map()

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('SupportedValues') is not None:
            temp_model = main_models.DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenanceSupportedValues()
            self.supported_values = temp_model.from_map(m.get('SupportedValues'))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeInstanceMaintenanceAttributesResponseBodyMaintenanceAttributesMaintenanceAttributeActionOnMaintenanceSupportedValues(DaraModel):
    def __init__(
        self,
        supported_value: List[str] = None,
    ):
        self.supported_value = supported_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_value is not None:
            result['SupportedValue'] = self.supported_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedValue') is not None:
            self.supported_value = m.get('SupportedValue')

        return self

