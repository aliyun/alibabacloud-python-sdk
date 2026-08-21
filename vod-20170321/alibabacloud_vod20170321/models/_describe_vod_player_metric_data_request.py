# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodPlayerMetricDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        filters: str = None,
        interval: str = None,
        language: str = None,
        metrics: str = None,
        os: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        terminal_type: str = None,
        top: int = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. Format: yyyy-mm-ddthh:mm:ssz (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metric dimension filters. A dimension consists of a dimension type (Field), an operator (Op), and a dimension value.
        # 
        # > - A maximum of three dimensions can be specified.
        # > - When the Metrics parameter includes the following four metrics, Filters do not take effect: Uv (playback users), AvgPerVv (average plays per user), AvgPerPlayDuration (average play duration per user), and AvgPerCompletionVv (average completion plays per user).
        # > - For provinces and countries, pass the regionCode.
        # > - Separate multiple values with #_#.
        # 
        # Valid values for dimension type (Field):
        # - SdkVersion: SDK version.
        # - AppVersion: app version.
        # - Codec: codec.
        # - VideoType: video format.
        # - Network: network type.
        # - Country: country.
        # - Isp: ISP.
        # - VideoDefinition: resolution.
        # - Domain: domain name.
        # - Province: province.
        # - IsHw: whether hardware decoding is used.
        # - ErrorCode: error code.
        # 
        # Valid values for operator (Op): = (equal to), > (greater than), < (less than), and != (not equal to).
        # > 
        # > - SdkVersion and VideoDefinition support all four operators. Other metrics support only = (equal to) and != (not equal to).
        # 
        # Retrieve dimension values by calling DescribeVodPlayerDimensionData.
        self.filters = filters
        # The time granularity for querying data. Valid values: **5m**, **1h**, and **1d**. The supported time granularity depends on the time span between `StartTime` and `EndTime`:
        # 
        # - Within 3 days: **5m**, **1h**, and **1d**.
        # - 4 to 7 days: **1h** and **1d**.
        # - More than 7 days: **1d**.
        # 
        # This parameter is required.
        self.interval = interval
        # The language of the response. Valid values:
        # 
        # - **zh** (**default**): Simplified Chinese.
        # 
        # - **en**: English.
        self.language = language
        # The metric types. You can select multiple metrics (up to 3).
        # 
        # > 
        # > - Percentage data is returned in decimal form.
        # 
        # Quality of Service (QoS) metrics:
        # - Vv: play count.
        # - RealVv: actual play count.
        # - FirstFrame: first frame time.
        # - SecondPlayRate: instant play rate.
        # - SlowPlayRate: slow play rate.
        # - StuckCountRate: stuttering rate by count.
        # - SeekDuration: seek duration.
        # - StuckDuration100s: stuttering duration per 100 seconds.
        # - StuckCount100s: stuttering count per 100 seconds.
        # - PlayFailRate: play failure rate.
        # - SeedFailRate: non-play rate.
        # - AvgPlayBitrate: average playback bitrate.
        # - AvgStartBitrate: average start bitrate.
        # - ErrorCount100s: error count per 100 seconds.
        # 
        # Quality of Experience (QoE) metrics:
        # - Uv: playback users.
        # - AvgPerVv: average plays per user.
        # - AvgVideoDuration: average video duration.
        # - AvgPerPlayDuration: average play duration per user.
        # - AvgPerCompletionVv: average completion plays per user.
        # - CompletionVv: completion count.
        # - CompletionRate: completion rate.
        # - AvgPlayDuration: average play duration.
        # - JumpRate5s: 5-second bounce rate.
        # 
        # This parameter is required.
        self.metrics = metrics
        # The operating system of the player. Specify this parameter to perform a filtered query for playback data of a specific operating system. Valid values: **Android**, **iOS**, **Harmony**, **Windows**, **MacOS**, and **Linux**.
        # The available values vary by terminal type:
        # 
        # - **native**: Android, iOS, Harmony.
        # - **web**: Android, iOS, Harmony, Windows, MacOs, Linux.
        # 
        # Separate multiple values with #_#.
        self.os = os
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **5000**. Maximum value: **5000**.
        self.page_size = page_size
        # The start time of the query. Format: <i>yyyy-mm-dd</i>t<i>hh:mm:ss</i>z (UTC).
        # > 
        # > - Supports querying playback data history for the past year.
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
        # Returns data for the top N items ranked by play count. If this parameter is not specified, data for all dimensions is returned.
        self.top = top

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

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.language is not None:
            result['Language'] = self.language

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.os is not None:
            result['Os'] = self.os

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

