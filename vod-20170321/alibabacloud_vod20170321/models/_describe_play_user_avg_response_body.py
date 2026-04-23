# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribePlayUserAvgResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_play_statis_avgs: main_models.DescribePlayUserAvgResponseBodyUserPlayStatisAvgs = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.user_play_statis_avgs = user_play_statis_avgs

    def validate(self):
        if self.user_play_statis_avgs:
            self.user_play_statis_avgs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_play_statis_avgs is not None:
            result['UserPlayStatisAvgs'] = self.user_play_statis_avgs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserPlayStatisAvgs') is not None:
            temp_model = main_models.DescribePlayUserAvgResponseBodyUserPlayStatisAvgs()
            self.user_play_statis_avgs = temp_model.from_map(m.get('UserPlayStatisAvgs'))

        return self

class DescribePlayUserAvgResponseBodyUserPlayStatisAvgs(DaraModel):
    def __init__(
        self,
        user_play_statis_avg: List[main_models.DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg] = None,
    ):
        self.user_play_statis_avg = user_play_statis_avg

    def validate(self):
        if self.user_play_statis_avg:
            for v1 in self.user_play_statis_avg:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserPlayStatisAvg'] = []
        if self.user_play_statis_avg is not None:
            for k1 in self.user_play_statis_avg:
                result['UserPlayStatisAvg'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_play_statis_avg = []
        if m.get('UserPlayStatisAvg') is not None:
            for k1 in m.get('UserPlayStatisAvg'):
                temp_model = main_models.DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg()
                self.user_play_statis_avg.append(temp_model.from_map(k1))

        return self

class DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg(DaraModel):
    def __init__(
        self,
        avg_play_count: str = None,
        avg_play_duration: str = None,
        date: str = None,
    ):
        self.avg_play_count = avg_play_count
        self.avg_play_duration = avg_play_duration
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_play_count is not None:
            result['AvgPlayCount'] = self.avg_play_count

        if self.avg_play_duration is not None:
            result['AvgPlayDuration'] = self.avg_play_duration

        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgPlayCount') is not None:
            self.avg_play_count = m.get('AvgPlayCount')

        if m.get('AvgPlayDuration') is not None:
            self.avg_play_duration = m.get('AvgPlayDuration')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

