# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        offline_datasource_id: str = None,
        offline_life_cycle: int = None,
        online_datasource_id: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.offline_datasource_id = offline_datasource_id
        self.offline_life_cycle = offline_life_cycle
        # This parameter is required.
        self.online_datasource_id = online_datasource_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id

        if self.offline_life_cycle is not None:
            result['OfflineLifeCycle'] = self.offline_life_cycle

        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')

        if m.get('OfflineLifeCycle') is not None:
            self.offline_life_cycle = m.get('OfflineLifeCycle')

        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

