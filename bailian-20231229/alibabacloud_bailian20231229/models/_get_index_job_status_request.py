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
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The knowledge base job ID, which is the `Data.Id` parameter returned by the [SubmitIndexJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexjob) or [SubmitIndexAddDocumentsJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexadddocumentsjob) operations.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Both the [SubmitIndexJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexjob) and [SubmitIndexAddDocumentsJob](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-submitindexadddocumentsjob) operations support batch import of documents. This operation returns both the overall `Status` of the job and the `Document.Status` of each document. If there are a large number of documents, you can use the `PageNumber` parameter to perform a paged query. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of document import jobs that are displayed on each page. No maximum value. Default value: 10.
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

