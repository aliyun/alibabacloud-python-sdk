# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoTranslationShrinkRequest(DaraModel):
    def __init__(
        self,
        capabilities_shrink: str = None,
        enable_quality_check: bool = None,
        erase_only: bool = None,
        remove_logo: bool = None,
        source_language: str = None,
        subtitle_mode: str = None,
        target_language: str = None,
        video_url: str = None,
    ):
        # The list of translation features. Valid values: speech and visual. You can select both. At least one feature must be specified. Duplicate values are not allowed.
        # 
        # This parameter is required.
        self.capabilities_shrink = capabilities_shrink
        # Specifies whether to enable the quality check for on-screen text processing. This parameter takes effect only when visual is included and explicitly set to true. If only speech is selected, this parameter is ignored. No quality check is performed, no quality check fields are returned, and no error is reported for this parameter. Enabling the quality check may increase the waiting time. Do not enable it unless necessary. Default value: false.
        self.enable_quality_check = enable_quality_check
        # Valid only when visual is included. Specifies whether to only erase the on-screen text without translation. Valid values:
        # - true: Erases the on-screen text without translation.
        # - false: Translates the on-screen text.
        # Default value: false.
        self.erase_only = erase_only
        # Valid only when visual is included. Specifies whether to erase brand logos. Valid values:
        # - true: Erases brand logos.
        # - false: Retains brand logos.
        # Default value: false. This parameter is independent of EraseOnly.
        self.remove_logo = remove_logo
        # The original language of the video. For supported languages, see Language support.
        self.source_language = source_language
        # Valid only when speech is included. Valid values:
        # - erase: Erases only the original subtitles.
        # - replace: Replaces the original subtitles with translated subtitles. This erases the original subtitles and adds subtitles synchronized with the translated speech.
        # - If not specified, the original subtitles are not processed. This means the original subtitles are neither erased nor replaced with new subtitles.
        self.subtitle_mode = subtitle_mode
        # Required when speech is included. Optional when only visual is selected and EraseOnly is set to true. If provided in this case, it is ignored. Required in all other cases.
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
        if self.capabilities_shrink is not None:
            result['Capabilities'] = self.capabilities_shrink

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
            self.capabilities_shrink = m.get('Capabilities')

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

