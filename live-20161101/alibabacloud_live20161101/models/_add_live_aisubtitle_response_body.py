# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveAISubtitleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        subtitle_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the subtitle template.
        self.subtitle_id = subtitle_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subtitle_id is not None:
            result['SubtitleId'] = self.subtitle_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubtitleId') is not None:
            self.subtitle_id = m.get('SubtitleId')

        return self

