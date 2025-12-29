# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFunctionInstanceRequest(DaraModel):
    def __init__(
        self,
        output: str = None,
    ):
        # Specifies the richness of returned information. Valid values:
        # 
        # *   simple: displays only the basic information.
        # *   normal: displays information such as createParameters and cron. This is the default value.
        # *   detail: returns the details of the training task.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')

        return self

