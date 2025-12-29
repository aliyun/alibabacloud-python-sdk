# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BuildPipelineRunLogLine(DaraModel):
    def __init__(
        self,
        content: str = None,
        offset: int = None,
    ):
        self.content = content
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.offset is not None:
            result['Offset'] = self.offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        return self

