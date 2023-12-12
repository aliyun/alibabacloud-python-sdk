# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateTaskRequestInput(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        format: str = None,
        progressive_callbacks_enabled: bool = None,
        sample_rate: int = None,
        source_language: str = None,
        task_id: str = None,
        task_key: str = None,
    ):
        self.file_url = file_url
        self.format = format
        self.progressive_callbacks_enabled = progressive_callbacks_enabled
        self.sample_rate = sample_rate
        self.source_language = source_language
        self.task_id = task_id
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format is not None:
            result['Format'] = self.format
        if self.progressive_callbacks_enabled is not None:
            result['ProgressiveCallbacksEnabled'] = self.progressive_callbacks_enabled
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_key is not None:
            result['TaskKey'] = self.task_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('ProgressiveCallbacksEnabled') is not None:
            self.progressive_callbacks_enabled = m.get('ProgressiveCallbacksEnabled')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')
        return self


class CreateTaskRequestParametersSummarization(TeaModel):
    def __init__(
        self,
        types: Dict[str, Any] = None,
    ):
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class CreateTaskRequestParametersTranscoding(TeaModel):
    def __init__(
        self,
        spectrum_enabled: bool = None,
        target_audio_format: str = None,
        target_video_format: str = None,
        video_thumbnail_enabled: bool = None,
    ):
        self.spectrum_enabled = spectrum_enabled
        self.target_audio_format = target_audio_format
        self.target_video_format = target_video_format
        self.video_thumbnail_enabled = video_thumbnail_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spectrum_enabled is not None:
            result['SpectrumEnabled'] = self.spectrum_enabled
        if self.target_audio_format is not None:
            result['TargetAudioFormat'] = self.target_audio_format
        if self.target_video_format is not None:
            result['TargetVideoFormat'] = self.target_video_format
        if self.video_thumbnail_enabled is not None:
            result['VideoThumbnailEnabled'] = self.video_thumbnail_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpectrumEnabled') is not None:
            self.spectrum_enabled = m.get('SpectrumEnabled')
        if m.get('TargetAudioFormat') is not None:
            self.target_audio_format = m.get('TargetAudioFormat')
        if m.get('TargetVideoFormat') is not None:
            self.target_video_format = m.get('TargetVideoFormat')
        if m.get('VideoThumbnailEnabled') is not None:
            self.video_thumbnail_enabled = m.get('VideoThumbnailEnabled')
        return self


class CreateTaskRequestParametersTranscriptionDiarization(TeaModel):
    def __init__(
        self,
        speaker_count: int = None,
    ):
        self.speaker_count = speaker_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.speaker_count is not None:
            result['SpeakerCount'] = self.speaker_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpeakerCount') is not None:
            self.speaker_count = m.get('SpeakerCount')
        return self


class CreateTaskRequestParametersTranscription(TeaModel):
    def __init__(
        self,
        audio_event_detection_enabled: bool = None,
        diarization: CreateTaskRequestParametersTranscriptionDiarization = None,
        diarization_enabled: bool = None,
        output_level: int = None,
        phrase_id: str = None,
    ):
        self.audio_event_detection_enabled = audio_event_detection_enabled
        self.diarization = diarization
        self.diarization_enabled = diarization_enabled
        self.output_level = output_level
        self.phrase_id = phrase_id

    def validate(self):
        if self.diarization:
            self.diarization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_event_detection_enabled is not None:
            result['AudioEventDetectionEnabled'] = self.audio_event_detection_enabled
        if self.diarization is not None:
            result['Diarization'] = self.diarization.to_map()
        if self.diarization_enabled is not None:
            result['DiarizationEnabled'] = self.diarization_enabled
        if self.output_level is not None:
            result['OutputLevel'] = self.output_level
        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioEventDetectionEnabled') is not None:
            self.audio_event_detection_enabled = m.get('AudioEventDetectionEnabled')
        if m.get('Diarization') is not None:
            temp_model = CreateTaskRequestParametersTranscriptionDiarization()
            self.diarization = temp_model.from_map(m['Diarization'])
        if m.get('DiarizationEnabled') is not None:
            self.diarization_enabled = m.get('DiarizationEnabled')
        if m.get('OutputLevel') is not None:
            self.output_level = m.get('OutputLevel')
        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')
        return self


class CreateTaskRequestParametersTranslation(TeaModel):
    def __init__(
        self,
        output_level: int = None,
        target_languages: Dict[str, Any] = None,
    ):
        self.output_level = output_level
        self.target_languages = target_languages

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_level is not None:
            result['OutputLevel'] = self.output_level
        if self.target_languages is not None:
            result['TargetLanguages'] = self.target_languages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputLevel') is not None:
            self.output_level = m.get('OutputLevel')
        if m.get('TargetLanguages') is not None:
            self.target_languages = m.get('TargetLanguages')
        return self


class CreateTaskRequestParameters(TeaModel):
    def __init__(
        self,
        auto_chapters_enabled: bool = None,
        meeting_assistance_enabled: bool = None,
        ppt_extraction_enabled: bool = None,
        summarization: CreateTaskRequestParametersSummarization = None,
        summarization_enabled: bool = None,
        transcoding: CreateTaskRequestParametersTranscoding = None,
        transcription: CreateTaskRequestParametersTranscription = None,
        translation: CreateTaskRequestParametersTranslation = None,
        translation_enabled: bool = None,
    ):
        self.auto_chapters_enabled = auto_chapters_enabled
        self.meeting_assistance_enabled = meeting_assistance_enabled
        self.ppt_extraction_enabled = ppt_extraction_enabled
        self.summarization = summarization
        self.summarization_enabled = summarization_enabled
        self.transcoding = transcoding
        self.transcription = transcription
        self.translation = translation
        self.translation_enabled = translation_enabled

    def validate(self):
        if self.summarization:
            self.summarization.validate()
        if self.transcoding:
            self.transcoding.validate()
        if self.transcription:
            self.transcription.validate()
        if self.translation:
            self.translation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_chapters_enabled is not None:
            result['AutoChaptersEnabled'] = self.auto_chapters_enabled
        if self.meeting_assistance_enabled is not None:
            result['MeetingAssistanceEnabled'] = self.meeting_assistance_enabled
        if self.ppt_extraction_enabled is not None:
            result['PptExtractionEnabled'] = self.ppt_extraction_enabled
        if self.summarization is not None:
            result['Summarization'] = self.summarization.to_map()
        if self.summarization_enabled is not None:
            result['SummarizationEnabled'] = self.summarization_enabled
        if self.transcoding is not None:
            result['Transcoding'] = self.transcoding.to_map()
        if self.transcription is not None:
            result['Transcription'] = self.transcription.to_map()
        if self.translation is not None:
            result['Translation'] = self.translation.to_map()
        if self.translation_enabled is not None:
            result['TranslationEnabled'] = self.translation_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoChaptersEnabled') is not None:
            self.auto_chapters_enabled = m.get('AutoChaptersEnabled')
        if m.get('MeetingAssistanceEnabled') is not None:
            self.meeting_assistance_enabled = m.get('MeetingAssistanceEnabled')
        if m.get('PptExtractionEnabled') is not None:
            self.ppt_extraction_enabled = m.get('PptExtractionEnabled')
        if m.get('Summarization') is not None:
            temp_model = CreateTaskRequestParametersSummarization()
            self.summarization = temp_model.from_map(m['Summarization'])
        if m.get('SummarizationEnabled') is not None:
            self.summarization_enabled = m.get('SummarizationEnabled')
        if m.get('Transcoding') is not None:
            temp_model = CreateTaskRequestParametersTranscoding()
            self.transcoding = temp_model.from_map(m['Transcoding'])
        if m.get('Transcription') is not None:
            temp_model = CreateTaskRequestParametersTranscription()
            self.transcription = temp_model.from_map(m['Transcription'])
        if m.get('Translation') is not None:
            temp_model = CreateTaskRequestParametersTranslation()
            self.translation = temp_model.from_map(m['Translation'])
        if m.get('TranslationEnabled') is not None:
            self.translation_enabled = m.get('TranslationEnabled')
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        input: CreateTaskRequestInput = None,
        parameters: CreateTaskRequestParameters = None,
        operation: str = None,
        type: str = None,
    ):
        self.app_key = app_key
        self.input = input
        self.parameters = parameters
        self.operation = operation
        self.type = type

    def validate(self):
        if self.input:
            self.input.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.operation is not None:
            result['operation'] = self.operation
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Input') is not None:
            temp_model = CreateTaskRequestInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Parameters') is not None:
            temp_model = CreateTaskRequestParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_key: str = None,
    ):
        self.task_id = task_id
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_key is not None:
            result['TaskKey'] = self.task_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTaskResponseBodyData = None,
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
            temp_model = CreateTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTranscriptionPhrasesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        word_weights: str = None,
    ):
        self.description = description
        self.name = name
        self.word_weights = word_weights

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.word_weights is not None:
            result['WordWeights'] = self.word_weights
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WordWeights') is not None:
            self.word_weights = m.get('WordWeights')
        return self


class CreateTranscriptionPhrasesResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        phrase_id: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.phrase_id = phrase_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateTranscriptionPhrasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTranscriptionPhrasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = CreateTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTranscriptionPhrasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTranscriptionPhrasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTranscriptionPhrasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTranscriptionPhrasesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteTranscriptionPhrasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTranscriptionPhrasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTranscriptionPhrasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_key: str = None,
        task_status: str = None,
    ):
        self.task_id = task_id
        self.task_key = task_key
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_key is not None:
            result['TaskKey'] = self.task_key
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTaskInfoResponseBodyData = None,
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
            temp_model = GetTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscriptionPhrasesResponseBodyDataPhrases(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        phrase_id: str = None,
        word_weights: str = None,
    ):
        self.description = description
        self.name = name
        self.phrase_id = phrase_id
        self.word_weights = word_weights

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id
        if self.word_weights is not None:
            result['WordWeights'] = self.word_weights
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')
        if m.get('WordWeights') is not None:
            self.word_weights = m.get('WordWeights')
        return self


class GetTranscriptionPhrasesResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        phrases: List[GetTranscriptionPhrasesResponseBodyDataPhrases] = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.phrases = phrases
        self.status = status

    def validate(self):
        if self.phrases:
            for k in self.phrases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Phrases'] = []
        if self.phrases is not None:
            for k in self.phrases:
                result['Phrases'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.phrases = []
        if m.get('Phrases') is not None:
            for k in m.get('Phrases'):
                temp_model = GetTranscriptionPhrasesResponseBodyDataPhrases()
                self.phrases.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTranscriptionPhrasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTranscriptionPhrasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = GetTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTranscriptionPhrasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTranscriptionPhrasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTranscriptionPhrasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTranscriptionPhrasesResponseBodyDataPhrases(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        phrase_id: str = None,
    ):
        self.description = description
        self.name = name
        self.phrase_id = phrase_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')
        return self


class ListTranscriptionPhrasesResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        phrases: List[ListTranscriptionPhrasesResponseBodyDataPhrases] = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.phrases = phrases
        self.status = status

    def validate(self):
        if self.phrases:
            for k in self.phrases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Phrases'] = []
        if self.phrases is not None:
            for k in self.phrases:
                result['Phrases'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.phrases = []
        if m.get('Phrases') is not None:
            for k in m.get('Phrases'):
                temp_model = ListTranscriptionPhrasesResponseBodyDataPhrases()
                self.phrases.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTranscriptionPhrasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListTranscriptionPhrasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = ListTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTranscriptionPhrasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTranscriptionPhrasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTranscriptionPhrasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTranscriptionPhrasesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        word_weights: str = None,
    ):
        self.description = description
        self.name = name
        self.word_weights = word_weights

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.word_weights is not None:
            result['WordWeights'] = self.word_weights
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WordWeights') is not None:
            self.word_weights = m.get('WordWeights')
        return self


class UpdateTranscriptionPhrasesResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateTranscriptionPhrasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateTranscriptionPhrasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = UpdateTranscriptionPhrasesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTranscriptionPhrasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTranscriptionPhrasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTranscriptionPhrasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


