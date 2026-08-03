# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetInsightSelectorsResponseBody(DaraModel):
    def __init__(
        self,
        insight_selectors: List[str] = None,
        request_id: str = None,
        trail_arn: str = None,
    ):
        # An array of Insights event types.
        self.insight_selectors = insight_selectors
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud Resource Name (ARN) of the trail.
        self.trail_arn = trail_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insight_selectors is not None:
            result['InsightSelectors'] = self.insight_selectors

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trail_arn is not None:
            result['TrailArn'] = self.trail_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsightSelectors') is not None:
            self.insight_selectors = m.get('InsightSelectors')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrailArn') is not None:
            self.trail_arn = m.get('TrailArn')

        return self

