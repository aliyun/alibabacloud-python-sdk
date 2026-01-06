# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDingtalkMeetingMemberListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.GetDingtalkMeetingMemberListResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.current_page = current_page
        self.data = data
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetDingtalkMeetingMemberListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetDingtalkMeetingMemberListResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        conference_id: str = None,
        device_type: str = None,
        duration: int = None,
        join_time: int = None,
        leave_time: int = None,
        network_quality: str = None,
        nick: str = None,
        role: str = None,
        session_id: str = None,
        status: str = None,
        union_id: str = None,
        version: str = None,
        work_no: str = None,
    ):
        self.channel_name = channel_name
        self.conference_id = conference_id
        self.device_type = device_type
        self.duration = duration
        self.join_time = join_time
        self.leave_time = leave_time
        self.network_quality = network_quality
        self.nick = nick
        self.role = role
        self.session_id = session_id
        self.status = status
        self.union_id = union_id
        self.version = version
        self.work_no = work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['channelName'] = self.channel_name

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.device_type is not None:
            result['deviceType'] = self.device_type

        if self.duration is not None:
            result['duration'] = self.duration

        if self.join_time is not None:
            result['joinTime'] = self.join_time

        if self.leave_time is not None:
            result['leaveTime'] = self.leave_time

        if self.network_quality is not None:
            result['networkQuality'] = self.network_quality

        if self.nick is not None:
            result['nick'] = self.nick

        if self.role is not None:
            result['role'] = self.role

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        if self.union_id is not None:
            result['unionId'] = self.union_id

        if self.version is not None:
            result['version'] = self.version

        if self.work_no is not None:
            result['workNo'] = self.work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('joinTime') is not None:
            self.join_time = m.get('joinTime')

        if m.get('leaveTime') is not None:
            self.leave_time = m.get('leaveTime')

        if m.get('networkQuality') is not None:
            self.network_quality = m.get('networkQuality')

        if m.get('nick') is not None:
            self.nick = m.get('nick')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('unionId') is not None:
            self.union_id = m.get('unionId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workNo') is not None:
            self.work_no = m.get('workNo')

        return self

