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
        # The ID of the speech recognition model. The default value is nls-base. Supported models include paraformer-realtime-v2 and paraformer-realtime-8k-v2.
        self.asr_model_id = asr_model_id
        # The input audio format. Supported formats are pcm, wav, and mp3.
        self.input_format = input_format
        # The output audio format.
        self.output_format = output_format
        # The pitch rate.
        # ● If \\`ttsModelId\\` is \\`nls-base\\`:
        # The value ranges from -500 to 500. The default is 0.
        # ● If \\`ttsModelId\\` is \\`cosyvoice-v2\\`: Specifies the pitch of the synthesized audio. The value ranges from 0.5 to 2.
        self.pitch_rate = pitch_rate
        # The sample rate.
        self.sample_rate = sample_rate
        # The speech rate.
        # ● If \\`ttsModelId\\` is \\`nls-base\\`: The value ranges from -500 to 500. The default is 0.
        # ● If \\`ttsModelId\\` is \\`cosyvoice-v2\\`:
        # Specifies the speech rate of the synthesized audio. The value ranges from 0.5 to 2.
        # ○ 0.5: Half the default speed.
        # ○ 1: The default speed. The default speed is the model\\"s standard output speed and may vary slightly by speaker. It is about four characters per second.
        # ○ 2: Twice the default speed.
        self.speech_rate = speech_rate
        # The ID of the speech synthesis model. The default value is nls-base. The cosyvoice-v2 model is supported.
        self.tts_model_id = tts_model_id
        # The voice parameter. This is available only for models that support word-level or sentence-level timestamps.
        self.voice_code = voice_code
        # The volume. The value ranges from 0 to 100. This parameter is optional. The default value is 50.
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

