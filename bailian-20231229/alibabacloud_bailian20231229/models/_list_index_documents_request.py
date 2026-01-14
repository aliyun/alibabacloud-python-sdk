# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIndexDocumentsRequest(DaraModel):
    def __init__(
        self,
        document_name: str = None,
        document_status: str = None,
        enable_name_like: str = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The names of the queried documents. The default value is null, which means the names are not used to filter the results.
        self.document_name = document_name
        # The import status of the documents to be queried. Valid values:
        # 
        # *   INSERT_ERROR
        # *   RUNNING
        # *   DELETED
        # *   FINISH
        # 
        # The default value is null, which means the import status is not used to filter the results.
        self.document_status = document_status
        self.enable_name_like = enable_name_like
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The page numbers of the pages to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of documents displayed on each page. No maximum value. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_name is not None:
            result['DocumentName'] = self.document_name

        if self.document_status is not None:
            result['DocumentStatus'] = self.document_status

        if self.enable_name_like is not None:
            result['EnableNameLike'] = self.enable_name_like

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')

        if m.get('DocumentStatus') is not None:
            self.document_status = m.get('DocumentStatus')

        if m.get('EnableNameLike') is not None:
            self.enable_name_like = m.get('EnableNameLike')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

