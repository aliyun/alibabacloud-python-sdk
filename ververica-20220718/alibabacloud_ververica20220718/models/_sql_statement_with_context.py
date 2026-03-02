# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class SqlStatementWithContext(DaraModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        batch_mode: bool = None,
        flink_configuration: Dict[str, Any] = None,
        statement: str = None,
        version_name: str = None,
    ):
        # The additional dependencies.
        self.additional_dependencies = additional_dependencies
        # Specifies whether the deployment is a batch deployment.
        # 
        # This parameter is required.
        self.batch_mode = batch_mode
        # The Realtime Compute for Apache Flink configuration.
        self.flink_configuration = flink_configuration
        # The code of the deployment.
        # 
        # This parameter is required.
        self.statement = statement
        # The engine version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies

        if self.batch_mode is not None:
            result['batchMode'] = self.batch_mode

        if self.flink_configuration is not None:
            result['flinkConfiguration'] = self.flink_configuration

        if self.statement is not None:
            result['statement'] = self.statement

        if self.version_name is not None:
            result['versionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')

        if m.get('batchMode') is not None:
            self.batch_mode = m.get('batchMode')

        if m.get('flinkConfiguration') is not None:
            self.flink_configuration = m.get('flinkConfiguration')

        if m.get('statement') is not None:
            self.statement = m.get('statement')

        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')

        return self

