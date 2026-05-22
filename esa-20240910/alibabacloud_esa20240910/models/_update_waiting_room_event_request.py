# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWaitingRoomEventRequest(DaraModel):
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
        site_id: int = None,
        start_time: str = None,
        total_active_users: str = None,
        waiting_room_event_id: int = None,
        waiting_room_type: str = None,
    ):
        self.custom_page_html = custom_page_html
        self.description = description
        self.disable_session_renewal_enable = disable_session_renewal_enable
        self.enable = enable
        self.end_time = end_time
        self.json_response_enable = json_response_enable
        self.language = language
        self.name = name
        self.new_users_per_minute = new_users_per_minute
        self.pre_queue_enable = pre_queue_enable
        self.pre_queue_start_time = pre_queue_start_time
        self.queuing_method = queuing_method
        self.queuing_status_code = queuing_status_code
        self.random_pre_queue_enable = random_pre_queue_enable
        self.session_duration = session_duration
        # This parameter is required.
        self.site_id = site_id
        self.start_time = start_time
        self.total_active_users = total_active_users
        # This parameter is required.
        self.waiting_room_event_id = waiting_room_event_id
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

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users

        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id

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

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')

        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')

        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')

        return self

