# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        group_paging_result: main_models.ListDataServiceGroupsResponseBodyGroupPagingResult = None,
        request_id: str = None,
    ):
        # The pagination result of business processes.
        self.group_paging_result = group_paging_result
        # The request ID. A unique identifier for the request.
        self.request_id = request_id

    def validate(self):
        if self.group_paging_result:
            self.group_paging_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_paging_result is not None:
            result['GroupPagingResult'] = self.group_paging_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupPagingResult') is not None:
            temp_model = main_models.ListDataServiceGroupsResponseBodyGroupPagingResult()
            self.group_paging_result = temp_model.from_map(m.get('GroupPagingResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataServiceGroupsResponseBodyGroupPagingResult(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListDataServiceGroupsResponseBodyGroupPagingResultGroups] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of business processes.
        self.groups = groups
        # The page number, which is the same as the PageNumber value in the request.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListDataServiceGroupsResponseBodyGroupPagingResultGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceGroupsResponseBodyGroupPagingResultGroups(DaraModel):
    def __init__(
        self,
        api_gateway_group_id: str = None,
        created_time: str = None,
        creator_id: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The ID of the API Gateway group associated with the business process.
        self.api_gateway_group_id = api_gateway_group_id
        # The time when the business process was created.
        # 
        # The format is `yyyy-MM-dd\\"T\\"HH:mm:ssZ`, for example, `2020-09-24T18:37:51+0800`. The time zone offset in this example is `+0800`.
        self.created_time = created_time
        # The UID of the creator. The creator UID may be empty for some legacy business processes.
        self.creator_id = creator_id
        # The description of the business process.
        self.description = description
        # The ID of the business process.
        self.group_id = group_id
        # The name of the business process.
        self.group_name = group_name
        # The time when the business process was last modified.
        # 
        # The format is `yyyy-MM-dd\\"T\\"HH:mm:ssZ`, for example, `2020-09-24T18:37:51+0800`. The time zone offset in this example is `+0800`.
        self.modified_time = modified_time
        # The workspace ID.
        self.project_id = project_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_gateway_group_id is not None:
            result['ApiGatewayGroupId'] = self.api_gateway_group_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiGatewayGroupId') is not None:
            self.api_gateway_group_id = m.get('ApiGatewayGroupId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

