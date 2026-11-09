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
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
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
        redact_result: main_models.MultiModalGuardAsyncResultResponseBodyDataRedactResult = None,
        suggestion: str = None,
        task_id: str = None,
    ):
        # The segmented audio moderation results.
        self.audio_result = audio_result
        # The value of the dataId parameter passed in the API request. If this parameter is not passed in the request, this field is not returned.
        self.data_id = data_id
        # The list of video frame capture results.
        self.frame_result = frame_result
        # The unique ID of the live stream.
        self.live_id = live_id
        # The data masking result.
        self.redact_result = redact_result
        # The suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
        self.suggestion = suggestion
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()
        if self.redact_result:
            self.redact_result.validate()

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

        if self.redact_result is not None:
            result['RedactResult'] = self.redact_result.to_map()

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

        if m.get('RedactResult') is not None:
            temp_model = main_models.MultiModalGuardAsyncResultResponseBodyDataRedactResult()
            self.redact_result = temp_model.from_map(m.get('RedactResult'))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class MultiModalGuardAsyncResultResponseBodyDataRedactResult(DaraModel):
    def __init__(
        self,
        process_type: str = None,
        result_oss_bucket_name: str = None,
        result_oss_object_name: str = None,
        result_oss_region_id: str = None,
        result_url: str = None,
        source_url: str = None,
        status: str = None,
    ):
        # The processing type.
        self.process_type = process_type
        # The name of the OSS bucket that stores the masked object.
        self.result_oss_bucket_name = result_oss_bucket_name
        # The name of the OSS object for the masked data.
        self.result_oss_object_name = result_oss_object_name
        # The region of the masked OSS object.
        self.result_oss_region_id = result_oss_region_id
        # The temporary URL of the masked object.
        self.result_url = result_url
        # The URL of the object before masking.
        self.source_url = source_url
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.result_oss_bucket_name is not None:
            result['ResultOssBucketName'] = self.result_oss_bucket_name

        if self.result_oss_object_name is not None:
            result['ResultOssObjectName'] = self.result_oss_object_name

        if self.result_oss_region_id is not None:
            result['ResultOssRegionId'] = self.result_oss_region_id

        if self.result_url is not None:
            result['ResultUrl'] = self.result_url

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('ResultOssBucketName') is not None:
            self.result_oss_bucket_name = m.get('ResultOssBucketName')

        if m.get('ResultOssObjectName') is not None:
            self.result_oss_object_name = m.get('ResultOssObjectName')

        if m.get('ResultOssRegionId') is not None:
            self.result_oss_region_id = m.get('ResultOssRegionId')

        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class MultiModalGuardAsyncResultResponseBodyDataFrameResult(DaraModel):
    def __init__(
        self,
        frames: List[main_models.MultiModalGuardAsyncResultResponseBodyDataFrameResultFrames] = None,
        slice_num: int = None,
        suggestion: str = None,
    ):
        # The frame moderation results.
        self.frames = frames
        # The number of segments.
        self.slice_num = slice_num
        # The moderation suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
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
        error_code: int = None,
        error_msg: str = None,
        offset: float = None,
        suggestion: str = None,
        timestamp: int = None,
        url: str = None,
    ):
        # The list of moderation results.
        self.detail = detail
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The position of the captured frame.
        self.offset = offset
        # The moderation suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
        self.suggestion = suggestion
        # The absolute timestamp, in milliseconds.
        self.timestamp = timestamp
        # The temporary URL of the segment.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

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

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

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
        # The risk level. Valid values:
        # - high: High risk. If a custom dictionary is hit, the risk level is high by default.
        # - medium: Medium risk.
        # - low: Low risk.
        # - none: No risk detected.
        self.level = level
        # The moderation result.
        self.result = result
        # The moderation suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
        self.suggestion = suggestion
        # The moderation type. Valid values:
        # - contentModeration: Content compliance moderation.
        # - promptAttack: Prompt attack detection.
        # - sensitiveData: Sensitive content detection.
        # - modelHallucination: Model hallucination detection.
        # - maliciousFile: Malicious file detection.
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
        # The confidence score. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The label description.
        self.description = description
        # The extended information of the moderation result.
        self.ext = ext
        # The label.
        self.label = label
        # The risk level. Valid values:
        # - high: High risk. If a custom dictionary is hit, the risk level is high by default.
        # - medium: Medium risk.
        # - low: Low risk.
        # - none: No risk detected.
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
        # The segment details.
        self.slice_details = slice_details
        # The number of segments.
        self.slice_num = slice_num
        # The suggestion.
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
        # The moderation details.
        self.detail = detail
        # The end time of the segment, in seconds.
        self.end_time = end_time
        # The start time of the segment, in seconds.
        self.start_time = start_time
        # The moderation suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
        self.suggestion = suggestion
        # The transcribed text of the audio segment.
        self.text = text
        # The temporary URL of the audio segment file.
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
        # - high: High risk. If a custom dictionary is hit, the risk level is high by default.
        # - medium: Medium risk.
        # - low: Low risk.
        # - none: No risk detected.
        self.level = level
        # The list of moderation results.
        self.result = result
        # The moderation suggestion. Valid values:
        # 
        # - block: Block the content.
        # - pass: Allow the content.
        # - watch: Review the content.
        # - mask: Mask the content.
        self.suggestion = suggestion
        # The moderation type. Valid values:
        # - contentModeration: Content compliance moderation.
        # - promptAttack: Prompt attack detection.
        # - sensitiveData: Sensitive content detection.
        # - modelHallucination: Model hallucination detection.
        # - maliciousFile: Malicious file detection.
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
        # The confidence score. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The label description.
        self.description = description
        # The extended information of the moderation result.
        self.ext = ext
        # The label.
        self.label = label
        # The risk level. Valid values:
        # - high: High risk. If a custom dictionary is hit, the risk level is high by default.
        # - medium: Medium risk.
        # - low: Low risk.
        # - none: No risk detected.
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

