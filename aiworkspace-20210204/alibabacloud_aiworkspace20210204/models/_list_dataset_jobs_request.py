# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetJobsRequest(DaraModel):
    def __init__(
        self,
        dataset_version: str = None,
        job_action: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The dataset version name.
        self.dataset_version = dataset_version
        # The action to be performed on the job.
        self.job_action = job_action
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.sort_by = sort_by
        self.status = status
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

