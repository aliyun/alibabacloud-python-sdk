# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetTextSparseEmbeddingRequest(DaraModel):
    def __init__(
        self,
        input: List[str] = None,
        input_type: str = None,
        return_token: bool = None,
    ):
        # This parameter is required.
        self.input = input
        self.input_type = input_type
        self.return_token = return_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input

        if self.input_type is not None:
            result['input_type'] = self.input_type

        if self.return_token is not None:
            result['return_token'] = self.return_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('input_type') is not None:
            self.input_type = m.get('input_type')

        if m.get('return_token') is not None:
            self.return_token = m.get('return_token')

        return self

