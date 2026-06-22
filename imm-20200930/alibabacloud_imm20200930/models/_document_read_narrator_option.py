# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentReadNarratorOption(DaraModel):
    def __init__(
        self,
        narrate: bool = None,
    ):
        # Whether to enable the document narration feature. Set to `true` to enable narration. Defaults to `false`.
        self.narrate = narrate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.narrate is not None:
            result['Narrate'] = self.narrate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Narrate') is not None:
            self.narrate = m.get('Narrate')

        return self

