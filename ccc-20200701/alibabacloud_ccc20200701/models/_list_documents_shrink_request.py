# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        next_page_token: str = None,
        page_size: int = None,
        request_id: str = None,
        schema_id: str = None,
        search_pattern: str = None,
        sorts_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.next_page_token = next_page_token
        self.page_size = page_size
        self.request_id = request_id
        # schema id
        # 
        # This parameter is required.
        self.schema_id = schema_id
        self.search_pattern = search_pattern
        self.sorts_shrink = sorts_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        if self.sorts_shrink is not None:
            result['Sorts'] = self.sorts_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        if m.get('Sorts') is not None:
            self.sorts_shrink = m.get('Sorts')

        return self

