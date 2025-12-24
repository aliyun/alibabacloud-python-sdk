# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateConfigGroupRequest(DaraModel):
    def __init__(
        self,
        config_timers: List[main_models.CreateConfigGroupRequestConfigTimers] = None,
        description: str = None,
        name: str = None,
        product_type: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The scheduled task groups.
        self.config_timers = config_timers
        # The description of the configuration group.
        self.description = description
        # The name of the configuration group.
        # 
        # This parameter is required.
        self.name = name
        # The service type of the configuration group.
        # 
        # Valid value:
        # 
        # *   CLOUD_DESKTOP: the cloud computer service.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The ID of the region. Set the value to `cn-shanghai`.
        self.region_id = region_id
        # The group type.
        # 
        # Valid value:
        # 
        # *   Timer: a scheduled task group.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.config_timers:
            for v1 in self.config_timers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigTimers'] = []
        if self.config_timers is not None:
            for k1 in self.config_timers:
                result['ConfigTimers'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_timers = []
        if m.get('ConfigTimers') is not None:
            for k1 in m.get('ConfigTimers'):
                temp_model = main_models.CreateConfigGroupRequestConfigTimers()
                self.config_timers.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateConfigGroupRequestConfigTimers(DaraModel):
    def __init__(
        self,
        allow_client_setting: bool = None,
        cron_expression: str = None,
        enforce: bool = None,
        interval: int = None,
        notification_time: int = None,
        operation_type: str = None,
        process_whitelist: List[str] = None,
        reset_type: str = None,
        segment_timers: List[main_models.CreateConfigGroupRequestConfigTimersSegmentTimers] = None,
        timer_type: str = None,
        trigger_type: str = None,
    ):
        # Specifies whether to allow end users to configure the scheduled task.
        self.allow_client_setting = allow_client_setting
        # The cron expression specified in the scheduled task.
        # 
        # >  The time must be in UTC. For example, for 24:00 (UTC+8), you must set the value to 0 0 16 ? \\* 1,2,3,4,5,6,7
        self.cron_expression = cron_expression
        # Specifies whether to forcefully execute the scheduled task.
        self.enforce = enforce
        # The interval at which the scheduled task is executed. Unit: minutes.
        self.interval = interval
        self.notification_time = notification_time
        # The type of the scheduled operation. If you set TimerType to NoConnect, you can specify this parameter.
        # 
        # Valid values:
        # 
        # *   Hibernate: scheduled hibernation.
        # *   Shutdown: scheduled shutdown.
        self.operation_type = operation_type
        # The process whitelist. If whitelisted processes are running, the scheduled task does not take effect.
        self.process_whitelist = process_whitelist
        # The reset option.
        # 
        # Valid values:
        # 
        # *   RESET_TYPE_SYSTEM: resets only the system disk.
        # *   RESET_TYPE_USER_DISK: resets only the data disk.
        # *   RESET_TYPE_BOTH: resets the system and data disks.
        self.reset_type = reset_type
        self.segment_timers = segment_timers
        # The scheduled task type.
        # 
        # Valid values:
        # 
        # *   NoOperationDisconnect: scheduled disconnection upon inactivity.
        # *   NoConnect: scheduled disconnection upon specified operation (OperationType).
        # *   TimerBoot: scheduled start.
        # *   TimerReset: scheduled reset.
        # *   NoOperationShutdown: scheduled shutdown upon inactivity.
        # *   NoOperationHibernate: scheduled hibernation upon inactivity.
        # *   TimerShutdown: scheduled shutdown.
        # *   NoOperationReboot: scheduled restart upon inactivity.
        # *   TimerReboot: scheduled restart.
        # 
        # This parameter is required.
        self.timer_type = timer_type
        # The method to trigger the scheduled task upon inactivity.
        # 
        # Valid values:
        # 
        # *   Advanced: intelligent detection.
        # *   Standard: standard detection.
        self.trigger_type = trigger_type

    def validate(self):
        if self.segment_timers:
            for v1 in self.segment_timers:
                 if v1:
                    v1.validate()

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

        if self.notification_time is not None:
            result['NotificationTime'] = self.notification_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.process_whitelist is not None:
            result['ProcessWhitelist'] = self.process_whitelist

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        result['SegmentTimers'] = []
        if self.segment_timers is not None:
            for k1 in self.segment_timers:
                result['SegmentTimers'].append(k1.to_map() if k1 else None)

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

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

        if m.get('NotificationTime') is not None:
            self.notification_time = m.get('NotificationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ProcessWhitelist') is not None:
            self.process_whitelist = m.get('ProcessWhitelist')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        self.segment_timers = []
        if m.get('SegmentTimers') is not None:
            for k1 in m.get('SegmentTimers'):
                temp_model = main_models.CreateConfigGroupRequestConfigTimersSegmentTimers()
                self.segment_timers.append(temp_model.from_map(k1))

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class CreateConfigGroupRequestConfigTimersSegmentTimers(DaraModel):
    def __init__(
        self,
        appointment_timer: int = None,
        end_cron_expression: str = None,
        enforce: bool = None,
        image_id: str = None,
        interval: int = None,
        lock_screen_time: int = None,
        notification_time: int = None,
        operation_type: str = None,
        process_whitelist: List[str] = None,
        reset_type: str = None,
        start_cron_expression: str = None,
        timer_order: int = None,
        timezone: str = None,
        trigger_type: str = None,
    ):
        self.appointment_timer = appointment_timer
        self.end_cron_expression = end_cron_expression
        self.enforce = enforce
        self.image_id = image_id
        self.interval = interval
        self.lock_screen_time = lock_screen_time
        self.notification_time = notification_time
        self.operation_type = operation_type
        self.process_whitelist = process_whitelist
        self.reset_type = reset_type
        self.start_cron_expression = start_cron_expression
        self.timer_order = timer_order
        self.timezone = timezone
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_timer is not None:
            result['AppointmentTimer'] = self.appointment_timer

        if self.end_cron_expression is not None:
            result['EndCronExpression'] = self.end_cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.lock_screen_time is not None:
            result['LockScreenTime'] = self.lock_screen_time

        if self.notification_time is not None:
            result['NotificationTime'] = self.notification_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.process_whitelist is not None:
            result['ProcessWhitelist'] = self.process_whitelist

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.start_cron_expression is not None:
            result['StartCronExpression'] = self.start_cron_expression

        if self.timer_order is not None:
            result['TimerOrder'] = self.timer_order

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointmentTimer') is not None:
            self.appointment_timer = m.get('AppointmentTimer')

        if m.get('EndCronExpression') is not None:
            self.end_cron_expression = m.get('EndCronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LockScreenTime') is not None:
            self.lock_screen_time = m.get('LockScreenTime')

        if m.get('NotificationTime') is not None:
            self.notification_time = m.get('NotificationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ProcessWhitelist') is not None:
            self.process_whitelist = m.get('ProcessWhitelist')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('StartCronExpression') is not None:
            self.start_cron_expression = m.get('StartCronExpression')

        if m.get('TimerOrder') is not None:
            self.timer_order = m.get('TimerOrder')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

