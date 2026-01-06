# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateEventRequest(DaraModel):
    def __init__(
        self,
        attendees: List[main_models.CreateEventRequestAttendees] = None,
        card_instances: List[main_models.CreateEventRequestCardInstances] = None,
        description: str = None,
        end: main_models.CreateEventRequestEnd = None,
        extra: Dict[str, str] = None,
        is_all_day: bool = None,
        location: main_models.CreateEventRequestLocation = None,
        online_meeting_info: main_models.CreateEventRequestOnlineMeetingInfo = None,
        recurrence: main_models.CreateEventRequestRecurrence = None,
        reminders: List[main_models.CreateEventRequestReminders] = None,
        rich_text_description: main_models.CreateEventRequestRichTextDescription = None,
        summary: str = None,
        ui_configs: List[main_models.CreateEventRequestUiConfigs] = None,
        calendar_id: str = None,
        start: main_models.CreateEventRequestStart = None,
    ):
        self.attendees = attendees
        self.card_instances = card_instances
        self.description = description
        self.end = end
        self.extra = extra
        self.is_all_day = is_all_day
        self.location = location
        self.online_meeting_info = online_meeting_info
        self.recurrence = recurrence
        self.reminders = reminders
        self.rich_text_description = rich_text_description
        # This parameter is required.
        self.summary = summary
        self.ui_configs = ui_configs
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.start = start

    def validate(self):
        if self.attendees:
            for v1 in self.attendees:
                 if v1:
                    v1.validate()
        if self.card_instances:
            for v1 in self.card_instances:
                 if v1:
                    v1.validate()
        if self.end:
            self.end.validate()
        if self.location:
            self.location.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for v1 in self.reminders:
                 if v1:
                    v1.validate()
        if self.rich_text_description:
            self.rich_text_description.validate()
        if self.ui_configs:
            for v1 in self.ui_configs:
                 if v1:
                    v1.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attendees'] = []
        if self.attendees is not None:
            for k1 in self.attendees:
                result['Attendees'].append(k1.to_map() if k1 else None)

        result['CardInstances'] = []
        if self.card_instances is not None:
            for k1 in self.card_instances:
                result['CardInstances'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.end is not None:
            result['End'] = self.end.to_map()

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.is_all_day is not None:
            result['IsAllDay'] = self.is_all_day

        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.online_meeting_info is not None:
            result['OnlineMeetingInfo'] = self.online_meeting_info.to_map()

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence.to_map()

        result['Reminders'] = []
        if self.reminders is not None:
            for k1 in self.reminders:
                result['Reminders'].append(k1.to_map() if k1 else None)

        if self.rich_text_description is not None:
            result['RichTextDescription'] = self.rich_text_description.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary

        result['UiConfigs'] = []
        if self.ui_configs is not None:
            for k1 in self.ui_configs:
                result['UiConfigs'].append(k1.to_map() if k1 else None)

        if self.calendar_id is not None:
            result['calendarId'] = self.calendar_id

        if self.start is not None:
            result['start'] = self.start.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('Attendees') is not None:
            for k1 in m.get('Attendees'):
                temp_model = main_models.CreateEventRequestAttendees()
                self.attendees.append(temp_model.from_map(k1))

        self.card_instances = []
        if m.get('CardInstances') is not None:
            for k1 in m.get('CardInstances'):
                temp_model = main_models.CreateEventRequestCardInstances()
                self.card_instances.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('End') is not None:
            temp_model = main_models.CreateEventRequestEnd()
            self.end = temp_model.from_map(m.get('End'))

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('IsAllDay') is not None:
            self.is_all_day = m.get('IsAllDay')

        if m.get('Location') is not None:
            temp_model = main_models.CreateEventRequestLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('OnlineMeetingInfo') is not None:
            temp_model = main_models.CreateEventRequestOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m.get('OnlineMeetingInfo'))

        if m.get('Recurrence') is not None:
            temp_model = main_models.CreateEventRequestRecurrence()
            self.recurrence = temp_model.from_map(m.get('Recurrence'))

        self.reminders = []
        if m.get('Reminders') is not None:
            for k1 in m.get('Reminders'):
                temp_model = main_models.CreateEventRequestReminders()
                self.reminders.append(temp_model.from_map(k1))

        if m.get('RichTextDescription') is not None:
            temp_model = main_models.CreateEventRequestRichTextDescription()
            self.rich_text_description = temp_model.from_map(m.get('RichTextDescription'))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        self.ui_configs = []
        if m.get('UiConfigs') is not None:
            for k1 in m.get('UiConfigs'):
                temp_model = main_models.CreateEventRequestUiConfigs()
                self.ui_configs.append(temp_model.from_map(k1))

        if m.get('calendarId') is not None:
            self.calendar_id = m.get('calendarId')

        if m.get('start') is not None:
            temp_model = main_models.CreateEventRequestStart()
            self.start = temp_model.from_map(m.get('start'))

        return self

class CreateEventRequestStart(DaraModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.date_time is not None:
            result['dateTime'] = self.date_time

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

class CreateEventRequestUiConfigs(DaraModel):
    def __init__(
        self,
        ui_name: str = None,
        ui_status: str = None,
    ):
        self.ui_name = ui_name
        self.ui_status = ui_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ui_name is not None:
            result['uiName'] = self.ui_name

        if self.ui_status is not None:
            result['uiStatus'] = self.ui_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uiName') is not None:
            self.ui_name = m.get('uiName')

        if m.get('uiStatus') is not None:
            self.ui_status = m.get('uiStatus')

        return self

class CreateEventRequestRichTextDescription(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class CreateEventRequestReminders(DaraModel):
    def __init__(
        self,
        method: str = None,
        minutes: int = None,
    ):
        self.method = method
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method is not None:
            result['method'] = self.method

        if self.minutes is not None:
            result['minutes'] = self.minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('minutes') is not None:
            self.minutes = m.get('minutes')

        return self

class CreateEventRequestRecurrence(DaraModel):
    def __init__(
        self,
        pattern: main_models.CreateEventRequestRecurrencePattern = None,
        range: main_models.CreateEventRequestRecurrenceRange = None,
    ):
        self.pattern = pattern
        self.range = range

    def validate(self):
        if self.pattern:
            self.pattern.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern is not None:
            result['pattern'] = self.pattern.to_map()

        if self.range is not None:
            result['range'] = self.range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pattern') is not None:
            temp_model = main_models.CreateEventRequestRecurrencePattern()
            self.pattern = temp_model.from_map(m.get('pattern'))

        if m.get('range') is not None:
            temp_model = main_models.CreateEventRequestRecurrenceRange()
            self.range = temp_model.from_map(m.get('range'))

        return self

class CreateEventRequestRecurrenceRange(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        number_of_occurrences: int = None,
        type: str = None,
    ):
        self.end_date = end_date
        self.number_of_occurrences = number_of_occurrences
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.number_of_occurrences is not None:
            result['numberOfOccurrences'] = self.number_of_occurrences

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('numberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('numberOfOccurrences')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateEventRequestRecurrencePattern(DaraModel):
    def __init__(
        self,
        day_of_month: int = None,
        days_of_week: str = None,
        index: str = None,
        interval: int = None,
        type: str = None,
    ):
        self.day_of_month = day_of_month
        self.days_of_week = days_of_week
        self.index = index
        self.interval = interval
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_of_month is not None:
            result['dayOfMonth'] = self.day_of_month

        if self.days_of_week is not None:
            result['daysOfWeek'] = self.days_of_week

        if self.index is not None:
            result['index'] = self.index

        if self.interval is not None:
            result['interval'] = self.interval

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfMonth') is not None:
            self.day_of_month = m.get('dayOfMonth')

        if m.get('daysOfWeek') is not None:
            self.days_of_week = m.get('daysOfWeek')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateEventRequestOnlineMeetingInfo(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateEventRequestLocation(DaraModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self

class CreateEventRequestEnd(DaraModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.date_time is not None:
            result['dateTime'] = self.date_time

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

class CreateEventRequestCardInstances(DaraModel):
    def __init__(
        self,
        out_track_id: str = None,
        scenario: str = None,
    ):
        self.out_track_id = out_track_id
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_track_id is not None:
            result['OutTrackId'] = self.out_track_id

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutTrackId') is not None:
            self.out_track_id = m.get('OutTrackId')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        return self

class CreateEventRequestAttendees(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_optional: bool = None,
    ):
        self.id = id
        self.is_optional = is_optional

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.is_optional is not None:
            result['isOptional'] = self.is_optional

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isOptional') is not None:
            self.is_optional = m.get('isOptional')

        return self

