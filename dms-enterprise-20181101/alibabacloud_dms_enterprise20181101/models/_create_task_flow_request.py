# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskFlowRequest(DaraModel):
    def __init__(
        self,
        dag_name: str = None,
        description: str = None,
        scenario_id: int = None,
        tid: int = None,
    ):
        # The name of the task flow.
        # 
        # This parameter is required.
        self.dag_name = dag_name
        # The description of the task flow.
        self.description = description
        # The ID of the scenario.
        self.scenario_id = scenario_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.description is not None:
            result['Description'] = self.description

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

