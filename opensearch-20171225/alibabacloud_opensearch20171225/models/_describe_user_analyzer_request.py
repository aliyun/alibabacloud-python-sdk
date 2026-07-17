# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserAnalyzerRequest(DaraModel):
    def __init__(
        self,
        with_: str = None,
    ):
        # Specifies related information to return. The properties are returned based on the specified level.
        # 
        # - all: Returns information about the associated application.
        self.with_ = with_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_ is not None:
            result['with'] = self.with_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('with') is not None:
            self.with_ = m.get('with')

        return self

