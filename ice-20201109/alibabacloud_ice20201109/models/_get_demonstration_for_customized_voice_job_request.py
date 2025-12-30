# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDemonstrationForCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        scenario: str = None,
    ):
        # The demonstration scenario.
        # 
        # Valid values:
        # 
        # *   **story**
        # *   **interaction**
        # *   **navigation**
        # 
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenario is not None:
            result['Scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        return self

