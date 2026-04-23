# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribePlayVideoStatisResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        video_play_statis_details: main_models.DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.video_play_statis_details = video_play_statis_details

    def validate(self):
        if self.video_play_statis_details:
            self.video_play_statis_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_play_statis_details is not None:
            result['VideoPlayStatisDetails'] = self.video_play_statis_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoPlayStatisDetails') is not None:
            temp_model = main_models.DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails()
            self.video_play_statis_details = temp_model.from_map(m.get('VideoPlayStatisDetails'))

        return self

class DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails(DaraModel):
    def __init__(
        self,
        video_play_statis_detail: List[main_models.DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail] = None,
    ):
        self.video_play_statis_detail = video_play_statis_detail

    def validate(self):
        if self.video_play_statis_detail:
            for v1 in self.video_play_statis_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoPlayStatisDetail'] = []
        if self.video_play_statis_detail is not None:
            for k1 in self.video_play_statis_detail:
                result['VideoPlayStatisDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_play_statis_detail = []
        if m.get('VideoPlayStatisDetail') is not None:
            for k1 in m.get('VideoPlayStatisDetail'):
                temp_model = main_models.DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail()
                self.video_play_statis_detail.append(temp_model.from_map(k1))

        return self

class DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail(DaraModel):
    def __init__(
        self,
        date: str = None,
        play_duration: str = None,
        play_range: str = None,
        title: str = None,
        uv: str = None,
        vv: str = None,
    ):
        self.date = date
        self.play_duration = play_duration
        self.play_range = play_range
        self.title = title
        self.uv = uv
        self.vv = vv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration

        if self.play_range is not None:
            result['PlayRange'] = self.play_range

        if self.title is not None:
            result['Title'] = self.title

        if self.uv is not None:
            result['UV'] = self.uv

        if self.vv is not None:
            result['VV'] = self.vv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')

        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UV') is not None:
            self.uv = m.get('UV')

        if m.get('VV') is not None:
            self.vv = m.get('VV')

        return self

