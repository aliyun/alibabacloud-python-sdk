# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentsRequest(DaraModel):
    def __init__(
        self,
        filters: str = None,
        kb_uuid: str = None,
        max_results: int = None,
        name_pattern: str = None,
        next_token: str = None,
        sort_field_name: str = None,
        sort_order: str = None,
    ):
        # The document property filter. The following properties are supported:
        # 
        # - `fileExt`: The document extension.
        # 
        # - `state`: The document status.
        self.filters = filters
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.kb_uuid = kb_uuid
        # The maximum number of documents to return per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The document name filter. Returns only documents whose names contain this value.
        self.name_pattern = name_pattern
        # The pagination token to retrieve the next page of results. Omit this parameter to retrieve the first page. A `NextToken` value in the response indicates that more results are available. To fetch the next page, pass this value in a subsequent request. A `null` value indicates that all results have been retrieved.
        self.next_token = next_token
        # The sort field. Valid values:
        # 
        # - `id` (default): The document ID.
        # 
        # - `hits`: The number of hits.
        # 
        # - `modifyTime`: The modification time.
        self.sort_field_name = sort_field_name
        # The sort order. Valid values:
        # 
        # - **ASC** (default): Sorts in ascending order.
        # 
        # - **DESC**: Sorts in descending order.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name_pattern is not None:
            result['NamePattern'] = self.name_pattern

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sort_field_name is not None:
            result['SortFieldName'] = self.sort_field_name

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NamePattern') is not None:
            self.name_pattern = m.get('NamePattern')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SortFieldName') is not None:
            self.sort_field_name = m.get('SortFieldName')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

