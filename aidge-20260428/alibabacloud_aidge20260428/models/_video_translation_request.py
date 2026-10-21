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
        # Specifies whether to enable quality inspection for on-screen text processing. Effective only when visual is included and this parameter is explicitly set to true. If only speech is selected, this parameter is ignored, no quality inspection is performed, no quality inspection fields are returned, and no error is reported due to this parameter. Enabling quality inspection may increase the processing time. Do not enable it unless necessary. Default value: false.
        self.enable_quality_check = enable_quality_check
        # Applicable only when visual is included. Specifies whether to erase on-screen text without translation. Valid values: true: erases on-screen text without translation. false: translates on-screen text. Default value: false.
        self.erase_only = erase_only
        # Applicable only when visual is included. Specifies whether to erase brand logos. Valid values: true: erases brand logos. false: retains brand logos. Default value: false. This parameter is independent of EraseOnly.
        self.remove_logo = remove_logo
        # The original language of the video (source language). For supported languages, see Language support.
        self.source_language = source_language
        # Applicable only when speech is included. Valid values: erase: erases the original subtitles only. replace: replaces the original subtitles with translated subtitles, which means erasing the original subtitles and adding subtitles synchronized with the translated speech. If not specified, the original subtitles are not processed, which means neither erasing the original subtitles nor adding new subtitles.
        self.subtitle_mode = subtitle_mode
        # Required when speech is included. Optional when only visual is included and EraseOnly is set to true. If specified in this case, it is ignored. Required in other cases.
        self.target_language = target_language
        # The video URL. Supported formats: MP4 and MOV. Maximum size: 200 MB.
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

