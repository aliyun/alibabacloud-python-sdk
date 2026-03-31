# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiExportRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
        param: str = None,
        region: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        # >For hybrid cloud scenarios only, you can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query the hybrid cloud clusters.
        self.cluster_id = cluster_id
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The extended parameters of the data export task. The parameter value is in the JSON format. The following keys are supported:
        # 
        # *   **instanceId**: the instance ID
        # *   **clusterId**: the ID of the hybrid cloud cluster
        # *   **orderKey**: the name of the field used to sort exported data
        # *   **orderWay**: the sorting method of the exported data
        self.param = param
        # Language type. Valid values:
        # - **cn**: Chinese.
        # - **en**: English.
        self.region = region
        # The region in which the Web Application Firewall (WAF) instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the data export task. Valid values:
        # 
        # *   **apisec_api**: API tasks
        # *   **apisec_abnormal**: API risk tasks
        # *   **apisec_event**: API security event tasks
        self.type = type
        # The ID of the time zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.param is not None:
            result['Param'] = self.param

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

