# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartCloudNoteRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_chapters: main_models.StartCloudNoteRequestAutoChapters = None,
        channel_id: str = None,
        custom_prompt: main_models.StartCloudNoteRequestCustomPrompt = None,
        language_hints: List[str] = None,
        meeting_assistance: main_models.StartCloudNoteRequestMeetingAssistance = None,
        realtime_subtitle: main_models.StartCloudNoteRequestRealtimeSubtitle = None,
        service_inspection: main_models.StartCloudNoteRequestServiceInspection = None,
        source_language: str = None,
        storage_config: main_models.StartCloudNoteRequestStorageConfig = None,
        summarization: main_models.StartCloudNoteRequestSummarization = None,
        task_id: str = None,
        text_polish: main_models.StartCloudNoteRequestTextPolish = None,
        transcription: main_models.StartCloudNoteRequestTranscription = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The auto chapters feature. When enabled, chapter titles and summaries are generated.
        self.auto_chapters = auto_chapters
        # The channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The custom prompt control parameter object.
        self.custom_prompt = custom_prompt
        # **[Deprecated]** This parameter is deprecated. You do not need to specify it.
        self.language_hints = language_hints
        # The intelligent meeting minutes feature. When enabled, keywords, key content, and to-do items are generated.
        self.meeting_assistance = meeting_assistance
        # The real-time subtitles.
        self.realtime_subtitle = realtime_subtitle
        # The service inspection feature.
        self.service_inspection = service_inspection
        # The source language model used by the channel. Valid values:
        # - cn: Chinese
        # - yue: Cantonese
        # - en: English
        # - multilingual: Multilingual
        # - ja: Japanese
        # - ko: Korean
        # - de: German
        # - fr: French
        # - ru: Russian
        # - es: Spanish
        # - vi: Vietnamese
        # - it: Italian
        # - sv: Swedish
        # - cs: Czech
        # - pl: Polish
        # - th: Thai
        # - fi: Finnish
        # - hi: Hindi
        # - id: Indonesian
        # - pt: Portuguese
        # - ar: Arabic
        # - fil: Filipino
        # - ms: Malay
        # - tr: Turkish
        # - hu: Hungarian
        # - lo: Lao
        # - pt-br: Portuguese (Brazil)
        # - es-ar: Spanish (Argentina)
        # - es-mx: Spanish (Mexico)
        self.source_language = source_language
        # The storage configuration.
        # 
        # This parameter is required.
        self.storage_config = storage_config
        # The summarization feature. When enabled, full-text summaries and speaker summaries are generated.
        self.summarization = summarization
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The text polishing feature.
        self.text_polish = text_polish
        # The transcription feature. Enabled by default.
        self.transcription = transcription

    def validate(self):
        if self.auto_chapters:
            self.auto_chapters.validate()
        if self.custom_prompt:
            self.custom_prompt.validate()
        if self.meeting_assistance:
            self.meeting_assistance.validate()
        if self.realtime_subtitle:
            self.realtime_subtitle.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.storage_config:
            self.storage_config.validate()
        if self.summarization:
            self.summarization.validate()
        if self.text_polish:
            self.text_polish.validate()
        if self.transcription:
            self.transcription.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_chapters is not None:
            result['AutoChapters'] = self.auto_chapters.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.custom_prompt is not None:
            result['CustomPrompt'] = self.custom_prompt.to_map()

        if self.language_hints is not None:
            result['LanguageHints'] = self.language_hints

        if self.meeting_assistance is not None:
            result['MeetingAssistance'] = self.meeting_assistance.to_map()

        if self.realtime_subtitle is not None:
            result['RealtimeSubtitle'] = self.realtime_subtitle.to_map()

        if self.service_inspection is not None:
            result['ServiceInspection'] = self.service_inspection.to_map()

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.storage_config is not None:
            result['StorageConfig'] = self.storage_config.to_map()

        if self.summarization is not None:
            result['Summarization'] = self.summarization.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text_polish is not None:
            result['TextPolish'] = self.text_polish.to_map()

        if self.transcription is not None:
            result['Transcription'] = self.transcription.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoChapters') is not None:
            temp_model = main_models.StartCloudNoteRequestAutoChapters()
            self.auto_chapters = temp_model.from_map(m.get('AutoChapters'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CustomPrompt') is not None:
            temp_model = main_models.StartCloudNoteRequestCustomPrompt()
            self.custom_prompt = temp_model.from_map(m.get('CustomPrompt'))

        if m.get('LanguageHints') is not None:
            self.language_hints = m.get('LanguageHints')

        if m.get('MeetingAssistance') is not None:
            temp_model = main_models.StartCloudNoteRequestMeetingAssistance()
            self.meeting_assistance = temp_model.from_map(m.get('MeetingAssistance'))

        if m.get('RealtimeSubtitle') is not None:
            temp_model = main_models.StartCloudNoteRequestRealtimeSubtitle()
            self.realtime_subtitle = temp_model.from_map(m.get('RealtimeSubtitle'))

        if m.get('ServiceInspection') is not None:
            temp_model = main_models.StartCloudNoteRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m.get('ServiceInspection'))

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('StorageConfig') is not None:
            temp_model = main_models.StartCloudNoteRequestStorageConfig()
            self.storage_config = temp_model.from_map(m.get('StorageConfig'))

        if m.get('Summarization') is not None:
            temp_model = main_models.StartCloudNoteRequestSummarization()
            self.summarization = temp_model.from_map(m.get('Summarization'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TextPolish') is not None:
            temp_model = main_models.StartCloudNoteRequestTextPolish()
            self.text_polish = temp_model.from_map(m.get('TextPolish'))

        if m.get('Transcription') is not None:
            temp_model = main_models.StartCloudNoteRequestTranscription()
            self.transcription = temp_model.from_map(m.get('Transcription'))

        return self

class StartCloudNoteRequestTranscription(DaraModel):
    def __init__(
        self,
        diarization_enabled: bool = None,
        phrase_id: str = None,
        speaker_count: int = None,
        transcription_level: int = None,
    ):
        # Specifies whether to enable speaker diarization.
        self.diarization_enabled = diarization_enabled
        # The hotword table ID.
        self.phrase_id = phrase_id
        # The number of speakers for speaker diarization. Default value: 0. Valid values:
        # - 0: The number of speakers is unknown.
        # - 2: The number of speakers is 2.
        self.speaker_count = speaker_count
        # The return level of speech recognition results. Default value: 2. Valid values:
        # - 1: Returns recognition results when a complete sentence is recognized.
        # - 2: Returns recognition results when intermediate results and complete sentences are recognized.
        self.transcription_level = transcription_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diarization_enabled is not None:
            result['DiarizationEnabled'] = self.diarization_enabled

        if self.phrase_id is not None:
            result['PhraseId'] = self.phrase_id

        if self.speaker_count is not None:
            result['SpeakerCount'] = self.speaker_count

        if self.transcription_level is not None:
            result['TranscriptionLevel'] = self.transcription_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiarizationEnabled') is not None:
            self.diarization_enabled = m.get('DiarizationEnabled')

        if m.get('PhraseId') is not None:
            self.phrase_id = m.get('PhraseId')

        if m.get('SpeakerCount') is not None:
            self.speaker_count = m.get('SpeakerCount')

        if m.get('TranscriptionLevel') is not None:
            self.transcription_level = m.get('TranscriptionLevel')

        return self

class StartCloudNoteRequestTextPolish(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable the feature.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class StartCloudNoteRequestSummarization(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        type: List[str] = None,
    ):
        # Specifies whether to enable the feature.
        self.enabled = enabled
        # The specific type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class StartCloudNoteRequestStorageConfig(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        bucket: str = None,
        region: int = None,
        secret_key: str = None,
        vendor: int = None,
    ):
        # The AccessKey.
        # 
        # This parameter is required.
        self.access_key = access_key
        # The bucket name.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The storage region.
        # 
        # | Region | AliYun OSS |
        # |--------|------------|
        # | 0 | CN_Hangzhou |
        # | 1 | CN_Shanghai |
        # | 2 | CN_Qingdao |
        # | 3 | CN_Beijing |
        # | 4 | CN_Zhangjiakou |
        # | 5 | CN_Huhehaote |
        # | 6 | CN_Shenzhen |
        # | 7 | CN_Hongkong |
        # | 8 | US_West_1 |
        # | 9 | US_East_1 |
        # | 10 | AP_Southeast_1 |
        # | 11 | AP_Southeast_2 |
        # | 12 | AP_Southeast_3 |
        # | 13 | AP_Southeast_5 |
        # | 14 | AP_Northeast_1 |
        # | 15 | AP_South_1 (Offline. Do not use.) |
        # | 16 | EU_Central_1 |
        # | 17 | EU_West_1 |
        # | 18 | EU_East_1(ME_East_1) |
        # | 19 | AP_Southeast_6 |
        # | 20 | CN_Heyuan |
        # | 21 | CN_Guangzhou |
        # | 22 | CN_Chengdu |
        # | 23 | CN_Nanjing |
        # | 24 | CN_Fuzhou |
        # | 25 | CN_Wulanchabu |
        # | 26 | AP_Northeast_2 |
        # | 27 | AP_Southeast_7 |
        # 
        # This parameter is required.
        self.region = region
        # The AccessKey secret.
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # The storage platform. Valid values:
        # 
        # | vendor | Object storage service | Remarks |
        # |--------|---------|---------|
        # | 1 | AliYun OSS | Alibaba Cloud |
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.region is not None:
            result['Region'] = self.region

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class StartCloudNoteRequestServiceInspection(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        inspection_contents: List[main_models.StartCloudNoteRequestServiceInspectionInspectionContents] = None,
        inspection_introduction: str = None,
        scene_introduction: str = None,
    ):
        # Specifies whether to enable the feature.
        self.enabled = enabled
        # The list of inspection dimensions for service inspection, including the names and definitions of the dimensions. This specifies the criteria for the large language model to determine whether a dimension is hit.
        # 
        # This parameter is required.
        self.inspection_contents = inspection_contents
        # The description of the inspection objectives and focus areas for service inspection.
        # 
        # This parameter is required.
        self.inspection_introduction = inspection_introduction
        # The description of the dialogue scene for service inspection.
        # 
        # This parameter is required.
        self.scene_introduction = scene_introduction

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
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['InspectionContents'] = []
        if self.inspection_contents is not None:
            for k1 in self.inspection_contents:
                result['InspectionContents'].append(k1.to_map() if k1 else None)

        if self.inspection_introduction is not None:
            result['InspectionIntroduction'] = self.inspection_introduction

        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.inspection_contents = []
        if m.get('InspectionContents') is not None:
            for k1 in m.get('InspectionContents'):
                temp_model = main_models.StartCloudNoteRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k1))

        if m.get('InspectionIntroduction') is not None:
            self.inspection_introduction = m.get('InspectionIntroduction')

        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')

        return self

class StartCloudNoteRequestServiceInspectionInspectionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        # The definition of the inspection dimension for service inspection.
        # 
        # This parameter is required.
        self.content = content
        # The name of the inspection dimension for service inspection.
        # 
        # This parameter is required.
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

class StartCloudNoteRequestRealtimeSubtitle(DaraModel):
    def __init__(
        self,
        asr_callback: bool = None,
        enabled: bool = None,
        translation: main_models.StartCloudNoteRequestRealtimeSubtitleTranslation = None,
    ):
        # Specifies whether to enable server-side callbacks.
        self.asr_callback = asr_callback
        # Specifies whether to enable the feature.
        self.enabled = enabled
        # The translation parameters. You can specify the target translation language by using the SDK.
        self.translation = translation

    def validate(self):
        if self.translation:
            self.translation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_callback is not None:
            result['AsrCallback'] = self.asr_callback

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.translation is not None:
            result['Translation'] = self.translation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrCallback') is not None:
            self.asr_callback = m.get('AsrCallback')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Translation') is not None:
            temp_model = main_models.StartCloudNoteRequestRealtimeSubtitleTranslation()
            self.translation = temp_model.from_map(m.get('Translation'))

        return self

class StartCloudNoteRequestRealtimeSubtitleTranslation(DaraModel):
    def __init__(
        self,
        translate_level: int = None,
    ):
        # The output level of the translated text. Default value: 2.
        # 
        # - 1: Returns results when a complete sentence is recognized.
        # - 2: Returns results when intermediate results and complete sentences are recognized.
        self.translate_level = translate_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.translate_level is not None:
            result['TranslateLevel'] = self.translate_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TranslateLevel') is not None:
            self.translate_level = m.get('TranslateLevel')

        return self

class StartCloudNoteRequestMeetingAssistance(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        meeting_assistance_type: List[str] = None,
    ):
        # Specifies whether to enable the feature.
        self.enabled = enabled
        # The algorithm type for the intelligent meeting minutes feature.
        # 
        # This parameter is required.
        self.meeting_assistance_type = meeting_assistance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.meeting_assistance_type is not None:
            result['MeetingAssistanceType'] = self.meeting_assistance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MeetingAssistanceType') is not None:
            self.meeting_assistance_type = m.get('MeetingAssistanceType')

        return self

class StartCloudNoteRequestCustomPrompt(DaraModel):
    def __init__(
        self,
        custom_prompt_contents: List[main_models.StartCloudNoteRequestCustomPromptCustomPromptContents] = None,
        enabled: bool = None,
    ):
        # The list of parameters for the custom prompt.
        # 
        # This parameter is required.
        self.custom_prompt_contents = custom_prompt_contents
        # Specifies whether to enable the feature.
        self.enabled = enabled

    def validate(self):
        if self.custom_prompt_contents:
            for v1 in self.custom_prompt_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPromptContents'] = []
        if self.custom_prompt_contents is not None:
            for k1 in self.custom_prompt_contents:
                result['CustomPromptContents'].append(k1.to_map() if k1 else None)

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_prompt_contents = []
        if m.get('CustomPromptContents') is not None:
            for k1 in m.get('CustomPromptContents'):
                temp_model = main_models.StartCloudNoteRequestCustomPromptCustomPromptContents()
                self.custom_prompt_contents.append(temp_model.from_map(k1))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class StartCloudNoteRequestCustomPromptCustomPromptContents(DaraModel):
    def __init__(
        self,
        model: str = None,
        name: str = None,
        prompt: str = None,
        trans_type: str = None,
    ):
        # The model used for the prompt. Valid values: tingwu-turbo, tingwu-plus, and qwen-max. Default value: tingwu-turbo.
        self.model = model
        # The custom name of the prompt, which is used to match the output results.
        # 
        # This parameter is required.
        self.name = name
        # The custom content of the prompt. The content must include the {Transcription} tag. The {Transcription} tag is automatically replaced with the speech transcription result as the model input.
        # 
        # This parameter is required.
        self.prompt = prompt
        # The format of the {Transcription} tag. Valid values:
        # 
        # - chat: The transcription result includes speaker information.
        # - default: The transcription result is in plain text format.
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

class StartCloudNoteRequestAutoChapters(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable the feature.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

