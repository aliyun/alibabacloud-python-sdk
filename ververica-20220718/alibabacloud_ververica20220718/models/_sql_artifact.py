# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SqlArtifact(DaraModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        sql_script: str = None,
    ):
        # The additional dependency files. If you want to use dependencies such as UDFs, connectors, and formats that are not registered on Ververica Platform (VVP), you need to configure this parameter. You do not need to configure this parameter for dependencies that are registered on VVP.
        self.additional_dependencies = additional_dependencies
        # The script of the SQL deployment.
        self.sql_script = sql_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies

        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')

        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')

        return self

