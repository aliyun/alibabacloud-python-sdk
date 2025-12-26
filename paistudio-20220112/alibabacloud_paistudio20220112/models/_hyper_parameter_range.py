# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HyperParameterRange(DaraModel):
    def __init__(
        self,
        enum: List[str] = None,
        exclusive_maximum: bool = None,
        exclusive_minimum: bool = None,
        max_length: int = None,
        maximum: str = None,
        min_length: int = None,
        minimum: str = None,
        pattern: str = None,
    ):
        self.enum = enum
        self.exclusive_maximum = exclusive_maximum
        self.exclusive_minimum = exclusive_minimum
        self.max_length = max_length
        self.maximum = maximum
        self.min_length = min_length
        self.minimum = minimum
        self.pattern = pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enum is not None:
            result['Enum'] = self.enum

        if self.exclusive_maximum is not None:
            result['ExclusiveMaximum'] = self.exclusive_maximum

        if self.exclusive_minimum is not None:
            result['ExclusiveMinimum'] = self.exclusive_minimum

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enum') is not None:
            self.enum = m.get('Enum')

        if m.get('ExclusiveMaximum') is not None:
            self.exclusive_maximum = m.get('ExclusiveMaximum')

        if m.get('ExclusiveMinimum') is not None:
            self.exclusive_minimum = m.get('ExclusiveMinimum')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        return self

