# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchCreateQualityProjectsRequest(DaraModel):
    def __init__(
        self,
        analysis_ids: List[int] = None,
        channel_touch_type: List[int] = None,
        check_freq_type: int = None,
        instance_list: List[str] = None,
        project_name: str = None,
        time_range_end: str = None,
        time_range_start: str = None,
    ):
        # This parameter is required.
        self.analysis_ids = analysis_ids
        self.channel_touch_type = channel_touch_type
        # This parameter is required.
        self.check_freq_type = check_freq_type
        # This parameter is required.
        self.instance_list = instance_list
        # This parameter is required.
        self.project_name = project_name
        self.time_range_end = time_range_end
        self.time_range_start = time_range_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids

        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type

        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end

        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')

        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')

        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')

        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')

        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')

        return self

