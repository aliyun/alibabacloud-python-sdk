# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveInteractionMetricDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        begin_ts: int = None,
        end_ts: int = None,
        metric_type: str = None,
        os: str = None,
        terminal_type: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.begin_ts = begin_ts
        # The end of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_ts = end_ts
        # The metric. Valid values:
        # 
        # *   JoinChannelSucRate: the success rate of joining a channel within 5 seconds.
        # *   VideoStuckRate: the video stuttering rate.
        # *   AudioStuckRate: the audio stuttering rate.
        # *   FirstFrameCost: the time to first frame.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The operating system. Valid values: iOS and Android.
        self.os = os
        # The terminal type. Valid values: web and mobile.
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

        if self.begin_ts is not None:
            result['BeginTs'] = self.begin_ts

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.os is not None:
            result['Os'] = self.os

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BeginTs') is not None:
            self.begin_ts = m.get('BeginTs')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        return self

