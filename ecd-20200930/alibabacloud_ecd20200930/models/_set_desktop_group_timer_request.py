# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDesktopGroupTimerRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        desktop_group_id: str = None,
        force: bool = None,
        region_id: str = None,
        reset_type: int = None,
        timer_type: int = None,
    ):
        # The cron expression for the scheduled task. This parameter is required when `TimerType` is set to 2, 3, or 4.
        self.cron_expression = cron_expression
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # Specifies whether to forcefully execute the scheduled task.
        self.force = force
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the disk that you want to reset.
        # 
        # Valid values:
        # 
        # - does not reset disks.
        # - resets only the system disk.
        # - resets only the user disk.
        # - resets the system disk and the user disk.
        self.reset_type = reset_type
        # The type of the scheduled task.
        # 
        # Valid values:
        # 
        # *   1: scheduled reset
        # *   2: scheduled startup
        # *   3: scheduled stop
        # *   4: scheduled restart
        # 
        # This parameter is required.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.force is not None:
            result['Force'] = self.force

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

