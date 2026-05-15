# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigAirflowRequest(DaraModel):
    def __init__(
        self,
        airflow_id: str = None,
        custom_airflow_cfg: List[str] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.airflow_id = airflow_id
        # This parameter is required.
        self.custom_airflow_cfg = custom_airflow_cfg
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

        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')

        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

