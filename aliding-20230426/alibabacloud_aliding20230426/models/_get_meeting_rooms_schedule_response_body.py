# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetMeetingRoomsScheduleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schedule_information: List[main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformation] = None,
    ):
        # requestId
        self.request_id = request_id
        self.schedule_information = schedule_information

    def validate(self):
        if self.schedule_information:
            for v1 in self.schedule_information:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['scheduleInformation'] = []
        if self.schedule_information is not None:
            for k1 in self.schedule_information:
                result['scheduleInformation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.schedule_information = []
        if m.get('scheduleInformation') is not None:
            for k1 in m.get('scheduleInformation'):
                temp_model = main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformation()
                self.schedule_information.append(temp_model.from_map(k1))

        return self

class GetMeetingRoomsScheduleResponseBodyScheduleInformation(DaraModel):
    def __init__(
        self,
        error: str = None,
        room_id: str = None,
        schedule_items: List[main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItems] = None,
    ):
        self.error = error
        self.room_id = room_id
        self.schedule_items = schedule_items

    def validate(self):
        if self.schedule_items:
            for v1 in self.schedule_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.room_id is not None:
            result['RoomId'] = self.room_id

        result['ScheduleItems'] = []
        if self.schedule_items is not None:
            for k1 in self.schedule_items:
                result['ScheduleItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        self.schedule_items = []
        if m.get('ScheduleItems') is not None:
            for k1 in m.get('ScheduleItems'):
                temp_model = main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItems()
                self.schedule_items.append(temp_model.from_map(k1))

        return self

class GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItems(DaraModel):
    def __init__(
        self,
        end: main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsEnd = None,
        event_id: str = None,
        organizer: main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsOrganizer = None,
        start: main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsStart = None,
        status: str = None,
    ):
        self.end = end
        self.event_id = event_id
        self.organizer = organizer
        self.start = start
        self.status = status

    def validate(self):
        if self.end:
            self.end.validate()
        if self.organizer:
            self.organizer.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end.to_map()

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.organizer is not None:
            result['Organizer'] = self.organizer.to_map()

        if self.start is not None:
            result['Start'] = self.start.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            temp_model = main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsEnd()
            self.end = temp_model.from_map(m.get('End'))

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Organizer') is not None:
            temp_model = main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsOrganizer()
            self.organizer = temp_model.from_map(m.get('Organizer'))

        if m.get('Start') is not None:
            temp_model = main_models.GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsStart()
            self.start = temp_model.from_map(m.get('Start'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsStart(DaraModel):
    def __init__(
        self,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsOrganizer(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetMeetingRoomsScheduleResponseBodyScheduleInformationScheduleItemsEnd(DaraModel):
    def __init__(
        self,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

