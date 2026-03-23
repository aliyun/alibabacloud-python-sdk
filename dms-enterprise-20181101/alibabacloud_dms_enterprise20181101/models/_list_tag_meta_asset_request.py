# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagMetaAssetRequest(DaraModel):
    def __init__(
        self,
        meta_parent_id: str = None,
        meta_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tag_name: str = None,
        tid: int = None,
    ):
        self.meta_parent_id = meta_parent_id
        # This parameter is required.
        self.meta_type = meta_type
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.search_key = search_key
        # This parameter is required.
        self.tag_name = tag_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_parent_id is not None:
            result['MetaParentId'] = self.meta_parent_id

        if self.meta_type is not None:
            result['MetaType'] = self.meta_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaParentId') is not None:
            self.meta_parent_id = m.get('MetaParentId')

        if m.get('MetaType') is not None:
            self.meta_type = m.get('MetaType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

