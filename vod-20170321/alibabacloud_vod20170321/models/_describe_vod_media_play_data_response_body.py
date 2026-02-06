# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodMediaPlayDataResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        qoe_info_list: List[main_models.DescribeVodMediaPlayDataResponseBodyQoeInfoList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The data returned.
        self.qoe_info_list = qoe_info_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.qoe_info_list:
            for v1 in self.qoe_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['QoeInfoList'] = []
        if self.qoe_info_list is not None:
            for k1 in self.qoe_info_list:
                result['QoeInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.qoe_info_list = []
        if m.get('QoeInfoList') is not None:
            for k1 in m.get('QoeInfoList'):
                temp_model = main_models.DescribeVodMediaPlayDataResponseBodyQoeInfoList()
                self.qoe_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVodMediaPlayDataResponseBodyQoeInfoList(DaraModel):
    def __init__(
        self,
        dau: float = None,
        media_id: str = None,
        play_duration: float = None,
        play_duration_per_uv: float = None,
        play_per_vv: float = None,
        play_success_vv: float = None,
        video_duration: float = None,
        video_title: str = None,
    ):
        # The number of visits to the audio or video per day.
        self.dau = dau
        # The ID of the media file (VideoId).
        self.media_id = media_id
        # The total playback duration of the audio or video. Unit: seconds.
        self.play_duration = play_duration
        # The average playback duration of the audio or video per viewer. Unit: seconds.
        self.play_duration_per_uv = play_duration_per_uv
        # The average number of times that the audio or video was played per viewer.
        self.play_per_vv = play_per_vv
        # The total number of times the audio or video has been played.
        self.play_success_vv = play_success_vv
        # The duration of the audio or video file. Unit: seconds.
        self.video_duration = video_duration
        # The name of the audio or video file.
        self.video_title = video_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dau is not None:
            result['DAU'] = self.dau

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration

        if self.play_duration_per_uv is not None:
            result['PlayDurationPerUv'] = self.play_duration_per_uv

        if self.play_per_vv is not None:
            result['PlayPerVv'] = self.play_per_vv

        if self.play_success_vv is not None:
            result['PlaySuccessVv'] = self.play_success_vv

        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration

        if self.video_title is not None:
            result['VideoTitle'] = self.video_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DAU') is not None:
            self.dau = m.get('DAU')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')

        if m.get('PlayDurationPerUv') is not None:
            self.play_duration_per_uv = m.get('PlayDurationPerUv')

        if m.get('PlayPerVv') is not None:
            self.play_per_vv = m.get('PlayPerVv')

        if m.get('PlaySuccessVv') is not None:
            self.play_success_vv = m.get('PlaySuccessVv')

        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')

        if m.get('VideoTitle') is not None:
            self.video_title = m.get('VideoTitle')

        return self

