# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSmartVoiceGroupsRequest(DaraModel):
    def __init__(
        self,
        voice_type: str = None,
    ):
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')

        return self

