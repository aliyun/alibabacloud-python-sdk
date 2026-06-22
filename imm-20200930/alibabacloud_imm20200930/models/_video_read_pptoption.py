# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoReadPPTOption(DaraModel):
    def __init__(
        self,
        extract: bool = None,
    ):
        # Specifies whether to extract content from the presentation slides. Set this parameter to `true` to enable extraction.
        self.extract = extract

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extract is not None:
            result['Extract'] = self.extract

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extract') is not None:
            self.extract = m.get('Extract')

        return self

