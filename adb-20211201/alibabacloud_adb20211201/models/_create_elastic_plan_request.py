# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateElasticPlanRequest(DaraModel):
    def __init__(
        self,
        auto_scale: bool = None,
        cron_expression: str = None,
        dbcluster_id: str = None,
        elastic_plan_name: str = None,
        enabled: bool = None,
        end_time: str = None,
        resource_group_name: str = None,
        start_time: str = None,
        target_size: str = None,
        type: str = None,
    ):
        # Specifies whether to enable **Default Proportional Scaling for EIUs**. Valid values:
        # 
        # *   true. In this case, storage resources are scaled along with computing resources, and the TargetSize and CronExpression parameters are not supported.
        # *   false
        # 
        # > 
        # 
        # *   This parameter must be specified when Type is set to WORKER. This parameter is not required when Type is set to EXECUTOR.
        # 
        # *   You can enable Default Proportional Scaling for EIUs for only a single scaling plan of a cluster.
        self.auto_scale = auto_scale
        # A CORN expression that specifies the scaling cycle and time for the scaling plan.
        self.cron_expression = cron_expression
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the scaling plan.
        # 
        # >  The name must be 2 to 30 characters in length and can contain letters, digits, and underscores (_). The name must start with a letter.
        # 
        # This parameter is required.
        self.elastic_plan_name = elastic_plan_name
        # Specifies whether to immediately enable the scaling plan after the plan is created. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.enabled = enabled
        # The end time of the scaling plan.
        # 
        # >  Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The name of the resource group.
        # 
        # > 
        # 
        # *   If you want to create a scaling plan that uses interactive resource groups, you must specify this parameter. If you want to create a scaling plan that uses elastic I/O units (EIUs), you do not need to specify this parameter.
        # 
        # *   You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the resource group name for a cluster.
        self.resource_group_name = resource_group_name
        # The start time of the scaling plan.
        # 
        # >  Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The desired specifications of elastic resources after scaling.
        # 
        # > 
        # 
        # *   If the scaling plan uses **EIUs** and **Default Proportional Scaling for EIUs** is enabled, you do not need to specify this parameter. In other cases, you must specify this parameter.
        # 
        # *   You can call the [DescribeElasticPlanSpecifications](https://help.aliyun.com/document_detail/601278.html) operation to query the specifications that are supported for scaling plans.
        self.target_size = target_size
        # The type of the scaling plan. Valid values:
        # 
        # *   EXECUTOR: the interactive resource group type, which indicates the computing resource type.
        # *   WORKER: the EIU type.
        # 
        # This parameter is required.
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

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_size is not None:
            result['TargetSize'] = self.target_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

