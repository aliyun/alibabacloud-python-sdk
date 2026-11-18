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
        # The end time of the query. Format: yyyy-mm-ddThh:mm:ssZ (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metric dimension filter. A dimension consists of a dimension type (Field), an operator (Op), and a dimension value.
        # 
        # > - You can specify up to three dimensions.
        # > - If the Metrics parameter includes any of the following four metrics, the Filters parameter does not take effect: Uv (number of playback users), AvgPerVv (average number of playbacks per user), AvgPerPlayDuration (average playback duration per user), and AvgPerCompletionVv (average number of completions per user).
        # > - Use regionCode to specify provinces and countries.
        # > - Separate multiple values with #_#.
        # 
        # Valid values for the dimension type (Field):
        # - SdkVersion: the SDK version.
        # - AppVersion: the app version.
        # - Codec: the codec.
        # - VideoType: the video format.
        # - Network: the network type.
        # - Country: the country.
        # - Isp: the ISP.
        # - VideoDefinition: the resolution.
        # - Domain: the domain name.
        # - Province: the province.
        # - IsHw: whether hardware decoding is used.
        # - ErrorCode: the error code.
        # 
        # Valid values for the operator (Op): = (equal to), > (greater than), < (less than), and != (not equal to).
        # > 
        # > - Operator availability: The SdkVersion and VideoDefinition metrics support all four operators. Other metrics support only = (equal to) and != (not equal to).
        # 
        # To obtain dimension values, call the DescribeVodPlayerDimensionData operation.
        self.filters = filters
        # The time granularity of the queried data. Valid values: **5m**, **1h**, and **1d**. The supported time granularity varies based on the time span specified by `StartTime` and `EndTime`:
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
        # The metric types. You can select multiple metrics, up to a maximum of three.
        # 
        # > 
        # > - Percentage data is returned in decimal format.
        # 
        # Quality of Service (QoS) metrics for playback:
        # - Vv: the number of playbacks.
        # - RealVv: the actual playback volume.
        # - FirstFrame: the first frame loading time.
        # - SecondPlayRate: the 1-second startup rate.
        # - SlowPlayRate: the slow startup rate.
        # - StuckCountRate: the stuttering rate by count.
        # - SeekDuration: the seek duration.
        # - StuckDuration100s: the stuttering duration per 100 seconds.
        # - StuckCount100s: the number of stuttering events per 100 seconds.
        # - PlayFailRate: the playback failure rate.
        # - SeedFailRate: the non-startup rate.
        # - AvgPlayBitrate: the average playback bitrate.
        # - AvgStartBitrate: the average startup bitrate.
        # - ErrorCount100s: the number of errors per 100 seconds.
        # 
        # Quality of Experience (QoE) metrics for playback:
        # - Uv: the number of playback users.
        # - AvgPerVv: the average number of playbacks per user.
        # - AvgVideoDuration: the average video duration.
        # - AvgPerPlayDuration: the average playback duration per user.
        # - AvgPerCompletionVv: the average number of completions per user.
        # - CompletionVv: the completion volume.
        # - CompletionRate: the completion rate.
        # - AvgPlayDuration: the average playback duration.
        # - JumpRate5s: the 5-second bounce rate.
        # 
        # This parameter is required.
        self.metrics = metrics
        # The operating system of the playback client. You can specify this parameter to perform a filtered query for playback data of a specific operating system. Valid values: **Android**, **iOS**, **Harmony**, **Windows**, **macOS**, and **Linux**.
        # The available values vary based on the terminal type:
        # 
        # - **native**: Android, iOS, and Harmony.
        # - **web**: Android, iOS, Harmony, Windows, macOS, and Linux.
        # 
        # Separate multiple operating systems with #_#.
        self.os = os
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **5000**. Maximum value: **5000**.
        self.page_size = page_size
        # The start time of the query. Format: <i>yyyy-mm-dd</i>T<i>hh:mm:ss</i>Z (UTC).
        # > 
        # > - You can query playback data history for up to one year.
        # > - The time range for a single query cannot exceed 31 days.
        # > - The time interval is left-closed and right-open [StartTime, EndTime).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The terminal type. Valid values:
        # - **web**: the web client.
        # - **mobile**: the native client.
        # 
        # This parameter is required.
        self.terminal_type = terminal_type
        # The number of top data entries by playback volume to return. If you do not specify this parameter, all dimension data is returned.
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

