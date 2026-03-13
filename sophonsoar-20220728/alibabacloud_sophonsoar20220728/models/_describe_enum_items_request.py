# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnumItemsRequest(DaraModel):
    def __init__(
        self,
        enum_type: str = None,
        lang: str = None,
    ):
        # The type of the enumeration item. Valid values:
        # 
        # *   **process**: scenarios
        # 
        # This parameter is required.
        self.enum_type = enum_type
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enum_type is not None:
            result['EnumType'] = self.enum_type

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnumType') is not None:
            self.enum_type = m.get('EnumType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

