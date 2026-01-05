# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataSourceSharedRuleRequest(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        env_type: str = None,
        shared_user: str = None,
        target_project_id: int = None,
    ):
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # Share data sources to the target project environment, including
        # - Dev (Development Environment)
        # - Prod (production environment)
        # 
        # This parameter is required.
        self.env_type = env_type
        # The user with which you want to share the data source. If you do not configure this parameter, the data source is shared to an entire workspace.
        self.shared_user = shared_user
        # The ID of the workspace to which you want to share the data source. You cannot share the data source to the workspace with which the data source is associated.
        # 
        # This parameter is required.
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

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.shared_user is not None:
            result['SharedUser'] = self.shared_user

        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('SharedUser') is not None:
            self.shared_user = m.get('SharedUser')

        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')

        return self

