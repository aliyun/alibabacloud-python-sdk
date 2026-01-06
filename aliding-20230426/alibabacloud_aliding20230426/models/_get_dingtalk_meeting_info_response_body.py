# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDingtalkMeetingInfoResponseBody(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        conference_id: str = None,
        creator_id: str = None,
        creator_nick: str = None,
        creator_work_no: str = None,
        dept_name: str = None,
        enable_quality_monitor: bool = None,
        end_time: int = None,
        free_type: str = None,
        request_id: str = None,
        scene: str = None,
        start_time: int = None,
        time_length: int = None,
        title: str = None,
        user_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.cluster_name = cluster_name
        self.conference_id = conference_id
        self.creator_id = creator_id
        self.creator_nick = creator_nick
        self.creator_work_no = creator_work_no
        self.dept_name = dept_name
        self.enable_quality_monitor = enable_quality_monitor
        self.end_time = end_time
        self.free_type = free_type
        self.request_id = request_id
        self.scene = scene
        self.start_time = start_time
        self.time_length = time_length
        self.title = title
        self.user_count = user_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_nick is not None:
            result['creatorNick'] = self.creator_nick

        if self.creator_work_no is not None:
            result['creatorWorkNo'] = self.creator_work_no

        if self.dept_name is not None:
            result['deptName'] = self.dept_name

        if self.enable_quality_monitor is not None:
            result['enableQualityMonitor'] = self.enable_quality_monitor

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.free_type is not None:
            result['freeType'] = self.free_type

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scene is not None:
            result['scene'] = self.scene

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time_length is not None:
            result['timeLength'] = self.time_length

        if self.title is not None:
            result['title'] = self.title

        if self.user_count is not None:
            result['userCount'] = self.user_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorNick') is not None:
            self.creator_nick = m.get('creatorNick')

        if m.get('creatorWorkNo') is not None:
            self.creator_work_no = m.get('creatorWorkNo')

        if m.get('deptName') is not None:
            self.dept_name = m.get('deptName')

        if m.get('enableQualityMonitor') is not None:
            self.enable_quality_monitor = m.get('enableQualityMonitor')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('freeType') is not None:
            self.free_type = m.get('freeType')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeLength') is not None:
            self.time_length = m.get('timeLength')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userCount') is not None:
            self.user_count = m.get('userCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

