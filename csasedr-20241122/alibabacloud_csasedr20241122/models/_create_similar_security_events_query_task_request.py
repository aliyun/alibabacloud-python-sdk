# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimilarSecurityEventsQueryTaskRequest(DaraModel):
    def __init__(
        self,
        security_event_id: int = None,
        similar_event_scenario_code: str = None,
    ):
        # The ID of the alert event.
        # 
        # This parameter is required.
        self.security_event_id = security_event_id
        # The scenario code of alerting events that are of the same type or have the same rule hits.
        self.similar_event_scenario_code = similar_event_scenario_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.similar_event_scenario_code is not None:
            result['SimilarEventScenarioCode'] = self.similar_event_scenario_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SimilarEventScenarioCode') is not None:
            self.similar_event_scenario_code = m.get('SimilarEventScenarioCode')

        return self

