# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeRunIdDeductionsResponseBody(DaraModel):
    def __init__(
        self,
        deductions: List[main_models.DescribeRunIdDeductionsResponseBodyDeductions] = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_used_time: int = None,
        total_used_time_decimal: str = None,
    ):
        # The deduction details.
        self.deductions = deductions
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token. Leave this parameter empty for the first request. For subsequent requests, use the `nextToken` value from the previous response.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page for a paged query.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of core-hour package deduction details in the query result.
        self.total_count = total_count
        # The total usage duration. Unit: seconds. Do not use this field for AI scenarios.
        self.total_used_time = total_used_time
        # The total credits used that match the specified conditions.
        self.total_used_time_decimal = total_used_time_decimal

    def validate(self):
        if self.deductions:
            for v1 in self.deductions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Deductions'] = []
        if self.deductions is not None:
            for k1 in self.deductions:
                result['Deductions'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time

        if self.total_used_time_decimal is not None:
            result['TotalUsedTimeDecimal'] = self.total_used_time_decimal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deductions = []
        if m.get('Deductions') is not None:
            for k1 in m.get('Deductions'):
                temp_model = main_models.DescribeRunIdDeductionsResponseBodyDeductions()
                self.deductions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')

        if m.get('TotalUsedTimeDecimal') is not None:
            self.total_used_time_decimal = m.get('TotalUsedTimeDecimal')

        return self

class DescribeRunIdDeductionsResponseBodyDeductions(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        end_time: str = None,
        group_resource_type: str = None,
        instance_id: str = None,
        model: str = None,
        package_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        run_id: str = None,
        start_time: str = None,
        summary: str = None,
        used_time: int = None,
        used_time_decimal: str = None,
    ):
        # The agent type: `CREDIT_PACKAGE` / `JVS_CLAW` / `OPEN_CLAW` / `JVS_COPILOT`.
        self.agent_type = agent_type
        # The end time of the period.
        self.end_time = end_time
        # The group resource type.
        self.group_resource_type = group_resource_type
        # The instance ID.
        self.instance_id = instance_id
        self.model = model
        # The credit or plan package ID.
        self.package_id = package_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The unique run ID.
        self.run_id = run_id
        # The start time.
        self.start_time = start_time
        # The summary of the large language model call.
        self.summary = summary
        # The usage duration. Unit: seconds. Do not use this field for AI scenarios.
        self.used_time = used_time
        # The credits used.
        self.used_time_decimal = used_time_decimal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_resource_type is not None:
            result['GroupResourceType'] = self.group_resource_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.used_time_decimal is not None:
            result['UsedTimeDecimal'] = self.used_time_decimal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupResourceType') is not None:
            self.group_resource_type = m.get('GroupResourceType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('UsedTimeDecimal') is not None:
            self.used_time_decimal = m.get('UsedTimeDecimal')

        return self

