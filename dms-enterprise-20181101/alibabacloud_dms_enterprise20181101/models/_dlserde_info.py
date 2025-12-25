# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DLSerdeInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        deserializer_class: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        serde_type: int = None,
        serialization_lib: str = None,
        serializer_class: str = None,
    ):
        self.description = description
        self.deserializer_class = deserializer_class
        self.name = name
        self.parameters = parameters
        self.serde_type = serde_type
        self.serialization_lib = serialization_lib
        self.serializer_class = serializer_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.deserializer_class is not None:
            result['DeserializerClass'] = self.deserializer_class

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.serde_type is not None:
            result['SerdeType'] = self.serde_type

        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib

        if self.serializer_class is not None:
            result['SerializerClass'] = self.serializer_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeserializerClass') is not None:
            self.deserializer_class = m.get('DeserializerClass')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SerdeType') is not None:
            self.serde_type = m.get('SerdeType')

        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')

        if m.get('SerializerClass') is not None:
            self.serializer_class = m.get('SerializerClass')

        return self

