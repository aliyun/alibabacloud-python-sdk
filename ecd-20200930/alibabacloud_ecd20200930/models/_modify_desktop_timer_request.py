# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyDesktopTimerRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        desktop_timers: List[main_models.ModifyDesktopTimerRequestDesktopTimers] = None,
        region_id: str = None,
        use_desktop_timers: bool = None,
    ):
        # The IDs of the cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The details of the scheduled task on cloud computers.
        self.desktop_timers = desktop_timers
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to use the `DesktopTimers`** parameter. Set the value to `true`**.
        self.use_desktop_timers = use_desktop_timers

    def validate(self):
        if self.desktop_timers:
            for v1 in self.desktop_timers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k1 in self.desktop_timers:
                result['DesktopTimers'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.use_desktop_timers is not None:
            result['UseDesktopTimers'] = self.use_desktop_timers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k1 in m.get('DesktopTimers'):
                temp_model = main_models.ModifyDesktopTimerRequestDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UseDesktopTimers') is not None:
            self.use_desktop_timers = m.get('UseDesktopTimers')

        return self

class ModifyDesktopTimerRequestDesktopTimers(DaraModel):
    def __init__(
        self,
        allow_client_setting: bool = None,
        cron_expression: str = None,
        enforce: bool = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        # Specifies whether to allow end users to configure the scheduled task.
        self.allow_client_setting = allow_client_setting
        # The cron expression of the schedule.
        # 
        # > The time must be in UTC. For example, for 24:00 (UTC+8), you must set the value to 0 0 16 ? \\* 1,2,3,4,5,6,7
        self.cron_expression = cron_expression
        # Specifies whether to forcibly execute the scheduled task.
        # 
        # Valid values:
        # 
        # *   true: forcibly executes the scheduled task regardless of the status and connection of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false: does not forcibly execute the scheduled task.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enforce = enforce
        # The interval at which the scheduled task is executed. Unit: minutes.
        self.interval = interval
        # The operations that scheduled tasks support. This parameter is valid only when TimerType is set to NoConnect.
        # 
        # Valid values:
        # 
        # *   Hibernate: hibernates the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Shutdown: stops the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.operation_type = operation_type
        # The reset type of the cloud computers.
        # 
        # Valid values:
        # 
        # *   RESET_TYPE_SYSTE: resets the system disk.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RESET_TYPE_BOTH: resets data and user disks.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.reset_type = reset_type
        # The type of the scheduled task.
        # 
        # Valid values:
        # 
        # *   NoOperationDisconnect: Disconnects the cloud computers without performing operations on the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   LogoutShutdown: Stops the cloud computers when end users log out Alibaba Cloud Workspace clients.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NoConnect: Disconnects the cloud computers when end users perform one of the actions that is specified by the OperationType parameter.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TimerBoot: Starts the cloud computers on schedule.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TimerReset: Resets the cloud computers on schedule.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   LoginAutoConnect: automatically connects to the cloud computers when end users log on to Alibaba Cloud Workspace clients.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NoOperationShutdown: Stops the cloud computers without performing operations on the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TimerShutdown: Stops the cloud computers on schedule.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NoOperationReboot: Restarts the cloud computers without performing operations on the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TimerReboot: Restarts the cloud computers on schedule.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

