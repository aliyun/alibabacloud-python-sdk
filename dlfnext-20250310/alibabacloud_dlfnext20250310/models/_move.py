# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Move(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        reference_field_name: str = None,
        type: str = None,
    ):
        self.field_name = field_name
        self.reference_field_name = reference_field_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.reference_field_name is not None:
            result['referenceFieldName'] = self.reference_field_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('referenceFieldName') is not None:
            self.reference_field_name = m.get('referenceFieldName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

