# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryConferenceInfoByRoomCodeResponseBody(DaraModel):
    def __init__(
        self,
        conference_list: List[main_models.QueryConferenceInfoByRoomCodeResponseBodyConferenceList] = None,
        dingtalk_request_id: str = None,
        has_more: bool = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.conference_list = conference_list
        self.dingtalk_request_id = dingtalk_request_id
        self.has_more = has_more
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.conference_list:
            for v1 in self.conference_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conferenceList'] = []
        if self.conference_list is not None:
            for k1 in self.conference_list:
                result['conferenceList'].append(k1.to_map() if k1 else None)

        if self.dingtalk_request_id is not None:
            result['dingtalkRequestId'] = self.dingtalk_request_id

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conference_list = []
        if m.get('conferenceList') is not None:
            for k1 in m.get('conferenceList'):
                temp_model = main_models.QueryConferenceInfoByRoomCodeResponseBodyConferenceList()
                self.conference_list.append(temp_model.from_map(k1))

        if m.get('dingtalkRequestId') is not None:
            self.dingtalk_request_id = m.get('dingtalkRequestId')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryConferenceInfoByRoomCodeResponseBodyConferenceList(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        conf_duration: int = None,
        conference_id: str = None,
        creator_id: str = None,
        creator_nick: str = None,
        end_time: int = None,
        external_link_url: str = None,
        room_code: str = None,
        schedule_conference_id: str = None,
        start_time: int = None,
        status: int = None,
        title: str = None,
    ):
        self.biz_type = biz_type
        self.conf_duration = conf_duration
        self.conference_id = conference_id
        self.creator_id = creator_id
        self.creator_nick = creator_nick
        self.end_time = end_time
        self.external_link_url = external_link_url
        self.room_code = room_code
        self.schedule_conference_id = schedule_conference_id
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

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

        if self.room_code is not None:
            result['RoomCode'] = self.room_code

        if self.schedule_conference_id is not None:
            result['ScheduleConferenceId'] = self.schedule_conference_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

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

        if m.get('RoomCode') is not None:
            self.room_code = m.get('RoomCode')

        if m.get('ScheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('ScheduleConferenceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

