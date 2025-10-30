# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDBInstancePlanStatusRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_id: str = None,
        plan_status: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](https://help.aliyun.com/document_detail/449398.html) operation to query the details of plans, including plan IDs.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # Specifies whether to enable or disable the plan. Valid values:
        # 
        # *   **disable**: disables the plan.
        # *   **enable**: enables the plan.
        # 
        # This parameter is required.
        self.plan_status = plan_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_status is not None:
            result['PlanStatus'] = self.plan_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanStatus') is not None:
            self.plan_status = m.get('PlanStatus')

        return self

