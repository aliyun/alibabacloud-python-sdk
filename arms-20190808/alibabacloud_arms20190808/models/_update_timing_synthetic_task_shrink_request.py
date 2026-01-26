# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTimingSyntheticTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        available_assertions_shrink: str = None,
        common_setting_shrink: str = None,
        custom_period_shrink: str = None,
        frequency: str = None,
        monitor_conf_shrink: str = None,
        monitors_shrink: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        task_id: str = None,
    ):
        # The list of assertions.
        self.available_assertions_shrink = available_assertions_shrink
        # The general settings.
        self.common_setting_shrink = common_setting_shrink
        # The custom cycle.
        self.custom_period_shrink = custom_period_shrink
        # The detection frequency. Valid values: 1m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, and 24h.
        self.frequency = frequency
        # The monitoring configurations.
        self.monitor_conf_shrink = monitor_conf_shrink
        # The list of monitoring points.
        self.monitors_shrink = monitors_shrink
        # The name of the task.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tags_shrink = tags_shrink
        # The ID of the synthetic monitoring task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_assertions_shrink is not None:
            result['AvailableAssertions'] = self.available_assertions_shrink

        if self.common_setting_shrink is not None:
            result['CommonSetting'] = self.common_setting_shrink

        if self.custom_period_shrink is not None:
            result['CustomPeriod'] = self.custom_period_shrink

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.monitor_conf_shrink is not None:
            result['MonitorConf'] = self.monitor_conf_shrink

        if self.monitors_shrink is not None:
            result['Monitors'] = self.monitors_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAssertions') is not None:
            self.available_assertions_shrink = m.get('AvailableAssertions')

        if m.get('CommonSetting') is not None:
            self.common_setting_shrink = m.get('CommonSetting')

        if m.get('CustomPeriod') is not None:
            self.custom_period_shrink = m.get('CustomPeriod')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('MonitorConf') is not None:
            self.monitor_conf_shrink = m.get('MonitorConf')

        if m.get('Monitors') is not None:
            self.monitors_shrink = m.get('Monitors')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

