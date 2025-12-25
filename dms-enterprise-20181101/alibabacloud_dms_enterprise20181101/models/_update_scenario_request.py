# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScenarioRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        scenario_id: str = None,
        scenario_name: str = None,
        tid: int = None,
    ):
        # The description of the business scenario.
        self.description = description
        # The ID of the business scenario.
        # 
        # This parameter is required.
        self.scenario_id = scenario_id
        # The name of the business scenario.
        # 
        # This parameter is required.
        self.scenario_name = scenario_name
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.scenario_name is not None:
            result['ScenarioName'] = self.scenario_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScenarioName') is not None:
            self.scenario_name = m.get('ScenarioName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

