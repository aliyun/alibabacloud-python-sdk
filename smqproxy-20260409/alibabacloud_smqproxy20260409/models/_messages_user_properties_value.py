# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MessagesUserPropertiesValue(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        string_value: str = None,
        binary_value: str = None,
    ):
        self.data_type = data_type
        self.string_value = string_value
        self.binary_value = binary_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.string_value is not None:
            result['StringValue'] = self.string_value

        if self.binary_value is not None:
            result['BinaryValue'] = self.binary_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')

        if m.get('BinaryValue') is not None:
            self.binary_value = m.get('BinaryValue')

        return self

