# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomAgentMonitorMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCustomAgentMonitorMetricsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the call fails.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCustomAgentMonitorMetricsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomAgentMonitorMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        active_user_count: int = None,
        custom_agent_id: str = None,
        dislike_count: int = None,
        end_time: int = None,
        granularity: str = None,
        like_count: int = None,
        session_count: int = None,
        start_time: int = None,
        trend: List[main_models.DescribeCustomAgentMonitorMetricsResponseBodyDataTrend] = None,
    ):
        # The number of active users.
        self.active_user_count = active_user_count
        # The custom agent ID.
        self.custom_agent_id = custom_agent_id
        # The total number of dislikes.
        self.dislike_count = dislike_count
        # The end time of the statistical period (epoch millis).
        self.end_time = end_time
        # The aggregation granularity: DAY / HOUR.
        self.granularity = granularity
        # The total number of likes.
        self.like_count = like_count
        # The total number of sessions.
        self.session_count = session_count
        # The start time of the statistical period (epoch millis).
        self.start_time = start_time
        # The trend data aggregated by the specified granularity. Time points without data are filled with 0. The data is sorted in chronological order.
        self.trend = trend

    def validate(self):
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_user_count is not None:
            result['ActiveUserCount'] = self.active_user_count

        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.dislike_count is not None:
            result['DislikeCount'] = self.dislike_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.like_count is not None:
            result['LikeCount'] = self.like_count

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['Trend'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCount') is not None:
            self.active_user_count = m.get('ActiveUserCount')

        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('DislikeCount') is not None:
            self.dislike_count = m.get('DislikeCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.trend = []
        if m.get('Trend') is not None:
            for k1 in m.get('Trend'):
                temp_model = main_models.DescribeCustomAgentMonitorMetricsResponseBodyDataTrend()
                self.trend.append(temp_model.from_map(k1))

        return self

class DescribeCustomAgentMonitorMetricsResponseBodyDataTrend(DaraModel):
    def __init__(
        self,
        active_user_count: int = None,
        dislike_count: int = None,
        like_count: int = None,
        session_count: int = None,
        stat_time: str = None,
        timestamp: int = None,
    ):
        # The number of active users within the statistical period.
        self.active_user_count = active_user_count
        # The number of dislikes within the statistical period.
        self.dislike_count = dislike_count
        # The number of likes within the statistical period.
        self.like_count = like_count
        # The number of sessions within the statistical period.
        self.session_count = session_count
        # The statistical time. For daily granularity, the format is 2026-09-01. For hourly granularity, the format is 2026-09-01 13:00.
        self.stat_time = stat_time
        # The start timestamp of the statistical period (epoch millis).
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_user_count is not None:
            result['ActiveUserCount'] = self.active_user_count

        if self.dislike_count is not None:
            result['DislikeCount'] = self.dislike_count

        if self.like_count is not None:
            result['LikeCount'] = self.like_count

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.stat_time is not None:
            result['StatTime'] = self.stat_time

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveUserCount') is not None:
            self.active_user_count = m.get('ActiveUserCount')

        if m.get('DislikeCount') is not None:
            self.dislike_count = m.get('DislikeCount')

        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('StatTime') is not None:
            self.stat_time = m.get('StatTime')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

