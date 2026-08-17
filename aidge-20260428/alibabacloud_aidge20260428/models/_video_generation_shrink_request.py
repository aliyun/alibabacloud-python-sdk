# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        intent_shrink: str = None,
        output_shrink: str = None,
    ):
        # The product input.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The intent parameters. Currently unavailable.
        self.intent_shrink = intent_shrink
        # The output parameters.
        # 
        # This parameter is required.
        self.output_shrink = output_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.intent_shrink is not None:
            result['Intent'] = self.intent_shrink

        if self.output_shrink is not None:
            result['Output'] = self.output_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Intent') is not None:
            self.intent_shrink = m.get('Intent')

        if m.get('Output') is not None:
            self.output_shrink = m.get('Output')

        return self

