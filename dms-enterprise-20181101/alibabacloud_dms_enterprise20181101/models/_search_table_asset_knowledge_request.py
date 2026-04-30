# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTableAssetKnowledgeRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        offset: int = None,
        search_key: str = None,
        show_type: str = None,
        size: int = None,
        table_name: str = None,
    ):
        # This parameter is required.
        self.db_id = db_id
        self.offset = offset
        self.search_key = search_key
        self.show_type = show_type
        self.size = size
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        if self.size is not None:
            result['Size'] = self.size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

