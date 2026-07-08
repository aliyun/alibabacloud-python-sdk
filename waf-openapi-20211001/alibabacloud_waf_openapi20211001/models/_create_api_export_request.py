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
        # The hybrid cloud cluster ID.
        # > This parameter applies only to hybrid cloud scenarios. You can call [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) to obtain hybrid cloud cluster information.
        self.cluster_id = cluster_id
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to obtain the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The extended parameters of the export task. You can filter the exported content by specifying conditions. The value is a JSON string constructed from a series of parameters.
        # > The specific parameters vary depending on the specified **export task type** (**Type**). For more information, refer to **Export task parameter description**.
        self.param = param
        # The language type. Valid values:
        # 
        # - **cn** (default): Chinese.
        # - **en**: English.
        self.region = region
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of the export task. Valid values:
        # 
        # - **apisec_api** (default): API asset task.
        # 
        # - **apisec_abnormal**: API risk task.
        # 
        # - **apisec_event**: API security event task.
        self.type = type
        # The time zone ID.
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

