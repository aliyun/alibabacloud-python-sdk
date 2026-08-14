# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tingwu20230930 import models as main_models
from darabonba.model import DaraModel

class GetTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # Returned object.
        self.data = data
        # Status description.
        self.message = message
        # Request ID, used only for joint debugging.
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
            temp_model = main_models.GetTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTaskInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        output_mp_3path: str = None,
        output_mp_4path: str = None,
        output_spectrum_path: str = None,
        output_thumbnail_path: str = None,
        result: main_models.GetTaskInfoResponseBodyDataResult = None,
        task_id: str = None,
        task_key: str = None,
        task_status: str = None,
    ):
        # Error code
        self.error_code = error_code
        # Error message
        self.error_message = error_message
        # URL link to the MP3 conversion result
        self.output_mp_3path = output_mp_3path
        # URL link to the MP4 conversion result
        self.output_mp_4path = output_mp_4path
        # URL link to the audio waveform graph
        self.output_spectrum_path = output_spectrum_path
        # URL link to the video thumbnail
        self.output_thumbnail_path = output_thumbnail_path
        # A collection of results from various algorithm processing tasks. The result is returned as an HTTP link, which the user can use to parse the native result.
        self.result = result
        # Job ID.
        self.task_id = task_id
        # The custom ID set by the user when creating the job.
        self.task_key = task_key
        # Task Status.
        # 
        # - ONGOING: The job is in progress.
        # - COMPLETED: The job is completed.
        # - FAILED: The job has failed.
        # - INVALID: The job is invalid.
        self.task_status = task_status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.output_mp_3path is not None:
            result['OutputMp3Path'] = self.output_mp_3path

        if self.output_mp_4path is not None:
            result['OutputMp4Path'] = self.output_mp_4path

        if self.output_spectrum_path is not None:
            result['OutputSpectrumPath'] = self.output_spectrum_path

        if self.output_thumbnail_path is not None:
            result['OutputThumbnailPath'] = self.output_thumbnail_path

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OutputMp3Path') is not None:
            self.output_mp_3path = m.get('OutputMp3Path')

        if m.get('OutputMp4Path') is not None:
            self.output_mp_4path = m.get('OutputMp4Path')

        if m.get('OutputSpectrumPath') is not None:
            self.output_spectrum_path = m.get('OutputSpectrumPath')

        if m.get('OutputThumbnailPath') is not None:
            self.output_thumbnail_path = m.get('OutputThumbnailPath')

        if m.get('Result') is not None:
            temp_model = main_models.GetTaskInfoResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class GetTaskInfoResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        auto_chapters: str = None,
        content_extraction: str = None,
        custom_prompt: str = None,
        identity_recognition: str = None,
        meeting_assistance: str = None,
        ppt_extraction: str = None,
        service_inspection: str = None,
        summarization: str = None,
        text_polish: str = None,
        transcription: str = None,
        translation: str = None,
    ):
        # Link to the result of the Auto Chapters feature.
        self.auto_chapters = auto_chapters
        # URL link to the result of conversation content extraction
        self.content_extraction = content_extraction
        # Link to the result of the Custom prompt
        self.custom_prompt = custom_prompt
        # The URL link to the identity recognition result.
        self.identity_recognition = identity_recognition
        # URL link to the result of Intelligent Meeting Summary
        self.meeting_assistance = meeting_assistance
        # URL link to the result of video PPT extraction and summarization
        self.ppt_extraction = ppt_extraction
        # Link to the result of service inspection
        self.service_inspection = service_inspection
        # Link to the result of LLM-based summarization.
        self.summarization = summarization
        # Link to the result of spoken-to-written text conversion
        self.text_polish = text_polish
        # Link to the result of speech transcription.
        self.transcription = transcription
        # URL link to the result of text translation
        self.translation = translation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_chapters is not None:
            result['AutoChapters'] = self.auto_chapters

        if self.content_extraction is not None:
            result['ContentExtraction'] = self.content_extraction

        if self.custom_prompt is not None:
            result['CustomPrompt'] = self.custom_prompt

        if self.identity_recognition is not None:
            result['IdentityRecognition'] = self.identity_recognition

        if self.meeting_assistance is not None:
            result['MeetingAssistance'] = self.meeting_assistance

        if self.ppt_extraction is not None:
            result['PptExtraction'] = self.ppt_extraction

        if self.service_inspection is not None:
            result['ServiceInspection'] = self.service_inspection

        if self.summarization is not None:
            result['Summarization'] = self.summarization

        if self.text_polish is not None:
            result['TextPolish'] = self.text_polish

        if self.transcription is not None:
            result['Transcription'] = self.transcription

        if self.translation is not None:
            result['Translation'] = self.translation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoChapters') is not None:
            self.auto_chapters = m.get('AutoChapters')

        if m.get('ContentExtraction') is not None:
            self.content_extraction = m.get('ContentExtraction')

        if m.get('CustomPrompt') is not None:
            self.custom_prompt = m.get('CustomPrompt')

        if m.get('IdentityRecognition') is not None:
            self.identity_recognition = m.get('IdentityRecognition')

        if m.get('MeetingAssistance') is not None:
            self.meeting_assistance = m.get('MeetingAssistance')

        if m.get('PptExtraction') is not None:
            self.ppt_extraction = m.get('PptExtraction')

        if m.get('ServiceInspection') is not None:
            self.service_inspection = m.get('ServiceInspection')

        if m.get('Summarization') is not None:
            self.summarization = m.get('Summarization')

        if m.get('TextPolish') is not None:
            self.text_polish = m.get('TextPolish')

        if m.get('Transcription') is not None:
            self.transcription = m.get('Transcription')

        if m.get('Translation') is not None:
            self.translation = m.get('Translation')

        return self

