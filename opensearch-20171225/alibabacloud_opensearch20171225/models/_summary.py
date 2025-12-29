# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class Summary(DaraModel):
    def __init__(
        self,
        active: bool = None,
        meta: main_models.SummaryMeta = None,
        name: str = None,
    ):
        self.active = active
        self.meta = meta
        self.name = name

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('meta') is not None:
            temp_model = main_models.SummaryMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class SummaryMeta(DaraModel):
    def __init__(
        self,
        element: str = None,
        ellipsis: str = None,
        field: str = None,
        len: int = None,
        snippet: str = None,
    ):
        self.element = element
        self.ellipsis = ellipsis
        self.field = field
        self.len = len
        self.snippet = snippet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element is not None:
            result['element'] = self.element

        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis

        if self.field is not None:
            result['field'] = self.field

        if self.len is not None:
            result['len'] = self.len

        if self.snippet is not None:
            result['snippet'] = self.snippet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')

        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')

        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('len') is not None:
            self.len = m.get('len')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        return self

