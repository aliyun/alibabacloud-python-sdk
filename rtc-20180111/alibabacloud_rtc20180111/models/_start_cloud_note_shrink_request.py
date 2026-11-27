# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartCloudNoteShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_chapters_shrink: str = None,
        channel_id: str = None,
        custom_prompt_shrink: str = None,
        language_hints: List[str] = None,
        meeting_assistance_shrink: str = None,
        realtime_subtitle_shrink: str = None,
        service_inspection_shrink: str = None,
        source_language: str = None,
        storage_config: main_models.StartCloudNoteShrinkRequestStorageConfig = None,
        summarization_shrink: str = None,
        task_id: str = None,
        text_polish_shrink: str = None,
        transcription_shrink: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The auto chapters feature. When enabled, chapter titles and summaries are generated.
        self.auto_chapters_shrink = auto_chapters_shrink
        # The channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The custom prompt control parameter object.
        self.custom_prompt_shrink = custom_prompt_shrink
        # **[Deprecated]** This parameter is deprecated. You do not need to specify it.
        self.language_hints = language_hints
        # The intelligent meeting minutes feature. When enabled, keywords, key content, and to-do items are generated.
        self.meeting_assistance_shrink = meeting_assistance_shrink
        # The real-time subtitles.
        self.realtime_subtitle_shrink = realtime_subtitle_shrink
        # The service inspection feature.
        self.service_inspection_shrink = service_inspection_shrink
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
        self.summarization_shrink = summarization_shrink
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The text polishing feature.
        self.text_polish_shrink = text_polish_shrink
        # The transcription feature. Enabled by default.
        self.transcription_shrink = transcription_shrink

    def validate(self):
        if self.storage_config:
            self.storage_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_chapters_shrink is not None:
            result['AutoChapters'] = self.auto_chapters_shrink

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.custom_prompt_shrink is not None:
            result['CustomPrompt'] = self.custom_prompt_shrink

        if self.language_hints is not None:
            result['LanguageHints'] = self.language_hints

        if self.meeting_assistance_shrink is not None:
            result['MeetingAssistance'] = self.meeting_assistance_shrink

        if self.realtime_subtitle_shrink is not None:
            result['RealtimeSubtitle'] = self.realtime_subtitle_shrink

        if self.service_inspection_shrink is not None:
            result['ServiceInspection'] = self.service_inspection_shrink

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.storage_config is not None:
            result['StorageConfig'] = self.storage_config.to_map()

        if self.summarization_shrink is not None:
            result['Summarization'] = self.summarization_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text_polish_shrink is not None:
            result['TextPolish'] = self.text_polish_shrink

        if self.transcription_shrink is not None:
            result['Transcription'] = self.transcription_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoChapters') is not None:
            self.auto_chapters_shrink = m.get('AutoChapters')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CustomPrompt') is not None:
            self.custom_prompt_shrink = m.get('CustomPrompt')

        if m.get('LanguageHints') is not None:
            self.language_hints = m.get('LanguageHints')

        if m.get('MeetingAssistance') is not None:
            self.meeting_assistance_shrink = m.get('MeetingAssistance')

        if m.get('RealtimeSubtitle') is not None:
            self.realtime_subtitle_shrink = m.get('RealtimeSubtitle')

        if m.get('ServiceInspection') is not None:
            self.service_inspection_shrink = m.get('ServiceInspection')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('StorageConfig') is not None:
            temp_model = main_models.StartCloudNoteShrinkRequestStorageConfig()
            self.storage_config = temp_model.from_map(m.get('StorageConfig'))

        if m.get('Summarization') is not None:
            self.summarization_shrink = m.get('Summarization')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TextPolish') is not None:
            self.text_polish_shrink = m.get('TextPolish')

        if m.get('Transcription') is not None:
            self.transcription_shrink = m.get('Transcription')

        return self

class StartCloudNoteShrinkRequestStorageConfig(DaraModel):
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

