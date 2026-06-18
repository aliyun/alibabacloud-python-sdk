# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIndexFileDetailsRequest(DaraModel):
    def __init__(
        self,
        document_name: str = None,
        document_status: str = None,
        enable_name_like: str = None,
        index_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The name of the documents to return. If you do not specify this parameter, the results are not filtered by name.
        self.document_name = document_name
        # The import status of the documents to return. Valid values:
        # 
        # - INSERT_ERROR: The document failed to be imported.
        # 
        # - RUNNING: The document is being imported.
        # 
        # - DELETED: The document has been deleted.
        # 
        # - FINISH: The document was imported successfully.
        # 
        # If you do not specify this parameter, the results are not filtered by import status.
        self.document_status = document_status
        # Specifies whether to perform a fuzzy search based on the document name. This parameter is used with the `DocumentName` parameter. Valid values:
        # 
        # - true: Performs a fuzzy search based on the document name.
        # 
        # - false: Performs an exact match based on the document name.
        # 
        # Default value: false.
        self.enable_name_like = enable_name_like
        # The ID of the knowledge base. This is the value of the `Data.Id` parameter returned by the **CreateIndex** operation.
        self.index_id = index_id
        # The number of the page to return. The value starts from 1. Default value: 1.
        self.page_number = page_number
        # The number of documents to return on each page. Maximum value: 10.
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

