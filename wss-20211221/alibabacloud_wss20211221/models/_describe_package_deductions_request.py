# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePackageDeductionsRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        agent_types: List[str] = None,
        biz_type: str = None,
        consume_wy_id: str = None,
        consume_wy_ids: List[str] = None,
        deduction_request_id: str = None,
        deduction_types: List[str] = None,
        end_time: int = None,
        group_resource_types: List[str] = None,
        instance_id: str = None,
        instance_id_type: str = None,
        instance_ids: List[str] = None,
        model: str = None,
        package_ids: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        resource_type: str = None,
        resource_types: List[str] = None,
        run_id: str = None,
        run_id_list: List[str] = None,
        start_time: int = None,
        wy_id: str = None,
    ):
        # The agent type.
        self.agent_type = agent_type
        # The list of agent types.
        self.agent_types = agent_types
        # The business type.
        self.biz_type = biz_type
        # The WUYING user ID. You can obtain it by calling the GetLoginToken operation. The response parameter is WyId.
        self.consume_wy_id = consume_wy_id
        # The WUYING user ID. You can obtain it by calling the GetLoginToken operation. The response parameter is WyId.
        self.consume_wy_ids = consume_wy_ids
        # The request ID.
        self.deduction_request_id = deduction_request_id
        # The deduction types.
        self.deduction_types = deduction_types
        # The end time of the query. The time is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The list of resource group types.
        self.group_resource_types = group_resource_types
        # The instance ID, such as ecd-xxx.
        self.instance_id = instance_id
        # The instance ID type.
        self.instance_id_type = instance_id_type
        # The list of Cloud Desktop IDs. If this field is specified, the PackageIds field is required.
        self.instance_ids = instance_ids
        # The model name.
        self.model = model
        # The list of core-hour package IDs in JSON format.
        self.package_ids = package_ids
        # The current page number. Default value: 1.
        self.page_num = page_num
        # The paging Settings for the number of entries to return on each page in a paged query. Maximum value: 100.
        self.page_size = page_size
        # The resource type.
        self.resource_type = resource_type
        # The array of resource types.
        self.resource_types = resource_types
        # The run ID.
        self.run_id = run_id
        # The list of run IDs.
        self.run_id_list = run_id_list
        # The start time of the query. The time is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The WUYING user ID. You can obtain it by calling the GetLoginToken operation. The response parameter is WyId.
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

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.consume_wy_id is not None:
            result['ConsumeWyId'] = self.consume_wy_id

        if self.consume_wy_ids is not None:
            result['ConsumeWyIds'] = self.consume_wy_ids

        if self.deduction_request_id is not None:
            result['DeductionRequestId'] = self.deduction_request_id

        if self.deduction_types is not None:
            result['DeductionTypes'] = self.deduction_types

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_resource_types is not None:
            result['GroupResourceTypes'] = self.group_resource_types

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_id_type is not None:
            result['InstanceIdType'] = self.instance_id_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.model is not None:
            result['Model'] = self.model

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

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.run_id_list is not None:
            result['RunIdList'] = self.run_id_list

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

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConsumeWyId') is not None:
            self.consume_wy_id = m.get('ConsumeWyId')

        if m.get('ConsumeWyIds') is not None:
            self.consume_wy_ids = m.get('ConsumeWyIds')

        if m.get('DeductionRequestId') is not None:
            self.deduction_request_id = m.get('DeductionRequestId')

        if m.get('DeductionTypes') is not None:
            self.deduction_types = m.get('DeductionTypes')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupResourceTypes') is not None:
            self.group_resource_types = m.get('GroupResourceTypes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIdType') is not None:
            self.instance_id_type = m.get('InstanceIdType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Model') is not None:
            self.model = m.get('Model')

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

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('RunIdList') is not None:
            self.run_id_list = m.get('RunIdList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

