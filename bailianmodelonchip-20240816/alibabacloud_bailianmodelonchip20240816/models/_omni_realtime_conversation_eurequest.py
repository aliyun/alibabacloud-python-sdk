# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OmniRealtimeConversationEURequest(DaraModel):
    def __init__(
        self,
        input_audio: str = None,
        user_prompt: str = None,
        voice: str = None,
    ):
        # This parameter is required.
        self.input_audio = input_audio
        self.user_prompt = user_prompt
        self.voice = voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_audio is not None:
            result['inputAudio'] = self.input_audio

        if self.user_prompt is not None:
            result['userPrompt'] = self.user_prompt

        if self.voice is not None:
            result['voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputAudio') is not None:
            self.input_audio = m.get('inputAudio')

        if m.get('userPrompt') is not None:
            self.user_prompt = m.get('userPrompt')

        if m.get('voice') is not None:
            self.voice = m.get('voice')

        return self

