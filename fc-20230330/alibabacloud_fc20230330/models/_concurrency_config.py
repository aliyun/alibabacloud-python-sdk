# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConcurrencyConfig(DaraModel):
    def __init__(
        self,
        function_arn: str = None,
        reserved_concurrency: int = None,
    ):
        self.function_arn = function_arn
        self.reserved_concurrency = reserved_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')

        return self

