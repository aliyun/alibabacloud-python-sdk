# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlarmsRequest(DaraModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        is_enable: bool = None,
        metric_name: str = None,
        metric_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        state: str = None,
    ):
        # The ID of the event-triggered task.
        self.alarm_task_id = alarm_task_id
        # Specifies whether the event-triggered task is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.is_enable = is_enable
        # The name of the metric.
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # 
        # - system: system metrics of CloudMonitor.
        # - custom: custom metrics reported to CloudMonitor.
        # - hybrid: metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        self.owner_id = owner_id
        # The page number of the scaling rule list. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The Settings for the number of entries per page in a paged query. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the region to which the event-triggered task belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group with which the event-triggered task is associated.
        self.scaling_group_id = scaling_group_id
        # The state of the event-triggered task. Valid values:
        # 
        # - ALARM: Alerting. The alert condition is met.
        # - OK: Normal. The alert condition is not met.
        # - INSUFFICIENT_DATA: Insufficient data. The data is insufficient to determine whether the alert condition is met.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

