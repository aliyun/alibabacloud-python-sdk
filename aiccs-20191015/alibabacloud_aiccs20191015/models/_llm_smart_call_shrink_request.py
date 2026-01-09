# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LlmSmartCallShrinkRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        biz_param_shrink: str = None,
        called_number: str = None,
        caller_number: str = None,
        customer_line_code: str = None,
        extension: str = None,
        out_id: str = None,
        prompt_param_shrink: str = None,
        session_timeout: int = None,
        start_word_param_shrink: str = None,
        tts_speed: int = None,
        tts_voice_code: str = None,
        tts_volume: int = None,
    ):
        # This parameter is required.
        self.application_code = application_code
        self.biz_param_shrink = biz_param_shrink
        # This parameter is required.
        self.called_number = called_number
        self.caller_number = caller_number
        self.customer_line_code = customer_line_code
        self.extension = extension
        self.out_id = out_id
        self.prompt_param_shrink = prompt_param_shrink
        self.session_timeout = session_timeout
        self.start_word_param_shrink = start_word_param_shrink
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

        if self.biz_param_shrink is not None:
            result['BizParam'] = self.biz_param_shrink

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.customer_line_code is not None:
            result['CustomerLineCode'] = self.customer_line_code

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.prompt_param_shrink is not None:
            result['PromptParam'] = self.prompt_param_shrink

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.start_word_param_shrink is not None:
            result['StartWordParam'] = self.start_word_param_shrink

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

        if m.get('BizParam') is not None:
            self.biz_param_shrink = m.get('BizParam')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('CustomerLineCode') is not None:
            self.customer_line_code = m.get('CustomerLineCode')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PromptParam') is not None:
            self.prompt_param_shrink = m.get('PromptParam')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StartWordParam') is not None:
            self.start_word_param_shrink = m.get('StartWordParam')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsVoiceCode') is not None:
            self.tts_voice_code = m.get('TtsVoiceCode')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        return self

