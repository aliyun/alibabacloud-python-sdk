# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBroadcastAudiosByIdShrinkRequest(DaraModel):
    def __init__(
        self,
        audio_ids_shrink: str = None,
    ):
        self.audio_ids_shrink = audio_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_ids_shrink is not None:
            result['audioIds'] = self.audio_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioIds') is not None:
            self.audio_ids_shrink = m.get('audioIds')

        return self

