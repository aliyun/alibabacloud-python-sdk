# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGrafanaWorkspaceRequest(DaraModel):
    def __init__(
        self,
        grafana_workspace_id: str = None,
        region_id: str = None,
    ):
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.grafana_workspace_id = grafana_workspace_id
        # The region ID. Default value: cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grafana_workspace_id is not None:
            result['GrafanaWorkspaceId'] = self.grafana_workspace_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('GrafanaWorkspaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

