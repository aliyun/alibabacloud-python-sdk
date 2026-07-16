# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentChapterSummarizeOption(DaraModel):
    def __init__(
        self,
        limit: int = None,
        marker: int = None,
        version: str = None,
    ):
        # The number of section-by-section summaries. If neither Marker nor Index is specified, the entire article is summarized by default. Marker and Index must either both be specified or both be omitted.
        self.limit = limit
        # The start position for section-by-section summarization.
        self.marker = marker
        # The version of section-by-section summarization.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

