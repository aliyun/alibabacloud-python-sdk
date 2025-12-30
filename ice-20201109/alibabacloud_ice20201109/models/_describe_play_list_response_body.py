# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DescribePlayListResponseBody(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        play_list: List[main_models.DescribePlayListResponseBodyPlayList] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The page number.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size
        # The playback records.
        self.play_list = play_list
        # The ID of the request.
        self.request_id = request_id
        # The total playback count.
        self.total_num = total_num

    def validate(self):
        if self.play_list:
            for v1 in self.play_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PlayList'] = []
        if self.play_list is not None:
            for k1 in self.play_list:
                result['PlayList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.play_list = []
        if m.get('PlayList') is not None:
            for k1 in m.get('PlayList'):
                temp_model = main_models.DescribePlayListResponseBodyPlayList()
                self.play_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class DescribePlayListResponseBodyPlayList(DaraModel):
    def __init__(
        self,
        first_frame_duration: str = None,
        play_duration: str = None,
        play_ts: str = None,
        play_type: str = None,
        session_id: str = None,
        status: str = None,
        stuck_duration: str = None,
        trace_id: str = None,
        video_duration: str = None,
        video_id: str = None,
    ):
        # Time to first frame.
        self.first_frame_duration = first_frame_duration
        # The playback duration.
        self.play_duration = play_duration
        # The timestamp when the playback started.
        self.play_ts = play_ts
        # The playback type.
        self.play_type = play_type
        # The ID of the player session.
        self.session_id = session_id
        # The playback status.
        self.status = status
        # The stuttering duration.
        self.stuck_duration = stuck_duration
        # The TraceId of the player.
        self.trace_id = trace_id
        # The duration of the video.
        self.video_duration = video_duration
        # The ID of the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_frame_duration is not None:
            result['FirstFrameDuration'] = self.first_frame_duration

        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration

        if self.play_ts is not None:
            result['PlayTs'] = self.play_ts

        if self.play_type is not None:
            result['PlayType'] = self.play_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stuck_duration is not None:
            result['StuckDuration'] = self.stuck_duration

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstFrameDuration') is not None:
            self.first_frame_duration = m.get('FirstFrameDuration')

        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')

        if m.get('PlayTs') is not None:
            self.play_ts = m.get('PlayTs')

        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StuckDuration') is not None:
            self.stuck_duration = m.get('StuckDuration')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

