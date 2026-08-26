# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIDBClusterRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        model_space: str = None,
    ):
        # The AI cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The model operator space.
        self.model_space = model_space

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.model_space is not None:
            result['ModelSpace'] = self.model_space

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ModelSpace') is not None:
            self.model_space = m.get('ModelSpace')

        return self

