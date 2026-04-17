# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetAutoScalingConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAutoScalingConfigurationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value 200 indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAutoScalingConfigurationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAutoScalingConfigurationResponseBodyData(DaraModel):
    def __init__(
        self,
        scheduled_scaling_rules: main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules = None,
    ):
        self.scheduled_scaling_rules = scheduled_scaling_rules

    def validate(self):
        if self.scheduled_scaling_rules:
            self.scheduled_scaling_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheduled_scaling_rules is not None:
            result['ScheduledScalingRules'] = self.scheduled_scaling_rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduledScalingRules') is not None:
            temp_model = main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules()
            self.scheduled_scaling_rules = temp_model.from_map(m.get('ScheduledScalingRules'))

        return self

class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRules(DaraModel):
    def __init__(
        self,
        scheduled_scaling_rules: List[main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules] = None,
    ):
        self.scheduled_scaling_rules = scheduled_scaling_rules

    def validate(self):
        if self.scheduled_scaling_rules:
            for v1 in self.scheduled_scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScheduledScalingRules'] = []
        if self.scheduled_scaling_rules is not None:
            for k1 in self.scheduled_scaling_rules:
                result['ScheduledScalingRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheduled_scaling_rules = []
        if m.get('ScheduledScalingRules') is not None:
            for k1 in m.get('ScheduledScalingRules'):
                temp_model = main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules()
                self.scheduled_scaling_rules.append(temp_model.from_map(k1))

        return self

class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRules(DaraModel):
    def __init__(
        self,
        duration_minutes: int = None,
        enable: bool = None,
        estimated_elastic_scaling_down_time_secs: int = None,
        estimated_elastic_scaling_up_time_secs: int = None,
        first_scheduled_time: int = None,
        repeat_type: str = None,
        reserved_pub_flow: int = None,
        reserved_sub_flow: int = None,
        rule_id: int = None,
        rule_name: str = None,
        schedule_type: str = None,
        time_zone: str = None,
        weekly_types: main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes = None,
    ):
        self.duration_minutes = duration_minutes
        self.enable = enable
        self.estimated_elastic_scaling_down_time_secs = estimated_elastic_scaling_down_time_secs
        self.estimated_elastic_scaling_up_time_secs = estimated_elastic_scaling_up_time_secs
        self.first_scheduled_time = first_scheduled_time
        self.repeat_type = repeat_type
        self.reserved_pub_flow = reserved_pub_flow
        self.reserved_sub_flow = reserved_sub_flow
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.schedule_type = schedule_type
        self.time_zone = time_zone
        self.weekly_types = weekly_types

    def validate(self):
        if self.weekly_types:
            self.weekly_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_minutes is not None:
            result['DurationMinutes'] = self.duration_minutes

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.estimated_elastic_scaling_down_time_secs is not None:
            result['EstimatedElasticScalingDownTimeSecs'] = self.estimated_elastic_scaling_down_time_secs

        if self.estimated_elastic_scaling_up_time_secs is not None:
            result['EstimatedElasticScalingUpTimeSecs'] = self.estimated_elastic_scaling_up_time_secs

        if self.first_scheduled_time is not None:
            result['FirstScheduledTime'] = self.first_scheduled_time

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.reserved_pub_flow is not None:
            result['ReservedPubFlow'] = self.reserved_pub_flow

        if self.reserved_sub_flow is not None:
            result['ReservedSubFlow'] = self.reserved_sub_flow

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationMinutes') is not None:
            self.duration_minutes = m.get('DurationMinutes')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EstimatedElasticScalingDownTimeSecs') is not None:
            self.estimated_elastic_scaling_down_time_secs = m.get('EstimatedElasticScalingDownTimeSecs')

        if m.get('EstimatedElasticScalingUpTimeSecs') is not None:
            self.estimated_elastic_scaling_up_time_secs = m.get('EstimatedElasticScalingUpTimeSecs')

        if m.get('FirstScheduledTime') is not None:
            self.first_scheduled_time = m.get('FirstScheduledTime')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('ReservedPubFlow') is not None:
            self.reserved_pub_flow = m.get('ReservedPubFlow')

        if m.get('ReservedSubFlow') is not None:
            self.reserved_sub_flow = m.get('ReservedSubFlow')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('WeeklyTypes') is not None:
            temp_model = main_models.GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes()
            self.weekly_types = temp_model.from_map(m.get('WeeklyTypes'))

        return self

class GetAutoScalingConfigurationResponseBodyDataScheduledScalingRulesScheduledScalingRulesWeeklyTypes(DaraModel):
    def __init__(
        self,
        weekly_types: List[str] = None,
    ):
        self.weekly_types = weekly_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.weekly_types is not None:
            result['WeeklyTypes'] = self.weekly_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WeeklyTypes') is not None:
            self.weekly_types = m.get('WeeklyTypes')

        return self

