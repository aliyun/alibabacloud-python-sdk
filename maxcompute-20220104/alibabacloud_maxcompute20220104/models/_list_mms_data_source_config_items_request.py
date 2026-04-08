# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMmsDataSourceConfigItemsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_type: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['lang'] = self.lang

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

