# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigAirflowShrinkRequest(DaraModel):
    def __init__(
        self,
        airflow_id: str = None,
        custom_airflow_cfg_shrink: str = None,
        workspace_id: str = None,
    ):
        # The unique ID of the Airflow instance.
        # 
        # This parameter is required.
        self.airflow_id = airflow_id
        # The list of custom Airflow configurations.
        # 
        # This parameter is required.
        self.custom_airflow_cfg_shrink = custom_airflow_cfg_shrink
        # The DMS workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id

        if self.custom_airflow_cfg_shrink is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')

        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg_shrink = m.get('CustomAirflowCfg')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

