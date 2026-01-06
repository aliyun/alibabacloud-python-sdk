# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterConfigRequest(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        parallel_operation: bool = None,
        parameters: str = None,
        region_id: str = None,
        switch_time_mode: str = None,
    ):
        # This parameter is required.
        self.config_key = config_key
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to perform parallel operations on the cluster node.
        self.parallel_operation = parallel_operation
        # This parameter is required.
        self.parameters = parameters
        self.region_id = region_id
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.parallel_operation is not None:
            result['ParallelOperation'] = self.parallel_operation

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ParallelOperation') is not None:
            self.parallel_operation = m.get('ParallelOperation')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

