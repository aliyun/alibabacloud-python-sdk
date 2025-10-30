# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancePlansRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_create_date: str = None,
        plan_desc: str = None,
        plan_id: str = None,
        plan_schedule_type: str = None,
        plan_type: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The time that is used to filter plans. If you specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format, the plans that are created before this time are returned. The time must be in UTC. If you do not specify this parameter, all plans are returned.
        self.plan_create_date = plan_create_date
        # The description of the plan.
        self.plan_desc = plan_desc
        # The plan ID.
        # 
        # > You can call the [DescribeDBInstancePlans](https://help.aliyun.com/document_detail/449398.html) operation to query the information about plans, including plan IDs.
        self.plan_id = plan_id
        # The execution mode of the plan. Valid values:
        # 
        # *   **Postpone**: The plan is executed later.
        # *   **Regular**: The plan is executed periodically.
        self.plan_schedule_type = plan_schedule_type
        # The type of the plan. Valid values:
        # 
        # *   **PauseResume**: pauses and resumes an instance.
        # *   **Resize**: scales an instance.
        # *   **ModifySpec**: changes compute node specifications.
        self.plan_type = plan_type

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

        if self.plan_create_date is not None:
            result['PlanCreateDate'] = self.plan_create_date

        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_schedule_type is not None:
            result['PlanScheduleType'] = self.plan_schedule_type

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlanCreateDate') is not None:
            self.plan_create_date = m.get('PlanCreateDate')

        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanScheduleType') is not None:
            self.plan_schedule_type = m.get('PlanScheduleType')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        return self

