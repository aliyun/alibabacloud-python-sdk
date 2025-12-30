# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EndToEndRealTimeDialogRequest(DaraModel):
    def __init__(
        self,
        asr_model_id: str = None,
        input_format: str = None,
        output_format: str = None,
        pitch_rate: int = None,
        sample_rate: str = None,
        speech_rate: int = None,
        tts_model_id: str = None,
        voice_code: str = None,
        volume: int = None,
    ):
        self.asr_model_id = asr_model_id
        self.input_format = input_format
        self.output_format = output_format
        self.pitch_rate = pitch_rate
        self.sample_rate = sample_rate
        self.speech_rate = speech_rate
        self.tts_model_id = tts_model_id
        self.voice_code = voice_code
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_model_id is not None:
            result['asrModelId'] = self.asr_model_id

        if self.input_format is not None:
            result['inputFormat'] = self.input_format

        if self.output_format is not None:
            result['outputFormat'] = self.output_format

        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate

        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate

        if self.speech_rate is not None:
            result['speechRate'] = self.speech_rate

        if self.tts_model_id is not None:
            result['ttsModelId'] = self.tts_model_id

        if self.voice_code is not None:
            result['voiceCode'] = self.voice_code

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asrModelId') is not None:
            self.asr_model_id = m.get('asrModelId')

        if m.get('inputFormat') is not None:
            self.input_format = m.get('inputFormat')

        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')

        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')

        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')

        if m.get('speechRate') is not None:
            self.speech_rate = m.get('speechRate')

        if m.get('ttsModelId') is not None:
            self.tts_model_id = m.get('ttsModelId')

        if m.get('voiceCode') is not None:
            self.voice_code = m.get('voiceCode')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

