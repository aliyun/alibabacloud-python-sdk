# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRunIdDeductionsRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        agent_types: List[str] = None,
        ali_uid: int = None,
        biz_type: str = None,
        deduction_types: List[str] = None,
        end_time: int = None,
        group_by_fields: List[str] = None,
        group_resource_types: List[str] = None,
        group_separator: bool = None,
        instance_id_type: str = None,
        instance_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        package_ids: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        resource_type: str = None,
        resource_types: List[str] = None,
        start_time: int = None,
        wy_id: str = None,
    ):
        # The agent type: `CREDIT_PACKAGE` / `JVS_CLAW` / `OPEN_CLAW` / `JVS_COPILOT`.
        self.agent_type = agent_type
        self.agent_types = agent_types
        # The Alibaba Cloud UID.
        self.ali_uid = ali_uid
        # The business type.
        self.biz_type = biz_type
        # The deduction types. Do not specify this parameter for non-knowledge base scenarios.
        self.deduction_types = deduction_types
        # The end time of the period.
        self.end_time = end_time
        self.group_by_fields = group_by_fields
        self.group_resource_types = group_resource_types
        # Specifies whether to group results by deduction type.
        self.group_separator = group_separator
        # The instance ID type. Do not specify this parameter for non-knowledge base scenarios.
        self.instance_id_type = instance_id_type
        # The list of cloud computer IDs. If this field has a value, the `PackageIds` field is required.
        self.instance_ids = instance_ids
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token. Leave this parameter empty for the first request. For subsequent requests, use the `nextToken` value from the previous response.
        self.next_token = next_token
        # The list of core-hour package IDs in JSON format.
        self.package_ids = package_ids
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page for a paged query.
        self.page_size = page_size
        # The resource type.
        self.resource_type = resource_type
        # The list of resource types in JSON array format.
        self.resource_types = resource_types
        # The start time.
        self.start_time = start_time
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.agent_types is not None:
            result['AgentTypes'] = self.agent_types

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.deduction_types is not None:
            result['DeductionTypes'] = self.deduction_types

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by_fields is not None:
            result['GroupByFields'] = self.group_by_fields

        if self.group_resource_types is not None:
            result['GroupResourceTypes'] = self.group_resource_types

        if self.group_separator is not None:
            result['GroupSeparator'] = self.group_separator

        if self.instance_id_type is not None:
            result['InstanceIdType'] = self.instance_id_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('AgentTypes') is not None:
            self.agent_types = m.get('AgentTypes')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DeductionTypes') is not None:
            self.deduction_types = m.get('DeductionTypes')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupByFields') is not None:
            self.group_by_fields = m.get('GroupByFields')

        if m.get('GroupResourceTypes') is not None:
            self.group_resource_types = m.get('GroupResourceTypes')

        if m.get('GroupSeparator') is not None:
            self.group_separator = m.get('GroupSeparator')

        if m.get('InstanceIdType') is not None:
            self.instance_id_type = m.get('InstanceIdType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

