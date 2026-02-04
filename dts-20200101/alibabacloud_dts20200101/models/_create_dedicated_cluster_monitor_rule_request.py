# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDedicatedClusterMonitorRuleRequest(DaraModel):
    def __init__(
        self,
        cpu_alarm_threshold: int = None,
        dedicated_cluster_id: str = None,
        disk_alarm_threshold: int = None,
        du_alarm_threshold: int = None,
        instance_id: str = None,
        mem_alarm_threshold: int = None,
        notice_switch: int = None,
        owner_id: str = None,
        phones: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The alert threshold for CPU utilization. Unit: percentage.
        self.cpu_alarm_threshold = cpu_alarm_threshold
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The alert threshold for disk usage. Unit: percentage.
        self.disk_alarm_threshold = disk_alarm_threshold
        # The alert threshold for DTS Unit (DU) usage. Unit: percentage.
        self.du_alarm_threshold = du_alarm_threshold
        # The ID of the instance.
        self.instance_id = instance_id
        # The alert threshold for memory usage. Unit: percentage.
        self.mem_alarm_threshold = mem_alarm_threshold
        # Specifies whether to enable the alert feature. Valid values:
        # 
        # *   **1**: enables the alert feature.
        # *   **0**: disables the alert feature.
        self.notice_switch = notice_switch
        self.owner_id = owner_id
        # The mobile phone number to which alerts are sent. Separate multiple mobile phone numbers with commas (,).
        # 
        # This parameter is required.
        self.phones = phones
        # The ID of the region in which the Data Transmission Service (DTS) instance resides.
        self.region_id = region_id
        # The resource group ID. This parameter is a global parameter and not required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_alarm_threshold is not None:
            result['CpuAlarmThreshold'] = self.cpu_alarm_threshold

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.disk_alarm_threshold is not None:
            result['DiskAlarmThreshold'] = self.disk_alarm_threshold

        if self.du_alarm_threshold is not None:
            result['DuAlarmThreshold'] = self.du_alarm_threshold

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mem_alarm_threshold is not None:
            result['MemAlarmThreshold'] = self.mem_alarm_threshold

        if self.notice_switch is not None:
            result['NoticeSwitch'] = self.notice_switch

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phones is not None:
            result['Phones'] = self.phones

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAlarmThreshold') is not None:
            self.cpu_alarm_threshold = m.get('CpuAlarmThreshold')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DiskAlarmThreshold') is not None:
            self.disk_alarm_threshold = m.get('DiskAlarmThreshold')

        if m.get('DuAlarmThreshold') is not None:
            self.du_alarm_threshold = m.get('DuAlarmThreshold')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemAlarmThreshold') is not None:
            self.mem_alarm_threshold = m.get('MemAlarmThreshold')

        if m.get('NoticeSwitch') is not None:
            self.notice_switch = m.get('NoticeSwitch')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Phones') is not None:
            self.phones = m.get('Phones')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

