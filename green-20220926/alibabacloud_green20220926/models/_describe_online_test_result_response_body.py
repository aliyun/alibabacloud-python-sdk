# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class DescribeOnlineTestResultResponseBody(DaraModel):
    def __init__(
        self,
        audio_data: main_models.DescribeOnlineTestResultResponseBodyAudioData = None,
        frame_data: main_models.DescribeOnlineTestResultResponseBodyFrameData = None,
        moderation_time: str = None,
        request_id: str = None,
        risk_level: str = None,
        service_code: str = None,
        summary_list: List[main_models.DescribeOnlineTestResultResponseBodySummaryList] = None,
        task_id: str = None,
        task_status: str = None,
        url: str = None,
    ):
        self.audio_data = audio_data
        self.frame_data = frame_data
        self.moderation_time = moderation_time
        self.request_id = request_id
        self.risk_level = risk_level
        self.service_code = service_code
        self.summary_list = summary_list
        self.task_id = task_id
        self.task_status = task_status
        self.url = url

    def validate(self):
        if self.audio_data:
            self.audio_data.validate()
        if self.frame_data:
            self.frame_data.validate()
        if self.summary_list:
            for v1 in self.summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_data is not None:
            result['AudioData'] = self.audio_data.to_map()

        if self.frame_data is not None:
            result['FrameData'] = self.frame_data.to_map()

        if self.moderation_time is not None:
            result['ModerationTime'] = self.moderation_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        result['SummaryList'] = []
        if self.summary_list is not None:
            for k1 in self.summary_list:
                result['SummaryList'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioData') is not None:
            temp_model = main_models.DescribeOnlineTestResultResponseBodyAudioData()
            self.audio_data = temp_model.from_map(m.get('AudioData'))

        if m.get('FrameData') is not None:
            temp_model = main_models.DescribeOnlineTestResultResponseBodyFrameData()
            self.frame_data = temp_model.from_map(m.get('FrameData'))

        if m.get('ModerationTime') is not None:
            self.moderation_time = m.get('ModerationTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        self.summary_list = []
        if m.get('SummaryList') is not None:
            for k1 in m.get('SummaryList'):
                temp_model = main_models.DescribeOnlineTestResultResponseBodySummaryList()
                self.summary_list.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeOnlineTestResultResponseBodySummaryList(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        risk_level: str = None,
        risk_level_summary: Dict[str, int] = None,
        slice_count: int = None,
    ):
        self.resource_type = resource_type
        self.risk_level = risk_level
        self.risk_level_summary = risk_level_summary
        self.slice_count = slice_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_level_summary is not None:
            result['RiskLevelSummary'] = self.risk_level_summary

        if self.slice_count is not None:
            result['SliceCount'] = self.slice_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskLevelSummary') is not None:
            self.risk_level_summary = m.get('RiskLevelSummary')

        if m.get('SliceCount') is not None:
            self.slice_count = m.get('SliceCount')

        return self

class DescribeOnlineTestResultResponseBodyFrameData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        url: str = None,
    ):
        self.time_stamp = time_stamp
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeOnlineTestResultResponseBodyAudioData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
    ):
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

