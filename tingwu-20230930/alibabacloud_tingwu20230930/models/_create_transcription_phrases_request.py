# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTranscriptionPhrasesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        word_weights: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.word_weights = word_weights

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.word_weights is not None:
            result['WordWeights'] = self.word_weights

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WordWeights') is not None:
            self.word_weights = m.get('WordWeights')

        return self

