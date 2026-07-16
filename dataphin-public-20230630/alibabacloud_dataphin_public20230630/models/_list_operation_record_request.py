# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListOperationRecordRequest(DaraModel):
    def __init__(
        self,
        list_command: main_models.ListOperationRecordRequestListCommand = None,
        op_tenant_id: int = None,
    ):
        # The query command.
        # 
        # This parameter is required.
        self.list_command = list_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_command:
            self.list_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_command is not None:
            result['ListCommand'] = self.list_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListCommand') is not None:
            temp_model = main_models.ListOperationRecordRequestListCommand()
            self.list_command = temp_model.from_map(m.get('ListCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListOperationRecordRequestListCommand(DaraModel):
    def __init__(
        self,
        begin_time_end: str = None,
        begin_time_start: str = None,
        code_content: str = None,
        code_type: List[int] = None,
        duration: List[int] = None,
        file_name: str = None,
        object_type: List[str] = None,
        page: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_type: int = None,
        status: List[int] = None,
        user_ids: List[str] = None,
    ):
        # The end of the start time range. Format: yyyy-MM-dd HH:mm:ss.
        self.begin_time_end = begin_time_end
        # The beginning of the start time range. Format: yyyy-MM-dd HH:mm:ss.
        self.begin_time_start = begin_time_start
        # The keyword for code search.
        self.code_content = code_content
        # The list of code types.
        self.code_type = code_type
        # The list of duration ranges.
        self.duration = duration
        # The script name.
        self.file_name = file_name
        # The list of object types.
        self.object_type = object_type
        # The page number. Default value: 1.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The sort type. Valid values: 0 (start time ascending), 1 (start time descending), 2 (object name).
        self.sort_type = sort_type
        # The list of task statuses.
        self.status = status
        # The list of executor IDs.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time_end is not None:
            result['BeginTimeEnd'] = self.begin_time_end

        if self.begin_time_start is not None:
            result['BeginTimeStart'] = self.begin_time_start

        if self.code_content is not None:
            result['CodeContent'] = self.code_content

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.status is not None:
            result['Status'] = self.status

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeEnd') is not None:
            self.begin_time_end = m.get('BeginTimeEnd')

        if m.get('BeginTimeStart') is not None:
            self.begin_time_start = m.get('BeginTimeStart')

        if m.get('CodeContent') is not None:
            self.code_content = m.get('CodeContent')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

