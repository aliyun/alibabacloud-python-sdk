# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class LlmSmartCallFullDuplexRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        called_number: str = None,
        caller_number: str = None,
        out_id: str = None,
        session_timeout: int = None,
        start_word_param: Dict[str, Any] = None,
        tts_speed: int = None,
        tts_voice_code: str = None,
        tts_volume: int = None,
    ):
        # This parameter is required.
        self.application_code = application_code
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.caller_number = caller_number
        self.out_id = out_id
        self.session_timeout = session_timeout
        self.start_word_param = start_word_param
        self.tts_speed = tts_speed
        self.tts_voice_code = tts_voice_code
        self.tts_volume = tts_volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.start_word_param is not None:
            result['StartWordParam'] = self.start_word_param

        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed

        if self.tts_voice_code is not None:
            result['TtsVoiceCode'] = self.tts_voice_code

        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StartWordParam') is not None:
            self.start_word_param = m.get('StartWordParam')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsVoiceCode') is not None:
            self.tts_voice_code = m.get('TtsVoiceCode')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        return self

