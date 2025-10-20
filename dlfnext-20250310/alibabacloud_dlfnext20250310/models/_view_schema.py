# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class ViewSchema(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dialects: Dict[str, str] = None,
        fields: List[main_models.DataField] = None,
        options: Dict[str, str] = None,
        query: str = None,
    ):
        self.comment = comment
        self.dialects = dialects
        self.fields = fields
        self.options = options
        self.query = query

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.dialects is not None:
            result['dialects'] = self.dialects

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.options is not None:
            result['options'] = self.options

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('dialects') is not None:
            self.dialects = m.get('dialects')

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.DataField()
                self.fields.append(temp_model.from_map(k1))

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

