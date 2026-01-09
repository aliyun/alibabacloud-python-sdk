# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EditQualityProjectRequest(DaraModel):
    def __init__(
        self,
        analysis_ids: List[int] = None,
        channel_touch_type: List[int] = None,
        check_freq_type: int = None,
        dep_list: List[int] = None,
        group_list: List[int] = None,
        instance_id: str = None,
        project_id: int = None,
        project_name: str = None,
        project_version: int = None,
        scope_type: int = None,
        servicer_list: List[str] = None,
        time_range_end: str = None,
        time_range_start: str = None,
    ):
        # This parameter is required.
        self.analysis_ids = analysis_ids
        # This parameter is required.
        self.channel_touch_type = channel_touch_type
        # This parameter is required.
        self.check_freq_type = check_freq_type
        self.dep_list = dep_list
        self.group_list = group_list
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.project_version = project_version
        # This parameter is required.
        self.scope_type = scope_type
        self.servicer_list = servicer_list
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

        if self.dep_list is not None:
            result['DepList'] = self.dep_list

        if self.group_list is not None:
            result['GroupList'] = self.group_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list

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

        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')

        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')

        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')

        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')

        return self

