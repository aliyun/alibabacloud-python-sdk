# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitImageToVideoTaskRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        pos_prompt: str = None,
    ):
        self.image_url = image_url
        self.pos_prompt = pos_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.pos_prompt is not None:
            result['posPrompt'] = self.pos_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('posPrompt') is not None:
            self.pos_prompt = m.get('posPrompt')

        return self

