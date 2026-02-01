# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVmcoreDiagnosisTaskRequest(DaraModel):
    def __init__(
        self,
        days: int = None,
    ):
        # This parameter is required.
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['days'] = self.days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')

        return self

