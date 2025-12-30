# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDocumentChunkListRequest(DaraModel):
    def __init__(
        self,
        chunk_id_list: List[str] = None,
        doc_id: str = None,
        library_id: str = None,
        order: str = None,
        order_by: str = None,
        page: int = None,
        page_size: int = None,
        search_query: str = None,
    ):
        self.chunk_id_list = chunk_id_list
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.library_id = library_id
        self.order = order
        self.order_by = order_by
        self.page = page
        self.page_size = page_size
        self.search_query = search_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id_list is not None:
            result['chunkIdList'] = self.chunk_id_list

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.order is not None:
            result['order'] = self.order

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.search_query is not None:
            result['searchQuery'] = self.search_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkIdList') is not None:
            self.chunk_id_list = m.get('chunkIdList')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')

        return self

