# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScenarioRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        name: str = None,
        region_id: str = None,
        scenario: str = None,
        sign: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.scenario = scenario
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.sign is not None:
            result['Sign'] = self.sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Sign') is not None:
            self.sign = m.get('Sign')

        return self

