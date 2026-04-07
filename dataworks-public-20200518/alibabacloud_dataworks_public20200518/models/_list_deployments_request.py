# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentsRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        end_create_time: int = None,
        end_execute_time: int = None,
        executor: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        project_identifier: str = None,
        status: int = None,
    ):
        # The ID of the Alibaba Cloud account used by the user who creates the deployment packages.
        self.creator = creator
        # The time when the deployment packages to be queried are created. This value must be a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_create_time = end_create_time
        # The time when the deployment packages are run. This value must be a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_execute_time = end_execute_time
        # The ID of the Alibaba Cloud account used by the user who runs the deployment packages.
        self.executor = executor
        # The keyword that is contained in the names of the deployment packages. A fuzzy search is supported. After you enter a keyword, all deployment packages whose names contain the keyword are displayed.
        self.keyword = keyword
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        # 
        # You must configure either this parameter or the ProjectIdentifier parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace name.
        # 
        # You must configure either this parameter or the ProjectId parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # The status of the deployment packages. Valid values:
        # 
        # *   0: The deployment packages are ready.
        # *   1: The deployment packages are deployed.
        # *   2: The deployment packages fail to be deployed.
        # *   6: The deployment packages are rejected.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time

        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')

        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

