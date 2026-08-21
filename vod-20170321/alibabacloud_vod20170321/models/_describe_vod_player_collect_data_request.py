# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodPlayerCollectDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        metrics: str = None,
        os: str = None,
        period: str = None,
        start_time: str = None,
        terminal_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. Format: yyyy-mm-ddthh:mm:ssz (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity for the query data. Valid values: **5m**, **1h**, and **1d**. The supported time granularity varies based on the time span specified by `StartTime` and `EndTime`:
        # 
        # - Within 3 days: **5m**, **1h**, and **1d**.
        # - 4 to 7 days: **1h** and **1d**.
        # - More than 7 days: **1d**.
        # 
        # This parameter is required.
        self.interval = interval
        # The metric type. You can specify up to 3 metrics.
        # 
        # > 
        # > - Percentage data is returned in decimal format.
        # 
        # Playback quality (QoS) metrics:
        # - Vv: play count.
        # - RealVv: actual play count.
        # - FirstFrame: first frame time.
        # - SecondPlayRate: instant play rate.
        # - SlowPlayRate: slow play rate.
        # - StuckCountRate: stuttering rate by count.
        # - SeekDuration: seek duration.
        # - StuckDuration100s: stuttering duration per 100 seconds.
        # - StuckCount100s: stuttering count per 100 seconds.
        # - PlayFailRate: playback failure rate.
        # - SeedFailRate: non-play rate.
        # - AvgPlayBitrate: average playback bitrate.
        # - AvgStartBitrate: average initial bitrate.
        # - ErrorCount100s: error count per 100 seconds.
        # 
        # Playback experience (QoE) metrics:
        # - Uv: unique viewers.
        # - AvgPerVv: average plays per user.
        # - AvgVideoDuration: average video duration.
        # - AvgPerPlayDuration: average playback duration per user.
        # - AvgPerCompletionVv: average completion count per user.
        # - CompletionVv: completion count.
        # - CompletionRate: completion rate.
        # - AvgPlayDuration: average playback duration.
        # - JumpRate5s: 5-second bounce rate.
        # 
        # This parameter is required.
        self.metrics = metrics
        # The operating system of the playback device. Specify this parameter to perform a filtered query for playback data of a specific operating system. Valid values: **Android**, **iOS**, **Harmony**, **Windows**, **MacOS**, and **Linux**.
        # The available values vary by terminal type:
        # 
        # - **native**: Android, iOS, Harmony.
        # - **web**: Android, iOS, Harmony, Windows, MacOs, Linux.
        # 
        # Separate multiple values with #_#.
        self.os = os
        # The time range for period-over-period analysis, in days (d).
        # 
        # For example, if you set this parameter to 1d (1 day), the period-over-period data is retrieved from the time range of StartTime-1d to EndTime-1d.
        self.period = period
        # The start time of the query. Format: <i>yyyy-mm-dd</i>t<i>hh:mm:ss</i>z (UTC).
        # > 
        # > - Playback data from the last year can be queried.
        # > - The time range for a single query cannot exceed 31 days.
        # > - The time interval is left-closed and right-open [StartTime, EndTime).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The terminal type. Valid values:
        # - **web**: web.
        # - **mobile**: native.
        # 
        # This parameter is required.
        self.terminal_type = terminal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.os is not None:
            result['Os'] = self.os

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        return self

