# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySearchParametersRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        parameters: str = None,
    ):
        # The ID of the primary PolarDB cluster, which is used to locate the Search cluster associated with the current account.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # A non-empty JSON object string where the keys are parameter names and all values must be strings, such as 10% for a percentage or 48mb for a capacity. Only parameters that are visible and modifiable in the current version template can be modified. Dynamic parameters take effect and are persisted immediately, whereas static parameters take effect after a restart triggered by the task flow. A successful response only indicates that the task has been accepted.
        # 
        # This parameter is required.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

