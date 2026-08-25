# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentPackagesRequest(DaraModel):
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
        # The Alibaba Cloud account UID of the deployment package creator.
        self.creator = creator
        # The maximum timestamp in milliseconds for the creation time of the deployment package.
        self.end_create_time = end_create_time
        # The maximum timestamp in milliseconds for the execution start time of the deployment package.
        self.end_execute_time = end_execute_time
        # The Alibaba Cloud account UID of the deployment package executor.
        self.executor = executor
        # The keyword in the deployment package name. DataWorks supports fuzzy match. You can enter a keyword to query deployment packages whose names contain the keyword.
        self.keyword = keyword
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the DataWorks console and go to the workspace configuration page to obtain the workspace ID. You must specify either this parameter or the ProjectIdentifier parameter to determine the DataWorks workspace for this API call.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed in the workspace switcher at the top of the DataStudio page. You must specify either this parameter or the ProjectId parameter to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # The current status of the deployment package. Valid values:
        # - 0: The deployment package is ready.
        # - 1: The deployment package is published.
        # - 2: The deployment package failed to be published.
        # - 6: The deployment package is rejected.
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

