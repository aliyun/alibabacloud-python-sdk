# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserTrafficRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        instance_id: str = None,
        interval: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        start_timestamp: int = None,
        type: str = None,
    ):
        # The end of the time range to query.
        self.end_timestamp = end_timestamp
        # Instance ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The time interval. Unit: seconds.
        self.interval = interval
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The beginning of the time range to query.
        self.start_timestamp = start_timestamp
        # The type of real-time user traffic. Valid values:
        # - bot: the number of bot management requests.
        # - risk: the number of times risk identification is triggered.
        # - custom_acl_captcha: the number of times the slider action of custom rules is triggered.
        # - qps: the peak QPS.
        # - apisec: the number of API security requests.
        # - alb: the number of requests connected through ALB.
        # - mse: the number of requests connected through MSE.
        # - fc: the number of requests connected through Function Compute.
        # - sae: the number of requests connected through Serverless App Engine.
        # - apig: the number of requests connected through Cloud Native API Gateway.
        # - nlb: the number of requests connected through NLB.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

