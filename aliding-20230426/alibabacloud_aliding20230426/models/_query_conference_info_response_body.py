# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryConferenceInfoResponseBody(DaraModel):
    def __init__(
        self,
        conf_info: main_models.QueryConferenceInfoResponseBodyConfInfo = None,
        request_id: str = None,
    ):
        self.conf_info = conf_info
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.conf_info:
            self.conf_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conf_info is not None:
            result['confInfo'] = self.conf_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confInfo') is not None:
            temp_model = main_models.QueryConferenceInfoResponseBodyConfInfo()
            self.conf_info = temp_model.from_map(m.get('confInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryConferenceInfoResponseBodyConfInfo(DaraModel):
    def __init__(
        self,
        active_num: int = None,
        attend_num: int = None,
        conf_duration: int = None,
        conference_id: str = None,
        creator_id: str = None,
        creator_nick: str = None,
        end_time: int = None,
        external_link_url: str = None,
        invited_num: int = None,
        room_code: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
    ):
        self.active_num = active_num
        self.attend_num = attend_num
        self.conf_duration = conf_duration
        self.conference_id = conference_id
        self.creator_id = creator_id
        self.creator_nick = creator_nick
        self.end_time = end_time
        self.external_link_url = external_link_url
        self.invited_num = invited_num
        self.room_code = room_code
        self.start_time = start_time
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_num is not None:
            result['ActiveNum'] = self.active_num

        if self.attend_num is not None:
            result['AttendNum'] = self.attend_num

        if self.conf_duration is not None:
            result['ConfDuration'] = self.conf_duration

        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick is not None:
            result['CreatorNick'] = self.creator_nick

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.external_link_url is not None:
            result['ExternalLinkUrl'] = self.external_link_url

        if self.invited_num is not None:
            result['InvitedNum'] = self.invited_num

        if self.room_code is not None:
            result['RoomCode'] = self.room_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveNum') is not None:
            self.active_num = m.get('ActiveNum')

        if m.get('AttendNum') is not None:
            self.attend_num = m.get('AttendNum')

        if m.get('ConfDuration') is not None:
            self.conf_duration = m.get('ConfDuration')

        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNick') is not None:
            self.creator_nick = m.get('CreatorNick')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExternalLinkUrl') is not None:
            self.external_link_url = m.get('ExternalLinkUrl')

        if m.get('InvitedNum') is not None:
            self.invited_num = m.get('InvitedNum')

        if m.get('RoomCode') is not None:
            self.room_code = m.get('RoomCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

