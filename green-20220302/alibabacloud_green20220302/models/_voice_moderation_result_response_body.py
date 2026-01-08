# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class VoiceModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.VoiceModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.VoiceModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VoiceModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        live_id: str = None,
        manual_task_id: str = None,
        risk_level: str = None,
        slice_details: List[main_models.VoiceModerationResultResponseBodyDataSliceDetails] = None,
        task_id: str = None,
        url: str = None,
    ):
        # The ID of the moderated object.
        self.data_id = data_id
        # The unique ID of the live stream.
        self.live_id = live_id
        self.manual_task_id = manual_task_id
        # Risk Level.
        self.risk_level = risk_level
        # The moderation results of audio segments.
        self.slice_details = slice_details
        # The task ID.
        self.task_id = task_id
        # The URL of the moderated content.
        self.url = url

    def validate(self):
        if self.slice_details:
            for v1 in self.slice_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k1 in self.slice_details:
                result['SliceDetails'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k1 in m.get('SliceDetails'):
                temp_model = main_models.VoiceModerationResultResponseBodyDataSliceDetails()
                self.slice_details.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class VoiceModerationResultResponseBodyDataSliceDetails(DaraModel):
    def __init__(
        self,
        descriptions: str = None,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        origin_algo_result: Dict[str, Any] = None,
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        # The description of the labels.
        self.descriptions = descriptions
        # The end time of the audio segment in seconds.
        self.end_time = end_time
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp
        # Extended fields.
        self.extend = extend
        # The details of the labels.
        self.labels = labels
        # Reserved parameter.
        self.origin_algo_result = origin_algo_result
        # Risk Level.
        self.risk_level = risk_level
        # The details of the risky content.
        self.risk_tips = risk_tips
        # The term hit by the risky content.
        self.risk_words = risk_words
        # The risk score. Default range: 0 to 99.
        self.score = score
        # The start time of the audio segment in seconds.
        self.start_time = start_time
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp
        # The text converted from the audio segment.
        self.text = text
        # The temporary URL of the audio segment.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descriptions is not None:
            result['Descriptions'] = self.descriptions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.origin_algo_result is not None:
            result['OriginAlgoResult'] = self.origin_algo_result

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips

        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words

        if self.score is not None:
            result['Score'] = self.score

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.text is not None:
            result['Text'] = self.text

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Descriptions') is not None:
            self.descriptions = m.get('Descriptions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('OriginAlgoResult') is not None:
            self.origin_algo_result = m.get('OriginAlgoResult')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')

        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

