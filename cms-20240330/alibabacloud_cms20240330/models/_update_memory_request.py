# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateMemoryRequest(DaraModel):
    def __init__(
        self,
        metadata: Dict[str, Any] = None,
        text: str = None,
    ):
        # The metadata of the Memory.
        self.metadata = metadata
        # The new text for the Memory.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

