# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManualDagInstancesRequest(DaraModel):
    def __init__(
        self,
        dag_id: str = None,
        project_env: str = None,
        project_name: str = None,
    ):
        # Instance ID of the DAG instance that triggers the manual workflow. You can call the [CreateManualDag](https://help.aliyun.com/document_detail/189728.html) operation to obtain instance ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The environment identifier of the Operation Center. Valid values: PROD (production environment) and DEV (development environment).
        # 
        # This parameter is required.
        self.project_env = project_env
        # The name of the workspace to which the manual workflow belongs. You can obtain the name on the workspace configuration page in the DataWorks console.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

