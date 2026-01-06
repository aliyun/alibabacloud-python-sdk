# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterMaintainTimeRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        maintain_time: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The maintenance window of the cluster. It must be in the hh:mmZ-hh:mmZ format.
        # 
        # > The interval must be 1 hour and start and end at the beginning of an hour.
        # 
        # This parameter is required.
        self.maintain_time = maintain_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        return self

