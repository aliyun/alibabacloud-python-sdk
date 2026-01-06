# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticPlanJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.DescribeElasticPlanJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried scaling plan jobs.
        self.jobs = jobs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of scaling plan jobs.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

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
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.DescribeElasticPlanJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeElasticPlanJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        elastic_acu: str = None,
        elastic_plan_name: str = None,
        end_time: str = None,
        instance_size: int = None,
        reserve_acu: str = None,
        resource_group_name: str = None,
        start_time: str = None,
        status: str = None,
        target_size: str = None,
        total_acu: str = None,
        type: str = None,
    ):
        # The amount of elastic resources.
        # 
        # > 
        # 
        # *   If Type is set to EXECUTOR, ElasticAcu indicates the amount of elastic resources in the current resource group.
        # 
        # *   If Type is set to WORKER, ElasticAcu indicates the total amount of elastic storage resources in the current cluster.
        self.elastic_acu = elastic_acu
        # The name of the scaling plan.
        self.elastic_plan_name = elastic_plan_name
        # The end time of the scaling plan job.
        # 
        # >  The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.end_time = end_time
        # The number of compute nodes or storage replica sets.
        # 
        # > 
        # 
        # *   If Type is set to EXECUTOR, InstanceSize indicates the number of compute nodes in the cluster.
        # 
        # *   If Type is set to EXECUTOR, InstanceSize indicates the number of storage replica sets in the cluster.
        self.instance_size = instance_size
        # The amount of reserved resources.
        # 
        # > 
        # 
        # *   If Type is set to EXECUTOR, ReserveAcu indicates the amount of reserved resources in the current resource group.
        # 
        # *   If Type is set to WORKER, ReserveAcu indicates the total amount of reserved storage resources in the current cluster.
        self.reserve_acu = reserve_acu
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The start time of the scaling plan job.
        # 
        # >  The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.start_time = start_time
        # The state of the scaling plan job. Valid values:
        # 
        # *   RUNNING
        # *   SUCCESSFUL
        # *   FAILED
        self.status = status
        # The desired specifications of elastic resources after scaling.
        self.target_size = target_size
        # The total amount of resources.
        # 
        # > 
        # 
        # *   If Type is set to EXECUTOR, TotalAcu indicates the total amount of computing resources in the current resource group.
        # 
        # *   If Type is set to WORKER, TotalAcu indicates the total amount of storage resources in the cluster.
        self.total_acu = total_acu
        # The type of the scaling plan job. Valid values:
        # 
        # *   EXECUTOR: the interactive resource group type, which indicates the computing resource type.
        # *   WORKER: the EIU type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_acu is not None:
            result['ElasticAcu'] = self.elastic_acu

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size

        if self.reserve_acu is not None:
            result['ReserveAcu'] = self.reserve_acu

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_size is not None:
            result['TargetSize'] = self.target_size

        if self.total_acu is not None:
            result['TotalAcu'] = self.total_acu

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticAcu') is not None:
            self.elastic_acu = m.get('ElasticAcu')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')

        if m.get('ReserveAcu') is not None:
            self.reserve_acu = m.get('ReserveAcu')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')

        if m.get('TotalAcu') is not None:
            self.total_acu = m.get('TotalAcu')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

