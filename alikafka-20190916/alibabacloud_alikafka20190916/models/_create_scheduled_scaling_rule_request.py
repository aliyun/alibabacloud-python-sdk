# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScheduledScalingRuleRequest(DaraModel):
    def __init__(
        self,
        duration_minutes: int = None,
        enable: bool = None,
        first_scheduled_time: int = None,
        instance_id: str = None,
        region_id: str = None,
        repeat_type: str = None,
        reserved_pub_flow: int = None,
        reserved_sub_flow: int = None,
        rule_name: str = None,
        schedule_type: str = None,
        time_zone: str = None,
        weekly_types: List[str] = None,
    ):
        # The duration (unit: minutes) of a single scheduled elastic scaling task.
        # 
        # > The value must be at least 15 minutes.
        # 
        # This parameter is required.
        self.duration_minutes = duration_minutes
        # Specifies whether to enable or disable the scheduled policy. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable = enable
        # The time when the scheduled policy starts to take effect.
        # 
        # If the schedule type is single execution, the start time must be at least 30 minutes later than the current time.
        # 
        # 
        # 
        # >Notice: To prevent the server from continuously performing scale-up and scale-down tasks, the interval between different scheduled tasks must be at least 60 minutes.
        # 
        # This parameter is required.
        self.first_scheduled_time = first_scheduled_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The repeat type. This parameter is required when ScheduleType is set to repeat. Valid values:
        #       <li> Daily: timed scheduling every day.
        #       <li> Weekly: timed scheduling every week.
        self.repeat_type = repeat_type
        # The reserved production specification for scheduled elastic scaling (unit: MB/s).
        # 
        # > At least one of ReservedPubFlow and ReservedSubFlow must be higher than the current specification.
        # 
        # This parameter is required.
        self.reserved_pub_flow = reserved_pub_flow
        # The reserved consumption specification for scheduled elastic scaling (unit: MB/s).
        # > At least one of ReservedSubFlow and ReservedPubFlow must be higher than the current specification.
        # 
        # This parameter is required.
        self.reserved_sub_flow = reserved_sub_flow
        # The name of the scheduled policy rule.
        # 
        # > The name must be unique among all rules of the same instance.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The schedule type. Valid values:
        # 
        # - at: scheduled once only.
        # 
        # - repeat: scheduled repeatedly.
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # The time zone (Coordinated Universal Time).
        # 
        # This parameter is required.
        self.time_zone = time_zone
        # The days of the week. Multiple days are supported for repeated execution.
        self.weekly_types = weekly_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_minutes is not None:
            result['DurationMinutes'] = self.duration_minutes

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.first_scheduled_time is not None:
            result['FirstScheduledTime'] = self.first_scheduled_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.reserved_pub_flow is not None:
            result['ReservedPubFlow'] = self.reserved_pub_flow

        if self.reserved_sub_flow is not None:
            result['ReservedSubFlow'] = self.reserved_sub_flow

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationMinutes') is not None:
            self.duration_minutes = m.get('DurationMinutes')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FirstScheduledTime') is not None:
            self.first_scheduled_time = m.get('FirstScheduledTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('ReservedPubFlow') is not None:
            self.reserved_pub_flow = m.get('ReservedPubFlow')

        if m.get('ReservedSubFlow') is not None:
            self.reserved_sub_flow = m.get('ReservedSubFlow')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('WeeklyTypes') is not None:
            self.weekly_types = m.get('WeeklyTypes')

        return self

