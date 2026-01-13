# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListActionPlansResponseBody(DaraModel):
    def __init__(
        self,
        action_plans: List[main_models.ListActionPlansResponseBodyActionPlans] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of execution plan results.
        self.action_plans = action_plans
        # The maximum number of records returned in this request.
        self.max_results = max_results
        # Indicates the read position returned by the current call. An empty value means all data has been read.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Total data count under the current request conditions (optional; not returned by default).
        self.total_count = total_count

    def validate(self):
        if self.action_plans:
            for v1 in self.action_plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActionPlans'] = []
        if self.action_plans is not None:
            for k1 in self.action_plans:
                result['ActionPlans'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_plans = []
        if m.get('ActionPlans') is not None:
            for k1 in m.get('ActionPlans'):
                temp_model = main_models.ListActionPlansResponseBodyActionPlans()
                self.action_plans.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListActionPlansResponseBodyActionPlans(DaraModel):
    def __init__(
        self,
        action_plan_id: str = None,
        action_plan_name: str = None,
        create_time: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The ID of the execution plan.
        self.action_plan_id = action_plan_id
        # The name of the execution plan.
        self.action_plan_name = action_plan_name
        # The time when the execution plan was created.
        self.create_time = create_time
        # The status of the execution plan. The possible values are as follows:
        # 
        # *   Active Instant tasks are dynamically managed only when the execution plan is in the Active state.
        # *   Inactive Instant tasks are no longer managed by execution plans in the Inactive state.
        # *   Deleting: The execution plan is being deleted. You cannot modify the parameters of an execution plan in this state.
        self.status = status
        # The time when the execution plan was last modified. The time follows the ISO 8601 standard and UTC +0. The format is yyyy-MM-ddTHH:mmZ.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_id is not None:
            result['ActionPlanId'] = self.action_plan_id

        if self.action_plan_name is not None:
            result['ActionPlanName'] = self.action_plan_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanId') is not None:
            self.action_plan_id = m.get('ActionPlanId')

        if m.get('ActionPlanName') is not None:
            self.action_plan_name = m.get('ActionPlanName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

