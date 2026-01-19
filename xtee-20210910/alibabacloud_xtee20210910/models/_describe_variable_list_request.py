# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVariableListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        current_page: str = None,
        page_size: str = None,
        ref_obj_id: str = None,
        reg_id: str = None,
        source_type: str = None,
        type: str = None,
        types_str: str = None,
        value: str = None,
    ):
        # Set the language type for requests and responses, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Creation type.
        self.create_type = create_type
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Associated event ID.
        self.ref_obj_id = ref_obj_id
        # Region code.
        self.reg_id = reg_id
        # Source type.
        self.source_type = source_type
        # Type.
        self.type = type
        # JSON array string of types.
        self.types_str = types_str
        # Value for fuzzy search.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.ref_obj_id is not None:
            result['refObjId'] = self.ref_obj_id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        if self.types_str is not None:
            result['typesStr'] = self.types_str

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('refObjId') is not None:
            self.ref_obj_id = m.get('refObjId')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('typesStr') is not None:
            self.types_str = m.get('typesStr')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

