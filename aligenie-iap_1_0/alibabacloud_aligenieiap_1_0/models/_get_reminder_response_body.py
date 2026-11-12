# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class GetReminderResponseBody(DaraModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: main_models.GetReminderResponseBodyModel = None,
        success: bool = None,
    ):
        # Error code.
        self.error_code = error_code
        # Detailed description of the error message.
        self.error_msg = error_msg
        # Reminder information.
        self.model = model
        # Indicates the result of the API call. true means succeeded, and false means failed.
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Model') is not None:
            temp_model = main_models.GetReminderResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetReminderResponseBodyModel(DaraModel):
    def __init__(
        self,
        remind_responses: List[main_models.GetReminderResponseBodyModelRemindResponses] = None,
    ):
        # List of reminder information returned by invoking this API.
        self.remind_responses = remind_responses

    def validate(self):
        if self.remind_responses:
            for v1 in self.remind_responses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k1 in self.remind_responses:
                result['RemindResponses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k1 in m.get('RemindResponses'):
                temp_model = main_models.GetReminderResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k1))

        return self

class GetReminderResponseBodyModelRemindResponses(DaraModel):
    def __init__(
        self,
        action_topic: str = None,
        day_desc: str = None,
        recurrence_rule: main_models.GetReminderResponseBodyModelRemindResponsesRecurrenceRule = None,
        remind_id: int = None,
        remind_time: str = None,
        repeat_count: int = None,
        week: str = None,
    ):
        # The topic of the action executed by the reminder.
        self.action_topic = action_topic
        # Description of the trigger condition for the reminder.
        self.day_desc = day_desc
        # Schedule information list, which contains detailed timing information for the reminder.
        self.recurrence_rule = recurrence_rule
        # The ID of the reminder message.
        self.remind_id = remind_id
        # Next reminder time.
        self.remind_time = remind_time
        # The number of times the reminder repeats.
        self.repeat_count = repeat_count
        # The day of the week on which the reminder is triggered, indicating which day of the week the reminder occurs.
        self.week = week

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic

        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc

        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time

        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count

        if self.week is not None:
            result['Week'] = self.week

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')

        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')

        if m.get('RecurrenceRule') is not None:
            temp_model = main_models.GetReminderResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m.get('RecurrenceRule'))

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('Week') is not None:
            self.week = m.get('Week')

        return self

class GetReminderResponseBodyModelRemindResponsesRecurrenceRule(DaraModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: str = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: str = None,
        year: int = None,
    ):
        # The date on which the reminder is triggered.
        self.day = day
        # Information for monthly reminders.
        self.days_of_month = days_of_month
        # Information for weekly reminders.
        self.days_of_week = days_of_week
        # The end time when the reminder becomes inactive.
        self.end_date_time = end_date_time
        # The loop epoch of the reminder.
        self.freq = freq
        # The hour of the time when the reminder is triggered.
        self.hour = hour
        # The minute when the reminder is triggered.
        self.minute = minute
        # Month in which the reminder is triggered.
        self.month = month
        # The second of the time when the reminder is triggered.
        self.second = second
        # The start time when the reminder becomes effective.
        self.start_date_time = start_date_time
        # The year when the reminder is triggered.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day is not None:
            result['Day'] = self.day

        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month

        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time

        if self.freq is not None:
            result['Freq'] = self.freq

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.month is not None:
            result['Month'] = self.month

        if self.second is not None:
            result['Second'] = self.second

        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')

        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')

        if m.get('Freq') is not None:
            self.freq = m.get('Freq')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

