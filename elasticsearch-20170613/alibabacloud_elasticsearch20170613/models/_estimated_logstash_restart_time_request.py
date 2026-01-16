# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EstimatedLogstashRestartTimeRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        force: bool = None,
    ):
        self.body = body
        # Specifies whether to forcibly restart the cluster. Default value: false.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.force is not None:
            result['force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('force') is not None:
            self.force = m.get('force')

        return self

