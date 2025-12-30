# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMediaMarksResponseBody(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_mark_ids: str = None,
        request_id: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The IDs of the deleted marks separated with commas (,).
        self.media_mark_ids = media_mark_ids
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaMarkIds') is not None:
            self.media_mark_ids = m.get('MediaMarkIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

