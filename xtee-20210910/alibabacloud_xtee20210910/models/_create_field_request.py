# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFieldRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        classify: str = None,
        description: str = None,
        enum_data: str = None,
        name: str = None,
        reg_id: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Field classification.
        self.classify = classify
        # Description information.
        self.description = description
        # Enum data.
        self.enum_data = enum_data
        # Field name.
        self.name = name
        # Region code.
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Business source.
        self.source = source
        # Title.
        self.title = title
        # Field type.
        self.type = type

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

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.source is not None:
            result['source'] = self.source

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

