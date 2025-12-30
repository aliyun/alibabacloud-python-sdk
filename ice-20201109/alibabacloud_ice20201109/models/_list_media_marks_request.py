# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaMarksRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_mark_ids: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The mark ID. You can specify multiple IDs separated with commas (,). This parameter is discontinued.
        self.media_mark_ids = media_mark_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_mark_ids is not None:
            result['MediaMarkIds'] = self.media_mark_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaMarkIds') is not None:
            self.media_mark_ids = m.get('MediaMarkIds')

        return self

