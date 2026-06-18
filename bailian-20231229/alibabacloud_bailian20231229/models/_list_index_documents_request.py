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
        # Filters the returned file list by file name (without the file extension). Default value: empty, which means the results are not filtered by file name.
        self.document_name = document_name
        # Filters the returned file list by file import status. Valid values:
        # - INSERT_ERROR: The file failed to be imported.
        # - RUNNING: The file is being imported.
        # - DELETED: The file has been deleted.
        # - FINISH: The file was imported.
        # 
        # Default value: empty, which means the results are not filtered by file import status.
        self.document_status = document_status
        # Specifies whether to enable fuzzy matching for file names. This parameter is used together with the `DocumentName` parameter. Valid values:
        # - true: Fuzzy matching is used to filter the returned file list by file name.
        # - false: Exact matching is used to filter the returned file list by file name.
        # 
        # Default value: false.
        self.enable_name_like = enable_name_like
        # The knowledge base ID, which is the `Data.Id` returned by the **CreateIndex** operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of files to display per page in a paging query. No maximum limit.
        # Default value: 10.
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

