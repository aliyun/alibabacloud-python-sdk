# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRouteStrategyRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        job_id: int = None,
        name: str = None,
        namespace: str = None,
        region_id: str = None,
        status: int = None,
        strategy_content: str = None,
        type: int = None,
    ):
        # The ID of the application group. You can obtain the ID on the **Application Management** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job ID. You can obtain the ID on the **Task Management** page in the SchedulerX console.
        self.job_id = job_id
        # The name of the routing policy.
        # 
        # This parameter is required.
        self.name = name
        # The namespace ID. You can obtain the namespace ID on the **Namespace** page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable the routing policy. Valid values:
        # 
        # *   **0**: disables the routing policy.
        # *   **1**: enables the routing policy.
        self.status = status
        # The details of the routing policy. The value is a JSON string. For more information about this parameter, see **the additional information about request parameters** below this table.
        self.strategy_content = strategy_content
        # The type of the routing policy. Valid value:
        # 
        # *   **3**: routes by proportion.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

