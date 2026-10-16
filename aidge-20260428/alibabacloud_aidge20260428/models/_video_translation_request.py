# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class VideoTranslationRequest(DaraModel):
    def __init__(
        self,
        capabilities: List[str] = None,
        enable_quality_check: bool = None,
        erase_only: bool = None,
        remove_logo: bool = None,
        source_language: str = None,
        subtitle_mode: str = None,
        target_language: str = None,
        video_url: str = None,
    ):
        # The list of translation features. Valid values: speech and visual. You can select both. At least one feature is required. Duplicate values are not accepted.
        # 
        # This parameter is required.
        self.capabilities = capabilities
        # Specifies whether to enable the quality check for on-screen text processing. Default value: false. The quality check is enabled when visual is included and this parameter is explicitly set to true. If only speech is selected, this parameter is ignored, no quality check is performed, no quality check fields are returned, and no errors are reported due to this parameter. Enabling the quality check may increase the waiting time. Do not enable it unless necessary.
        self.enable_quality_check = enable_quality_check
        # Specifies whether to only erase the source language text in the video frames without translating it. This parameter is valid only when visual is included. Valid values: true (erases only) and false (translates the on-screen text). Default value: false.
        self.erase_only = erase_only
        # Specifies whether to erase brand logos. This parameter is valid only when visual is included. Valid values: true (erases brand logos) and false (retains logos). Default value: false. This parameter is independent of eraseOnly.
        self.remove_logo = remove_logo
        # The source language. For supported languages, see Language support.
        self.source_language = source_language
        # The subtitle processing mode. This parameter is valid only when speech is included. Valid values: erase (erases only the original subtitles) and replace (erases the original subtitles and adds new subtitles). If this parameter is omitted, the original subtitles are not processed and no new subtitles are added.
        self.subtitle_mode = subtitle_mode
        # The target language. This parameter is required.
        self.target_language = target_language
        # The URL of the video. Supported formats: MP4 and MOV. Maximum size: 200 MB.
        # 
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.enable_quality_check is not None:
            result['EnableQualityCheck'] = self.enable_quality_check

        if self.erase_only is not None:
            result['EraseOnly'] = self.erase_only

        if self.remove_logo is not None:
            result['RemoveLogo'] = self.remove_logo

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.subtitle_mode is not None:
            result['SubtitleMode'] = self.subtitle_mode

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('EnableQualityCheck') is not None:
            self.enable_quality_check = m.get('EnableQualityCheck')

        if m.get('EraseOnly') is not None:
            self.erase_only = m.get('EraseOnly')

        if m.get('RemoveLogo') is not None:
            self.remove_logo = m.get('RemoveLogo')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SubtitleMode') is not None:
            self.subtitle_mode = m.get('SubtitleMode')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

