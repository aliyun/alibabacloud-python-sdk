# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListBroadcastVideosByIdRequest(DaraModel):
    def __init__(
        self,
        video_ids: List[str] = None,
    ):
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_ids is not None:
            result['videoIds'] = self.video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoIds') is not None:
            self.video_ids = m.get('videoIds')

        return self

