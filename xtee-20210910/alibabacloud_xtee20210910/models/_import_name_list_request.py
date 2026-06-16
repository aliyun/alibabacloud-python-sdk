# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportNameListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        data: str = None,
        description: str = None,
        import_type: str = None,
        memo: str = None,
        name_list_type: str = None,
        reg_id: str = None,
        title: str = None,
        variable_id: int = None,
    ):
        # The language type for the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The creation type.
        self.create_type = create_type
        # The list of names to import.
        self.data = data
        # The description.
        self.description = description
        # The document import type. Valid values:
        # 
        # INPUT: data entry.
        # CSV: CSV upload.
        # NONE: no upload.
        # 
        # This parameter is required.
        self.import_type = import_type
        # The description.
        self.memo = memo
        # The nameListType.
        self.name_list_type = name_list_type
        # The region code.
        self.reg_id = reg_id
        # The title.
        # 
        # This parameter is required.
        self.title = title
        # The variable ID.
        self.variable_id = variable_id

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

        if self.data is not None:
            result['data'] = self.data

        if self.description is not None:
            result['description'] = self.description

        if self.import_type is not None:
            result['importType'] = self.import_type

        if self.memo is not None:
            result['memo'] = self.memo

        if self.name_list_type is not None:
            result['nameListType'] = self.name_list_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.title is not None:
            result['title'] = self.title

        if self.variable_id is not None:
            result['variableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('importType') is not None:
            self.import_type = m.get('importType')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('nameListType') is not None:
            self.name_list_type = m.get('nameListType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('variableId') is not None:
            self.variable_id = m.get('variableId')

        return self

