# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ToolCall(DaraModel):
    def __init__(
        self,
        function: main_models.FunctionCall = None,
        type: str = None,
    ):
        # The definition of the function that can be called by the AI assistant.
        self.function = function
        # The type of the tool.
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = main_models.FunctionCall()
            self.function = temp_model.from_map(m.get('Function'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

