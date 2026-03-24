# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BeginSessionResponseBody(DaraModel):
    def __init__(
        self,
        asr_max_end_silence: int = None,
        interruptible: bool = None,
        request_id: str = None,
        silence_reply_timeout: int = None,
        welcome_message: str = None,
    ):
        self.asr_max_end_silence = asr_max_end_silence
        self.interruptible = interruptible
        self.request_id = request_id
        # 静默超时时间
        self.silence_reply_timeout = silence_reply_timeout
        self.welcome_message = welcome_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_max_end_silence is not None:
            result['AsrMaxEndSilence'] = self.asr_max_end_silence

        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.silence_reply_timeout is not None:
            result['SilenceReplyTimeout'] = self.silence_reply_timeout

        if self.welcome_message is not None:
            result['WelcomeMessage'] = self.welcome_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrMaxEndSilence') is not None:
            self.asr_max_end_silence = m.get('AsrMaxEndSilence')

        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SilenceReplyTimeout') is not None:
            self.silence_reply_timeout = m.get('SilenceReplyTimeout')

        if m.get('WelcomeMessage') is not None:
            self.welcome_message = m.get('WelcomeMessage')

        return self

