# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScenarioRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        scenario_id: int = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The ID of the business monitoring job. You can obtain the ID by calling the ListScenario operation.
        # 
        # This parameter is required.
        self.scenario_id = scenario_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        return self

