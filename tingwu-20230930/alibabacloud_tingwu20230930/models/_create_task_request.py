# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_tingwu20230930 import models as main_models
from darabonba.model import DaraModel

class CreateTaskRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        input: main_models.CreateTaskRequestInput = None,
        parameters: main_models.CreateTaskRequestParameters = None,
        operation: str = None,
        type: str = None,
    ):
        self.app_key = app_key
        self.input = input
        self.parameters = parameters
        self.operation = operation
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.input:
            self.input.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CreateTaskRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Parameters') is not None:
            temp_model = main_models.CreateTaskRequestParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateTaskRequestParameters(DaraModel):
    def __init__(
        self,
        auto_chapters: main_models.CreateTaskRequestParametersAutoChapters = None,
        auto_chapters_enabled: bool = None,
        content_extraction: main_models.CreateTaskRequestParametersContentExtraction = None,
        content_extraction_enabled: bool = None,
        custom_prompt: main_models.CreateTaskRequestParametersCustomPrompt = None,
        custom_prompt_enabled: bool = None,
        extra_params: main_models.CreateTaskRequestParametersExtraParams = None,
        identity_recognition: main_models.CreateTaskRequestParametersIdentityRecognition = None,
        identity_recognition_enabled: bool = None,
        llm_output_language: str = None,
        meeting_assistance: main_models.CreateTaskRequestParametersMeetingAssistance = None,
        meeting_assistance_enabled: bool = None,
        model: str = None,
        ppt_extraction_enabled: bool = None,
        service_inspection: main_models.CreateTaskRequestParametersServiceInspection = None,
        service_inspection_enabled: bool = None,
        summarization: main_models.CreateTaskRequestParametersSummarization = None,
        summarization_enabled: bool = None,
        text_polish_enabled: bool = None,
        transcoding: main_models.CreateTaskRequestParametersTranscoding = None,
        transcription: main_models.CreateTaskRequestParametersTranscription = None,
        translation: main_models.CreateTaskRequestParametersTranslation = None,
        translation_enabled: bool = None,
    ):
        self.auto_chapters = auto_chapters
        self.auto_chapters_enabled = auto_chapters_enabled
        self.content_extraction = content_extraction
        self.content_extraction_enabled = content_extraction_enabled
        self.custom_prompt = custom_prompt
        self.custom_prompt_enabled = custom_prompt_enabled
        self.extra_params = extra_params
        self.identity_recognition = identity_recognition
        self.identity_recognition_enabled = identity_recognition_enabled
        self.llm_output_language = llm_output_language
        self.meeting_assistance = meeting_assistance
        self.meeting_assistance_enabled = meeting_assistance_enabled
        self.model = model
        self.ppt_extraction_enabled = ppt_extraction_enabled
        self.service_inspection = service_inspection
        self.service_inspection_enabled = service_inspection_enabled
        self.summarization = summarization
        self.summarization_enabled = summarization_enabled
        self.text_polish_enabled = text_polish_enabled
        self.transcoding = transcoding
        self.transcription = transcription
        self.translation = translation
        self.translation_enabled = translation_enabled

    def validate(self):
        if self.auto_chapters:
            self.auto_chapters.validate()
        if self.content_extraction:
            self.content_extraction.validate()
        if self.custom_prompt:
            self.custom_prompt.validate()
        if self.extra_params:
            self.extra_params.validate()
        if self.identity_recognition:
            self.identity_recognition.validate()
        if self.meeting_assistance:
            self.meeting_assistance.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.summarization:
            self.summarization.validate()
        if self.transcoding:
            self.transcoding.validate()
        if self.transcription:
            self.transcription.validate()
        if self.translation:
            self.translation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_chapters is not None:
            result['AutoChapters'] = self.auto_chapters.to_map()

        if self.auto_chapters_enabled is not None:
            result['AutoChaptersEnabled'] = self.auto_chapters_enabled

        if self.content_extraction is not None:
            result['ContentExtraction'] = self.content_extraction.to_map()

        if self.content_extraction_enabled is not None:
            result['ContentExtractionEnabled'] = self.content_extraction_enabled

        if self.custom_prompt is not None:
            result['CustomPrompt'] = self.custom_prompt.to_map()

        if self.custom_prompt_enabled is not None:
            result['CustomPromptEnabled'] = self.custom_prompt_enabled

        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params.to_map()

        if self.identity_recognition is not None:
            result['IdentityRecognition'] = self.identity_recognition.to_map()

        if self.identity_recognition_enabled is not None:
            result['IdentityRecognitionEnabled'] = self.identity_recognition_enabled

        if self.llm_output_language is not None:
            result['LlmOutputLanguage'] = self.llm_output_language

        if self.meeting_assistance is not None:
            result['MeetingAssistance'] = self.meeting_assistance.to_map()

        if self.meeting_assistance_enabled is not None:
            result['MeetingAssistanceEnabled'] = self.meeting_assistance_enabled

        if self.model is not None:
            result['Model'] = self.model

        if self.ppt_extraction_enabled is not None:
            result['PptExtractionEnabled'] = self.ppt_extraction_enabled

        if self.service_inspection is not None:
            result['ServiceInspection'] = self.service_inspection.to_map()

        if self.service_inspection_enabled is not None:
            result['ServiceInspectionEnabled'] = self.service_inspection_enabled

        if self.summarization is not None:
            result['Summarization'] = self.summarization.to_map()

        if self.summarization_enabled is not None:
            result['SummarizationEnabled'] = self.summarization_enabled

        if self.text_polish_enabled is not None:
            result['TextPolishEnabled'] = self.text_polish_enabled

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
        if m.get('AutoChapters') is not None:
            temp_model = main_models.CreateTaskRequestParametersAutoChapters()
            self.auto_chapters = temp_model.from_map(m.get('AutoChapters'))

        if m.get('AutoChaptersEnabled') is not None:
            self.auto_chapters_enabled = m.get('AutoChaptersEnabled')

        if m.get('ContentExtraction') is not None:
            temp_model = main_models.CreateTaskRequestParametersContentExtraction()
            self.content_extraction = temp_model.from_map(m.get('ContentExtraction'))

        if m.get('ContentExtractionEnabled') is not None:
            self.content_extraction_enabled = m.get('ContentExtractionEnabled')

        if m.get('CustomPrompt') is not None:
            temp_model = main_models.CreateTaskRequestParametersCustomPrompt()
            self.custom_prompt = temp_model.from_map(m.get('CustomPrompt'))

        if m.get('CustomPromptEnabled') is not None:
            self.custom_prompt_enabled = m.get('CustomPromptEnabled')

        if m.get('ExtraParams') is not None:
            temp_model = main_models.CreateTaskRequestParametersExtraParams()
            self.extra_params = temp_model.from_map(m.get('ExtraParams'))

        if m.get('IdentityRecognition') is not None:
            temp_model = main_models.CreateTaskRequestParametersIdentityRecognition()
            self.identity_recognition = temp_model.from_map(m.get('IdentityRecognition'))

        if m.get('IdentityRecognitionEnabled') is not None:
            self.identity_recognition_enabled = m.get('IdentityRecognitionEnabled')

        if m.get('LlmOutputLanguage') is not None:
            self.llm_output_language = m.get('LlmOutputLanguage')

        if m.get('MeetingAssistance') is not None:
            temp_model = main_models.CreateTaskRequestParametersMeetingAssistance()
            self.meeting_assistance = temp_model.from_map(m.get('MeetingAssistance'))

        if m.get('MeetingAssistanceEnabled') is not None:
            self.meeting_assistance_enabled = m.get('MeetingAssistanceEnabled')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PptExtractionEnabled') is not None:
            self.ppt_extraction_enabled = m.get('PptExtractionEnabled')

        if m.get('ServiceInspection') is not None:
            temp_model = main_models.CreateTaskRequestParametersServiceInspection()
            self.service_inspection = temp_model.from_map(m.get('ServiceInspection'))

        if m.get('ServiceInspectionEnabled') is not None:
            self.service_inspection_enabled = m.get('ServiceInspectionEnabled')

        if m.get('Summarization') is not None:
            temp_model = main_models.CreateTaskRequestParametersSummarization()
            self.summarization = temp_model.from_map(m.get('Summarization'))

        if m.get('SummarizationEnabled') is not None:
            self.summarization_enabled = m.get('SummarizationEnabled')

        if m.get('TextPolishEnabled') is not None:
            self.text_polish_enabled = m.get('TextPolishEnabled')

        if m.get('Transcoding') is not None:
            temp_model = main_models.CreateTaskRequestParametersTranscoding()
            self.transcoding = temp_model.from_map(m.get('Transcoding'))

        if m.get('Transcription') is not None:
            temp_model = main_models.CreateTaskRequestParametersTranscription()
            self.transcription = temp_model.from_map(m.get('Transcription'))

        if m.get('Translation') is not None:
            temp_model = main_models.CreateTaskRequestParametersTranslation()
            self.translation = temp_model.from_map(m.get('Translation'))

        if m.get('TranslationEnabled') is not None:
            self.translation_enabled = m.get('TranslationEnabled')

        return self

class CreateTaskRequestParametersTranslation(DaraModel):
    def __init__(
        self,
        additional_stream_output_level: int = None,
        output_level: int = None,
        target_languages: List[str] = None,
    ):
        self.additional_stream_output_level = additional_stream_output_level
        self.output_level = output_level
        self.target_languages = target_languages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_stream_output_level is not None:
            result['AdditionalStreamOutputLevel'] = self.additional_stream_output_level

        if self.output_level is not None:
            result['OutputLevel'] = self.output_level

        if self.target_languages is not None:
            result['TargetLanguages'] = self.target_languages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalStreamOutputLevel') is not None:
            self.additional_stream_output_level = m.get('AdditionalStreamOutputLevel')

        if m.get('OutputLevel') is not None:
            self.output_level = m.get('OutputLevel')

        if m.get('TargetLanguages') is not None:
            self.target_languages = m.get('TargetLanguages')

        return self

class CreateTaskRequestParametersTranscription(DaraModel):
    def __init__(
        self,
        additional_stream_output_level: int = None,
        audio_event_detection_enabled: bool = None,
        diarization: main_models.CreateTaskRequestParametersTranscriptionDiarization = None,
        diarization_enabled: bool = None,
        model: str = None,
        output_level: int = None,
        phrase_id: str = None,
        profanity_filter_enabled: bool = None,
        realtime_diarization_enabled: bool = None,
    ):
        self.additional_stream_output_level = additional_stream_output_level
        self.audio_event_detection_enabled = audio_event_detection_enabled
        self.diarization = diarization
        self.diarization_enabled = diarization_enabled
        self.model = model
        self.output_level = output_level
        self.phrase_id = phrase_id
        self.profanity_filter_enabled = profanity_filter_enabled
        self.realtime_diarization_enabled = realtime_diarization_enabled

    def validate(self):
        if self.diarization:
            self.diarization.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_stream_output_level is not None:
            result['AdditionalStreamOutputLevel'] = self.additional_stream_output_level

        if self.audio_event_detection_enabled is not None:
            result['AudioEventDetectionEnabled'] = self.audio_event_detection_enabled

        if self.diarization is not None:
            result['Diarization'] = self.diarization.to_map()

        if self.diarization_enabled is not None:
            result['DiarizationEnabled'] = self.diarization_enabled

        if self.model is not None:
            result['Model'] = self.model

        if self.output_level is not None:
            result['OutputLevel'] = self.output_level

        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id

        if self.profanity_filter_enabled is not None:
            result['ProfanityFilterEnabled'] = self.profanity_filter_enabled

        if self.realtime_diarization_enabled is not None:
            result['RealtimeDiarizationEnabled'] = self.realtime_diarization_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalStreamOutputLevel') is not None:
            self.additional_stream_output_level = m.get('AdditionalStreamOutputLevel')

        if m.get('AudioEventDetectionEnabled') is not None:
            self.audio_event_detection_enabled = m.get('AudioEventDetectionEnabled')

        if m.get('Diarization') is not None:
            temp_model = main_models.CreateTaskRequestParametersTranscriptionDiarization()
            self.diarization = temp_model.from_map(m.get('Diarization'))

        if m.get('DiarizationEnabled') is not None:
            self.diarization_enabled = m.get('DiarizationEnabled')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OutputLevel') is not None:
            self.output_level = m.get('OutputLevel')

        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')

        if m.get('ProfanityFilterEnabled') is not None:
            self.profanity_filter_enabled = m.get('ProfanityFilterEnabled')

        if m.get('RealtimeDiarizationEnabled') is not None:
            self.realtime_diarization_enabled = m.get('RealtimeDiarizationEnabled')

        return self

class CreateTaskRequestParametersTranscriptionDiarization(DaraModel):
    def __init__(
        self,
        speaker_count: int = None,
    ):
        self.speaker_count = speaker_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.speaker_count is not None:
            result['SpeakerCount'] = self.speaker_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpeakerCount') is not None:
            self.speaker_count = m.get('SpeakerCount')

        return self

class CreateTaskRequestParametersTranscoding(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateTaskRequestParametersSummarization(DaraModel):
    def __init__(
        self,
        types: List[str] = None,
    ):
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

class CreateTaskRequestParametersServiceInspection(DaraModel):
    def __init__(
        self,
        inspection_contents: List[main_models.CreateTaskRequestParametersServiceInspectionInspectionContents] = None,
        inspection_introduction: str = None,
        scene_introduction: str = None,
        speaker_map: Dict[str, Any] = None,
    ):
        self.inspection_contents = inspection_contents
        self.inspection_introduction = inspection_introduction
        self.scene_introduction = scene_introduction
        self.speaker_map = speaker_map

    def validate(self):
        if self.inspection_contents:
            for v1 in self.inspection_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InspectionContents'] = []
        if self.inspection_contents is not None:
            for k1 in self.inspection_contents:
                result['InspectionContents'].append(k1.to_map() if k1 else None)

        if self.inspection_introduction is not None:
            result['InspectionIntroduction'] = self.inspection_introduction

        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction

        if self.speaker_map is not None:
            result['SpeakerMap'] = self.speaker_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('InspectionContents') is not None:
            for k1 in m.get('InspectionContents'):
                temp_model = main_models.CreateTaskRequestParametersServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k1))

        if m.get('InspectionIntroduction') is not None:
            self.inspection_introduction = m.get('InspectionIntroduction')

        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')

        if m.get('SpeakerMap') is not None:
            self.speaker_map = m.get('SpeakerMap')

        return self

class CreateTaskRequestParametersServiceInspectionInspectionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CreateTaskRequestParametersMeetingAssistance(DaraModel):
    def __init__(
        self,
        types: List[str] = None,
    ):
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

class CreateTaskRequestParametersIdentityRecognition(DaraModel):
    def __init__(
        self,
        identity_contents: List[main_models.CreateTaskRequestParametersIdentityRecognitionIdentityContents] = None,
        scene_introduction: str = None,
    ):
        self.identity_contents = identity_contents
        self.scene_introduction = scene_introduction

    def validate(self):
        if self.identity_contents:
            for v1 in self.identity_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdentityContents'] = []
        if self.identity_contents is not None:
            for k1 in self.identity_contents:
                result['IdentityContents'].append(k1.to_map() if k1 else None)

        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.identity_contents = []
        if m.get('IdentityContents') is not None:
            for k1 in m.get('IdentityContents'):
                temp_model = main_models.CreateTaskRequestParametersIdentityRecognitionIdentityContents()
                self.identity_contents.append(temp_model.from_map(k1))

        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')

        return self

class CreateTaskRequestParametersIdentityRecognitionIdentityContents(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateTaskRequestParametersExtraParams(DaraModel):
    def __init__(
        self,
        domain_education_enabled: bool = None,
        full_text_summary_format: str = None,
        max_keywords: int = None,
        nfix_enabled: bool = None,
        ocr_auxiliary_enabled: bool = None,
        translate_llm_scene_enabled: bool = None,
        translation_hotword_map: main_models.CreateTaskRequestParametersExtraParamsTranslationHotwordMap = None,
    ):
        self.domain_education_enabled = domain_education_enabled
        self.full_text_summary_format = full_text_summary_format
        self.max_keywords = max_keywords
        self.nfix_enabled = nfix_enabled
        self.ocr_auxiliary_enabled = ocr_auxiliary_enabled
        self.translate_llm_scene_enabled = translate_llm_scene_enabled
        self.translation_hotword_map = translation_hotword_map

    def validate(self):
        if self.translation_hotword_map:
            self.translation_hotword_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_education_enabled is not None:
            result['DomainEducationEnabled'] = self.domain_education_enabled

        if self.full_text_summary_format is not None:
            result['FullTextSummaryFormat'] = self.full_text_summary_format

        if self.max_keywords is not None:
            result['MaxKeywords'] = self.max_keywords

        if self.nfix_enabled is not None:
            result['NfixEnabled'] = self.nfix_enabled

        if self.ocr_auxiliary_enabled is not None:
            result['OcrAuxiliaryEnabled'] = self.ocr_auxiliary_enabled

        if self.translate_llm_scene_enabled is not None:
            result['TranslateLlmSceneEnabled'] = self.translate_llm_scene_enabled

        if self.translation_hotword_map is not None:
            result['TranslationHotwordMap'] = self.translation_hotword_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainEducationEnabled') is not None:
            self.domain_education_enabled = m.get('DomainEducationEnabled')

        if m.get('FullTextSummaryFormat') is not None:
            self.full_text_summary_format = m.get('FullTextSummaryFormat')

        if m.get('MaxKeywords') is not None:
            self.max_keywords = m.get('MaxKeywords')

        if m.get('NfixEnabled') is not None:
            self.nfix_enabled = m.get('NfixEnabled')

        if m.get('OcrAuxiliaryEnabled') is not None:
            self.ocr_auxiliary_enabled = m.get('OcrAuxiliaryEnabled')

        if m.get('TranslateLlmSceneEnabled') is not None:
            self.translate_llm_scene_enabled = m.get('TranslateLlmSceneEnabled')

        if m.get('TranslationHotwordMap') is not None:
            temp_model = main_models.CreateTaskRequestParametersExtraParamsTranslationHotwordMap()
            self.translation_hotword_map = temp_model.from_map(m.get('TranslationHotwordMap'))

        return self

class CreateTaskRequestParametersExtraParamsTranslationHotwordMap(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_user_id: str = None,
    ):
        self.biz_type = biz_type
        self.biz_user_id = biz_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.biz_user_id is not None:
            result['bizUserId'] = self.biz_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('bizUserId') is not None:
            self.biz_user_id = m.get('bizUserId')

        return self

class CreateTaskRequestParametersCustomPrompt(DaraModel):
    def __init__(
        self,
        contents: List[main_models.CreateTaskRequestParametersCustomPromptContents] = None,
    ):
        self.contents = contents

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.CreateTaskRequestParametersCustomPromptContents()
                self.contents.append(temp_model.from_map(k1))

        return self

class CreateTaskRequestParametersCustomPromptContents(DaraModel):
    def __init__(
        self,
        model: str = None,
        name: str = None,
        prompt: str = None,
        trans_type: str = None,
    ):
        self.model = model
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.prompt = prompt
        self.trans_type = trans_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.trans_type is not None:
            result['TransType'] = self.trans_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TransType') is not None:
            self.trans_type = m.get('TransType')

        return self

class CreateTaskRequestParametersContentExtraction(DaraModel):
    def __init__(
        self,
        extraction_contents: List[main_models.CreateTaskRequestParametersContentExtractionExtractionContents] = None,
        scene_introduction: str = None,
        speaker_map: Dict[str, Any] = None,
    ):
        self.extraction_contents = extraction_contents
        self.scene_introduction = scene_introduction
        self.speaker_map = speaker_map

    def validate(self):
        if self.extraction_contents:
            for v1 in self.extraction_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExtractionContents'] = []
        if self.extraction_contents is not None:
            for k1 in self.extraction_contents:
                result['ExtractionContents'].append(k1.to_map() if k1 else None)

        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction

        if self.speaker_map is not None:
            result['SpeakerMap'] = self.speaker_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extraction_contents = []
        if m.get('ExtractionContents') is not None:
            for k1 in m.get('ExtractionContents'):
                temp_model = main_models.CreateTaskRequestParametersContentExtractionExtractionContents()
                self.extraction_contents.append(temp_model.from_map(k1))

        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')

        if m.get('SpeakerMap') is not None:
            self.speaker_map = m.get('SpeakerMap')

        return self

class CreateTaskRequestParametersContentExtractionExtractionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        identity: str = None,
        title: str = None,
    ):
        self.content = content
        self.identity = identity
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CreateTaskRequestParametersAutoChapters(DaraModel):
    def __init__(
        self,
        chapter_granularity: str = None,
    ):
        self.chapter_granularity = chapter_granularity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chapter_granularity is not None:
            result['ChapterGranularity'] = self.chapter_granularity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChapterGranularity') is not None:
            self.chapter_granularity = m.get('ChapterGranularity')

        return self



class CreateTaskRequestInput(DaraModel):
    def __init__(
        self,
        audio_channel_mode: str = None,
        file_url: str = None,
        format: str = None,
        language_hints: List[str] = None,
        multiple_streams_enabled: bool = None,
        output_path: str = None,
        progressive_callbacks_enabled: bool = None,
        sample_rate: int = None,
        source_language: str = None,
        task_id: str = None,
        task_key: str = None,
    ):
        self.audio_channel_mode = audio_channel_mode
        self.file_url = file_url
        self.format = format
        self.language_hints = language_hints
        self.multiple_streams_enabled = multiple_streams_enabled
        self.output_path = output_path
        self.progressive_callbacks_enabled = progressive_callbacks_enabled
        self.sample_rate = sample_rate
        # This parameter is required.
        self.source_language = source_language
        self.task_id = task_id
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_channel_mode is not None:
            result['AudioChannelMode'] = self.audio_channel_mode

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.language_hints is not None:
            result['LanguageHints'] = self.language_hints

        if self.multiple_streams_enabled is not None:
            result['MultipleStreamsEnabled'] = self.multiple_streams_enabled

        if self.output_path is not None:
            result['OutputPath'] = self.output_path

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
        if m.get('AudioChannelMode') is not None:
            self.audio_channel_mode = m.get('AudioChannelMode')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('LanguageHints') is not None:
            self.language_hints = m.get('LanguageHints')

        if m.get('MultipleStreamsEnabled') is not None:
            self.multiple_streams_enabled = m.get('MultipleStreamsEnabled')

        if m.get('OutputPath') is not None:
            self.output_path = m.get('OutputPath')

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

