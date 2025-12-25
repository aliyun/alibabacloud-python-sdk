# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScenarioRequest(DaraModel):
    def __init__(
        self,
        scenario_id: int = None,
        tid: int = None,
    ):
        # The ID of the business scenario.
        # 
        # This parameter is required.
        self.scenario_id = scenario_id
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

