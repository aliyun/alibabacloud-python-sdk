# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWaitingRoomShrinkRequest(DaraModel):
    def __init__(
        self,
        cookie_name: str = None,
        custom_page_html: str = None,
        description: str = None,
        disable_session_renewal_enable: str = None,
        enable: str = None,
        host_name_and_path_shrink: str = None,
        json_response_enable: str = None,
        language: str = None,
        name: str = None,
        new_users_per_minute: str = None,
        queue_all_enable: str = None,
        queuing_method: str = None,
        queuing_status_code: str = None,
        session_duration: str = None,
        site_id: int = None,
        total_active_users: str = None,
        waiting_room_id: str = None,
        waiting_room_type: str = None,
    ):
        # The name of the custom cookie.
        self.cookie_name = cookie_name
        # The content of the custom waiting room page. You must specify this parameter if you set WaitingRoomType to custom. The content must be Base64-encoded.
        self.custom_page_html = custom_page_html
        # The description of the waiting room.
        self.description = description
        # Specifies whether to disable session renewal. Valid values:
        # 
        # *   on
        # *   off
        self.disable_session_renewal_enable = disable_session_renewal_enable
        # Specifies whether to enable the waiting room. Valid values:
        # 
        # *   on
        # *   off
        self.enable = enable
        # The hostname and path.
        self.host_name_and_path_shrink = host_name_and_path_shrink
        # Specifies whether to enable JSON response. If JSON response is enabled, a JSON body is returned for requests to the waiting room with the header Accept: application/json. Valid values:
        # 
        # *   on
        # *   off
        self.json_response_enable = json_response_enable
        # The language of the waiting room page. You must specify this parameter if you set WaitingRoomType to default. Valid values:
        # 
        # *   enus: English.
        # *   zhcn: Simplified Chinese.
        # *   zhhk: Traditional Chinese.
        self.language = language
        # The name of the waiting room.
        self.name = name
        # The maximum number of new users per minute.
        self.new_users_per_minute = new_users_per_minute
        # Specifies whether to queue all requests. Valid values:
        # 
        # *   on
        # *   off
        self.queue_all_enable = queue_all_enable
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
        # The maximum duration for which a session remains valid after a user leaves the origin. Unit: minutes.
        self.session_duration = session_duration
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The maximum number of active users.
        self.total_active_users = total_active_users
        # The ID of the waiting room, which can be obtained by calling the [ListWaitingRooms](https://help.aliyun.com/document_detail/2850279.html) operation.
        # 
        # This parameter is required.
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
        if self.cookie_name is not None:
            result['CookieName'] = self.cookie_name

        if self.custom_page_html is not None:
            result['CustomPageHtml'] = self.custom_page_html

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_session_renewal_enable is not None:
            result['DisableSessionRenewalEnable'] = self.disable_session_renewal_enable

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.host_name_and_path_shrink is not None:
            result['HostNameAndPath'] = self.host_name_and_path_shrink

        if self.json_response_enable is not None:
            result['JsonResponseEnable'] = self.json_response_enable

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.new_users_per_minute is not None:
            result['NewUsersPerMinute'] = self.new_users_per_minute

        if self.queue_all_enable is not None:
            result['QueueAllEnable'] = self.queue_all_enable

        if self.queuing_method is not None:
            result['QueuingMethod'] = self.queuing_method

        if self.queuing_status_code is not None:
            result['QueuingStatusCode'] = self.queuing_status_code

        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.total_active_users is not None:
            result['TotalActiveUsers'] = self.total_active_users

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        if self.waiting_room_type is not None:
            result['WaitingRoomType'] = self.waiting_room_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieName') is not None:
            self.cookie_name = m.get('CookieName')

        if m.get('CustomPageHtml') is not None:
            self.custom_page_html = m.get('CustomPageHtml')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableSessionRenewalEnable') is not None:
            self.disable_session_renewal_enable = m.get('DisableSessionRenewalEnable')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('HostNameAndPath') is not None:
            self.host_name_and_path_shrink = m.get('HostNameAndPath')

        if m.get('JsonResponseEnable') is not None:
            self.json_response_enable = m.get('JsonResponseEnable')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewUsersPerMinute') is not None:
            self.new_users_per_minute = m.get('NewUsersPerMinute')

        if m.get('QueueAllEnable') is not None:
            self.queue_all_enable = m.get('QueueAllEnable')

        if m.get('QueuingMethod') is not None:
            self.queuing_method = m.get('QueuingMethod')

        if m.get('QueuingStatusCode') is not None:
            self.queuing_status_code = m.get('QueuingStatusCode')

        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TotalActiveUsers') is not None:
            self.total_active_users = m.get('TotalActiveUsers')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        if m.get('WaitingRoomType') is not None:
            self.waiting_room_type = m.get('WaitingRoomType')

        return self

