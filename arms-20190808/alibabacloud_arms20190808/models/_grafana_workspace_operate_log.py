# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceOperateLog(DaraModel):
    def __init__(
        self,
        date: float = None,
        detail: str = None,
        grafana_workspace_id: str = None,
        id: int = None,
        operator_id: str = None,
    ):
        self.date = date
        self.detail = detail
        self.grafana_workspace_id = grafana_workspace_id
        self.id = id
        self.operator_id = operator_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.detail is not None:
            result['detail'] = self.detail

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.id is not None:
            result['id'] = self.id

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        return self

