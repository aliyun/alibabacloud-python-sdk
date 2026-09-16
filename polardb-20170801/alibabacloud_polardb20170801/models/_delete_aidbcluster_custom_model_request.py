# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIDBClusterCustomModelRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        model_name: str = None,
        region_id: str = None,
    ):
        # The ID of the PolarDB AI 3.0 logical instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The key of the custom model registration to delete.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

