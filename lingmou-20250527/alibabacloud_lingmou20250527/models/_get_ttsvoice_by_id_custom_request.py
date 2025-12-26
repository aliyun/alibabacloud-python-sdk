# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTTSVoiceByIdCustomRequest(DaraModel):
    def __init__(
        self,
        voice_id: str = None,
    ):
        self.voice_id = voice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.voice_id is not None:
            result['voiceId'] = self.voice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')

        return self

