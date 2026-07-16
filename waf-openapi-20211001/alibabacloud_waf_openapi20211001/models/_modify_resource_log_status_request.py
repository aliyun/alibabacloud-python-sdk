# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class ModifyResourceLogStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        resource: str = None,
        resource_manager_resource_group_id: str = None,
        status: bool = None,
        trace_config: main_models.ModifyResourceLogStatusRequestTraceConfig = None,
        trace_status: bool = None,
    ):
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region of the WAF instance. Valid values:
        # 
        # - **cn-hangzhou**: The Chinese mainland.
        # 
        # - **ap-southeast-1**: Outside the Chinese mainland.
        self.region_id = region_id
        # The protected object on which you want to manage the log collection feature.
        # 
        # This parameter is required.
        self.resource = resource
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # Specifies whether to enable the log collection feature for the protected object. Valid values:
        # 
        # - **true**: Enables the feature.
        # 
        # - **false**: Disables the feature.
        # 
        # This parameter is required.
        self.status = status
        self.trace_config = trace_config
        self.trace_status = trace_status

    def validate(self):
        if self.trace_config:
            self.trace_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.trace_config is not None:
            result['TraceConfig'] = self.trace_config.to_map()

        if self.trace_status is not None:
            result['TraceStatus'] = self.trace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TraceConfig') is not None:
            temp_model = main_models.ModifyResourceLogStatusRequestTraceConfig()
            self.trace_config = temp_model.from_map(m.get('TraceConfig'))

        if m.get('TraceStatus') is not None:
            self.trace_status = m.get('TraceStatus')

        return self

class ModifyResourceLogStatusRequestTraceConfig(DaraModel):
    def __init__(
        self,
        rate_per_mille: int = None,
        workspace: str = None,
    ):
        self.rate_per_mille = rate_per_mille
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rate_per_mille is not None:
            result['RatePerMille'] = self.rate_per_mille

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RatePerMille') is not None:
            self.rate_per_mille = m.get('RatePerMille')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

