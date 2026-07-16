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
        # An array of scheduled task configurations.
        self.config_timers = config_timers
        # The description of the configuration group.
        self.description = description
        # The name of the configuration group.
        # 
        # This parameter is required.
        self.name = name
        # The product to which the configuration group applies.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The region ID. This feature is not region-specific. You must set this parameter to cn-shanghai.
        self.region_id = region_id
        # The type of the configuration group.
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
        # Whether to allow end users to configure the scheduled task.
        self.allow_client_setting = allow_client_setting
        # The cron expression for the scheduled task.
        # 
        # >Notice: 
        # 
        # The cron expression is based on UTC. For example, to run a task at 00:00 China Standard Time (UTC+8) every day, set this parameter to `0 0 16 ? * 1,2,3,4,5,6,7`.
        self.cron_expression = cron_expression
        # Whether to forcefully execute the scheduled task.
        self.enforce = enforce
        # The time interval, in minutes.
        self.interval = interval
        self.notification_time = notification_time
        # The operation to perform for the scheduled task. This parameter is valid only when `TimerType` is set to `NoConnect`.
        self.operation_type = operation_type
        # The process whitelist for smart detection. If a process from this whitelist is running, the inactivity-based scheduled task does not run.
        self.process_whitelist = process_whitelist
        # The reset type for the cloud desktop.
        self.reset_type = reset_type
        self.segment_timers = segment_timers
        # The type of the scheduled task.
        # 
        # This parameter is required.
        self.timer_type = timer_type
        # The trigger condition for inactivity-based scheduled tasks.
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
        create_snapshot: bool = None,
        end_cron_expression: str = None,
        enforce: bool = None,
        image_id: str = None,
        interval: int = None,
        ip_segments: List[str] = None,
        lock_screen_time: int = None,
        notification_time: int = None,
        operation_type: str = None,
        patch_id: str = None,
        process_whitelist: List[str] = None,
        reset_type: str = None,
        start_cron_expression: str = None,
        timer_order: int = None,
        timezone: str = None,
        trigger_type: str = None,
        verification_notification_time: int = None,
        verification_time: int = None,
    ):
        # The execution time for a one-time scheduled task, specified as a UNIX timestamp in milliseconds.
        self.appointment_timer = appointment_timer
        self.create_snapshot = create_snapshot
        self.end_cron_expression = end_cron_expression
        self.enforce = enforce
        # The image ID for a scheduled task that changes the image of a cloud desktop.
        self.image_id = image_id
        self.interval = interval
        self.ip_segments = ip_segments
        # The amount of inactive time, in seconds, before the screen automatically locks. This parameter applies only to Active Directory desktops.
        self.lock_screen_time = lock_screen_time
        self.notification_time = notification_time
        self.operation_type = operation_type
        self.patch_id = patch_id
        self.process_whitelist = process_whitelist
        self.reset_type = reset_type
        self.start_cron_expression = start_cron_expression
        self.timer_order = timer_order
        self.timezone = timezone
        self.trigger_type = trigger_type
        self.verification_notification_time = verification_notification_time
        self.verification_time = verification_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_timer is not None:
            result['AppointmentTimer'] = self.appointment_timer

        if self.create_snapshot is not None:
            result['CreateSnapshot'] = self.create_snapshot

        if self.end_cron_expression is not None:
            result['EndCronExpression'] = self.end_cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.ip_segments is not None:
            result['IpSegments'] = self.ip_segments

        if self.lock_screen_time is not None:
            result['LockScreenTime'] = self.lock_screen_time

        if self.notification_time is not None:
            result['NotificationTime'] = self.notification_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

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

        if self.verification_notification_time is not None:
            result['VerificationNotificationTime'] = self.verification_notification_time

        if self.verification_time is not None:
            result['VerificationTime'] = self.verification_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointmentTimer') is not None:
            self.appointment_timer = m.get('AppointmentTimer')

        if m.get('CreateSnapshot') is not None:
            self.create_snapshot = m.get('CreateSnapshot')

        if m.get('EndCronExpression') is not None:
            self.end_cron_expression = m.get('EndCronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IpSegments') is not None:
            self.ip_segments = m.get('IpSegments')

        if m.get('LockScreenTime') is not None:
            self.lock_screen_time = m.get('LockScreenTime')

        if m.get('NotificationTime') is not None:
            self.notification_time = m.get('NotificationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

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

        if m.get('VerificationNotificationTime') is not None:
            self.verification_notification_time = m.get('VerificationNotificationTime')

        if m.get('VerificationTime') is not None:
            self.verification_time = m.get('VerificationTime')

        return self

