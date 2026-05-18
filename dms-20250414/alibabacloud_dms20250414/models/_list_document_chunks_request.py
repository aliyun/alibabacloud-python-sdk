# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentChunksRequest(DaraModel):
    def __init__(
        self,
        chunk_title_pattern: str = None,
        document_name: str = None,
        kb_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field_name: str = None,
        sort_order: str = None,
    ):
        self.chunk_title_pattern = chunk_title_pattern
        self.document_name = document_name
        # This parameter is required.
        self.kb_uuid = kb_uuid
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field_name = sort_field_name
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_title_pattern is not None:
            result['ChunkTitlePattern'] = self.chunk_title_pattern

        if self.document_name is not None:
            result['DocumentName'] = self.document_name

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sort_field_name is not None:
            result['SortFieldName'] = self.sort_field_name

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkTitlePattern') is not None:
            self.chunk_title_pattern = m.get('ChunkTitlePattern')

        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SortFieldName') is not None:
            self.sort_field_name = m.get('SortFieldName')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

