# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Function(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        description: str = None,
        function_language: str = None,
        function_type: str = None,
        gmt_modified: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.class_name = class_name
        self.description = description
        # This parameter is required.
        self.function_language = function_language
        # This parameter is required.
        self.function_type = function_type
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['className'] = self.class_name

        if self.description is not None:
            result['description'] = self.description

        if self.function_language is not None:
            result['functionLanguage'] = self.function_language

        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('functionLanguage') is not None:
            self.function_language = m.get('functionLanguage')

        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

