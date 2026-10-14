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
        op_user_id: str = None,
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
        # The ID of the operator.
        self.op_user_id = op_user_id

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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

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

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

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
        # The user IDs of the creators used for filtering. If this parameter is left empty, no filtering is performed. If multiple IDs are specified, they are evaluated by using the OR operator.
        self.creator_list = creator_list
        # The user IDs of the development owners used for filtering. If this parameter is left empty, no filtering is performed. If multiple IDs are specified, they are evaluated by using the OR operator.
        self.develop_owner_list = develop_owner_list
        # The full paths of the directories to query. If this parameter is left empty, the root directory is queried.
        self.directories = directories
        # Specifies whether an exact match is performed on the node name. Default value: false.
        self.exact_match = exact_match
        # The keywords used to filter task names. This parameter is optional. If this parameter is left empty, tasks are not filtered by name. If exact match is enabled, this parameter specifies a list of full names. If fuzzy match is used, this parameter specifies a list of keywords. If multiple keywords are specified, they are evaluated by using the OR operator.
        self.keywords = keywords
        # The cursor for the next page. Leave this parameter empty for the first page. For subsequent pages, pass the NextCursor value returned from the previous page.
        self.next_cursor = next_cursor
        # The user IDs of the O&M owners used for filtering. If this parameter is left empty, no filtering is performed. If multiple IDs are specified, they are evaluated by using the OR operator.
        self.ops_owner_list = ops_owner_list
        # The page number. Default value: 1. The value starts from 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The task types. Default value: [0]. Valid values: 0: offline integration. 1: real-time integration. 13: data ingestion. 14: offline unstructured workflow. 15: real-time unstructured workflow. 16: online unstructured workflow. If you pass null or an empty list, the default value [0] is used.
        self.pipeline_type_list = pipeline_type_list
        # Specifies whether to recursively query subdirectories. Default value: false.
        self.recursive = recursive
        # The schedule types used for filtering. If this parameter is left empty, no filtering is performed. Valid values: 1: periodic scheduling. 3: manual scheduling. 5: real-time scheduling. 7: online workflow.
        self.schedule_type_list = schedule_type_list
        # The submit statuses used for filtering. If this parameter is left empty, no filtering is performed. Valid values: DRAFT: draft. SUBMITTING: submitting. SUBMITTED: submitted. PUBLISHED: published.
        self.submit_status_list = submit_status_list
        # The tag names used for filtering. If this parameter is left empty, no filtering is performed. If multiple names are specified, they are evaluated by using the OR operator.
        self.tag_list = tag_list
        # The total number of records.
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
        # The environment identifier. Valid values: DEV: development environment. PROD: production environment. Default value: PROD.
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

