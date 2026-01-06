# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryGroupLiveInfoResponseBody(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        duration: int = None,
        end_time: int = None,
        introduction: str = None,
        live_id: str = None,
        live_play_url: str = None,
        live_status: int = None,
        playback_duration: int = None,
        replay_url: str = None,
        request_id: str = None,
        staff_id: str = None,
        start_time: int = None,
        subscribe_count: int = None,
        title: str = None,
        uv: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.cover_url = cover_url
        self.duration = duration
        self.end_time = end_time
        self.introduction = introduction
        self.live_id = live_id
        self.live_play_url = live_play_url
        self.live_status = live_status
        self.playback_duration = playback_duration
        self.replay_url = replay_url
        # requestId
        self.request_id = request_id
        self.staff_id = staff_id
        self.start_time = start_time
        self.subscribe_count = subscribe_count
        self.title = title
        self.uv = uv
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.introduction is not None:
            result['introduction'] = self.introduction

        if self.live_id is not None:
            result['liveId'] = self.live_id

        if self.live_play_url is not None:
            result['livePlayUrl'] = self.live_play_url

        if self.live_status is not None:
            result['liveStatus'] = self.live_status

        if self.playback_duration is not None:
            result['playbackDuration'] = self.playback_duration

        if self.replay_url is not None:
            result['replayUrl'] = self.replay_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.staff_id is not None:
            result['staffId'] = self.staff_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.subscribe_count is not None:
            result['subscribeCount'] = self.subscribe_count

        if self.title is not None:
            result['title'] = self.title

        if self.uv is not None:
            result['uv'] = self.uv

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('introduction') is not None:
            self.introduction = m.get('introduction')

        if m.get('liveId') is not None:
            self.live_id = m.get('liveId')

        if m.get('livePlayUrl') is not None:
            self.live_play_url = m.get('livePlayUrl')

        if m.get('liveStatus') is not None:
            self.live_status = m.get('liveStatus')

        if m.get('playbackDuration') is not None:
            self.playback_duration = m.get('playbackDuration')

        if m.get('replayUrl') is not None:
            self.replay_url = m.get('replayUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('staffId') is not None:
            self.staff_id = m.get('staffId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('subscribeCount') is not None:
            self.subscribe_count = m.get('subscribeCount')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uv') is not None:
            self.uv = m.get('uv')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

