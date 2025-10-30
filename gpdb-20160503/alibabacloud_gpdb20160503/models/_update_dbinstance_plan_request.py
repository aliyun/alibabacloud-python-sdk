# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDBInstancePlanRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        plan_config: str = None,
        plan_desc: str = None,
        plan_end_date: str = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_start_date: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The execution information of the plan. Specify the parameter in the JSON format. The parameter value varies based on the values of **PlanType** and **PlanScheduleType**. The following section describes the PlanConfig parameter.
        self.plan_config = plan_config
        # The description of the plan.
        self.plan_desc = plan_desc
        # The end time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # > 
        # 
        # *   This parameter must be specified only for **periodically executed** plans.
        # 
        # *   If you do not specify this parameter, the plan stops until the plan is deleted.
        self.plan_end_date = plan_end_date
        # The ID of the plan.
        # 
        # >  You can call the [DescribeDBInstancePlans](https://help.aliyun.com/document_detail/449398.html) operation to query the details of plans, including plan IDs.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The name of the plan.
        self.plan_name = plan_name
        # The start time of the plan. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   This parameter must be specified only for **periodically executed** plans.
        # 
        # *   If you do not specify this parameter, the current time is used.
        self.plan_start_date = plan_start_date

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

        if self.plan_config is not None:
            result['PlanConfig'] = self.plan_config

        if self.plan_desc is not None:
            result['PlanDesc'] = self.plan_desc

        if self.plan_end_date is not None:
            result['PlanEndDate'] = self.plan_end_date

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_start_date is not None:
            result['PlanStartDate'] = self.plan_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlanConfig') is not None:
            self.plan_config = m.get('PlanConfig')

        if m.get('PlanDesc') is not None:
            self.plan_desc = m.get('PlanDesc')

        if m.get('PlanEndDate') is not None:
            self.plan_end_date = m.get('PlanEndDate')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanStartDate') is not None:
            self.plan_start_date = m.get('PlanStartDate')

        return self

