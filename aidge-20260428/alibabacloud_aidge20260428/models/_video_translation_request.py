# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class VideoTranslationRequest(DaraModel):
    def __init__(
        self,
        capabilities: List[str] = None,
        source_language: str = None,
        target_language: str = None,
        video_url: str = None,
    ):
        # The array of translation capabilities. Valid values: ["visual"].
        # 
        # This parameter is required.
        self.capabilities = capabilities
        # The source language. This parameter is optional. Default value: auto (automatic detection).
        self.source_language = source_language
        # The target language. This parameter is required.
        # 
        # This parameter is required.
        self.target_language = target_language
        # The video URL (MP4/MOV, ≤ 200 MB).
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
            self.capabilities = m.get('Capabilities')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

