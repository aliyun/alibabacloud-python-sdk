# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoTranslationShrinkRequest(DaraModel):
    def __init__(
        self,
        capabilities_shrink: str = None,
        enable_quality_check: bool = None,
        source_language: str = None,
        target_language: str = None,
        video_url: str = None,
    ):
        # The list of translation features. Valid values: `speech` and `visual`. You can select both. At least one feature is required. Duplicate values are not accepted.
        # 
        # This parameter is required.
        self.capabilities_shrink = capabilities_shrink
        # Default value: false. If `visual` is included and this parameter is explicitly set to true, the quality check for on-screen text processing is enabled. If only `speech` is selected, this parameter is ignored. No quality check is performed, no quality check fields are returned, and no errors are reported due to this parameter. Enabling the quality check may increase the waiting time. Do not enable it unless necessary.
        self.enable_quality_check = enable_quality_check
        # The source language. For supported languages, see "Supported languages".
        self.source_language = source_language
        # The target language. This parameter is required.
        # 
        # This parameter is required.
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
        if self.capabilities_shrink is not None:
            result['Capabilities'] = self.capabilities_shrink

        if self.enable_quality_check is not None:
            result['EnableQualityCheck'] = self.enable_quality_check

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

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

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

