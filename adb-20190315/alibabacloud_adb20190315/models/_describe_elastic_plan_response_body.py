# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticPlanResponseBody(DaraModel):
    def __init__(
        self,
        elastic_plan_list: List[main_models.DescribeElasticPlanResponseBodyElasticPlanList] = None,
        request_id: str = None,
    ):
        # The queried scaling plans.
        self.elastic_plan_list = elastic_plan_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.elastic_plan_list:
            for v1 in self.elastic_plan_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticPlanList'] = []
        if self.elastic_plan_list is not None:
            for k1 in self.elastic_plan_list:
                result['ElasticPlanList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_plan_list = []
        if m.get('ElasticPlanList') is not None:
            for k1 in m.get('ElasticPlanList'):
                temp_model = main_models.DescribeElasticPlanResponseBodyElasticPlanList()
                self.elastic_plan_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticPlanResponseBodyElasticPlanList(DaraModel):
    def __init__(
        self,
        elastic_node_num: int = None,
        elastic_plan_type: str = None,
        elastic_plan_worker_spec: str = None,
        enable: bool = None,
        end_day: str = None,
        end_time: str = None,
        monthly_repeat: str = None,
        plan_name: str = None,
        resource_pool_name: str = None,
        start_day: str = None,
        start_time: str = None,
        weekly_repeat: str = None,
    ):
        # The number of nodes that are involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, a value of 0 or null is returned.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, a value greater than 0 is returned.
        self.elastic_node_num = elastic_node_num
        # The type of the scaling plan. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker** (default): scales both elastic I/O resources and computing resources by proportion.
        self.elastic_plan_type = elastic_plan_type
        # The resource specifications that can be scaled up by the scaling plan. Valid values:
        # 
        # *   8 Core 64 GB (default)
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        # Indicates whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.enable = enable
        # The end date of the scaling plan. This parameter is returned only if the end date of the scaling plan is set. The date is in the yyyy-MM-dd format.
        self.end_day = end_day
        # The restoration time of the scaling plan. The interval between the scale-up time and the restoration time cannot be more than 24 hours. The time is in the HH:mm:ss format.
        self.end_time = end_time
        # The days of the month when the scaling plan was executed. A value indicates a day of the month. Multiple values are separated by commas (,).
        self.monthly_repeat = monthly_repeat
        # The name of the scaling plan.
        self.plan_name = plan_name
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The start date of the scaling plan. This parameter is returned only if the start date of the scaling plan is set. The date is in the yyyy-MM-dd format.
        self.start_day = start_day
        # The scale-up time of the scaling plan. The time is in the HH:mm:ss format.
        self.start_time = start_time
        # The days of the week when the scaling plan was executed. Valid values: 0 to 6, which indicate Sunday to Saturday. Multiple values are separated by commas (,).
        self.weekly_repeat = weekly_repeat

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num

        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type

        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_day is not None:
            result['EndDay'] = self.end_day

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.monthly_repeat is not None:
            result['MonthlyRepeat'] = self.monthly_repeat

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name

        if self.start_day is not None:
            result['StartDay'] = self.start_day

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.weekly_repeat is not None:
            result['WeeklyRepeat'] = self.weekly_repeat

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')

        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')

        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndDay') is not None:
            self.end_day = m.get('EndDay')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MonthlyRepeat') is not None:
            self.monthly_repeat = m.get('MonthlyRepeat')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')

        if m.get('StartDay') is not None:
            self.start_day = m.get('StartDay')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WeeklyRepeat') is not None:
            self.weekly_repeat = m.get('WeeklyRepeat')

        return self

