# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelineRunsRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        object_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        status: str = None,
    ):
        # The creator of the deployment pipeline. This parameter is used as a filter condition.
        self.creator = creator
        # The ID of the deployment object.
        self.object_id = object_id
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can logon to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace for the current API invoke operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The current status of the deployment pipeline. This parameter is used as a filter condition.
        # 
        # Valid values:
        # 
        # - Init: Initialized.
        # - Running: Running.
        # - Success: Succeeded.
        # - Fail: Failed.
        # - Termination: Terminated.
        # - Cancel: Canceled.
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

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

