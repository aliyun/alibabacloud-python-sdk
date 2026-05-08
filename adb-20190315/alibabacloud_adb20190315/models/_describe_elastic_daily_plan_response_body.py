# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticDailyPlanResponseBody(DaraModel):
    def __init__(
        self,
        elastic_daily_plan_list: List[main_models.DescribeElasticDailyPlanResponseBodyElasticDailyPlanList] = None,
        request_id: str = None,
    ):
        # Details of the current-day scaling plans.
        self.elastic_daily_plan_list = elastic_daily_plan_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.elastic_daily_plan_list:
            for v1 in self.elastic_daily_plan_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticDailyPlanList'] = []
        if self.elastic_daily_plan_list is not None:
            for k1 in self.elastic_daily_plan_list:
                result['ElasticDailyPlanList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_daily_plan_list = []
        if m.get('ElasticDailyPlanList') is not None:
            for k1 in m.get('ElasticDailyPlanList'):
                temp_model = main_models.DescribeElasticDailyPlanResponseBodyElasticDailyPlanList()
                self.elastic_daily_plan_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticDailyPlanResponseBodyElasticDailyPlanList(DaraModel):
    def __init__(
        self,
        day: str = None,
        elastic_node_num: int = None,
        elastic_plan_type: str = None,
        elastic_plan_worker_spec: str = None,
        end_ts: str = None,
        plan_end_ts: str = None,
        plan_name: str = None,
        plan_start_ts: str = None,
        resource_pool_name: str = None,
        start_ts: str = None,
        status: int = None,
    ):
        # The start date of the current-day scaling plan. The date is in the yyyy-MM-dd format.
        self.day = day
        # The number of nodes involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, a value of 0 or null is returned.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, a value greater than 0 is returned.
        self.elastic_node_num = elastic_node_num
        # The type of the scaling plan. Default value: executorcombineworker. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker**: scales both elastic I/O resources and computing resources by proportion.
        self.elastic_plan_type = elastic_plan_type
        # The resource specifications that can be scaled up by the scaling plan. Default value: 8 Core 64 GB. Valid values:
        # 
        # *   8 Core 64 GB
        # *   16 Core 64 GB
        # *   32 Core 64 GB
        # *   64 Core 128 GB
        # *   12 Core 96 GB
        # *   24 Core 96 GB
        # *   52 Core 86 GB
        self.elastic_plan_worker_spec = elastic_plan_worker_spec
        # The actual restoration time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.end_ts = end_ts
        # The scheduled restoration time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.plan_end_ts = plan_end_ts
        # The name of the scaling plan.
        self.plan_name = plan_name
        # The scheduled scale-up time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.plan_start_ts = plan_start_ts
        # The name of the resource group.
        self.resource_pool_name = resource_pool_name
        # The actual scale-up time. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.start_ts = start_ts
        # The execution state of the current-day scaling plan. Multiple values are separated by commas (,). Valid values:
        # 
        # *   **1**: The scaling plan is not executed.
        # *   **2**: The scaling plan is being executed.
        # *   **3**: The scaling plan is executed.
        # *   **4**: The scaling plan fails to be executed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day is not None:
            result['Day'] = self.day

        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num

        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type

        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.plan_end_ts is not None:
            result['PlanEndTs'] = self.plan_end_ts

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_start_ts is not None:
            result['PlanStartTs'] = self.plan_start_ts

        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')

        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')

        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('PlanEndTs') is not None:
            self.plan_end_ts = m.get('PlanEndTs')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanStartTs') is not None:
            self.plan_start_ts = m.get('PlanStartTs')

        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

