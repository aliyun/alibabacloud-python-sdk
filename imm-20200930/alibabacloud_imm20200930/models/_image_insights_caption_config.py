# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageInsightsCaptionConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        prompt: str = None,
    ):
        self.enable = enable
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

