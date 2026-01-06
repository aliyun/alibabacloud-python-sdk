# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticPlansResponseBody(DaraModel):
    def __init__(
        self,
        elastic_plans: List[main_models.DescribeElasticPlansResponseBodyElasticPlans] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried scaling plans.
        self.elastic_plans = elastic_plans
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.elastic_plans:
            for v1 in self.elastic_plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticPlans'] = []
        if self.elastic_plans is not None:
            for k1 in self.elastic_plans:
                result['ElasticPlans'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_plans = []
        if m.get('ElasticPlans') is not None:
            for k1 in m.get('ElasticPlans'):
                temp_model = main_models.DescribeElasticPlansResponseBodyElasticPlans()
                self.elastic_plans.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeElasticPlansResponseBodyElasticPlans(DaraModel):
    def __init__(
        self,
        auto_scale: bool = None,
        elastic_plan_name: str = None,
        enabled: bool = None,
        next_schedule_time: str = None,
        resource_group_name: str = None,
        target_size: str = None,
        type: str = None,
    ):
        # Indicates whether **Proportional Default Scaling for EIUs** is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_scale = auto_scale
        # The name of the scaling plan.
        self.elastic_plan_name = elastic_plan_name
        # Indicates whether the scaling plan is immediately enabled after the plan is created. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The time when the next scheduling is performed.
        # 
        # > The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        self.next_schedule_time = next_schedule_time
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the name of a resource group within a cluster.
        self.resource_group_name = resource_group_name
        # The amount of elastic resources after scaling.
        self.target_size = target_size
        # The type of the scaling plan. Valid values:
        # 
        # *   **EXECUTOR**: the interactive resource group type, which specifies the computing resource type.
        # *   **WORKER**: the EIU type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.next_schedule_time is not None:
            result['NextScheduleTime'] = self.next_schedule_time

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.target_size is not None:
            result['TargetSize'] = self.target_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NextScheduleTime') is not None:
            self.next_schedule_time = m.get('NextScheduleTime')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

