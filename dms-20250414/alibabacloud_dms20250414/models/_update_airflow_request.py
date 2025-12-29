# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAirflowRequest(DaraModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        client_token: str = None,
        dags_dir: str = None,
        description: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        startup_file: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.client_token = client_token
        self.dags_dir = dags_dir
        self.description = description
        self.plugins_dir = plugins_dir
        self.requirement_file = requirement_file
        self.startup_file = startup_file
        self.worker_serverless_replicas = worker_serverless_replicas
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

        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name

        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir

        if self.description is not None:
            result['Description'] = self.description

        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir

        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file

        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file

        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')

        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')

        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')

        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')

        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')

        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

