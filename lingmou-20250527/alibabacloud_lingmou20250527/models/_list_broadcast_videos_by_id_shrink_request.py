# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBroadcastVideosByIdShrinkRequest(DaraModel):
    def __init__(
        self,
        video_ids_shrink: str = None,
    ):
        self.video_ids_shrink = video_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_ids_shrink is not None:
            result['videoIds'] = self.video_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoIds') is not None:
            self.video_ids_shrink = m.get('videoIds')

        return self

