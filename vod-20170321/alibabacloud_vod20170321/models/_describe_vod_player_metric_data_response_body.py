# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodPlayerMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVodPlayerMetricDataResponseBodyDataList] = None,
        extend: main_models.DescribeVodPlayerMetricDataResponseBodyExtend = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.data_list = data_list
        self.extend = extend
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.extend:
            self.extend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.extend is not None:
            result['Extend'] = self.extend.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVodPlayerMetricDataResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('Extend') is not None:
            temp_model = main_models.DescribeVodPlayerMetricDataResponseBodyExtend()
            self.extend = temp_model.from_map(m.get('Extend'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeVodPlayerMetricDataResponseBodyExtend(DaraModel):
    def __init__(
        self,
        actual_end_time: str = None,
        actual_start_time: str = None,
        interval_seconds: int = None,
    ):
        self.actual_end_time = actual_end_time
        self.actual_start_time = actual_start_time
        self.interval_seconds = interval_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_end_time is not None:
            result['ActualEndTime'] = self.actual_end_time

        if self.actual_start_time is not None:
            result['ActualStartTime'] = self.actual_start_time

        if self.interval_seconds is not None:
            result['IntervalSeconds'] = self.interval_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualEndTime') is not None:
            self.actual_end_time = m.get('ActualEndTime')

        if m.get('ActualStartTime') is not None:
            self.actual_start_time = m.get('ActualStartTime')

        if m.get('IntervalSeconds') is not None:
            self.interval_seconds = m.get('IntervalSeconds')

        return self

class DescribeVodPlayerMetricDataResponseBodyDataList(DaraModel):
    def __init__(
        self,
        avg_per_completion_vv: float = None,
        avg_per_play_duration: float = None,
        avg_per_vv: float = None,
        avg_play_bitrate: float = None,
        avg_play_duration: float = None,
        avg_start_bitrate: float = None,
        avg_video_duration: float = None,
        completion_rate: float = None,
        completion_vv: float = None,
        dimension: str = None,
        error_count_100s: float = None,
        first_frame: float = None,
        jump_rate_5s: float = None,
        play_fail_rate: float = None,
        real_vv: float = None,
        second_play_rate: float = None,
        seed_fail_rate: float = None,
        seek_duration: float = None,
        slow_play_rate: float = None,
        stuck_count_100s: str = None,
        stuck_count_rate: float = None,
        stuck_duration_100s: float = None,
        time_stamp: str = None,
        total_play_duration: float = None,
        uv: float = None,
        vv: float = None,
    ):
        self.avg_per_completion_vv = avg_per_completion_vv
        self.avg_per_play_duration = avg_per_play_duration
        self.avg_per_vv = avg_per_vv
        self.avg_play_bitrate = avg_play_bitrate
        self.avg_play_duration = avg_play_duration
        self.avg_start_bitrate = avg_start_bitrate
        self.avg_video_duration = avg_video_duration
        self.completion_rate = completion_rate
        self.completion_vv = completion_vv
        self.dimension = dimension
        self.error_count_100s = error_count_100s
        self.first_frame = first_frame
        self.jump_rate_5s = jump_rate_5s
        self.play_fail_rate = play_fail_rate
        self.real_vv = real_vv
        self.second_play_rate = second_play_rate
        self.seed_fail_rate = seed_fail_rate
        self.seek_duration = seek_duration
        self.slow_play_rate = slow_play_rate
        self.stuck_count_100s = stuck_count_100s
        self.stuck_count_rate = stuck_count_rate
        self.stuck_duration_100s = stuck_duration_100s
        self.time_stamp = time_stamp
        self.total_play_duration = total_play_duration
        self.uv = uv
        self.vv = vv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_per_completion_vv is not None:
            result['AvgPerCompletionVv'] = self.avg_per_completion_vv

        if self.avg_per_play_duration is not None:
            result['AvgPerPlayDuration'] = self.avg_per_play_duration

        if self.avg_per_vv is not None:
            result['AvgPerVv'] = self.avg_per_vv

        if self.avg_play_bitrate is not None:
            result['AvgPlayBitrate'] = self.avg_play_bitrate

        if self.avg_play_duration is not None:
            result['AvgPlayDuration'] = self.avg_play_duration

        if self.avg_start_bitrate is not None:
            result['AvgStartBitrate'] = self.avg_start_bitrate

        if self.avg_video_duration is not None:
            result['AvgVideoDuration'] = self.avg_video_duration

        if self.completion_rate is not None:
            result['CompletionRate'] = self.completion_rate

        if self.completion_vv is not None:
            result['CompletionVv'] = self.completion_vv

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.error_count_100s is not None:
            result['ErrorCount100s'] = self.error_count_100s

        if self.first_frame is not None:
            result['FirstFrame'] = self.first_frame

        if self.jump_rate_5s is not None:
            result['JumpRate5s'] = self.jump_rate_5s

        if self.play_fail_rate is not None:
            result['PlayFailRate'] = self.play_fail_rate

        if self.real_vv is not None:
            result['RealVv'] = self.real_vv

        if self.second_play_rate is not None:
            result['SecondPlayRate'] = self.second_play_rate

        if self.seed_fail_rate is not None:
            result['SeedFailRate'] = self.seed_fail_rate

        if self.seek_duration is not None:
            result['SeekDuration'] = self.seek_duration

        if self.slow_play_rate is not None:
            result['SlowPlayRate'] = self.slow_play_rate

        if self.stuck_count_100s is not None:
            result['StuckCount100s'] = self.stuck_count_100s

        if self.stuck_count_rate is not None:
            result['StuckCountRate'] = self.stuck_count_rate

        if self.stuck_duration_100s is not None:
            result['StuckDuration100s'] = self.stuck_duration_100s

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_play_duration is not None:
            result['TotalPlayDuration'] = self.total_play_duration

        if self.uv is not None:
            result['Uv'] = self.uv

        if self.vv is not None:
            result['Vv'] = self.vv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgPerCompletionVv') is not None:
            self.avg_per_completion_vv = m.get('AvgPerCompletionVv')

        if m.get('AvgPerPlayDuration') is not None:
            self.avg_per_play_duration = m.get('AvgPerPlayDuration')

        if m.get('AvgPerVv') is not None:
            self.avg_per_vv = m.get('AvgPerVv')

        if m.get('AvgPlayBitrate') is not None:
            self.avg_play_bitrate = m.get('AvgPlayBitrate')

        if m.get('AvgPlayDuration') is not None:
            self.avg_play_duration = m.get('AvgPlayDuration')

        if m.get('AvgStartBitrate') is not None:
            self.avg_start_bitrate = m.get('AvgStartBitrate')

        if m.get('AvgVideoDuration') is not None:
            self.avg_video_duration = m.get('AvgVideoDuration')

        if m.get('CompletionRate') is not None:
            self.completion_rate = m.get('CompletionRate')

        if m.get('CompletionVv') is not None:
            self.completion_vv = m.get('CompletionVv')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('ErrorCount100s') is not None:
            self.error_count_100s = m.get('ErrorCount100s')

        if m.get('FirstFrame') is not None:
            self.first_frame = m.get('FirstFrame')

        if m.get('JumpRate5s') is not None:
            self.jump_rate_5s = m.get('JumpRate5s')

        if m.get('PlayFailRate') is not None:
            self.play_fail_rate = m.get('PlayFailRate')

        if m.get('RealVv') is not None:
            self.real_vv = m.get('RealVv')

        if m.get('SecondPlayRate') is not None:
            self.second_play_rate = m.get('SecondPlayRate')

        if m.get('SeedFailRate') is not None:
            self.seed_fail_rate = m.get('SeedFailRate')

        if m.get('SeekDuration') is not None:
            self.seek_duration = m.get('SeekDuration')

        if m.get('SlowPlayRate') is not None:
            self.slow_play_rate = m.get('SlowPlayRate')

        if m.get('StuckCount100s') is not None:
            self.stuck_count_100s = m.get('StuckCount100s')

        if m.get('StuckCountRate') is not None:
            self.stuck_count_rate = m.get('StuckCountRate')

        if m.get('StuckDuration100s') is not None:
            self.stuck_duration_100s = m.get('StuckDuration100s')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalPlayDuration') is not None:
            self.total_play_duration = m.get('TotalPlayDuration')

        if m.get('Uv') is not None:
            self.uv = m.get('Uv')

        if m.get('Vv') is not None:
            self.vv = m.get('Vv')

        return self

