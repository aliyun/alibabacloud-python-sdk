# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIndexJobStatusRequest(DaraModel):
    def __init__(
        self,
        index_id: str = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The knowledge base ID, which is the `Data.Id` returned by the **CreateIndex** operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The knowledge base job ID, which is the `Data.Id` returned by the **SubmitIndexJob** or **SubmitIndexAddDocumentsJob** operation.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The **SubmitIndexJob** and **SubmitIndexAddDocumentsJob** operations support batch file import. This operation returns the overall knowledge base job status `Status` and the import status of each file `Document.Status`. If there are many files, use the `PageNumber` parameter for paging. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of file import tasks to display per page in a paged query. No maximum limit. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

