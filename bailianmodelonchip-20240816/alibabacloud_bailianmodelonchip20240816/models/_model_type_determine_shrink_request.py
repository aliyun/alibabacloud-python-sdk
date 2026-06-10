# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelTypeDetermineShrinkRequest(DaraModel):
    def __init__(
        self,
        history_shrink: str = None,
        input_text: str = None,
    ):
        self.history_shrink = history_shrink
        # This parameter is required.
        self.input_text = input_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_shrink is not None:
            result['history'] = self.history_shrink

        if self.input_text is not None:
            result['inputText'] = self.input_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('history') is not None:
            self.history_shrink = m.get('history')

        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')

        return self

