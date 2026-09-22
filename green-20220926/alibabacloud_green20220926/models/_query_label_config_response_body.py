# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class QueryLabelConfigResponseBody(DaraModel):
    def __init__(
        self,
        content_moderation: List[Any] = None,
        request_id: str = None,
    ):
        # The content moderation configuration.
        self.content_moderation = content_moderation
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_moderation is not None:
            result['ContentModeration'] = self.content_moderation

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentModeration') is not None:
            self.content_moderation = m.get('ContentModeration')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

