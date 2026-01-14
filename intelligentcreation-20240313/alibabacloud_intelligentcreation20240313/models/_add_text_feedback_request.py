# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTextFeedbackRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        quality: int = None,
        text_id: int = None,
    ):
        self.content = content
        self.quality = quality
        self.text_id = text_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.quality is not None:
            result['quality'] = self.quality

        if self.text_id is not None:
            result['textId'] = self.text_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('quality') is not None:
            self.quality = m.get('quality')

        if m.get('textId') is not None:
            self.text_id = m.get('textId')

        return self

