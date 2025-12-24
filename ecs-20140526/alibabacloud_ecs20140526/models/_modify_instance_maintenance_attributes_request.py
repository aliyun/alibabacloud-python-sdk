# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceMaintenanceAttributesRequest(DaraModel):
    def __init__(
        self,
        action_on_maintenance: str = None,
        instance_id: List[str] = None,
        maintenance_window: List[main_models.ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow] = None,
        notify_on_maintenance: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The maintenance action. Valid values:
        # 
        # *   Stop: stops the instance.
        # *   AutoRecover: automatically recovers the instance.
        # *   AutoRedeploy: redeploys the instance, which may damage the data disks attached to the instance.
        self.action_on_maintenance = action_on_maintenance
        # The ID of instance N. Valid values of N: 1 to 100.
        self.instance_id = instance_id
        # The maintenance windows.
        self.maintenance_window = maintenance_window
        # Specifies whether to send an event notification before maintenance. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.notify_on_maintenance = notify_on_maintenance
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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
        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['MaintenanceWindow'] = []
        if self.maintenance_window is not None:
            for k1 in self.maintenance_window:
                result['MaintenanceWindow'].append(k1.to_map() if k1 else None)

        if self.notify_on_maintenance is not None:
            result['NotifyOnMaintenance'] = self.notify_on_maintenance

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.maintenance_window = []
        if m.get('MaintenanceWindow') is not None:
            for k1 in m.get('MaintenanceWindow'):
                temp_model = main_models.ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow()
                self.maintenance_window.append(temp_model.from_map(k1))

        if m.get('NotifyOnMaintenance') is not None:
            self.notify_on_maintenance = m.get('NotifyOnMaintenance')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyInstanceMaintenanceAttributesRequestMaintenanceWindow(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time of the maintenance window. The time must be on the hour. You must configure both StartTime and EndTime. The value of EndTime must be 1 to 23 hours later than the value of StartTime. Specify the time in the `HH:mm:ss` format. The time must be in UTC+8. Set the value of N to 1.
        self.end_time = end_time
        # The start time of the maintenance window. The time must be on the hour. You must configure both StartTime and EndTime. The value of EndTime must be 1 to 23 hours later than the value of StartTime. Specify the time in the `HH:mm:ss` format. The time must be in UTC+8. Set the value of N to 1.
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

