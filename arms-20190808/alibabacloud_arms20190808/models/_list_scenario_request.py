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
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The name of the business monitoring job.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The scenario where the business monitoring job is used. Valid values:
        # 
        # *   `USER-DEFINED`: user-defined. This is the default value.
        # *   `EDAS-ROLLOUT`: application release in Enterprise Distributed Application Service (EDAS)
        # *   `OAM-ROLLOUT`: application release based on Open Application Model (OAM)
        # *   `MSC-CANARY`: canary release based on Microservice Engine (MSE)
        self.scenario = scenario
        # The code of the business monitoring job. Set this parameter when you know the code of the business monitoring job you want to query.
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

