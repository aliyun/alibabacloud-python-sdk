# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecycleBinJobsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The task ID.
        self.job_id = job_id
        # The page number of the current page in a paged query.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of entries per page in a paged query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The task status. Valid values:
        # 
        # - Running: The task is running.
        # - Defragmenting: Data is being defragmented.
        # - PartialSuccess: The task partially succeeded.
        # - Success: The task succeeded.
        # - Fail: The task failed.
        # - Cancelled: The task is canceled.
        # - All (default): All statuses.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

