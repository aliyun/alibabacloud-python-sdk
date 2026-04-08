# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SLSLogDestination(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        project: str = None,
    ):
        # SLS日志库名称
        self.log_store = log_store
        # SLS项目名称
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store is not None:
            result['logStore'] = self.log_store

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logStore') is not None:
            self.log_store = m.get('logStore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

