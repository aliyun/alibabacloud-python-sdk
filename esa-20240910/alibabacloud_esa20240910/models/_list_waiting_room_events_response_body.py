# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWaitingRoomEventsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_events: List[main_models.ListWaitingRoomEventsResponseBodyWaitingRoomEvents] = None,
    ):
        # The request ID, which is used to trace a call.
        self.request_id = request_id
        # The details of the waiting room events.
        self.waiting_room_events = waiting_room_events

    def validate(self):
        if self.waiting_room_events:
            for v1 in self.waiting_room_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WaitingRoomEvents'] = []
        if self.waiting_room_events is not None:
            for k1 in self.waiting_room_events:
                result['WaitingRoomEvents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.waiting_room_events = []
        if m.get('WaitingRoomEvents') is not None:
            for k1 in m.get('WaitingRoomEvents'):
                temp_model = main_models.ListWaitingRoomEventsResponseBodyWaitingRoomEvents()
                self.waiting_room_events.append(temp_model.from_map(k1))

        return self

class ListWaitingRoomEventsResponseBodyWaitingRoomEvents(DaraModel):
    def __init__(
        self,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        end_time: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        pre_queue_enable: str = None,
        pre_queue_start_time: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        random_pre_queue_enable: str = None,
        session_duration: str = None,
        start_time: str = None,
        total_active_users: str = None,
        waiting_room_event_id: int = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        # The content of the custom waiting room page. This parameter is returned when the waiting room type is set to custom. The content is URL-encoded.
        self.custom_page_html = custom_page_html
        # The event description.
        self.description = description
        # Indicates whether session renewal is disabled. Valid values:
        # 
        # *   on
        # *   off
        self.disable_session_renewal_enable = disable_session_renewal_enable
        # The event status. Valid values:
        # 
        # *   on
        # *   off
        self.enable = enable
        # The end time of the event. This value is a UNIX timestamp.
        self.end_time = end_time
        # Indicates whether JOSN response is enabled. If JSON response is enabled, a JSON body is returned for requests to the waiting room with the header Accept: application/json. Valid values:
        # 
        # *   on
        # *   off
        self.json_response_enable = json_response_enable
        # The language of the waiting room page. This parameter is returned when the waiting room type is set to default. Valid values:
        # 
        # *   enus: English.
        # *   zhcn: Simplified Chinese.
        # *   zhhk: Traditional Chinese.
        self.language = language
        # The custom event name.
        self.name = name
        # The maximum number of new users per minute.
        self.new_users_per_minute = new_users_per_minute
        # Indicates whether pre-queuing is enabled. Valid values:
        # 
        # *   on
        # *   off
        self.pre_queue_enable = pre_queue_enable
        # The start time for pre-queuing. This value is a UNIX timestamp. This parameter is valid only when pre-queuing is enabled.
        self.pre_queue_start_time = pre_queue_start_time
        # The queuing method. Valid values:
        # 
        # *   random: Users gain access to the origin randomly, regardless of the arrival time.
        # *   fifo: Users gain access to the origin in order of arrival.
        # *   passthrough: Users pass through the waiting room and go straight to the origin.
        # *   reject-all: Users are blocked from reaching the origin.
        self.queuing_method = queuing_method
        # The HTTP status code to return while a user is in the queue. Valid values:
        # 
        # *   200
        # *   202
        # *   429
        self.queuing_status_code = queuing_status_code
        # Indicates whether random queuing is enabled. Valid values:
        # 
        # *   on
        # *   off
        self.random_pre_queue_enable = random_pre_queue_enable
        # The maximum duration for which a session remains valid after a user leaves the origin. Unit: minutes.
        self.session_duration = session_duration
        # The start time of the event. This value is a UNIX timestamp.
        self.start_time = start_time
        # The maximum number of active users.
        self.total_active_users = total_active_users
        # The unique ID of the waiting room event.
        self.waiting_room_event_id = waiting_room_event_id
        # The ID of the waiting room associated with the event.
        self.waiting_room_id = waiting_room_id
        # The type of the waiting room. Valid values:
        # 
        # *   default
        # *   custom
        self.waiting_room_type = waiting_room_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute

        if self.pre_queue_enable is not None:
            result['PreQueueEnable'] = self.pre_queue_enable

        if self.pre_queue_start_time is not None:
            result['PreQueueStartTime'] = self.pre_queue_start_time

        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method

        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code

        if self.random_pre_queue_enable is not None:
            result['RandomPreQueueEnable'] = self.random_pre_queue_enable

        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users

        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')

        if m.get('PreQueueEnable') is not None:
            self.pre_queue_enable = m.get('PreQueueEnable')

        if m.get('PreQueueStartTime') is not None:
            self.pre_queue_start_time = m.get('PreQueueStartTime')

        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')

        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')

        if m.get('RandomPreQueueEnable') is not None:
            self.random_pre_queue_enable = m.get('RandomPreQueueEnable')

        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')

        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')

        return self

