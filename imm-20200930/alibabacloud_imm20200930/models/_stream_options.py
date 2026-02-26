# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StreamOptions(DaraModel):
    def __init__(
        self,
        incremental_output: bool = None,
        need_return_final_result: bool = None,
    ):
        self.incremental_output = incremental_output
        self.need_return_final_result = need_return_final_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incremental_output is not None:
            result['IncrementalOutput'] = self.incremental_output

        if self.need_return_final_result is not None:
            result['NeedReturnFinalResult'] = self.need_return_final_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncrementalOutput') is not None:
            self.incremental_output = m.get('IncrementalOutput')

        if m.get('NeedReturnFinalResult') is not None:
            self.need_return_final_result = m.get('NeedReturnFinalResult')

        return self

