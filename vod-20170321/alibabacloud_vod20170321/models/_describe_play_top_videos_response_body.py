# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribePlayTopVideosResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        top_play_videos: main_models.DescribePlayTopVideosResponseBodyTopPlayVideos = None,
        total_num: int = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.top_play_videos = top_play_videos
        # The total number of entries that were collected in playback statistics on top videos.
        self.total_num = total_num

    def validate(self):
        if self.top_play_videos:
            self.top_play_videos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.top_play_videos is not None:
            result['TopPlayVideos'] = self.top_play_videos.to_map()

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TopPlayVideos') is not None:
            temp_model = main_models.DescribePlayTopVideosResponseBodyTopPlayVideos()
            self.top_play_videos = temp_model.from_map(m.get('TopPlayVideos'))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class DescribePlayTopVideosResponseBodyTopPlayVideos(DaraModel):
    def __init__(
        self,
        top_play_video_statis: List[main_models.DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis] = None,
    ):
        self.top_play_video_statis = top_play_video_statis

    def validate(self):
        if self.top_play_video_statis:
            for v1 in self.top_play_video_statis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopPlayVideoStatis'] = []
        if self.top_play_video_statis is not None:
            for k1 in self.top_play_video_statis:
                result['TopPlayVideoStatis'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_play_video_statis = []
        if m.get('TopPlayVideoStatis') is not None:
            for k1 in m.get('TopPlayVideoStatis'):
                temp_model = main_models.DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis()
                self.top_play_video_statis.append(temp_model.from_map(k1))

        return self

class DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis(DaraModel):
    def __init__(
        self,
        play_duration: str = None,
        title: str = None,
        uv: str = None,
        vv: str = None,
        video_id: str = None,
    ):
        self.play_duration = play_duration
        self.title = title
        self.uv = uv
        self.vv = vv
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration

        if self.title is not None:
            result['Title'] = self.title

        if self.uv is not None:
            result['UV'] = self.uv

        if self.vv is not None:
            result['VV'] = self.vv

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UV') is not None:
            self.uv = m.get('UV')

        if m.get('VV') is not None:
            self.vv = m.get('VV')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

