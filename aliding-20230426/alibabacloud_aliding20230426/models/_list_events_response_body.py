# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.ListEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
        sync_token: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.events = events
        self.next_token = next_token
        # requestId
        self.request_id = request_id
        self.sync_token = sync_token
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sync_token is not None:
            result['syncToken'] = self.sync_token

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.ListEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('syncToken') is not None:
            self.sync_token = m.get('syncToken')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        attendees: List[main_models.ListEventsResponseBodyEventsAttendees] = None,
        categories: List[main_models.ListEventsResponseBodyEventsCategories] = None,
        create_time: str = None,
        description: str = None,
        end: main_models.ListEventsResponseBodyEventsEnd = None,
        extended_properties: main_models.ListEventsResponseBodyEventsExtendedProperties = None,
        id: str = None,
        is_all_day: bool = None,
        location: main_models.ListEventsResponseBodyEventsLocation = None,
        meeting_rooms: List[main_models.ListEventsResponseBodyEventsMeetingRooms] = None,
        online_meeting_info: main_models.ListEventsResponseBodyEventsOnlineMeetingInfo = None,
        organizer: main_models.ListEventsResponseBodyEventsOrganizer = None,
        origin_start: main_models.ListEventsResponseBodyEventsOriginStart = None,
        recurrence: main_models.ListEventsResponseBodyEventsRecurrence = None,
        reminders: List[main_models.ListEventsResponseBodyEventsReminders] = None,
        rich_text_description: main_models.ListEventsResponseBodyEventsRichTextDescription = None,
        series_master_id: str = None,
        start: main_models.ListEventsResponseBodyEventsStart = None,
        status: str = None,
        summary: str = None,
        update_time: str = None,
    ):
        self.attendees = attendees
        self.categories = categories
        self.create_time = create_time
        self.description = description
        self.end = end
        self.extended_properties = extended_properties
        self.id = id
        self.is_all_day = is_all_day
        self.location = location
        self.meeting_rooms = meeting_rooms
        self.online_meeting_info = online_meeting_info
        self.organizer = organizer
        self.origin_start = origin_start
        self.recurrence = recurrence
        self.reminders = reminders
        self.rich_text_description = rich_text_description
        self.series_master_id = series_master_id
        self.start = start
        self.status = status
        self.summary = summary
        self.update_time = update_time

    def validate(self):
        if self.attendees:
            for v1 in self.attendees:
                 if v1:
                    v1.validate()
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()
        if self.end:
            self.end.validate()
        if self.extended_properties:
            self.extended_properties.validate()
        if self.location:
            self.location.validate()
        if self.meeting_rooms:
            for v1 in self.meeting_rooms:
                 if v1:
                    v1.validate()
        if self.online_meeting_info:
            self.online_meeting_info.validate()
        if self.organizer:
            self.organizer.validate()
        if self.origin_start:
            self.origin_start.validate()
        if self.recurrence:
            self.recurrence.validate()
        if self.reminders:
            for v1 in self.reminders:
                 if v1:
                    v1.validate()
        if self.rich_text_description:
            self.rich_text_description.validate()
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

        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end is not None:
            result['End'] = self.end.to_map()

        if self.extended_properties is not None:
            result['ExtendedProperties'] = self.extended_properties.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.is_all_day is not None:
            result['IsAllDay'] = self.is_all_day

        if self.location is not None:
            result['Location'] = self.location.to_map()

        result['MeetingRooms'] = []
        if self.meeting_rooms is not None:
            for k1 in self.meeting_rooms:
                result['MeetingRooms'].append(k1.to_map() if k1 else None)

        if self.online_meeting_info is not None:
            result['OnlineMeetingInfo'] = self.online_meeting_info.to_map()

        if self.organizer is not None:
            result['Organizer'] = self.organizer.to_map()

        if self.origin_start is not None:
            result['OriginStart'] = self.origin_start.to_map()

        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence.to_map()

        result['Reminders'] = []
        if self.reminders is not None:
            for k1 in self.reminders:
                result['Reminders'].append(k1.to_map() if k1 else None)

        if self.rich_text_description is not None:
            result['RichTextDescription'] = self.rich_text_description.to_map()

        if self.series_master_id is not None:
            result['SeriesMasterId'] = self.series_master_id

        if self.start is not None:
            result['Start'] = self.start.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attendees = []
        if m.get('Attendees') is not None:
            for k1 in m.get('Attendees'):
                temp_model = main_models.ListEventsResponseBodyEventsAttendees()
                self.attendees.append(temp_model.from_map(k1))

        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.ListEventsResponseBodyEventsCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('End') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsEnd()
            self.end = temp_model.from_map(m.get('End'))

        if m.get('ExtendedProperties') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsExtendedProperties()
            self.extended_properties = temp_model.from_map(m.get('ExtendedProperties'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsAllDay') is not None:
            self.is_all_day = m.get('IsAllDay')

        if m.get('Location') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsLocation()
            self.location = temp_model.from_map(m.get('Location'))

        self.meeting_rooms = []
        if m.get('MeetingRooms') is not None:
            for k1 in m.get('MeetingRooms'):
                temp_model = main_models.ListEventsResponseBodyEventsMeetingRooms()
                self.meeting_rooms.append(temp_model.from_map(k1))

        if m.get('OnlineMeetingInfo') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsOnlineMeetingInfo()
            self.online_meeting_info = temp_model.from_map(m.get('OnlineMeetingInfo'))

        if m.get('Organizer') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsOrganizer()
            self.organizer = temp_model.from_map(m.get('Organizer'))

        if m.get('OriginStart') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsOriginStart()
            self.origin_start = temp_model.from_map(m.get('OriginStart'))

        if m.get('Recurrence') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsRecurrence()
            self.recurrence = temp_model.from_map(m.get('Recurrence'))

        self.reminders = []
        if m.get('Reminders') is not None:
            for k1 in m.get('Reminders'):
                temp_model = main_models.ListEventsResponseBodyEventsReminders()
                self.reminders.append(temp_model.from_map(k1))

        if m.get('RichTextDescription') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsRichTextDescription()
            self.rich_text_description = temp_model.from_map(m.get('RichTextDescription'))

        if m.get('SeriesMasterId') is not None:
            self.series_master_id = m.get('SeriesMasterId')

        if m.get('Start') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsStart()
            self.start = temp_model.from_map(m.get('Start'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListEventsResponseBodyEventsStart(DaraModel):
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
            result['Date'] = self.date

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class ListEventsResponseBodyEventsRichTextDescription(DaraModel):
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
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ListEventsResponseBodyEventsReminders(DaraModel):
    def __init__(
        self,
        method: str = None,
        minutes: str = None,
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
            result['Method'] = self.method

        if self.minutes is not None:
            result['Minutes'] = self.minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')

        return self

class ListEventsResponseBodyEventsRecurrence(DaraModel):
    def __init__(
        self,
        pattern: main_models.ListEventsResponseBodyEventsRecurrencePattern = None,
        range: main_models.ListEventsResponseBodyEventsRecurrenceRange = None,
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
            result['Pattern'] = self.pattern.to_map()

        if self.range is not None:
            result['Range'] = self.range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pattern') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsRecurrencePattern()
            self.pattern = temp_model.from_map(m.get('Pattern'))

        if m.get('Range') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsRecurrenceRange()
            self.range = temp_model.from_map(m.get('Range'))

        return self

class ListEventsResponseBodyEventsRecurrenceRange(DaraModel):
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
            result['EndDate'] = self.end_date

        if self.number_of_occurrences is not None:
            result['NumberOfOccurrences'] = self.number_of_occurrences

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('NumberOfOccurrences') is not None:
            self.number_of_occurrences = m.get('NumberOfOccurrences')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListEventsResponseBodyEventsRecurrencePattern(DaraModel):
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
            result['DayOfMonth'] = self.day_of_month

        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.index is not None:
            result['Index'] = self.index

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayOfMonth') is not None:
            self.day_of_month = m.get('DayOfMonth')

        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListEventsResponseBodyEventsOriginStart(DaraModel):
    def __init__(
        self,
        date_time: str = None,
    ):
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['DateTime'] = self.date_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        return self

class ListEventsResponseBodyEventsOrganizer(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        response_status: str = None,
        self_: bool = None,
    ):
        self.display_name = display_name
        self.response_status = response_status
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.response_status is not None:
            result['ResponseStatus'] = self.response_status

        if self.self_ is not None:
            result['Self'] = self.self_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ResponseStatus') is not None:
            self.response_status = m.get('ResponseStatus')

        if m.get('Self') is not None:
            self.self_ = m.get('Self')

        return self

class ListEventsResponseBodyEventsOnlineMeetingInfo(DaraModel):
    def __init__(
        self,
        conference_id: str = None,
        extra_info: Dict[str, Any] = None,
        type: str = None,
        url: str = None,
    ):
        self.conference_id = conference_id
        self.extra_info = extra_info
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListEventsResponseBodyEventsMeetingRooms(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        response_status: str = None,
        room_id: str = None,
    ):
        self.display_name = display_name
        self.response_status = response_status
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.response_status is not None:
            result['ResponseStatus'] = self.response_status

        if self.room_id is not None:
            result['RoomId'] = self.room_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ResponseStatus') is not None:
            self.response_status = m.get('ResponseStatus')

        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        return self

class ListEventsResponseBodyEventsLocation(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        meeting_rooms: List[str] = None,
    ):
        self.display_name = display_name
        self.meeting_rooms = meeting_rooms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.meeting_rooms is not None:
            result['MeetingRooms'] = self.meeting_rooms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('MeetingRooms') is not None:
            self.meeting_rooms = m.get('MeetingRooms')

        return self

class ListEventsResponseBodyEventsExtendedProperties(DaraModel):
    def __init__(
        self,
        shared_properties: main_models.ListEventsResponseBodyEventsExtendedPropertiesSharedProperties = None,
    ):
        self.shared_properties = shared_properties

    def validate(self):
        if self.shared_properties:
            self.shared_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shared_properties is not None:
            result['SharedProperties'] = self.shared_properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SharedProperties') is not None:
            temp_model = main_models.ListEventsResponseBodyEventsExtendedPropertiesSharedProperties()
            self.shared_properties = temp_model.from_map(m.get('SharedProperties'))

        return self

class ListEventsResponseBodyEventsExtendedPropertiesSharedProperties(DaraModel):
    def __init__(
        self,
        belong_corp_id: str = None,
        source_open_cid: str = None,
    ):
        self.belong_corp_id = belong_corp_id
        self.source_open_cid = source_open_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_corp_id is not None:
            result['BelongCorpId'] = self.belong_corp_id

        if self.source_open_cid is not None:
            result['SourceOpenCid'] = self.source_open_cid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongCorpId') is not None:
            self.belong_corp_id = m.get('BelongCorpId')

        if m.get('SourceOpenCid') is not None:
            self.source_open_cid = m.get('SourceOpenCid')

        return self

class ListEventsResponseBodyEventsEnd(DaraModel):
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
            result['Date'] = self.date

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class ListEventsResponseBodyEventsCategories(DaraModel):
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
            result['DisplayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        return self

class ListEventsResponseBodyEventsAttendees(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        is_optional: bool = None,
        response_status: str = None,
        self_: bool = None,
    ):
        self.display_name = display_name
        self.is_optional = is_optional
        self.response_status = response_status
        self.self_ = self_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_optional is not None:
            result['IsOptional'] = self.is_optional

        if self.response_status is not None:
            result['ResponseStatus'] = self.response_status

        if self.self_ is not None:
            result['Self'] = self.self_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsOptional') is not None:
            self.is_optional = m.get('IsOptional')

        if m.get('ResponseStatus') is not None:
            self.response_status = m.get('ResponseStatus')

        if m.get('Self') is not None:
            self.self_ = m.get('Self')

        return self

