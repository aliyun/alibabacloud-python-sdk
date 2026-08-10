# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPipelinesRequest(DaraModel):
    def __init__(
        self,
        context: main_models.ListPipelinesRequestContext = None,
        list_command: main_models.ListPipelinesRequestListCommand = None,
        op_tenant_id: int = None,
    ):
        # The request context.
        # 
        # This parameter is required.
        self.context = context
        # The query parameters.
        # 
        # This parameter is required.
        self.list_command = list_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.context:
            self.context.validate()
        if self.list_command:
            self.list_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.list_command is not None:
            result['ListCommand'] = self.list_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.ListPipelinesRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('ListCommand') is not None:
            temp_model = main_models.ListPipelinesRequestListCommand()
            self.list_command = temp_model.from_map(m.get('ListCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListPipelinesRequestListCommand(DaraModel):
    def __init__(
        self,
        creator_list: List[str] = None,
        develop_owner_list: List[str] = None,
        directories: List[str] = None,
        exact_match: bool = None,
        keywords: List[str] = None,
        next_cursor: int = None,
        ops_owner_list: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        pipeline_type_list: List[int] = None,
        recursive: bool = None,
        schedule_type_list: List[int] = None,
        submit_status_list: List[str] = None,
        tag_list: List[str] = None,
        total_count: int = None,
    ):
        # The list of creator user IDs for filtering. If left empty, no filtering is applied. Multiple values have an OR relationship.
        self.creator_list = creator_list
        # The list of development owner user IDs for filtering. If left empty, no filtering is applied. Multiple values have an OR relationship.
        self.develop_owner_list = develop_owner_list
        # The list of full folder paths to query. If left empty, the root folder is queried.
        self.directories = directories
        # Specifies whether to use exact match for node names. Default value: false.
        self.exact_match = exact_match
        # The list of node name keywords. This parameter is optional. If left empty, no filtering by name is applied. For exact match, this is a list of full names. For fuzzy match, this is a list of keywords. Multiple values have an OR relationship.
        self.keywords = keywords
        # The cursor-based pagination parameter (an opaque cursor that callers do not need to interpret). This parameter is optional. If not specified, the request is treated as a first-page request and returns the actual total count. If specified, the request is treated as a subsequent-page request. Pass the NextCursor value from the previous page response as-is. The SQL layer automatically filters by incrementing ID to query the next page without re-querying the total count. No OFFSET is used throughout, which avoids performance degradation in deep paging scenarios.
        self.next_cursor = next_cursor
        # The list of O&M owner user IDs for filtering. If left empty, no filtering is applied. Multiple values have an OR relationship.
        self.ops_owner_list = ops_owner_list
        # The page number. Default value: 1. Starts from 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of node types. Valid values:
        # 
        # - 0: offline integration.
        # - 1: real-time integration.
        # - 13: data aggregation.
        # - 14: offline unstructured workflow.
        # - 15: real-time unstructured workflow.
        # - 16: online unstructured workflow.
        # 
        # Default value: [0]. If null or an empty list is passed, the default value [0] is used.
        self.pipeline_type_list = pipeline_type_list
        # Specifies whether to recursively query subfolders. Default value: false.
        self.recursive = recursive
        # The list of scheduling types for filtering. If left empty, no filtering is applied. Valid values:
        # 
        # - 1: periodic scheduling.
        # - 3: manual scheduling.
        # - 5: real-time scheduling.
        # - 7: online workflow.
        self.schedule_type_list = schedule_type_list
        # The list of submit statuses for filtering. If left empty, no filtering is applied. Valid values:
        # 
        # - DRAFT: draft.
        # - SUBMITTING: submitting.
        # - SUBMITTED: submitted.
        # - PUBLISHED: published.
        self.submit_status_list = submit_status_list
        # The list of label names for filtering. If left empty, no filtering is applied. Multiple values have an OR relationship.
        self.tag_list = tag_list
        # The total number of records for cursor-based pagination. This parameter is optional and takes effect only when NextCursor is not empty. After the first-page request returns the actual total count, pass this value back as-is for subsequent pages. The server does not re-query the total count and directly returns this value, which avoids redundant count overhead. If not specified, the system falls back to querying one extra record to determine whether a next page exists.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_list is not None:
            result['CreatorList'] = self.creator_list

        if self.develop_owner_list is not None:
            result['DevelopOwnerList'] = self.develop_owner_list

        if self.directories is not None:
            result['Directories'] = self.directories

        if self.exact_match is not None:
            result['ExactMatch'] = self.exact_match

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor

        if self.ops_owner_list is not None:
            result['OpsOwnerList'] = self.ops_owner_list

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pipeline_type_list is not None:
            result['PipelineTypeList'] = self.pipeline_type_list

        if self.recursive is not None:
            result['Recursive'] = self.recursive

        if self.schedule_type_list is not None:
            result['ScheduleTypeList'] = self.schedule_type_list

        if self.submit_status_list is not None:
            result['SubmitStatusList'] = self.submit_status_list

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorList') is not None:
            self.creator_list = m.get('CreatorList')

        if m.get('DevelopOwnerList') is not None:
            self.develop_owner_list = m.get('DevelopOwnerList')

        if m.get('Directories') is not None:
            self.directories = m.get('Directories')

        if m.get('ExactMatch') is not None:
            self.exact_match = m.get('ExactMatch')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')

        if m.get('OpsOwnerList') is not None:
            self.ops_owner_list = m.get('OpsOwnerList')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipelineTypeList') is not None:
            self.pipeline_type_list = m.get('PipelineTypeList')

        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')

        if m.get('ScheduleTypeList') is not None:
            self.schedule_type_list = m.get('ScheduleTypeList')

        if m.get('SubmitStatusList') is not None:
            self.submit_status_list = m.get('SubmitStatusList')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPipelinesRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The environment identifier. Valid values:
        # 
        # - DEV: development environment.
        # - PROD: production environment.
        # 
        # Default value: PROD.
        self.env = env
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

