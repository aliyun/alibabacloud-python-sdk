# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticPlanAttributeResponseBody(DaraModel):
    def __init__(
        self,
        elastic_plan: main_models.DescribeElasticPlanAttributeResponseBodyElasticPlan = None,
        request_id: str = None,
    ):
        # The queried scaling plan.
        self.elastic_plan = elastic_plan
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.elastic_plan:
            self.elastic_plan.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_plan is not None:
            result['ElasticPlan'] = self.elastic_plan.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticPlan') is not None:
            temp_model = main_models.DescribeElasticPlanAttributeResponseBodyElasticPlan()
            self.elastic_plan = temp_model.from_map(m.get('ElasticPlan'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticPlanAttributeResponseBodyElasticPlan(DaraModel):
    def __init__(
        self,
        auto_scale: bool = None,
        cron_expression: str = None,
        elastic_plan_name: str = None,
        enabled: bool = None,
        end_time: str = None,
        resource_group_name: str = None,
        start_time: str = None,
        target_size: str = None,
        type: str = None,
    ):
        # Indicates whether **Default Proportional Scaling for EIUs** is enabled. Valid values: true: Default Proportional Scaling for EIUs is enabled. If you set this parameter to true, storage resources are scaled along with computing resources. false: Default Proportional Scaling for EIUs is not enabled.
        # 
        # >  You can enable Default Proportional Scaling for EIUs for only a single scaling plan of a cluster. After you enable a scaling plan of the Default Proportional Scaling for EIUs type, you cannot enable scaling plans of other types.
        self.auto_scale = auto_scale
        # A CORN expression that indicates the scaling cycle and time for the scaling plan.
        self.cron_expression = cron_expression
        # The name of the scaling plan.
        self.elastic_plan_name = elastic_plan_name
        # Indicates whether the scaling plan is enabled.
        self.enabled = enabled
        # The end time of the scaling plan.
        # 
        # >  The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The name of the resource group used by the scaling plan.
        self.resource_group_name = resource_group_name
        # The start time of the scaling plan.
        # 
        # >  The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The amount of elastic resources after scaling.
        self.target_size = target_size
        # The type of the scaling plan.
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

