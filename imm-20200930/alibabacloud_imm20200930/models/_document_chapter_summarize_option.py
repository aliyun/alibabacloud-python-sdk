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
        # The maximum number of results to return per request. If you do not specify this parameter, the default value is used.
        self.limit = limit
        # The pagination token. It specifies the starting point for the query. To retrieve the next page of results, set this parameter to the marker value from the previous response.
        self.marker = marker
        # The summarization model version. If you do not specify this parameter, the default model version is used.
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

