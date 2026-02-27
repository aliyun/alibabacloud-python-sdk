# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAutoGroupingRemediationsRequest(DaraModel):
    def __init__(
        self,
        earliest_remediation_time: str = None,
        latest_remediation_time: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        resource_type: str = None,
        rule_id: str = None,
        service: str = None,
        target_resource_group_id: str = None,
    ):
        # The earliest remediation time. This parameter is empty by default.
        self.earliest_remediation_time = earliest_remediation_time
        # The latest remediation time. This parameter is empty by default.
        self.latest_remediation_time = latest_remediation_time
        # The maximum number of data entries to return.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The resource ID,
        self.resource_id = resource_id
        # The resource type,
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service
        # The ID of the new resource group.
        self.target_resource_group_id = target_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.earliest_remediation_time is not None:
            result['EarliestRemediationTime'] = self.earliest_remediation_time

        if self.latest_remediation_time is not None:
            result['LatestRemediationTime'] = self.latest_remediation_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.service is not None:
            result['Service'] = self.service

        if self.target_resource_group_id is not None:
            result['TargetResourceGroupId'] = self.target_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EarliestRemediationTime') is not None:
            self.earliest_remediation_time = m.get('EarliestRemediationTime')

        if m.get('LatestRemediationTime') is not None:
            self.latest_remediation_time = m.get('LatestRemediationTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('TargetResourceGroupId') is not None:
            self.target_resource_group_id = m.get('TargetResourceGroupId')

        return self

