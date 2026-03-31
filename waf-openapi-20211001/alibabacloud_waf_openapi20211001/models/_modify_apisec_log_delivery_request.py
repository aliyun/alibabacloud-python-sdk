# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApisecLogDeliveryRequest(DaraModel):
    def __init__(
        self,
        assert_key: str = None,
        instance_id: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        project_name: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The type of the log subscription. Valid values:
        # 
        # *   **risk**: risk information.
        # *   **event**: attack event information.
        # *   **asset**: asset information.
        # 
        # This parameter is required.
        self.assert_key = assert_key
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where logs are stored.
        # 
        # >  You can call the [DescribeUserSlsLogRegions](https://help.aliyun.com/document_detail/2712598.html) operation to query available log storage regions.
        # 
        # This parameter is required.
        self.log_region_id = log_region_id
        # The name of the Logstore in Simple Log Service.
        # 
        # >  API security logs can be delivered only to Logstores whose names start with apisec-.
        # 
        # This parameter is required.
        self.log_store_name = log_store_name
        # The name of the project in Simple Log Service.
        # 
        # >  API security logs can be delivered only to projects whose names start with apisec-.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The region where the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assert_key is not None:
            result['AssertKey'] = self.assert_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssertKey') is not None:
            self.assert_key = m.get('AssertKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

