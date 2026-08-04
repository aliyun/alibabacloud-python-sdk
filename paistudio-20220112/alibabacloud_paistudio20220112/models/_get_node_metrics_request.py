# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNodeMetricsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        gputype: str = None,
        start_time: str = None,
        time_step: str = None,
        verbose: bool = None,
    ):
        # The end time.
        self.end_time = end_time
        # The GPU type. Valid values:
        # - V100
        # - A100
        # - A10
        # - T4
        # - P100
        self.gputype = gputype
        # The start time.
        self.start_time = start_time
        # The time step. Default value: 5m. The supported time units are:
        # 
        # - h: hours.
        # 
        # - m: minutes.
        # 
        # - s: seconds.
        # 
        # If the value does not contain a unit, the default unit is s (seconds).
        self.time_step = time_step
        # Specifies whether to display non-essential information. Non-essential information currently includes Labels.
        # Valid values:
        # 
        # false: does not display non-essential information (default value)
        # true: displays non-essential information
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_step is not None:
            result['TimeStep'] = self.time_step

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

