# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeTimerGroupResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeTimerGroupResponseBodyData = None,
        request_id: str = None,
    ):
        # The configuration group.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeTimerGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTimerGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_count: int = None,
        bind_count_map: Dict[str, int] = None,
        config_timers: List[main_models.DescribeTimerGroupResponseBodyDataConfigTimers] = None,
        description: str = None,
        group_id: str = None,
        inner_timer_desc: str = None,
        inner_timer_name: str = None,
        is_bind: bool = None,
        is_update: bool = None,
        name: str = None,
        product_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The number of resources that are bound to the configuration group.
        self.bind_count = bind_count
        # The number of bound resources.
        self.bind_count_map = bind_count_map
        # The scheduled tasks.
        self.config_timers = config_timers
        # The description of the configuration group.
        self.description = description
        # The ID of the configuration group.
        self.group_id = group_id
        self.inner_timer_desc = inner_timer_desc
        self.inner_timer_name = inner_timer_name
        self.is_bind = is_bind
        self.is_update = is_update
        # The name of the configuration group.
        self.name = name
        # The service type of the configuration group.
        # 
        # Valid value:
        # 
        # *   CLOUD_DESKTOP: the cloud computer service.
        self.product_type = product_type
        # The state of the configuration group.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The configuration group is available.
        # *   UNAVAILABLE: The configuration group is deleted.
        # *   DELETING: The configuration group is being deleted.
        # *   UPDATING: The configuration group is being modified.
        self.status = status
        # The type of the configuration group.
        # 
        # Valid value:
        # 
        # *   Timer: the scheduled task type.
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
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.bind_count_map is not None:
            result['BindCountMap'] = self.bind_count_map

        result['ConfigTimers'] = []
        if self.config_timers is not None:
            for k1 in self.config_timers:
                result['ConfigTimers'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.inner_timer_desc is not None:
            result['InnerTimerDesc'] = self.inner_timer_desc

        if self.inner_timer_name is not None:
            result['InnerTimerName'] = self.inner_timer_name

        if self.is_bind is not None:
            result['IsBind'] = self.is_bind

        if self.is_update is not None:
            result['IsUpdate'] = self.is_update

        if self.name is not None:
            result['Name'] = self.name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('BindCountMap') is not None:
            self.bind_count_map = m.get('BindCountMap')

        self.config_timers = []
        if m.get('ConfigTimers') is not None:
            for k1 in m.get('ConfigTimers'):
                temp_model = main_models.DescribeTimerGroupResponseBodyDataConfigTimers()
                self.config_timers.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InnerTimerDesc') is not None:
            self.inner_timer_desc = m.get('InnerTimerDesc')

        if m.get('InnerTimerName') is not None:
            self.inner_timer_name = m.get('InnerTimerName')

        if m.get('IsBind') is not None:
            self.is_bind = m.get('IsBind')

        if m.get('IsUpdate') is not None:
            self.is_update = m.get('IsUpdate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeTimerGroupResponseBodyDataConfigTimers(DaraModel):
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
        segment_timers: List[main_models.DescribeTimerGroupResponseBodyDataConfigTimersSegmentTimers] = None,
        timer_type: str = None,
        trigger_type: str = None,
    ):
        # Indicates whether end users can configure scheduled tasks.
        self.allow_client_setting = allow_client_setting
        # The CRON expression for the scheduled task.
        self.cron_expression = cron_expression
        # Specifies whether to forcibly execute the scheduled task. A value of true specifies the scheduled task will run forcefully, ignoring the cloud computer and connection status.
        self.enforce = enforce
        # The interval at which the scheduled task is executed. Unit: minutes.
        self.interval = interval
        self.notification_time = notification_time
        # The type of the scheduled disconnection task.
        # 
        # Valid values:
        # 
        # *   Hibernate: scheduled hibernation.
        # *   Shutdown: scheduled shutdown.
        self.operation_type = operation_type
        # The process whitelist. If whitelisted processes are running, the scheduled task upon inactivity does not take effect.
        self.process_whitelist = process_whitelist
        # The reset operation of the scheduled task.
        # 
        # Valid values:
        # 
        # *   RESET_TYPE_SYSTEM: resets the system disk.
        # *   RESET_TYPE_USER_DISK: resets the data disk.
        # *   RESET_TYPE_BOTH: resets the system disk and data disk.
        self.reset_type = reset_type
        self.segment_timers = segment_timers
        # The type of the scheduled task.
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
                temp_model = main_models.DescribeTimerGroupResponseBodyDataConfigTimersSegmentTimers()
                self.segment_timers.append(temp_model.from_map(k1))

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class DescribeTimerGroupResponseBodyDataConfigTimersSegmentTimers(DaraModel):
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

