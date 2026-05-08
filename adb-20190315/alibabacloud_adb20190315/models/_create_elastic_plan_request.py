# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateElasticPlanRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        elastic_plan_enable: bool = None,
        elastic_plan_end_day: str = None,
        elastic_plan_monthly_repeat: str = None,
        elastic_plan_name: str = None,
        elastic_plan_node_num: int = None,
        elastic_plan_start_day: str = None,
        elastic_plan_time_end: str = None,
        elastic_plan_time_start: str = None,
        elastic_plan_type: str = None,
        elastic_plan_weekly_repeat: str = None,
        elastic_plan_worker_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether the scaling plan takes effect. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.elastic_plan_enable = elastic_plan_enable
        # The end date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_end_day = elastic_plan_end_day
        # The dates of the month when you want to execute the scaling plan. A number specifies a date of the month. Separate multiple values with commas (,).
        self.elastic_plan_monthly_repeat = elastic_plan_monthly_repeat
        # The name of the scaling plan.
        # 
        # *   The name must be 2 to 30 characters in length.
        # *   The name can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.elastic_plan_name = elastic_plan_name
        # The number of nodes that are involved in the scaling plan.
        # 
        # *   If ElasticPlanType is set to **worker**, you can set this parameter to 0 or leave this parameter empty.
        # *   If ElasticPlanType is set to **executorcombineworker** or **executor**, you must set this parameter to a value that is greater than 0.
        self.elastic_plan_node_num = elastic_plan_node_num
        # The start date of the scaling plan. Specify the date in the yyyy-MM-dd format.
        self.elastic_plan_start_day = elastic_plan_start_day
        # The restoration time of the scaling plan. Specify the time on the hour in the HH:mm:ss format. The interval between the scale-up time and the restoration time cannot be more than 24 hours.
        # 
        # This parameter is required.
        self.elastic_plan_time_end = elastic_plan_time_end
        # The scale-up time of the scaling plan. Specify the time on the hour in the HH:mm:ss format.
        # 
        # This parameter is required.
        self.elastic_plan_time_start = elastic_plan_time_start
        # The type of the scaling plan. Valid values:
        # 
        # *   **worker**: scales only elastic I/O resources.
        # *   **executor**: scales only computing resources.
        # *   **executorcombineworker** (default): scales both elastic I/O resources and computing resources by proportion.
        # > - If you want to set this parameter to **executorcombineworker**, make sure that the cluster runs a minor version of 3.1.3.2 or later.
        # > - If you want to set this parameter to **worker** or **executor**, make sure that the cluster runs a minor version of 3.1.6.1 or later and a ticket is submitted. After your request is approved, you can set this parameter to **worker** or **executor**.
        self.elastic_plan_type = elastic_plan_type
        # The days of the week when you want to execute the scaling plan. Valid values: 0 to 6 (Sunday to Saturday). Separate multiple values with commas (,).
        self.elastic_plan_weekly_repeat = elastic_plan_weekly_repeat
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
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the resource group.
        # 
        # >  You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/466685.html) operation to query the resource group name.
        self.resource_pool_name = resource_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable

        if self.elastic_plan_end_day is not None:
            result['ElasticPlanEndDay'] = self.elastic_plan_end_day

        if self.elastic_plan_monthly_repeat is not None:
            result['ElasticPlanMonthlyRepeat'] = self.elastic_plan_monthly_repeat

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.elastic_plan_node_num is not None:
            result['ElasticPlanNodeNum'] = self.elastic_plan_node_num

        if self.elastic_plan_start_day is not None:
            result['ElasticPlanStartDay'] = self.elastic_plan_start_day

        if self.elastic_plan_time_end is not None:
            result['ElasticPlanTimeEnd'] = self.elastic_plan_time_end

        if self.elastic_plan_time_start is not None:
            result['ElasticPlanTimeStart'] = self.elastic_plan_time_start

        if self.elastic_plan_type is not None:
            result['ElasticPlanType'] = self.elastic_plan_type

        if self.elastic_plan_weekly_repeat is not None:
            result['ElasticPlanWeeklyRepeat'] = self.elastic_plan_weekly_repeat

        if self.elastic_plan_worker_spec is not None:
            result['ElasticPlanWorkerSpec'] = self.elastic_plan_worker_spec

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')

        if m.get('ElasticPlanEndDay') is not None:
            self.elastic_plan_end_day = m.get('ElasticPlanEndDay')

        if m.get('ElasticPlanMonthlyRepeat') is not None:
            self.elastic_plan_monthly_repeat = m.get('ElasticPlanMonthlyRepeat')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('ElasticPlanNodeNum') is not None:
            self.elastic_plan_node_num = m.get('ElasticPlanNodeNum')

        if m.get('ElasticPlanStartDay') is not None:
            self.elastic_plan_start_day = m.get('ElasticPlanStartDay')

        if m.get('ElasticPlanTimeEnd') is not None:
            self.elastic_plan_time_end = m.get('ElasticPlanTimeEnd')

        if m.get('ElasticPlanTimeStart') is not None:
            self.elastic_plan_time_start = m.get('ElasticPlanTimeStart')

        if m.get('ElasticPlanType') is not None:
            self.elastic_plan_type = m.get('ElasticPlanType')

        if m.get('ElasticPlanWeeklyRepeat') is not None:
            self.elastic_plan_weekly_repeat = m.get('ElasticPlanWeeklyRepeat')

        if m.get('ElasticPlanWorkerSpec') is not None:
            self.elastic_plan_worker_spec = m.get('ElasticPlanWorkerSpec')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')

        return self

