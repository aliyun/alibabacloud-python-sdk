# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class SerDeInfoModel(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        ser_de_id: int = None,
        serialization_lib: str = None,
    ):
        self.name = name
        self.parameters = parameters
        self.ser_de_id = ser_de_id
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.ser_de_id is not None:
            result['SerDeId'] = self.ser_de_id

        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SerDeId') is not None:
            self.ser_de_id = m.get('SerDeId')

        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')

        return self

