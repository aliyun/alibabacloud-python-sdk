# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutInsightSelectorsRequest(DaraModel):
    def __init__(
        self,
        insight_selectors: str = None,
        trail_name: str = None,
    ):
        # The types of Insights events that the trail should deliver.
        self.insight_selectors = insight_selectors
        # The name of the trail.
        # 
        # This parameter is required.
        self.trail_name = trail_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insight_selectors is not None:
            result['InsightSelectors'] = self.insight_selectors

        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsightSelectors') is not None:
            self.insight_selectors = m.get('InsightSelectors')

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        return self

