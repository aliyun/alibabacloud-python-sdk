# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVoiceModelsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        res_spec_type: str = None,
        use_scene: str = None,
        voice_language: str = None,
        voice_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.res_spec_type = res_spec_type
        self.use_scene = use_scene
        self.voice_language = voice_language
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_type is not None:
            result['voiceType'] = self.voice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceType') is not None:
            self.voice_type = m.get('voiceType')

        return self

