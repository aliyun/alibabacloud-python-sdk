# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Field(DaraModel):
    def __init__(
        self,
        blob_value: str = None,
        boolean_value: bool = None,
        double_value: float = None,
        is_null: bool = None,
        long_value: int = None,
        string_value: str = None,
    ):
        self.blob_value = blob_value
        self.boolean_value = boolean_value
        self.double_value = double_value
        self.is_null = is_null
        self.long_value = long_value
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blob_value is not None:
            result['BlobValue'] = self.blob_value

        if self.boolean_value is not None:
            result['BooleanValue'] = self.boolean_value

        if self.double_value is not None:
            result['DoubleValue'] = self.double_value

        if self.is_null is not None:
            result['IsNull'] = self.is_null

        if self.long_value is not None:
            result['LongValue'] = self.long_value

        if self.string_value is not None:
            result['StringValue'] = self.string_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlobValue') is not None:
            self.blob_value = m.get('BlobValue')

        if m.get('BooleanValue') is not None:
            self.boolean_value = m.get('BooleanValue')

        if m.get('DoubleValue') is not None:
            self.double_value = m.get('DoubleValue')

        if m.get('IsNull') is not None:
            self.is_null = m.get('IsNull')

        if m.get('LongValue') is not None:
            self.long_value = m.get('LongValue')

        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')

        return self

