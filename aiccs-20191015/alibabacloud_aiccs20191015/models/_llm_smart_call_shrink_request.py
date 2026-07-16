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
        # LLM application code. View it in the [Application Management](https://aiccs.console.aliyun.com/engine/llmApp) interface.
        # 
        # This parameter is required.
        self.application_code = application_code
        # Business parameters. These parameters are passed to the customer model when invoking the customer model.
        self.biz_param_shrink = biz_param_shrink
        # Called number that receives the intelligent outbound call.
        # 
        # This parameter is required.
        self.called_number = called_number
        # Caller number. This parameter is required and supports only numbers from the Chinese mainland. View available numbers in the Voice Service [Number Management](https://dyvmsnext.console.aliyun.com/number/list/normal) interface.
        self.caller_number = caller_number
        # Customer-provided ingest endpoint encoding.
        # 
        # > 
        # > - If you use your own line, contact Alibaba Cloud support to enable this feature.
        # > - The line encoding is provided by Alibaba Cloud support. Do not set this parameter if you do not have one.
        self.customer_line_code = customer_line_code
        # The extension number of the X number, up to 5 digits.
        # 
        # >Notice: Fill this field only in AXN extension mode. If no extension number exists, do not fill it.
        self.extension = extension
        # An ID reserved for the caller. This ID will be returned to the caller through a receipt message. Length: 1–15 bytes.
        self.out_id = out_id
        # Prompt variable. Go to the [Application Management](https://aiccs.console.aliyun.com/engine/llmApp) interface and click Details to view the prompt variables you created.
        self.prompt_param_shrink = prompt_param_shrink
        # Maximum call duration. The call is automatically disconnected after timeout. Unit: seconds.
        # >
        # >- Maximum value: 3600 s.
        # >- Minimum value: 600 s.
        self.session_timeout = session_timeout
        # Start-word variables. Go to the [LLM Application Management](https://aiccs.console.aliyun.com/engine/llmApp) interface and click Details to view the start-word variables of your created LLM application.
        self.start_word_param_shrink = start_word_param_shrink
        # Voice speed during TTS playback.
        # 
        # > 
        # > - Value range: -200 to 200. Default value is 0.
        # > - If this parameter is not set, the voice speed configured in the LLM application is used by default.
        self.tts_speed = tts_speed
        # The voice code used for TTS playback.
        # > 
        # > - If no value is set, the voice code configured in the LLM application is used by default.
        # > - You can use the [ListAvailableTts](https://help.aliyun.com/document_detail/2926668.html) API to view all available voice codes.
        self.tts_voice_code = tts_voice_code
        # The volume for TTS playback.
        # > 
        # > - Value range: 0–100. Default value is 0.
        # > - If no value is set, the volume configured in the LLM application is used by default.
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

