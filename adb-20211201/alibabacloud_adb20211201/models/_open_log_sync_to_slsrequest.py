# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenLogSyncToSLSRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        log_type: str = None,
        region_id: str = None,
        target_log_store: str = None,
        target_project: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The log type. Valid values:
        # 
        # - **ADBMYSQL_AUDIT_LOG**
        # - **ADBMYSQL_INSERT_LOG**
        # 
        # Default value: `ADBMYSQL_AUDIT_LOG`.
        self.log_type = log_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The Simple Log Service LogStore.
        # 
        # This parameter is required.
        self.target_log_store = target_log_store
        # The Simple Log Service project.
        # 
        # This parameter is required.
        self.target_project = target_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        return self

