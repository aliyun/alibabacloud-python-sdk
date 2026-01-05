# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourceSharedRulesRequest(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        target_project_id: int = None,
    ):
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The ID of the workspace to which the data source is shared. You cannot share the data source to the workspace with which the data source is associated.
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')

        return self

