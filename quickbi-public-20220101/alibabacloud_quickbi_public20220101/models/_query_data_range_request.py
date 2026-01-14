# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataRangeRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        type: str = None,
    ):
        # Name, for fuzzy search.
        self.keyword = keyword
        # Data range type:
        # 
        # - llmCube: LlmCube resource.
        # - llmCubeTheme: Analysis theme.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

