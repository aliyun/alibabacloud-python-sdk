# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApisecModuleStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        report_status: int = None,
        resource_groups: str = None,
        resource_manager_resource_group_id: str = None,
        resources: str = None,
        trace_status: int = None,
    ):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region in which the Web Application Firewall (WAF) instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id
        # The status of the compliance check feature. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.report_status = report_status
        # The name of the protected object group to which the protected object belongs.
        self.resource_groups = resource_groups
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The name of the protected object.
        self.resources = resources
        # The status of the tracing and auditing feature. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.trace_status = trace_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.trace_status is not None:
            result['TraceStatus'] = self.trace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ResourceGroups') is not None:
            self.resource_groups = m.get('ResourceGroups')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('TraceStatus') is not None:
            self.trace_status = m.get('TraceStatus')

        return self

