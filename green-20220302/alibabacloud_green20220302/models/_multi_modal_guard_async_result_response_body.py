# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class MultiModalGuardAsyncResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.MultiModalGuardAsyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code of the response.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.MultiModalGuardAsyncResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MultiModalGuardAsyncResultResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_result: main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResult = None,
        data_id: str = None,
        frame_result: main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResult = None,
        live_id: str = None,
        suggestion: str = None,
        task_id: str = None,
    ):
        # The audio moderation result.
        self.audio_result = audio_result
        # The value of the `dataId` parameter from the request. This field is omitted if `dataId` was not provided.
        self.data_id = data_id
        # The video frame moderation result.
        self.frame_result = frame_result
        # The unique identifier for the live stream.
        self.live_id = live_id
        # The recommended action. Valid values:
        # 
        # - `block`: Block the content.
        # 
        # - `pass`: Pass the content.
        # 
        # - `watch`: The content requires review.
        # 
        # - `mask`: Mask the content.
        self.suggestion = suggestion
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_result is not None:
            result['AudioResult'] = self.audio_result.to_map()

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.frame_result is not None:
            result['FrameResult'] = self.frame_result.to_map()

        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioResult') is not None:
            temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResult()
            self.audio_result = temp_model.from_map(m.get('AudioResult'))

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('FrameResult') is not None:
            temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResult()
            self.frame_result = temp_model.from_map(m.get('FrameResult'))

        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class MultiModalGuardAsyncResultResponseBodyDataFrameResult(DaraModel):
    def __init__(
        self,
        frames: List[main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFrames] = None,
        slice_num: int = None,
        suggestion: str = None,
    ):
        # The moderation results for video frames.
        self.frames = frames
        # The frame count.
        self.slice_num = slice_num
        # The recommended action. Valid values:
        # 
        # - `block`: Block the content.
        # 
        # - `pass`: Pass the content.
        # 
        # - `watch`: The content requires review.
        # 
        # - `mask`: Mask the content.
        self.suggestion = suggestion

    def validate(self):
        if self.frames:
            for v1 in self.frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Frames'] = []
        if self.frames is not None:
            for k1 in self.frames:
                result['Frames'].append(k1.to_map() if k1 else None)

        if self.slice_num is not None:
            result['SliceNum'] = self.slice_num

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k1 in m.get('Frames'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFrames()
                self.frames.append(temp_model.from_map(k1))

        if m.get('SliceNum') is not None:
            self.slice_num = m.get('SliceNum')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class MultiModalGuardAsyncResultResponseBodyDataFrameResultFrames(DaraModel):
    def __init__(
        self,
        detail: List[main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetail] = None,
        offset: float = None,
        suggestion: str = None,
        timestamp: int = None,
        url: str = None,
    ):
        # A list of detection results.
        self.detail = detail
        # The time offset of the frame in the video, in seconds.
        self.offset = offset
        # The recommended action. Valid values:
        # 
        # - `block`: Block the content.
        # 
        # - `pass`: Pass the content.
        # 
        # - `watch`: The content requires review.
        # 
        # - `mask`: Mask the content.
        self.suggestion = suggestion
        # The absolute timestamp of the frame, in milliseconds.
        self.timestamp = timestamp
        # The temporary URL of the video frame.
        self.url = url

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetail(DaraModel):
    def __init__(
        self,
        level: str = None,
        result: List[main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetailResult] = None,
        suggestion: str = None,
        type: str = None,
    ):
        # The risk level. Valid values include:
        # 
        # - high: High risk. If a match is found in a custom dictionary, the risk level defaults to high.
        # 
        # - medium: Medium risk.
        # 
        # - low: Low risk.
        # 
        # - none: No risk detected.
        self.level = level
        # A list of detection results.
        self.result = result
        # Suggestion
        # 
        # - block: A suggestion to block.
        # 
        # - pass: A suggestion to pass.
        # 
        # - watch: A suggestion to watch.
        # 
        # - mask: A suggestion to mask.
        self.suggestion = suggestion
        # The detection type. Valid values:
        # 
        # - `contentModeration`: Content moderation.
        # 
        # - `promptAttack`: Prompt attack detection.
        # 
        # - `sensitiveData`: Sensitive data detection.
        # 
        # - `modelHallucination`: Model hallucination.
        # 
        # - `maliciousFile`: Malicious file detection.
        self.type = type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetailResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MultiModalGuardAsyncResultResponseBodyDataFrameResultFramesDetailResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        ext: Any = None,
        label: str = None,
        level: str = None,
    ):
        # The confidence score, ranging from 0 to 100, accurate to two decimal places.
        self.confidence = confidence
        # The description of the label.
        self.description = description
        # Additional information about the detection result.
        self.ext = ext
        # The label of the detection result.
        self.label = label
        # The risk level. Valid values:
        # 
        # - `high`: High risk. If the content matches an entry in a custom keyword library, the risk level defaults to high.
        # 
        # - `medium`: Medium risk.
        # 
        # - `low`: Low risk.
        # 
        # - `none`: No risk detected.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.label is not None:
            result['Label'] = self.label

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class MultiModalGuardAsyncResultResponseBodyDataAudioResult(DaraModel):
    def __init__(
        self,
        slice_details: List[main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetails] = None,
        slice_num: int = None,
        suggestion: str = None,
    ):
        # Details for each audio slice.
        self.slice_details = slice_details
        # The slice count.
        self.slice_num = slice_num
        # The overall recommended action for the audio content.
        self.suggestion = suggestion

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
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k1 in self.slice_details:
                result['SliceDetails'].append(k1.to_map() if k1 else None)

        if self.slice_num is not None:
            result['SliceNum'] = self.slice_num

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k1 in m.get('SliceDetails'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k1))

        if m.get('SliceNum') is not None:
            self.slice_num = m.get('SliceNum')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetails(DaraModel):
    def __init__(
        self,
        detail: List[main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetail] = None,
        end_time: int = None,
        start_time: int = None,
        suggestion: str = None,
        text: str = None,
        url: str = None,
    ):
        # Detection details for the audio slice.
        self.detail = detail
        # The end time of the audio slice, in seconds.
        self.end_time = end_time
        # The start time of the audio slice, in seconds.
        self.start_time = start_time
        # The recommended action. Valid values:
        # 
        # - `block`: Block the content.
        # 
        # - `pass`: Pass the content.
        # 
        # - `watch`: The content requires review.
        # 
        # - `mask`: Mask the content.
        self.suggestion = suggestion
        # The speech-to-text transcript of the audio slice.
        self.text = text
        # The temporary URL of the audio slice.
        self.url = url

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.text is not None:
            result['Text'] = self.text

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetail(DaraModel):
    def __init__(
        self,
        level: str = None,
        result: List[main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetailResult] = None,
        suggestion: str = None,
        type: str = None,
    ):
        # The risk level. Valid values:
        # 
        # - `high`: High risk. If the content matches an entry in a custom keyword library, the risk level defaults to high.
        # 
        # - `medium`: Medium risk.
        # 
        # - `low`: Low risk.
        # 
        # - `none`: No risk detected.
        self.level = level
        # A list of detection results.
        self.result = result
        # The recommended action. Valid values:
        # 
        # - `block`: Block the content.
        # 
        # - `pass`: Pass the content.
        # 
        # - `watch`: The content requires review.
        # 
        # - `mask`: Mask the content.
        self.suggestion = suggestion
        # The detection type. Valid values:
        # 
        # - `contentModeration`: Content moderation.
        # 
        # - `promptAttack`: Prompt attack detection.
        # 
        # - `sensitiveData`: Sensitive data detection.
        # 
        # - `modelHallucination`: Model hallucination.
        # 
        # - `maliciousFile`: Malicious file detection.
        self.type = type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetailResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MultiModalGuardAsyncResultResponseBodyDataAudioResultSliceDetailsDetailResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        ext: Any = None,
        label: str = None,
        level: str = None,
    ):
        # The confidence score, ranging from 0 to 100, accurate to two decimal places.
        self.confidence = confidence
        # The description of the label.
        self.description = description
        # Additional information about the detection result.
        self.ext = ext
        # The label of the detection result.
        self.label = label
        # The risk level. Valid values:
        # 
        # - `high`: High risk. If the content matches an entry in a custom keyword library, the risk level defaults to high.
        # 
        # - `medium`: Medium risk.
        # 
        # - `low`: Low risk.
        # 
        # - `none`: No risk detected.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.label is not None:
            result['Label'] = self.label

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

