# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetInsightTypesResponseBody(DaraModel):
    def __init__(
        self,
        insight_types: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # The types of Insights events.
        self.insight_types = insight_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insight_types is not None:
            result['InsightTypes'] = self.insight_types

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsightTypes') is not None:
            self.insight_types = m.get('InsightTypes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

