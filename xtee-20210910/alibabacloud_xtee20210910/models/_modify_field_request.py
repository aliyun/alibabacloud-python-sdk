# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFieldRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        classify: str = None,
        description: str = None,
        enum_data: str = None,
        id: int = None,
        name: str = None,
        reg_id: str = None,
        title: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Field classification
        self.classify = classify
        # Description information.
        self.description = description
        # Enum type
        self.enum_data = enum_data
        # Variable ID
        self.id = id
        # Variable name
        self.name = name
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.classify is not None:
            result['classify'] = self.classify

        if self.description is not None:
            result['description'] = self.description

        if self.enum_data is not None:
            result['enumData'] = self.enum_data

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('classify') is not None:
            self.classify = m.get('classify')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enumData') is not None:
            self.enum_data = m.get('enumData')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

