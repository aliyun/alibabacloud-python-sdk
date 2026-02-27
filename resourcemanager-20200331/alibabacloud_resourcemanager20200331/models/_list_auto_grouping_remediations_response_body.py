# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListAutoGroupingRemediationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        remediations: List[main_models.ListAutoGroupingRemediationsResponseBodyRemediations] = None,
        request_id: str = None,
    ):
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The remediation records.
        self.remediations = remediations
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.remediations:
            for v1 in self.remediations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Remediations'] = []
        if self.remediations is not None:
            for k1 in self.remediations:
                result['Remediations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.remediations = []
        if m.get('Remediations') is not None:
            for k1 in m.get('Remediations'):
                temp_model = main_models.ListAutoGroupingRemediationsResponseBodyRemediations()
                self.remediations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAutoGroupingRemediationsResponseBodyRemediations(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        remediation_id: str = None,
        remediation_time: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
        target_resource_group_info: main_models.ListAutoGroupingRemediationsResponseBodyRemediationsTargetResourceGroupInfo = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The remediation record ID.
        self.remediation_id = remediation_id
        # The remediation time.
        self.remediation_time = remediation_time
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service
        # The information about the new resource group.
        self.target_resource_group_info = target_resource_group_info

    def validate(self):
        if self.target_resource_group_info:
            self.target_resource_group_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

        if self.remediation_time is not None:
            result['RemediationTime'] = self.remediation_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service is not None:
            result['Service'] = self.service

        if self.target_resource_group_info is not None:
            result['TargetResourceGroupInfo'] = self.target_resource_group_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        if m.get('RemediationTime') is not None:
            self.remediation_time = m.get('RemediationTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('TargetResourceGroupInfo') is not None:
            temp_model = main_models.ListAutoGroupingRemediationsResponseBodyRemediationsTargetResourceGroupInfo()
            self.target_resource_group_info = temp_model.from_map(m.get('TargetResourceGroupInfo'))

        return self

class ListAutoGroupingRemediationsResponseBodyRemediationsTargetResourceGroupInfo(DaraModel):
    def __init__(
        self,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
    ):
        # The resource group name.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

