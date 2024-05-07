# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AsrRealtimeRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        customization_id: str = None,
        disfluency: bool = None,
        enable_ignore_sentence_timeout: bool = None,
        enable_intermediate_result: bool = None,
        enable_inverse_text_normalization: bool = None,
        enable_punctuation_prediction: bool = None,
        enable_semantic_sentence_detection: bool = None,
        enable_words: bool = None,
        file_url: str = None,
        format: str = None,
        max_sentence_silence: int = None,
        sample_rate: int = None,
        speech_noise_threshold: float = None,
        vocabulary_id: str = None,
    ):
        self.app_id = app_id
        self.customization_id = customization_id
        self.disfluency = disfluency
        self.enable_ignore_sentence_timeout = enable_ignore_sentence_timeout
        self.enable_intermediate_result = enable_intermediate_result
        self.enable_inverse_text_normalization = enable_inverse_text_normalization
        self.enable_punctuation_prediction = enable_punctuation_prediction
        self.enable_semantic_sentence_detection = enable_semantic_sentence_detection
        self.enable_words = enable_words
        self.file_url = file_url
        self.format = format
        self.max_sentence_silence = max_sentence_silence
        self.sample_rate = sample_rate
        self.speech_noise_threshold = speech_noise_threshold
        self.vocabulary_id = vocabulary_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.customization_id is not None:
            result['CustomizationId'] = self.customization_id
        if self.disfluency is not None:
            result['Disfluency'] = self.disfluency
        if self.enable_ignore_sentence_timeout is not None:
            result['EnableIgnoreSentenceTimeout'] = self.enable_ignore_sentence_timeout
        if self.enable_intermediate_result is not None:
            result['EnableIntermediateResult'] = self.enable_intermediate_result
        if self.enable_inverse_text_normalization is not None:
            result['EnableInverseTextNormalization'] = self.enable_inverse_text_normalization
        if self.enable_punctuation_prediction is not None:
            result['EnablePunctuationPrediction'] = self.enable_punctuation_prediction
        if self.enable_semantic_sentence_detection is not None:
            result['EnableSemanticSentenceDetection'] = self.enable_semantic_sentence_detection
        if self.enable_words is not None:
            result['EnableWords'] = self.enable_words
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format is not None:
            result['Format'] = self.format
        if self.max_sentence_silence is not None:
            result['MaxSentenceSilence'] = self.max_sentence_silence
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.speech_noise_threshold is not None:
            result['SpeechNoiseThreshold'] = self.speech_noise_threshold
        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')
        if m.get('Disfluency') is not None:
            self.disfluency = m.get('Disfluency')
        if m.get('EnableIgnoreSentenceTimeout') is not None:
            self.enable_ignore_sentence_timeout = m.get('EnableIgnoreSentenceTimeout')
        if m.get('EnableIntermediateResult') is not None:
            self.enable_intermediate_result = m.get('EnableIntermediateResult')
        if m.get('EnableInverseTextNormalization') is not None:
            self.enable_inverse_text_normalization = m.get('EnableInverseTextNormalization')
        if m.get('EnablePunctuationPrediction') is not None:
            self.enable_punctuation_prediction = m.get('EnablePunctuationPrediction')
        if m.get('EnableSemanticSentenceDetection') is not None:
            self.enable_semantic_sentence_detection = m.get('EnableSemanticSentenceDetection')
        if m.get('EnableWords') is not None:
            self.enable_words = m.get('EnableWords')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('MaxSentenceSilence') is not None:
            self.max_sentence_silence = m.get('MaxSentenceSilence')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SpeechNoiseThreshold') is not None:
            self.speech_noise_threshold = m.get('SpeechNoiseThreshold')
        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')
        return self


class AsrRealtimeResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        code: int = None,
        confidence: float = None,
        id: str = None,
        message: str = None,
        name: str = None,
        result: str = None,
        status: str = None,
        task_id: str = None,
        time: int = None,
    ):
        self.begin_time = begin_time
        self.code = code
        self.confidence = confidence
        self.id = id
        self.message = message
        self.name = name
        self.result = result
        self.status = status
        self.task_id = task_id
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.code is not None:
            result['Code'] = self.code
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class AsrRealtimeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AsrRealtimeResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AsrRealtimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AsrRealtimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsrRealtimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AsrRealtimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsrSentenceRequestAsrRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        enable_inverse_text_normalization: bool = None,
        enable_punctuation_prediction: bool = None,
        enable_voice_detection: bool = None,
        file_url: str = None,
        format: str = None,
        sample_rate: int = None,
    ):
        self.app_id = app_id
        self.enable_inverse_text_normalization = enable_inverse_text_normalization
        self.enable_punctuation_prediction = enable_punctuation_prediction
        self.enable_voice_detection = enable_voice_detection
        self.file_url = file_url
        self.format = format
        self.sample_rate = sample_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.enable_inverse_text_normalization is not None:
            result['EnableInverseTextNormalization'] = self.enable_inverse_text_normalization
        if self.enable_punctuation_prediction is not None:
            result['EnablePunctuationPrediction'] = self.enable_punctuation_prediction
        if self.enable_voice_detection is not None:
            result['EnableVoiceDetection'] = self.enable_voice_detection
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format is not None:
            result['Format'] = self.format
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnableInverseTextNormalization') is not None:
            self.enable_inverse_text_normalization = m.get('EnableInverseTextNormalization')
        if m.get('EnablePunctuationPrediction') is not None:
            self.enable_punctuation_prediction = m.get('EnablePunctuationPrediction')
        if m.get('EnableVoiceDetection') is not None:
            self.enable_voice_detection = m.get('EnableVoiceDetection')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class AsrSentenceRequest(TeaModel):
    def __init__(
        self,
        asr_request: AsrSentenceRequestAsrRequest = None,
    ):
        self.asr_request = asr_request

    def validate(self):
        if self.asr_request:
            self.asr_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_request is not None:
            result['AsrRequest'] = self.asr_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrRequest') is not None:
            temp_model = AsrSentenceRequestAsrRequest()
            self.asr_request = temp_model.from_map(m['AsrRequest'])
        return self


class AsrSentenceShrinkRequest(TeaModel):
    def __init__(
        self,
        asr_request_shrink: str = None,
    ):
        self.asr_request_shrink = asr_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_request_shrink is not None:
            result['AsrRequest'] = self.asr_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrRequest') is not None:
            self.asr_request_shrink = m.get('AsrRequest')
        return self


class AsrSentenceResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        result: str = None,
        task_id: str = None,
    ):
        self.code = code
        self.id = id
        self.message = message
        self.name = name
        self.result = result
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.result is not None:
            result['Result'] = self.result
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AsrSentenceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AsrSentenceResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AsrSentenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AsrSentenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsrSentenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AsrSentenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsrTaskRequestRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        asr_task_id: str = None,
        event: str = None,
        room_id: str = None,
        timestamp: int = None,
    ):
        self.app_id = app_id
        self.asr_task_id = asr_task_id
        self.event = event
        self.room_id = room_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.asr_task_id is not None:
            result['AsrTaskId'] = self.asr_task_id
        if self.event is not None:
            result['Event'] = self.event
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AsrTaskId') is not None:
            self.asr_task_id = m.get('AsrTaskId')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class AsrTaskRequest(TeaModel):
    def __init__(
        self,
        request: AsrTaskRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = AsrTaskRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class AsrTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        request_shrink: str = None,
    ):
        self.request_shrink = request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        return self


class AsrTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class AsrTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AsrTaskResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AsrTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AsrTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AsrTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AsrTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_base_param: str = None,
        client_version: str = None,
        department_id: str = None,
        room_id: str = None,
    ):
        self.app_id = app_id
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.department_id = department_id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class AssociateRoomResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AssociateRoomResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        errors: List[AssociateRoomResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = AssociateRoomResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssociateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        department_id: str = None,
        name: str = None,
        package_name: str = None,
    ):
        self.client_token = client_token
        self.department_id = department_id
        self.name = name
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class CreateAppResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        creator_name: str = None,
        disabled: bool = None,
        id: str = None,
        name: str = None,
    ):
        self.created_at = created_at
        self.creator_name = creator_name
        self.disabled = disabled
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # code
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDepartmentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        label: str = None,
        name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.label = label
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDepartmentResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateDepartmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateDepartmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDetectProcessRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        draft: str = None,
        name: str = None,
        type: str = None,
    ):
        self.content = content
        self.draft = draft
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        disabled: bool = None,
        draft: str = None,
        id: str = None,
        md_5: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        self.disabled = disabled
        self.draft = draft
        # ID
        self.id = id
        self.md_5 = md_5
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateDetectProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        name: str = None,
    ):
        self.client_token = client_token
        self.content = content
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSignatureRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_base_param: str = None,
        client_version: str = None,
        expire_time: int = None,
        uid: str = None,
    ):
        self.app_id = app_id
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.expire_time = expire_time
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CreateSignatureResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        rtc_app_id: str = None,
        rtc_biz_name: str = None,
        rtc_sign: str = None,
        rtc_workspace_id: str = None,
    ):
        self.expire_time = expire_time
        self.rtc_app_id = rtc_app_id
        self.rtc_biz_name = rtc_biz_name
        self.rtc_sign = rtc_sign
        self.rtc_workspace_id = rtc_workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.rtc_app_id is not None:
            result['RtcAppId'] = self.rtc_app_id
        if self.rtc_biz_name is not None:
            result['RtcBizName'] = self.rtc_biz_name
        if self.rtc_sign is not None:
            result['RtcSign'] = self.rtc_sign
        if self.rtc_workspace_id is not None:
            result['RtcWorkspaceId'] = self.rtc_workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RtcAppId') is not None:
            self.rtc_app_id = m.get('RtcAppId')
        if m.get('RtcBizName') is not None:
            self.rtc_biz_name = m.get('RtcBizName')
        if m.get('RtcSign') is not None:
            self.rtc_sign = m.get('RtcSign')
        if m.get('RtcWorkspaceId') is not None:
            self.rtc_workspace_id = m.get('RtcWorkspaceId')
        return self


class CreateSignatureResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSignatureResponseBodyData = None,
        errors: List[CreateSignatureResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = CreateSignatureResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSignatureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskGroupRequestVideoInfo(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        video_meta_url: str = None,
        video_url: str = None,
    ):
        self.rule_id = rule_id
        self.video_meta_url = video_meta_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class CreateTaskGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        day: List[int] = None,
        expire_at: str = None,
        group_name: str = None,
        rule_id: str = None,
        runnable_time_from: str = None,
        runnable_time_to: str = None,
        trigger_period: str = None,
        video_info: List[CreateTaskGroupRequestVideoInfo] = None,
    ):
        self.app_id = app_id
        self.client_token = client_token
        self.day = day
        self.expire_at = expire_at
        self.group_name = group_name
        self.rule_id = rule_id
        self.runnable_time_from = runnable_time_from
        self.runnable_time_to = runnable_time_to
        self.trigger_period = trigger_period
        self.video_info = video_info

    def validate(self):
        if self.video_info:
            for k in self.video_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.day is not None:
            result['Day'] = self.day
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.runnable_time_from is not None:
            result['RunnableTimeFrom'] = self.runnable_time_from
        if self.runnable_time_to is not None:
            result['RunnableTimeTo'] = self.runnable_time_to
        if self.trigger_period is not None:
            result['TriggerPeriod'] = self.trigger_period
        result['VideoInfo'] = []
        if self.video_info is not None:
            for k in self.video_info:
                result['VideoInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RunnableTimeFrom') is not None:
            self.runnable_time_from = m.get('RunnableTimeFrom')
        if m.get('RunnableTimeTo') is not None:
            self.runnable_time_to = m.get('RunnableTimeTo')
        if m.get('TriggerPeriod') is not None:
            self.trigger_period = m.get('TriggerPeriod')
        self.video_info = []
        if m.get('VideoInfo') is not None:
            for k in m.get('VideoInfo'):
                temp_model = CreateTaskGroupRequestVideoInfo()
                self.video_info.append(temp_model.from_map(k))
        return self


class CreateTaskGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        completed_tasks: int = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        task_ids: List[str] = None,
        total_tasks: int = None,
    ):
        self.completed_tasks = completed_tasks
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status
        self.task_ids = task_ids
        self.total_tasks = total_tasks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        return self


class CreateTaskGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTaskGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateTaskGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTaskGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTtsQuestionRequestRequest(TeaModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
        question_group_id: str = None,
    ):
        self.answer = answer
        self.question = question
        self.question_group_id = question_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.question is not None:
            result['Question'] = self.question
        if self.question_group_id is not None:
            result['QuestionGroupId'] = self.question_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('QuestionGroupId') is not None:
            self.question_group_id = m.get('QuestionGroupId')
        return self


class CreateTtsQuestionRequest(TeaModel):
    def __init__(
        self,
        request: CreateTtsQuestionRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateTtsQuestionRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateTtsQuestionShrinkRequest(TeaModel):
    def __init__(
        self,
        request_shrink: str = None,
    ):
        self.request_shrink = request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        return self


class CreateTtsQuestionResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateTtsQuestionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateTtsQuestionResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTtsQuestionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTtsQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTtsQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTtsQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTtsQuestionGroupRequestRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        pitch_rate: int = None,
        sample_rate: int = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.format = format
        self.pitch_rate = pitch_rate
        self.sample_rate = sample_rate
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class CreateTtsQuestionGroupRequest(TeaModel):
    def __init__(
        self,
        request: CreateTtsQuestionGroupRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateTtsQuestionGroupRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateTtsQuestionGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        request_shrink: str = None,
    ):
        self.request_shrink = request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        return self


class CreateTtsQuestionGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateTtsQuestionGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateTtsQuestionGroupResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTtsQuestionGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTtsQuestionGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTtsQuestionGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTtsQuestionGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserDepartmentsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        department_id: List[str] = None,
        user_id: List[str] = None,
    ):
        self.client_token = client_token
        self.department_id = department_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoMergeTaskRequestVideoMergeRequestLayoutStylesVideoStyles(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        height: int = None,
        position_x: int = None,
        position_y: int = None,
        width: int = None,
    ):
        self.file_name = file_name
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.height is not None:
            result['Height'] = self.height
        if self.position_x is not None:
            result['PositionX'] = self.position_x
        if self.position_y is not None:
            result['PositionY'] = self.position_y
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('PositionX') is not None:
            self.position_x = m.get('PositionX')
        if m.get('PositionY') is not None:
            self.position_y = m.get('PositionY')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateVideoMergeTaskRequestVideoMergeRequestLayoutStyles(TeaModel):
    def __init__(
        self,
        height: int = None,
        input_num: int = None,
        video_styles: List[CreateVideoMergeTaskRequestVideoMergeRequestLayoutStylesVideoStyles] = None,
        width: int = None,
    ):
        self.height = height
        self.input_num = input_num
        self.video_styles = video_styles
        self.width = width

    def validate(self):
        if self.video_styles:
            for k in self.video_styles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.input_num is not None:
            result['InputNum'] = self.input_num
        result['VideoStyles'] = []
        if self.video_styles is not None:
            for k in self.video_styles:
                result['VideoStyles'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('InputNum') is not None:
            self.input_num = m.get('InputNum')
        self.video_styles = []
        if m.get('VideoStyles') is not None:
            for k in m.get('VideoStyles'):
                temp_model = CreateVideoMergeTaskRequestVideoMergeRequestLayoutStylesVideoStyles()
                self.video_styles.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateVideoMergeTaskRequestVideoMergeRequestVideoList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        file_name: str = None,
        file_url: str = None,
        merge_begin_time: int = None,
        merge_end_time: int = None,
        prime_video: bool = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.file_name = file_name
        self.file_url = file_url
        self.merge_begin_time = merge_begin_time
        self.merge_end_time = merge_end_time
        self.prime_video = prime_video
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.merge_begin_time is not None:
            result['MergeBeginTime'] = self.merge_begin_time
        if self.merge_end_time is not None:
            result['MergeEndTime'] = self.merge_end_time
        if self.prime_video is not None:
            result['PrimeVideo'] = self.prime_video
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('MergeBeginTime') is not None:
            self.merge_begin_time = m.get('MergeBeginTime')
        if m.get('MergeEndTime') is not None:
            self.merge_end_time = m.get('MergeEndTime')
        if m.get('PrimeVideo') is not None:
            self.prime_video = m.get('PrimeVideo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateVideoMergeTaskRequestVideoMergeRequestWatermark(TeaModel):
    def __init__(
        self,
        font_color: str = None,
        font_size: int = None,
        position_x: int = None,
        position_y: int = None,
        text: str = None,
        timestamp: int = None,
    ):
        self.font_color = font_color
        self.font_size = font_size
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.position_x is not None:
            result['PositionX'] = self.position_x
        if self.position_y is not None:
            result['PositionY'] = self.position_y
        if self.text is not None:
            result['Text'] = self.text
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('PositionX') is not None:
            self.position_x = m.get('PositionX')
        if m.get('PositionY') is not None:
            self.position_y = m.get('PositionY')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class CreateVideoMergeTaskRequestVideoMergeRequest(TeaModel):
    def __init__(
        self,
        callback_url: str = None,
        layout_styles: List[CreateVideoMergeTaskRequestVideoMergeRequestLayoutStyles] = None,
        video_list: List[CreateVideoMergeTaskRequestVideoMergeRequestVideoList] = None,
        watermark: CreateVideoMergeTaskRequestVideoMergeRequestWatermark = None,
    ):
        self.callback_url = callback_url
        self.layout_styles = layout_styles
        self.video_list = video_list
        self.watermark = watermark

    def validate(self):
        if self.layout_styles:
            for k in self.layout_styles:
                if k:
                    k.validate()
        if self.video_list:
            for k in self.video_list:
                if k:
                    k.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        result['LayoutStyles'] = []
        if self.layout_styles is not None:
            for k in self.layout_styles:
                result['LayoutStyles'].append(k.to_map() if k else None)
        result['VideoList'] = []
        if self.video_list is not None:
            for k in self.video_list:
                result['VideoList'].append(k.to_map() if k else None)
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        self.layout_styles = []
        if m.get('LayoutStyles') is not None:
            for k in m.get('LayoutStyles'):
                temp_model = CreateVideoMergeTaskRequestVideoMergeRequestLayoutStyles()
                self.layout_styles.append(temp_model.from_map(k))
        self.video_list = []
        if m.get('VideoList') is not None:
            for k in m.get('VideoList'):
                temp_model = CreateVideoMergeTaskRequestVideoMergeRequestVideoList()
                self.video_list.append(temp_model.from_map(k))
        if m.get('Watermark') is not None:
            temp_model = CreateVideoMergeTaskRequestVideoMergeRequestWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class CreateVideoMergeTaskRequest(TeaModel):
    def __init__(
        self,
        video_merge_request: CreateVideoMergeTaskRequestVideoMergeRequest = None,
    ):
        self.video_merge_request = video_merge_request

    def validate(self):
        if self.video_merge_request:
            self.video_merge_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_merge_request is not None:
            result['VideoMergeRequest'] = self.video_merge_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoMergeRequest') is not None:
            temp_model = CreateVideoMergeTaskRequestVideoMergeRequest()
            self.video_merge_request = temp_model.from_map(m['VideoMergeRequest'])
        return self


class CreateVideoMergeTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        video_merge_request_shrink: str = None,
    ):
        self.video_merge_request_shrink = video_merge_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_merge_request_shrink is not None:
            result['VideoMergeRequest'] = self.video_merge_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoMergeRequest') is not None:
            self.video_merge_request_shrink = m.get('VideoMergeRequest')
        return self


class CreateVideoMergeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        status: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateVideoMergeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVideoMergeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVideoMergeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWatermarkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateWatermarkResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateWatermarkResponseBodyData = None,
        errors: List[CreateWatermarkResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = CreateWatermarkResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDepartmentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DeleteRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteUserResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        errors: List[DeleteUserResponseBodyErrors] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.errors = errors
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
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
            self.data = m.get('Data')
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = DeleteUserResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserDepartmentsRequest(TeaModel):
    def __init__(
        self,
        department_id: List[str] = None,
        user_id: List[str] = None,
    ):
        self.department_id = department_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWatermarkRequest(TeaModel):
    def __init__(
        self,
        watermark_id: str = None,
    ):
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class DeleteWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DeleteWatermarkResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteWatermarkResponseBodyData = None,
        errors: List[DeleteWatermarkResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = DeleteWatermarkResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceCompareRequestFaceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source_image: str = None,
        target_image: str = None,
    ):
        self.app_id = app_id
        self.source_image = source_image
        self.target_image = target_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source_image is not None:
            result['SourceImage'] = self.source_image
        if self.target_image is not None:
            result['TargetImage'] = self.target_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SourceImage') is not None:
            self.source_image = m.get('SourceImage')
        if m.get('TargetImage') is not None:
            self.target_image = m.get('TargetImage')
        return self


class FaceCompareRequest(TeaModel):
    def __init__(
        self,
        face_request: FaceCompareRequestFaceRequest = None,
    ):
        self.face_request = face_request

    def validate(self):
        if self.face_request:
            self.face_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request is not None:
            result['FaceRequest'] = self.face_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            temp_model = FaceCompareRequestFaceRequest()
            self.face_request = temp_model.from_map(m['FaceRequest'])
        return self


class FaceCompareShrinkRequest(TeaModel):
    def __init__(
        self,
        face_request_shrink: str = None,
    ):
        self.face_request_shrink = face_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request_shrink is not None:
            result['FaceRequest'] = self.face_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            self.face_request_shrink = m.get('FaceRequest')
        return self


class FaceCompareResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        message: str = None,
        passed: str = None,
        request_id: str = None,
        status: str = None,
        verify_score: float = None,
    ):
        self.code = code
        # ID
        self.id = id
        self.message = message
        self.passed = passed
        self.request_id = request_id
        self.status = status
        self.verify_score = verify_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        return self


class FaceCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FaceCompareResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FaceCompareResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FaceCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceCompareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FaceCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceLivenessRequestFaceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        source_image: str = None,
    ):
        self.app_id = app_id
        self.source_image = source_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source_image is not None:
            result['SourceImage'] = self.source_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SourceImage') is not None:
            self.source_image = m.get('SourceImage')
        return self


class FaceLivenessRequest(TeaModel):
    def __init__(
        self,
        face_request: FaceLivenessRequestFaceRequest = None,
    ):
        self.face_request = face_request

    def validate(self):
        if self.face_request:
            self.face_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request is not None:
            result['FaceRequest'] = self.face_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            temp_model = FaceLivenessRequestFaceRequest()
            self.face_request = temp_model.from_map(m['FaceRequest'])
        return self


class FaceLivenessShrinkRequest(TeaModel):
    def __init__(
        self,
        face_request_shrink: str = None,
    ):
        self.face_request_shrink = face_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request_shrink is not None:
            result['FaceRequest'] = self.face_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            self.face_request_shrink = m.get('FaceRequest')
        return self


class FaceLivenessResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        passed: str = None,
        public_id: str = None,
        score: float = None,
        status: str = None,
    ):
        self.code = code
        self.message = message
        self.passed = passed
        self.public_id = public_id
        self.score = score
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.public_id is not None:
            result['PublicId'] = self.public_id
        if self.score is not None:
            result['Score'] = self.score
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('PublicId') is not None:
            self.public_id = m.get('PublicId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FaceLivenessResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FaceLivenessResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FaceLivenessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FaceLivenessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceLivenessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FaceLivenessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceRecognizeRequestFaceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        liveness: bool = None,
        source_image: str = None,
        target_image: str = None,
    ):
        self.app_id = app_id
        self.liveness = liveness
        self.source_image = source_image
        self.target_image = target_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.source_image is not None:
            result['SourceImage'] = self.source_image
        if self.target_image is not None:
            result['TargetImage'] = self.target_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('SourceImage') is not None:
            self.source_image = m.get('SourceImage')
        if m.get('TargetImage') is not None:
            self.target_image = m.get('TargetImage')
        return self


class FaceRecognizeRequest(TeaModel):
    def __init__(
        self,
        face_request: FaceRecognizeRequestFaceRequest = None,
    ):
        self.face_request = face_request

    def validate(self):
        if self.face_request:
            self.face_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request is not None:
            result['FaceRequest'] = self.face_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            temp_model = FaceRecognizeRequestFaceRequest()
            self.face_request = temp_model.from_map(m['FaceRequest'])
        return self


class FaceRecognizeShrinkRequest(TeaModel):
    def __init__(
        self,
        face_request_shrink: str = None,
    ):
        self.face_request_shrink = face_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_request_shrink is not None:
            result['FaceRequest'] = self.face_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRequest') is not None:
            self.face_request_shrink = m.get('FaceRequest')
        return self


class FaceRecognizeResponseBodyData(TeaModel):
    def __init__(
        self,
        compare_passed: str = None,
        compare_score: float = None,
        liveness_passed: str = None,
        liveness_score: float = None,
    ):
        self.compare_passed = compare_passed
        self.compare_score = compare_score
        self.liveness_passed = liveness_passed
        self.liveness_score = liveness_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_passed is not None:
            result['ComparePassed'] = self.compare_passed
        if self.compare_score is not None:
            result['CompareScore'] = self.compare_score
        if self.liveness_passed is not None:
            result['LivenessPassed'] = self.liveness_passed
        if self.liveness_score is not None:
            result['LivenessScore'] = self.liveness_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparePassed') is not None:
            self.compare_passed = m.get('ComparePassed')
        if m.get('CompareScore') is not None:
            self.compare_score = m.get('CompareScore')
        if m.get('LivenessPassed') is not None:
            self.liveness_passed = m.get('LivenessPassed')
        if m.get('LivenessScore') is not None:
            self.liveness_score = m.get('LivenessScore')
        return self


class FaceRecognizeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FaceRecognizeResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FaceRecognizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FaceRecognizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceRecognizeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FaceRecognizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        client_version: str = None,
        device_id: str = None,
        id: str = None,
        package_name: str = None,
    ):
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.device_id = device_id
        self.id = id
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class GetAppResponseBodyData(TeaModel):
    def __init__(
        self,
        config: str = None,
        created_at: str = None,
        disabled: str = None,
        fee_id: str = None,
        name: str = None,
    ):
        self.config = config
        self.created_at = created_at
        self.disabled = disabled
        self.fee_id = fee_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.fee_id is not None:
            result['FeeId'] = self.fee_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('FeeId') is not None:
            self.fee_id = m.get('FeeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetAppResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsrResultRequest(TeaModel):
    def __init__(
        self,
        asr_task_id: str = None,
    ):
        self.asr_task_id = asr_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_task_id is not None:
            result['AsrTaskId'] = self.asr_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrTaskId') is not None:
            self.asr_task_id = m.get('AsrTaskId')
        return self


class GetAsrResultResponseBodyData(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetAsrResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAsrResultResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAsrResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsrResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsrResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsrResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepartmentRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDepartmentResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.description = description
        # ID
        self.id = id
        self.name = name
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDepartmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDepartmentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectProcessRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        draft: str = None,
        id: str = None,
        md_5: str = None,
        name: str = None,
        new_version: bool = None,
        updated_at: str = None,
    ):
        self.content = content
        self.created_at = created_at
        self.draft = draft
        # ID
        self.id = id
        self.md_5 = md_5
        self.name = name
        self.new_version = new_version
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.new_version is not None:
            result['NewVersion'] = self.new_version
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewVersion') is not None:
            self.new_version = m.get('NewVersion')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDetectProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectProcessJsonFileRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectProcessJsonFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectProcessJsonFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectProcessJsonFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDetectProcessJsonFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectionRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDetectionResponseBodyDataTasks(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        status: str = None,
        video_meta_url: str = None,
        video_url: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.status = status
        self.video_meta_url = video_meta_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetDetectionResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        department_id: str = None,
        department_name: str = None,
        id: str = None,
        recording_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        tasks: List[GetDetectionResponseBodyDataTasks] = None,
    ):
        self.created_at = created_at
        self.department_id = department_id
        self.department_name = department_name
        # ID
        self.id = id
        self.recording_type = recording_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.id is not None:
            result['Id'] = self.id
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = GetDetectionResponseBodyDataTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class GetDetectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDetectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDetectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDetectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreSignedUrlRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        client_version: str = None,
        prefix: str = None,
    ):
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class GetPreSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPreSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPreSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPreSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordResultRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        record_id: str = None,
    ):
        self.client_base_param = client_base_param
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class GetRecordResultResponseBodyDataRecordRoomList(TeaModel):
    def __init__(
        self,
        outer_business_id: str = None,
        record_type: str = None,
        role: str = None,
        room_meta_url: str = None,
        room_record_at: str = None,
        room_result_url: str = None,
        room_status: str = None,
        room_video_url: str = None,
        rtc_record_id: str = None,
    ):
        self.outer_business_id = outer_business_id
        self.record_type = record_type
        self.role = role
        self.room_meta_url = room_meta_url
        self.room_record_at = room_record_at
        self.room_result_url = room_result_url
        self.room_status = room_status
        self.room_video_url = room_video_url
        self.rtc_record_id = rtc_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.role is not None:
            result['Role'] = self.role
        if self.room_meta_url is not None:
            result['RoomMetaUrl'] = self.room_meta_url
        if self.room_record_at is not None:
            result['RoomRecordAt'] = self.room_record_at
        if self.room_result_url is not None:
            result['RoomResultUrl'] = self.room_result_url
        if self.room_status is not None:
            result['RoomStatus'] = self.room_status
        if self.room_video_url is not None:
            result['RoomVideoUrl'] = self.room_video_url
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoomMetaUrl') is not None:
            self.room_meta_url = m.get('RoomMetaUrl')
        if m.get('RoomRecordAt') is not None:
            self.room_record_at = m.get('RoomRecordAt')
        if m.get('RoomResultUrl') is not None:
            self.room_result_url = m.get('RoomResultUrl')
        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')
        if m.get('RoomVideoUrl') is not None:
            self.room_video_url = m.get('RoomVideoUrl')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        return self


class GetRecordResultResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        created_at: str = None,
        department_name: str = None,
        detect_process_name: str = None,
        duration: int = None,
        id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        record_room_list: List[GetRecordResultResponseBodyDataRecordRoomList] = None,
        result_url: str = None,
        room_id: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.app_name = app_name
        self.created_at = created_at
        self.department_name = department_name
        self.detect_process_name = detect_process_name
        self.duration = duration
        self.id = id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.record_room_list = record_room_list
        self.result_url = result_url
        self.room_id = room_id
        self.status = status
        self.video_url = video_url

    def validate(self):
        if self.record_room_list:
            for k in self.record_room_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.detect_process_name is not None:
            result['DetectProcessName'] = self.detect_process_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        result['RecordRoomList'] = []
        if self.record_room_list is not None:
            for k in self.record_room_list:
                result['RecordRoomList'].append(k.to_map() if k else None)
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('DetectProcessName') is not None:
            self.detect_process_name = m.get('DetectProcessName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        self.record_room_list = []
        if m.get('RecordRoomList') is not None:
            for k in m.get('RecordRoomList'):
                temp_model = GetRecordResultResponseBodyDataRecordRoomList()
                self.record_room_list.append(temp_model.from_map(k))
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetRecordResultResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetRecordResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRecordResultResponseBodyData = None,
        errors: List[GetRecordResultResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRecordResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetRecordResultResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRecordResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecordResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRecordResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordsByFeeIdRequest(TeaModel):
    def __init__(
        self,
        fee_id: str = None,
    ):
        self.fee_id = fee_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fee_id is not None:
            result['FeeId'] = self.fee_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeeId') is not None:
            self.fee_id = m.get('FeeId')
        return self


class GetRecordsByFeeIdResponseBodyDataRecordRoomList(TeaModel):
    def __init__(
        self,
        outer_business_id: str = None,
        record_type: str = None,
        role: str = None,
        room_meta_url: str = None,
        room_record_at: str = None,
        room_result_url: str = None,
        room_status: str = None,
        room_video_url: str = None,
        rtc_record_id: str = None,
    ):
        self.outer_business_id = outer_business_id
        self.record_type = record_type
        self.role = role
        self.room_meta_url = room_meta_url
        self.room_record_at = room_record_at
        self.room_result_url = room_result_url
        self.room_status = room_status
        self.room_video_url = room_video_url
        self.rtc_record_id = rtc_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.role is not None:
            result['Role'] = self.role
        if self.room_meta_url is not None:
            result['RoomMetaUrl'] = self.room_meta_url
        if self.room_record_at is not None:
            result['RoomRecordAt'] = self.room_record_at
        if self.room_result_url is not None:
            result['RoomResultUrl'] = self.room_result_url
        if self.room_status is not None:
            result['RoomStatus'] = self.room_status
        if self.room_video_url is not None:
            result['RoomVideoUrl'] = self.room_video_url
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoomMetaUrl') is not None:
            self.room_meta_url = m.get('RoomMetaUrl')
        if m.get('RoomRecordAt') is not None:
            self.room_record_at = m.get('RoomRecordAt')
        if m.get('RoomResultUrl') is not None:
            self.room_result_url = m.get('RoomResultUrl')
        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')
        if m.get('RoomVideoUrl') is not None:
            self.room_video_url = m.get('RoomVideoUrl')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        return self


class GetRecordsByFeeIdResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        created_at: str = None,
        department_name: str = None,
        detect_process_name: str = None,
        duration: int = None,
        id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        record_room_list: List[GetRecordsByFeeIdResponseBodyDataRecordRoomList] = None,
        result_url: str = None,
        room_id: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.app_name = app_name
        self.created_at = created_at
        self.department_name = department_name
        self.detect_process_name = detect_process_name
        self.duration = duration
        self.id = id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.record_room_list = record_room_list
        self.result_url = result_url
        self.room_id = room_id
        self.status = status
        self.video_url = video_url

    def validate(self):
        if self.record_room_list:
            for k in self.record_room_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.detect_process_name is not None:
            result['DetectProcessName'] = self.detect_process_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        result['RecordRoomList'] = []
        if self.record_room_list is not None:
            for k in self.record_room_list:
                result['RecordRoomList'].append(k.to_map() if k else None)
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('DetectProcessName') is not None:
            self.detect_process_name = m.get('DetectProcessName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        self.record_room_list = []
        if m.get('RecordRoomList') is not None:
            for k in m.get('RecordRoomList'):
                temp_model = GetRecordsByFeeIdResponseBodyDataRecordRoomList()
                self.record_room_list.append(temp_model.from_map(k))
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetRecordsByFeeIdResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetRecordsByFeeIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRecordsByFeeIdResponseBodyData] = None,
        errors: List[GetRecordsByFeeIdResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetRecordsByFeeIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetRecordsByFeeIdResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRecordsByFeeIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecordsByFeeIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRecordsByFeeIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordsByOuterBusinessIdRequest(TeaModel):
    def __init__(
        self,
        outer_business_id: str = None,
    ):
        self.outer_business_id = outer_business_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        return self


class GetRecordsByOuterBusinessIdResponseBodyDataRecordRoomList(TeaModel):
    def __init__(
        self,
        outer_business_id: str = None,
        record_type: str = None,
        role: str = None,
        room_meta_url: str = None,
        room_record_at: str = None,
        room_result_url: str = None,
        room_status: str = None,
        room_video_url: str = None,
        rtc_record_id: str = None,
    ):
        self.outer_business_id = outer_business_id
        self.record_type = record_type
        self.role = role
        self.room_meta_url = room_meta_url
        self.room_record_at = room_record_at
        self.room_result_url = room_result_url
        self.room_status = room_status
        self.room_video_url = room_video_url
        self.rtc_record_id = rtc_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.role is not None:
            result['Role'] = self.role
        if self.room_meta_url is not None:
            result['RoomMetaUrl'] = self.room_meta_url
        if self.room_record_at is not None:
            result['RoomRecordAt'] = self.room_record_at
        if self.room_result_url is not None:
            result['RoomResultUrl'] = self.room_result_url
        if self.room_status is not None:
            result['RoomStatus'] = self.room_status
        if self.room_video_url is not None:
            result['RoomVideoUrl'] = self.room_video_url
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoomMetaUrl') is not None:
            self.room_meta_url = m.get('RoomMetaUrl')
        if m.get('RoomRecordAt') is not None:
            self.room_record_at = m.get('RoomRecordAt')
        if m.get('RoomResultUrl') is not None:
            self.room_result_url = m.get('RoomResultUrl')
        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')
        if m.get('RoomVideoUrl') is not None:
            self.room_video_url = m.get('RoomVideoUrl')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        return self


class GetRecordsByOuterBusinessIdResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        created_at: str = None,
        department_name: str = None,
        detect_process_name: str = None,
        duration: int = None,
        id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        record_room_list: List[GetRecordsByOuterBusinessIdResponseBodyDataRecordRoomList] = None,
        result_url: str = None,
        room_id: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.app_name = app_name
        self.created_at = created_at
        self.department_name = department_name
        self.detect_process_name = detect_process_name
        self.duration = duration
        self.id = id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.record_room_list = record_room_list
        self.result_url = result_url
        self.room_id = room_id
        self.status = status
        self.video_url = video_url

    def validate(self):
        if self.record_room_list:
            for k in self.record_room_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.detect_process_name is not None:
            result['DetectProcessName'] = self.detect_process_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        result['RecordRoomList'] = []
        if self.record_room_list is not None:
            for k in self.record_room_list:
                result['RecordRoomList'].append(k.to_map() if k else None)
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('DetectProcessName') is not None:
            self.detect_process_name = m.get('DetectProcessName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        self.record_room_list = []
        if m.get('RecordRoomList') is not None:
            for k in m.get('RecordRoomList'):
                temp_model = GetRecordsByOuterBusinessIdResponseBodyDataRecordRoomList()
                self.record_room_list.append(temp_model.from_map(k))
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetRecordsByOuterBusinessIdResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetRecordsByOuterBusinessIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRecordsByOuterBusinessIdResponseBodyData] = None,
        errors: List[GetRecordsByOuterBusinessIdResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetRecordsByOuterBusinessIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetRecordsByOuterBusinessIdResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRecordsByOuterBusinessIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecordsByOuterBusinessIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRecordsByOuterBusinessIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatisticsRecordsByFeeIdRequest(TeaModel):
    def __init__(
        self,
        fee_id: str = None,
    ):
        self.fee_id = fee_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fee_id is not None:
            result['FeeId'] = self.fee_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeeId') is not None:
            self.fee_id = m.get('FeeId')
        return self


class GetStatisticsRecordsByFeeIdResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        begin_at: str = None,
        charge_duration: int = None,
        created_at: str = None,
        department_id: int = None,
        detection_duration: int = None,
        device_id: str = None,
        device_type: int = None,
        end_at: str = None,
        fee_id: str = None,
        hour: int = None,
        tenant_id: int = None,
        type: str = None,
        updated_at: str = None,
    ):
        # appid
        self.app_id = app_id
        self.begin_at = begin_at
        self.charge_duration = charge_duration
        self.created_at = created_at
        self.department_id = department_id
        self.detection_duration = detection_duration
        self.device_id = device_id
        self.device_type = device_type
        self.end_at = end_at
        self.fee_id = fee_id
        self.hour = hour
        self.tenant_id = tenant_id
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.begin_at is not None:
            result['BeginAt'] = self.begin_at
        if self.charge_duration is not None:
            result['ChargeDuration'] = self.charge_duration
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.detection_duration is not None:
            result['DetectionDuration'] = self.detection_duration
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.end_at is not None:
            result['EndAt'] = self.end_at
        if self.fee_id is not None:
            result['FeeId'] = self.fee_id
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BeginAt') is not None:
            self.begin_at = m.get('BeginAt')
        if m.get('ChargeDuration') is not None:
            self.charge_duration = m.get('ChargeDuration')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DetectionDuration') is not None:
            self.detection_duration = m.get('DetectionDuration')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EndAt') is not None:
            self.end_at = m.get('EndAt')
        if m.get('FeeId') is not None:
            self.fee_id = m.get('FeeId')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetStatisticsRecordsByFeeIdResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetStatisticsRecordsByFeeIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetStatisticsRecordsByFeeIdResponseBodyData] = None,
        errors: List[GetStatisticsRecordsByFeeIdResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetStatisticsRecordsByFeeIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetStatisticsRecordsByFeeIdResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetStatisticsRecordsByFeeIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStatisticsRecordsByFeeIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStatisticsRecordsByFeeIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        task_id: str = None,
    ):
        self.client_base_param = client_base_param
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.status = status
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskGroupRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        completed_tasks: int = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        task_ids: List[str] = None,
        total_tasks: int = None,
    ):
        self.completed_tasks = completed_tasks
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status
        # -\
        self.task_ids = task_ids
        self.total_tasks = total_tasks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        return self


class GetTaskGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTaskGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetTaskGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTtsQuestionByGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetTtsQuestionByGroupIdResponseBodyDataQuestions(TeaModel):
    def __init__(
        self,
        answer: str = None,
        duration: float = None,
        id: int = None,
        oss_url: str = None,
        question: str = None,
        question_group_id: int = None,
        question_key: str = None,
        tenant_id: int = None,
    ):
        self.answer = answer
        self.duration = duration
        self.id = id
        self.oss_url = oss_url
        self.question = question
        self.question_group_id = question_group_id
        self.question_key = question_key
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.question is not None:
            result['Question'] = self.question
        if self.question_group_id is not None:
            result['QuestionGroupId'] = self.question_group_id
        if self.question_key is not None:
            result['QuestionKey'] = self.question_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('QuestionGroupId') is not None:
            self.question_group_id = m.get('QuestionGroupId')
        if m.get('QuestionKey') is not None:
            self.question_key = m.get('QuestionKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetTtsQuestionByGroupIdResponseBodyData(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        questions: List[GetTtsQuestionByGroupIdResponseBodyDataQuestions] = None,
    ):
        self.group_id = group_id
        self.questions = questions

    def validate(self):
        if self.questions:
            for k in self.questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        result['Questions'] = []
        if self.questions is not None:
            for k in self.questions:
                result['Questions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        self.questions = []
        if m.get('Questions') is not None:
            for k in m.get('Questions'):
                temp_model = GetTtsQuestionByGroupIdResponseBodyDataQuestions()
                self.questions.append(temp_model.from_map(k))
        return self


class GetTtsQuestionByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTtsQuestionByGroupIdResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTtsQuestionByGroupIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTtsQuestionByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTtsQuestionByGroupIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTtsQuestionByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        id: str = None,
    ):
        self.client_base_param = client_base_param
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserResponseBodyDataDepartments(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        name: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        departments: List[GetUserResponseBodyDataDepartments] = None,
        email: str = None,
        id: str = None,
        name: str = None,
        phone_number: str = None,
        role: str = None,
        source: str = None,
        updated_at: str = None,
        username: str = None,
    ):
        self.created_at = created_at
        self.departments = departments
        self.email = email
        # ID
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.role = role
        self.source = source
        self.updated_at = updated_at
        self.username = username

    def validate(self):
        if self.departments:
            for k in self.departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        result['Departments'] = []
        if self.departments is not None:
            for k in self.departments:
                result['Departments'].append(k.to_map() if k else None)
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.role is not None:
            result['Role'] = self.role
        if self.source is not None:
            result['Source'] = self.source
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        self.departments = []
        if m.get('Departments') is not None:
            for k in m.get('Departments'):
                temp_model = GetUserResponseBodyDataDepartments()
                self.departments.append(temp_model.from_map(k))
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUserResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoMergeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoMergeTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        client_trace_id: str = None,
        duration: float = None,
        height: int = None,
        merge_file_id: str = None,
        task_id: str = None,
        width: int = None,
    ):
        self.client_trace_id = client_trace_id
        self.duration = duration
        self.height = height
        self.merge_file_id = merge_file_id
        self.task_id = task_id
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_trace_id is not None:
            result['ClientTraceId'] = self.client_trace_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.merge_file_id is not None:
            result['MergeFileId'] = self.merge_file_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientTraceId') is not None:
            self.client_trace_id = m.get('ClientTraceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('MergeFileId') is not None:
            self.merge_file_id = m.get('MergeFileId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetVideoMergeTaskResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetVideoMergeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVideoMergeTaskResponseBodyData = None,
        errors: List[GetVideoMergeTaskResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetVideoMergeTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetVideoMergeTaskResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVideoMergeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoMergeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVideoMergeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWatermarkRequest(TeaModel):
    def __init__(
        self,
        client_base_param: str = None,
        client_version: str = None,
        watermark_id: str = None,
    ):
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class GetWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetWatermarkResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetWatermarkResponseBodyData = None,
        errors: List[GetWatermarkResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetWatermarkResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        room_token: str = None,
        stream_id: str = None,
    ):
        self.app_id = app_id
        self.room_id = room_id
        self.room_token = room_token
        self.stream_id = stream_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.room_token is not None:
            result['RoomToken'] = self.room_token
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RoomToken') is not None:
            self.room_token = m.get('RoomToken')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class JoinRoomResponseBodyData(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        stream_id: str = None,
    ):
        self.room_id = room_id
        self.stream_id = stream_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class JoinRoomResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: JoinRoomResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = JoinRoomResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class JoinRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JoinRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = JoinRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LeaveRoomRequest(TeaModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class LeaveRoomResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LeaveRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LeaveRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LeaveRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        department_id: str = None,
        department_name: str = None,
        disabled: bool = None,
        id: str = None,
        name: str = None,
        package_name: str = None,
    ):
        self.created_at = created_at
        self.department_id = department_id
        self.department_name = department_name
        self.disabled = disabled
        # ID
        self.id = id
        self.name = name
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class ListAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListAppsResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListAppsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAppsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDepartmentsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        self.name = name
        self.page_index = page_index
        self.page_size = page_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListDepartmentsResponseBodyDataItemsAdministrators(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListDepartmentsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        administrators: List[ListDepartmentsResponseBodyDataItemsAdministrators] = None,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        updated_at: str = None,
    ):
        self.administrators = administrators
        self.created_at = created_at
        self.description = description
        # ID
        self.id = id
        self.name = name
        self.updated_at = updated_at

    def validate(self):
        if self.administrators:
            for k in self.administrators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Administrators'] = []
        if self.administrators is not None:
            for k in self.administrators:
                result['Administrators'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.administrators = []
        if m.get('Administrators') is not None:
            for k in m.get('Administrators'):
                temp_model = ListDepartmentsResponseBodyDataItemsAdministrators()
                self.administrators.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListDepartmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDepartmentsResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDepartmentsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListDepartmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDepartmentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDepartmentsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDepartmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDepartmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDepartmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetectProcessesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
        publish_status: bool = None,
        sort: str = None,
        sort_key: str = None,
        type: str = None,
    ):
        self.name = name
        self.page_index = page_index
        self.page_size = page_size
        self.publish_status = publish_status
        self.sort = sort
        self.sort_key = sort_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDetectProcessesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_at: str = None,
        created_at: str = None,
        draft: str = None,
        draft_at: str = None,
        file_url: str = None,
        id: str = None,
        md_5: str = None,
        name: str = None,
        new_version: bool = None,
        published: bool = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.content = content
        self.content_at = content_at
        self.created_at = created_at
        self.draft = draft
        self.draft_at = draft_at
        self.file_url = file_url
        # ID
        self.id = id
        self.md_5 = md_5
        self.name = name
        self.new_version = new_version
        self.published = published
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_at is not None:
            result['ContentAt'] = self.content_at
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.draft_at is not None:
            result['DraftAt'] = self.draft_at
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        if self.new_version is not None:
            result['NewVersion'] = self.new_version
        if self.published is not None:
            result['Published'] = self.published
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentAt') is not None:
            self.content_at = m.get('ContentAt')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('DraftAt') is not None:
            self.draft_at = m.get('DraftAt')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewVersion') is not None:
            self.new_version = m.get('NewVersion')
        if m.get('Published') is not None:
            self.published = m.get('Published')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListDetectProcessesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDetectProcessesResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDetectProcessesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListDetectProcessesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDetectProcessesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDetectProcessesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDetectProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDetectProcessesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDetectProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetectionsRequest(TeaModel):
    def __init__(
        self,
        create_date_from: str = None,
        create_date_to: str = None,
        department_id: str = None,
        page_index: int = None,
        page_size: int = None,
        recording_type: str = None,
        rule_id: str = None,
    ):
        self.create_date_from = create_date_from
        self.create_date_to = create_date_to
        self.department_id = department_id
        self.page_index = page_index
        self.page_size = page_size
        self.recording_type = recording_type
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date_from is not None:
            result['CreateDateFrom'] = self.create_date_from
        if self.create_date_to is not None:
            result['CreateDateTo'] = self.create_date_to
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDateFrom') is not None:
            self.create_date_from = m.get('CreateDateFrom')
        if m.get('CreateDateTo') is not None:
            self.create_date_to = m.get('CreateDateTo')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListDetectionsResponseBodyDataItemsTasks(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        status: str = None,
        video_meta_url: str = None,
        video_url: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.status = status
        self.video_meta_url = video_meta_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListDetectionsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        department_id: str = None,
        department_name: str = None,
        id: str = None,
        recording_type: str = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        tasks: List[ListDetectionsResponseBodyDataItemsTasks] = None,
    ):
        self.created_at = created_at
        self.department_id = department_id
        self.department_name = department_name
        # ID
        self.id = id
        self.recording_type = recording_type
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.id is not None:
            result['Id'] = self.id
        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListDetectionsResponseBodyDataItemsTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListDetectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListDetectionsResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListDetectionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListDetectionsResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListDetectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDetectionsResponseBodyData = None,
        errors: List[ListDetectionsResponseBodyErrors] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # -\
        self.data = data
        # -\
        self.errors = errors
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
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
            temp_model = ListDetectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = ListDetectionsResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDetectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDetectionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDetectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        prefix: str = None,
    ):
        self.limit = limit
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListFilesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecordResultsRequest(TeaModel):
    def __init__(
        self,
        create_date_from: str = None,
        create_date_to: str = None,
        department_id: str = None,
        outer_business_id: str = None,
        page_index: int = None,
        page_size: int = None,
        record_id: str = None,
        type: str = None,
    ):
        self.create_date_from = create_date_from
        self.create_date_to = create_date_to
        self.department_id = department_id
        self.outer_business_id = outer_business_id
        self.page_index = page_index
        self.page_size = page_size
        self.record_id = record_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date_from is not None:
            result['CreateDateFrom'] = self.create_date_from
        if self.create_date_to is not None:
            result['CreateDateTo'] = self.create_date_to
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDateFrom') is not None:
            self.create_date_from = m.get('CreateDateFrom')
        if m.get('CreateDateTo') is not None:
            self.create_date_to = m.get('CreateDateTo')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecordResultsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        created_at: str = None,
        department_name: str = None,
        detect_process_name: str = None,
        duration: int = None,
        id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        result_url: str = None,
        room_id: str = None,
        rtc_record_id: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.app_name = app_name
        self.created_at = created_at
        self.department_name = department_name
        self.detect_process_name = detect_process_name
        self.duration = duration
        self.id = id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.result_url = result_url
        self.room_id = room_id
        self.rtc_record_id = rtc_record_id
        self.status = status
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name
        if self.detect_process_name is not None:
            result['DetectProcessName'] = self.detect_process_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')
        if m.get('DetectProcessName') is not None:
            self.detect_process_name = m.get('DetectProcessName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListRecordResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListRecordResultsResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListRecordResultsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListRecordResultsResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListRecordResultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListRecordResultsResponseBodyData = None,
        errors: List[ListRecordResultsResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListRecordResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = ListRecordResultsResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRecordResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecordResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRecordResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRulesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListRulesResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListRulesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskGroupsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTaskGroupsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        completed_tasks: int = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        status: str = None,
        task_ids: List[str] = None,
        total_tasks: int = None,
    ):
        self.completed_tasks = completed_tasks
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status
        self.task_ids = task_ids
        self.total_tasks = total_tasks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_tasks is not None:
            result['CompletedTasks'] = self.completed_tasks
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTasks') is not None:
            self.completed_tasks = m.get('CompletedTasks')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')
        return self


class ListTaskGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListTaskGroupsResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListTaskGroupsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListTaskGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTaskGroupsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListTaskGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTaskGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskItemsRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTaskItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        message: str = None,
        name: str = None,
        output: str = None,
        segment_seq: int = None,
        status: str = None,
    ):
        self.created_at = created_at
        self.message = message
        self.name = name
        self.output = output
        self.segment_seq = segment_seq
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.segment_seq is not None:
            result['SegmentSeq'] = self.segment_seq
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('SegmentSeq') is not None:
            self.segment_seq = m.get('SegmentSeq')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTaskItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTaskItemsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTaskItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTaskItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        task_group_id: str = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.task_group_id = task_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        return self


class ListTasksResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        status: str = None,
        video_meta_url: str = None,
        video_url: str = None,
    ):
        self.created_at = created_at
        # ID
        self.id = id
        self.status = status
        self.video_meta_url = video_meta_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.video_meta_url is not None:
            result['VideoMetaUrl'] = self.video_meta_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoMetaUrl') is not None:
            self.video_meta_url = m.get('VideoMetaUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListTasksResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListTasksResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        # -\
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        page_index: int = None,
        page_size: int = None,
        username: str = None,
    ):
        self.department_id = department_id
        self.page_index = page_index
        self.page_size = page_size
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBodyDataItemsDepartments(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.description = description
        # ID
        self.id = id
        self.name = name
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListUsersResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        departments: List[ListUsersResponseBodyDataItemsDepartments] = None,
        email: str = None,
        id: str = None,
        name: str = None,
        phone_number: str = None,
        ram_username: str = None,
        role: str = None,
        source: str = None,
        updated_at: str = None,
        username: str = None,
    ):
        self.created_at = created_at
        self.departments = departments
        self.email = email
        # ID
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.ram_username = ram_username
        self.role = role
        self.source = source
        self.updated_at = updated_at
        self.username = username

    def validate(self):
        if self.departments:
            for k in self.departments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        result['Departments'] = []
        if self.departments is not None:
            for k in self.departments:
                result['Departments'].append(k.to_map() if k else None)
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.ram_username is not None:
            result['RamUsername'] = self.ram_username
        if self.role is not None:
            result['Role'] = self.role
        if self.source is not None:
            result['Source'] = self.source
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        self.departments = []
        if m.get('Departments') is not None:
            for k in m.get('Departments'):
                temp_model = ListUsersResponseBodyDataItemsDepartments()
                self.departments.append(temp_model.from_map(k))
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RamUsername') is not None:
            self.ram_username = m.get('RamUsername')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListUsersResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListUsersResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListUsersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWatermarksRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListWatermarksResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListWatermarksResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListWatermarksResponseBodyDataItems] = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListWatermarksResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListWatermarksResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListWatermarksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListWatermarksResponseBodyData = None,
        errors: List[ListWatermarksResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListWatermarksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = ListWatermarksResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWatermarksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWatermarksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWatermarksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDetectProcessRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RenameDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        draft: str = None,
        id: str = None,
        md_5: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        self.draft = draft
        # ID
        self.id = id
        self.md_5 = md_5
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RenameDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RenameDetectProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = RenameDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenameDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TtsCommonRequestTtsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        format: str = None,
        pitch_rate: int = None,
        sample_rate: int = None,
        speech_rate: int = None,
        text: str = None,
        voice: str = None,
        volume: int = None,
    ):
        # appid
        self.app_id = app_id
        self.format = format
        self.pitch_rate = pitch_rate
        self.sample_rate = sample_rate
        self.speech_rate = speech_rate
        self.text = text
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.format is not None:
            result['Format'] = self.format
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class TtsCommonRequest(TeaModel):
    def __init__(
        self,
        tts_request: TtsCommonRequestTtsRequest = None,
    ):
        self.tts_request = tts_request

    def validate(self):
        if self.tts_request:
            self.tts_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tts_request is not None:
            result['TtsRequest'] = self.tts_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TtsRequest') is not None:
            temp_model = TtsCommonRequestTtsRequest()
            self.tts_request = temp_model.from_map(m['TtsRequest'])
        return self


class TtsCommonShrinkRequest(TeaModel):
    def __init__(
        self,
        tts_request_shrink: str = None,
    ):
        self.tts_request_shrink = tts_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tts_request_shrink is not None:
            result['TtsRequest'] = self.tts_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TtsRequest') is not None:
            self.tts_request_shrink = m.get('TtsRequest')
        return self


class TtsCommonResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        public_url: str = None,
        task_id: str = None,
    ):
        self.code = code
        self.id = id
        self.message = message
        self.name = name
        self.public_url = public_url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TtsCommonResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TtsCommonResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TtsCommonResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TtsCommonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TtsCommonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TtsCommonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TtsTaskRequestRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        room_id: str = None,
        timestamp: int = None,
    ):
        self.key = key
        self.room_id = room_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TtsTaskRequest(TeaModel):
    def __init__(
        self,
        request: TtsTaskRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = TtsTaskRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class TtsTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        request_shrink: str = None,
    ):
        self.request_shrink = request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        return self


class TtsTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        answer: str = None,
        duration: float = None,
        question: str = None,
        speech_rate: int = None,
    ):
        self.answer = answer
        self.duration = duration
        self.question = question
        self.speech_rate = speech_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.question is not None:
            result['Question'] = self.question
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        return self


class TtsTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TtsTaskResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TtsTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TtsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TtsTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TtsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        department_id: str = None,
        disabled: bool = None,
        id: str = None,
        name: str = None,
        package_name: str = None,
    ):
        self.department_id = department_id
        self.disabled = disabled
        self.id = id
        self.name = name
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDepartmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        label: str = None,
        name: str = None,
    ):
        self.description = description
        # ID
        self.id = id
        self.label = label
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDepartmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDepartmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDepartmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDepartmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDetectProcessRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        draft: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        self.draft = draft
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDetectProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        draft: str = None,
        id: str = None,
        md_5: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        self.draft = draft
        # ID
        self.id = id
        self.md_5 = md_5
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.draft is not None:
            result['Draft'] = self.draft
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDetectProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateDetectProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateDetectProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDetectProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDetectProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDetectProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
    ):
        self.content = content
        self.created_at = created_at
        # ID
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        id: str = None,
        name: str = None,
        phone_number: str = None,
        role: str = None,
    ):
        self.email = email
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWatermarkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        watermark_id: str = None,
    ):
        self.name = name
        self.value = value
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class UpdateWatermarkResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateWatermarkResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateWatermarkResponseBodyData = None,
        errors: List[UpdateWatermarkResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateWatermarkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = UpdateWatermarkResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadReportRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_base_param: str = None,
        client_version: str = None,
        department_id: str = None,
        detect_process_id: str = None,
        duration: int = None,
        fee_id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        result_url: str = None,
        role: str = None,
        room_id: str = None,
        rtc_record_id: str = None,
        type: str = None,
        user_id: str = None,
        video_type: str = None,
        video_url: str = None,
    ):
        self.app_id = app_id
        self.client_base_param = client_base_param
        self.client_version = client_version
        self.department_id = department_id
        self.detect_process_id = detect_process_id
        self.duration = duration
        self.fee_id = fee_id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.result_url = result_url
        self.role = role
        self.room_id = room_id
        self.rtc_record_id = rtc_record_id
        self.type = type
        self.user_id = user_id
        self.video_type = video_type
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_base_param is not None:
            result['ClientBaseParam'] = self.client_base_param
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.detect_process_id is not None:
            result['DetectProcessId'] = self.detect_process_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fee_id is not None:
            result['FeeId'] = self.fee_id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.role is not None:
            result['Role'] = self.role
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.video_type is not None:
            result['VideoType'] = self.video_type
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientBaseParam') is not None:
            self.client_base_param = m.get('ClientBaseParam')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('DetectProcessId') is not None:
            self.detect_process_id = m.get('DetectProcessId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FeeId') is not None:
            self.fee_id = m.get('FeeId')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VideoType') is not None:
            self.video_type = m.get('VideoType')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class UploadReportResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        duration: int = None,
        id: str = None,
        meta_url: str = None,
        outer_business_id: str = None,
        record_at: str = None,
        result_url: str = None,
        rtc_record_id: str = None,
        video_url: str = None,
    ):
        self.created_at = created_at
        self.duration = duration
        self.id = id
        self.meta_url = meta_url
        self.outer_business_id = outer_business_id
        self.record_at = record_at
        self.result_url = result_url
        self.rtc_record_id = rtc_record_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.outer_business_id is not None:
            result['OuterBusinessId'] = self.outer_business_id
        if self.record_at is not None:
            result['RecordAt'] = self.record_at
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.rtc_record_id is not None:
            result['RtcRecordId'] = self.rtc_record_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('OuterBusinessId') is not None:
            self.outer_business_id = m.get('OuterBusinessId')
        if m.get('RecordAt') is not None:
            self.record_at = m.get('RecordAt')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('RtcRecordId') is not None:
            self.rtc_record_id = m.get('RtcRecordId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class UploadReportResponseBodyErrors(TeaModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
    ):
        self.field = field
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UploadReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadReportResponseBodyData = None,
        errors: List[UploadReportResponseBodyErrors] = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.errors = errors
        self.http_code = http_code
        self.message = message
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UploadReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = UploadReportResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


