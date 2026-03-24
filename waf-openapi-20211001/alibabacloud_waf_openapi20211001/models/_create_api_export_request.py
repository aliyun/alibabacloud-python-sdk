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
        # 
        # > This parameter is applicable only to hybrid cloud scenarios. You can call the [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) operation to query hybrid cloud clusters.
        self.cluster_id = cluster_id
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The filter conditions for the export task. The value is a JSON string.
        # 
        # > The filter conditions vary based on the export task type specified by **Type**. For more information, see **Export task parameters**.
        self.param = param
        # The language of the response. Valid values:
        # 
        # - **cn** (default): Chinese.
        # 
        # - **en**: English.
        self.region = region
        # The region ID of the WAF instance. Valid values:
        # 
        # - **cn-hangzhou**: Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the export task. Valid values:
        # 
        # - **apisec_api** (default): Exports API asset data.
        # 
        # - **apisec_abnormal**: Exports API threat data.
        # 
        # - **apisec_event**: Exports API security event data.
        self.type = type
        # The time zone of the export data, such as **Asia/Shanghai**.
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

