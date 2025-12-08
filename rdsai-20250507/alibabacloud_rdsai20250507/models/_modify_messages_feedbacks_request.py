# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMessagesFeedbacksRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        message_id: str = None,
        rating: str = None,
    ):
        self.content = content
        self.message_id = message_id
        self.rating = rating

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.rating is not None:
            result['Rating'] = self.rating

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        return self

