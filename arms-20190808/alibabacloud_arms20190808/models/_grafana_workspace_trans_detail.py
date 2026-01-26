# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceTransDetail(DaraModel):
    def __init__(
        self,
        dashboard_amount: int = None,
        data_source_amount: int = None,
        original: int = None,
        original_name: str = None,
        target: int = None,
        target_name: str = None,
    ):
        self.dashboard_amount = dashboard_amount
        self.data_source_amount = data_source_amount
        self.original = original
        self.original_name = original_name
        self.target = target
        self.target_name = target_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_amount is not None:
            result['dashboardAmount'] = self.dashboard_amount

        if self.data_source_amount is not None:
            result['dataSourceAmount'] = self.data_source_amount

        if self.original is not None:
            result['original'] = self.original

        if self.original_name is not None:
            result['originalName'] = self.original_name

        if self.target is not None:
            result['target'] = self.target

        if self.target_name is not None:
            result['targetName'] = self.target_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardAmount') is not None:
            self.dashboard_amount = m.get('dashboardAmount')

        if m.get('dataSourceAmount') is not None:
            self.data_source_amount = m.get('dataSourceAmount')

        if m.get('original') is not None:
            self.original = m.get('original')

        if m.get('originalName') is not None:
            self.original_name = m.get('originalName')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('targetName') is not None:
            self.target_name = m.get('targetName')

        return self

