# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveTaskFlowToScenarioRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        scenario_id: int = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the business scenario to which you want to migrate your task flow. If this parameter is set to the default value or a value that is less than or equal to 0, the task flow is migrated to the default business scenario.
        self.scenario_id = scenario_id
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
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

